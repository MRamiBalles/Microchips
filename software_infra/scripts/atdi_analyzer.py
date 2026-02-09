#!/usr/bin/env python3
"""
ATDI Analyzer - Architectural Technical Debt Index for Hardware Design
Silicon Synthesis Corp - Guardian Agent Component

Este script analiza diseños de interposer y calcula el score ATDI,
bloqueando automáticamente diseños que violan la Constitution.
"""

import json
import sys
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional


class Severity(Enum):
    CRITICAL = "CRITICAL"  # Bloqueo inmediato
    HIGH = "HIGH"          # Requiere revisión
    MEDIUM = "MEDIUM"      # Monitoreo
    LOW = "LOW"            # Optimización sugerida


class Action(Enum):
    BLOCK = "BLOCK_DESIGN"
    ALERT = "ALERT_REVIEW"
    MONITOR = "MONITOR"
    PASS = "PASS"


@dataclass
class Smell:
    """Representa un 'olor arquitectónico' detectado en el diseño."""
    smell_type: str
    location: str
    value: float
    threshold: float
    severity: Severity
    recommendation: str
    
    @property
    def weight(self) -> float:
        """Peso del smell para cálculo ATDI."""
        weights = {
            "CYCLIC_DEPENDENCY": 1.0,
            "DENSE_STRUCTURE": 0.8,
            "HUB_LIKE": 0.5,
            "GOD_COMPONENT": 0.4,
            "UNSTABLE_DEPENDENCY": 0.3,
            "FEATURE_CONCENTRATION": 0.2,
            "SCATTERED_FUNCTIONALITY": 0.1,
        }
        return weights.get(self.smell_type, 0.1)


@dataclass
class ATDIReport:
    """Reporte completo de análisis ATDI."""
    atdi_score: float
    status: str
    smells_detected: list[Smell]
    blocking_issues: int
    constitution_check: str
    timestamp: str
    design_file: str
    
    def to_json(self) -> str:
        return json.dumps({
            "atdi_score": round(self.atdi_score, 3),
            "status": self.status,
            "smells_detected": [
                {
                    "type": s.smell_type,
                    "location": s.location,
                    "value": s.value,
                    "threshold": s.threshold,
                    "severity": s.severity.value,
                    "recommendation": s.recommendation,
                }
                for s in self.smells_detected
            ],
            "blocking_issues": self.blocking_issues,
            "constitution_check": self.constitution_check,
            "timestamp": self.timestamp,
            "design_file": self.design_file,
        }, indent=2)


class ConstitutionRules:
    """Reglas inmutables de constitution.md"""
    
    # Artículo II: Reglas Físicas
    PHY_001_THERMAL_MAX_C = 105
    PHY_002_TSV_DENSITY_MAX = 10000  # per mm²
    PHY_003_MICROBUMP_PITCH_MIN_UM = 40
    PHY_004_HBM_STACK_MAX = 12
    PHY_005_INTERPOSER_AREA_MAX_MM2 = 2500
    PHY_006_WARPAGE_MAX_UM = 200
    
    # Artículo II: Reglas de Routing
    RT_001_SIGNAL_LENGTH_MAX_MM = 15
    RT_002_CURRENT_DENSITY_MAX = 2.5  # mA/μm²
    RT_003_VIAS_PER_HBM_SIGNAL = 3
    RT_004_IR_DROP_MAX_PERCENT = 3
    
    # Artículo II-B: ATDI
    ATDI_003_HUB_CONNECTIONS_MAX = 8
    ATDI_004_FUNCTIONS_PER_BLOCK_MAX = 5
    ATDI_QUALITY_GATE = 0.3


class ATDIAnalyzer:
    """Analizador de Deuda Técnica Arquitectónica para diseños de hardware."""
    
    def __init__(self, design_path: str):
        self.design_path = Path(design_path)
        self.smells: list[Smell] = []
        self.rules = ConstitutionRules()
    
    def load_design(self) -> dict:
        """Carga el archivo de diseño JSON."""
        if not self.design_path.exists():
            raise FileNotFoundError(f"Design file not found: {self.design_path}")
        
        with open(self.design_path) as f:
            return json.load(f)
    
    def check_cyclic_dependencies(self, design: dict) -> None:
        """ATDI-001: Detecta bucles de dependencia en señales."""
        signal_graph = design.get("signal_graph", {})
        
        # Algoritmo simple de detección de ciclos (DFS)
        visited = set()
        rec_stack = set()
        
        def has_cycle(node: str, path: list) -> Optional[list]:
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in signal_graph.get(node, []):
                if neighbor not in visited:
                    result = has_cycle(neighbor, path + [neighbor])
                    if result:
                        return result
                elif neighbor in rec_stack:
                    return path + [neighbor]
            
            rec_stack.remove(node)
            return None
        
        for node in signal_graph:
            if node not in visited:
                cycle = has_cycle(node, [node])
                if cycle:
                    self.smells.append(Smell(
                        smell_type="CYCLIC_DEPENDENCY",
                        location=" → ".join(cycle),
                        value=len(cycle),
                        threshold=0,
                        severity=Severity.CRITICAL,
                        recommendation="Eliminar ciclo de señales. Insertar buffer o rediseñar topología."
                    ))
    
    def check_tsv_density(self, design: dict) -> None:
        """PHY-002 / ATDI-002: Verifica densidad de TSV."""
        regions = design.get("tsv_regions", [])
        
        for region in regions:
            density = region.get("tsv_count", 0) / max(region.get("area_mm2", 1), 0.001)
            if density > self.rules.PHY_002_TSV_DENSITY_MAX:
                self.smells.append(Smell(
                    smell_type="DENSE_STRUCTURE",
                    location=region.get("name", "unknown"),
                    value=density,
                    threshold=self.rules.PHY_002_TSV_DENSITY_MAX,
                    severity=Severity.CRITICAL,
                    recommendation=f"Reducir TSVs o expandir área. Actual: {density:.0f}/mm², Max: {self.rules.PHY_002_TSV_DENSITY_MAX}/mm²"
                ))
    
    def check_hub_like_nodes(self, design: dict) -> None:
        """ATDI-003: Detecta nodos con demasiadas conexiones."""
        nodes = design.get("routing_nodes", {})
        
        for node_id, connections in nodes.items():
            conn_count = len(connections)
            if conn_count > self.rules.ATDI_003_HUB_CONNECTIONS_MAX:
                self.smells.append(Smell(
                    smell_type="HUB_LIKE",
                    location=node_id,
                    value=conn_count,
                    threshold=self.rules.ATDI_003_HUB_CONNECTIONS_MAX,
                    severity=Severity.HIGH,
                    recommendation=f"Dividir nodo en sub-controladores. Conexiones: {conn_count}, Max: {self.rules.ATDI_003_HUB_CONNECTIONS_MAX}"
                ))
    
    def check_god_components(self, design: dict) -> None:
        """ATDI-004: Detecta bloques monolíticos."""
        blocks = design.get("blocks", [])
        
        for block in blocks:
            func_count = len(block.get("functions", []))
            if func_count > self.rules.ATDI_004_FUNCTIONS_PER_BLOCK_MAX:
                self.smells.append(Smell(
                    smell_type="GOD_COMPONENT",
                    location=block.get("name", "unknown"),
                    value=func_count,
                    threshold=self.rules.ATDI_004_FUNCTIONS_PER_BLOCK_MAX,
                    severity=Severity.HIGH,
                    recommendation=f"Descomponer bloque. Funciones: {func_count}, Max: {self.rules.ATDI_004_FUNCTIONS_PER_BLOCK_MAX}"
                ))
    
    def check_signal_lengths(self, design: dict) -> None:
        """RT-001: Verifica longitudes de señal."""
        signals = design.get("signals", [])
        
        for signal in signals:
            length = signal.get("length_mm", 0)
            if length > self.rules.RT_001_SIGNAL_LENGTH_MAX_MM:
                self.smells.append(Smell(
                    smell_type="SCATTERED_FUNCTIONALITY",
                    location=signal.get("name", "unknown"),
                    value=length,
                    threshold=self.rules.RT_001_SIGNAL_LENGTH_MAX_MM,
                    severity=Severity.MEDIUM,
                    recommendation=f"Acortar ruta o añadir repeater. Longitud: {length}mm, Max: {self.rules.RT_001_SIGNAL_LENGTH_MAX_MM}mm"
                ))
    
    def calculate_atdi_score(self) -> float:
        """Calcula el score ATDI basado en smells detectados."""
        if not self.smells:
            return 0.0
        
        total_weight = sum(smell.weight for smell in self.smells)
        # Normalizar por número de componentes (asumimos 10 como baseline)
        normalized = total_weight / 10.0
        return min(normalized, 1.0)  # Cap at 1.0
    
    def analyze(self) -> ATDIReport:
        """Ejecuta análisis completo del diseño."""
        design = self.load_design()
        
        # Ejecutar todos los checks
        self.check_cyclic_dependencies(design)
        self.check_tsv_density(design)
        self.check_hub_like_nodes(design)
        self.check_god_components(design)
        self.check_signal_lengths(design)
        
        # Calcular score
        atdi_score = self.calculate_atdi_score()
        
        # Contar issues bloqueantes
        blocking = sum(1 for s in self.smells if s.severity == Severity.CRITICAL)
        
        # Determinar status
        if blocking > 0:
            status = "BLOCKED"
            constitution_check = "FAIL"
        elif atdi_score > self.rules.ATDI_QUALITY_GATE:
            status = "REQUIRES_REFACTORING"
            constitution_check = "WARN"
        elif atdi_score > 0.2:
            status = "ACCEPTABLE"
            constitution_check = "PASS"
        else:
            status = "EXCELLENT"
            constitution_check = "PASS"
        
        return ATDIReport(
            atdi_score=atdi_score,
            status=status,
            smells_detected=self.smells,
            blocking_issues=blocking,
            constitution_check=constitution_check,
            timestamp=datetime.utcnow().isoformat() + "Z",
            design_file=str(self.design_path),
        )


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python atdi_analyzer.py <design.json>")
        print("       python atdi_analyzer.py --demo")
        sys.exit(1)
    
    if sys.argv[1] == "--demo":
        # Crear archivo de demo para testing
        demo_design = {
            "signal_graph": {
                "CLK": ["HBM_CTRL"],
                "HBM_CTRL": ["MEM_PHY"],
                "MEM_PHY": ["DATA_BUS"],
                "DATA_BUS": []
            },
            "tsv_regions": [
                {"name": "HBM_NORTH", "tsv_count": 8000, "area_mm2": 1.0},
                {"name": "HBM_SOUTH", "tsv_count": 5000, "area_mm2": 1.0}
            ],
            "routing_nodes": {
                "CENTRAL_HUB": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],  # 10 connections
                "NORTH_NODE": ["X", "Y", "Z"]
            },
            "blocks": [
                {"name": "GPU_CORE", "functions": ["compute", "cache", "scheduler"]},
                {"name": "HBM_CONTROLLER", "functions": ["read", "write", "refresh", "ecc", "thermal", "power"]}
            ],
            "signals": [
                {"name": "DATA_0", "length_mm": 8.5},
                {"name": "DATA_1", "length_mm": 18.2}  # Exceeds limit
            ]
        }
        
        demo_path = Path("demo_design.json")
        with open(demo_path, "w") as f:
            json.dump(demo_design, f, indent=2)
        print(f"Demo design created: {demo_path}")
        design_path = str(demo_path)
    else:
        design_path = sys.argv[1]
    
    try:
        analyzer = ATDIAnalyzer(design_path)
        report = analyzer.analyze()
        
        print("\n" + "="*60)
        print("  ATDI ANALYSIS REPORT - Silicon Synthesis Corp")
        print("="*60)
        print(report.to_json())
        print("="*60)
        
        # Exit code based on status
        if report.status == "BLOCKED":
            print("\n🔴 DESIGN BLOCKED - Cannot proceed to tape-out")
            sys.exit(1)
        elif report.status == "REQUIRES_REFACTORING":
            print("\n🟠 REFACTORING REQUIRED - ATDI score exceeds quality gate")
            sys.exit(2)
        else:
            print(f"\n✅ Design analysis complete - Status: {report.status}")
            sys.exit(0)
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing design file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
