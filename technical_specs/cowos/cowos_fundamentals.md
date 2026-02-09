# CoWoS Fundamentals
## Chip-on-Wafer-on-Substrate Technology

> **Nivel:** Especificación Técnica  
> **Aplicación:** Diseño de interposers para Silicon Synthesis Corp

---

## 1. ¿Qué es CoWoS?

**CoWoS (Chip-on-Wafer-on-Substrate)** es una tecnología de empaquetado avanzado 2.5D desarrollada por TSMC que permite integrar múltiples chiplets (GPU, CPU, HBM) sobre un único interposer de silicio.

```
┌─────────────────────────────────────────────────────────────┐
│  Vista Lateral de un Paquete CoWoS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                        │
│    │ HBM │ │ HBM │ │ GPU │ │ HBM │   ← Chiplets           │
│    └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘                        │
│       │       │       │       │      ← Micro-bumps         │
│  ╔════╧═══════╧═══════╧═══════╧════╗                       │
│  ║     INTERPOSER (Silicio)        ║  ← TSVs internos     │
│  ╚═══════════════╤═════════════════╝                       │
│                  │                   ← C4 Bumps            │
│  ┌───────────────┴───────────────┐                         │
│  │      SUBSTRATE (Orgánico)     │                         │
│  └───────────────────────────────┘                         │
│                  │                   ← BGA Balls           │
│  ════════════════╧═════════════════  ← PCB                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Variantes de CoWoS

| Variante | Interposer | Uso Principal | Tamaño Máx |
|----------|------------|---------------|------------|
| **CoWoS-S** | Silicio completo | HPC, AI (H100, MI300) | ~2500 mm² |
| **CoWoS-R** | RDL (Redistribution Layer) | Costo reducido | ~1700 mm² |
| **CoWoS-L** | LSI (Local Silicon Interconnect) | Híbrido | ~2x reticle |

---

## 3. Componentes Críticos

### 3.1 Through-Silicon Vias (TSV)

Conexiones verticales que atraviesan el interposer de silicio.

| Parámetro | Valor Típico | Límite Constitution.md |
|-----------|--------------|------------------------|
| Diámetro | 5-10 μm | - |
| Pitch mínimo | 40-50 μm | **≥ 40 μm (PHY-003)** |
| Densidad máxima | 5,000-10,000/mm² | **≤ 10,000/mm² (PHY-002)** |
| Profundidad | 50-100 μm | - |

### 3.2 Micro-bumps

Conexiones entre chiplets y el interposer.

| Parámetro | Valor Típico | Notas |
|-----------|--------------|-------|
| Pitch | 40-55 μm | **≥ 40 μm (PHY-003)** |
| Material | Cu pillar + SnAg cap | - |
| Altura | 25-45 μm | - |

### 3.3 HBM Stack

Memoria de Alto Ancho de Banda apilada verticalmente.

| Parámetro | HBM2e | HBM3 | HBM3e |
|-----------|-------|------|-------|
| Capacidad/stack | 8-16 GB | 16-24 GB | 24-36 GB |
| Ancho banda | 460 GB/s | 819 GB/s | 1.15 TB/s |
| Dies apilados | 8 | 8-12 | 8-12 |
| Altura stack | ~720 μm | ~775 μm | ~775 μm |

> [!IMPORTANT]
> **PHY-004:** Stack máximo de HBM: **12 dies** (límite térmico)

---

## 4. Restricciones Físicas (Constitution Compliance)

### 4.1 Límites Térmicos

```yaml
# Valores para constitution.md
thermal_limits:
  junction_temp_max_c: 105    # PHY-001
  interposer_temp_max_c: 95
  hbm_temp_max_c: 95
  power_density_max_w_mm2: 0.5
```

**Cálculo de Disipación:**
```
P_total = P_gpu + (N_hbm × P_hbm_per_stack)
P_density = P_total / Area_interposer

Si P_density > 0.5 W/mm² → RIESGO TÉRMICO
```

### 4.2 Límites de Routing

```yaml
# Valores para constitution.md
routing_limits:
  metal_layers_interposer: 4-6
  min_trace_width_um: 0.4
  min_trace_spacing_um: 0.4
  max_current_density_ma_um2: 2.5
  max_signal_length_mm: 15  # Para timing
```

### 4.3 Límites Estructurales

```yaml
# Valores para constitution.md
structural_limits:
  interposer_size_max_mm2: 2500  # ~1.7x reticle
  interposer_thickness_um: 100
  warpage_max_um: 200
  tsv_keep_out_zone_um: 5
```

---

## 5. Design Rules para Neuro-Weave

### 5.1 Reglas de Placement

| ID | Regla | Valor | Justificación |
|----|-------|-------|---------------|
| PL-001 | Separación HBM-GPU | ≥ 500 μm | Zona de transición térmica |
| PL-002 | HBM cerca del borde | ≤ 2 mm del edge | Facilita thermal vias |
| PL-003 | No chiplets en esquinas | 5 mm exclusion | Estrés mecánico |

### 5.2 Reglas de Routing

| ID | Regla | Valor | Justificación |
|----|-------|-------|---------------|
| RT-001 | Longitud máxima señal | ≤ 15 mm | Timing closure |
| RT-002 | Vías por señal HBM | ≤ 3 | Minimizar resistencia |
| RT-003 | Densidad rutas/mm | ≤ 500 | Manufacturabilidad |

### 5.3 Reglas de Power Delivery

| ID | Regla | Valor | Justificación |
|----|-------|-------|---------------|
| PW-001 | IR drop máximo | ≤ 3% Vdd | Integridad de señal |
| PW-002 | Decoupling caps | ≥ 1/mm² | Estabilidad |
| PW-003 | Ancho pista power | ≥ 10 μm | Capacidad corriente |

---

## 6. Integración con ATDI

Los smells de hardware se mapean a violaciones de estas reglas:

| Design Rule Violada | Smell Equivalente | ATDI Impact |
|---------------------|-------------------|-------------|
| TSV density > 10k/mm² | Dense Structure | +0.8 |
| > 8 conexiones/nodo | Hub-Like | +0.5 |
| Longitud señal > 15mm | Scattered Func. | +0.1 |
| Ciclo de señales | Cyclic Dep. | BLOQUEO |

---

## 7. Proveedores de Referencia

| Componente | Proveedor Principal | Alternativa |
|------------|---------------------|-------------|
| Interposer fab | TSMC | Samsung |
| HBM memory | SK Hynix | Samsung, Micron |
| Micro-bumps | TSMC (integrado) | ASE |
| Substrate | Ibiden | Shinko |
| EUV Lithography | ASML | (exclusivo) |

---

## 8. Checklist de Verificación CoWoS

```markdown
## Pre-Tape-out Checklist

### Física
- [ ] Densidad TSV ≤ 10,000/mm²
- [ ] Pitch micro-bumps ≥ 40 μm
- [ ] HBM stack ≤ 12 dies
- [ ] TJ máximo ≤ 105°C (simulación térmica)

### Routing
- [ ] Señal máxima ≤ 15 mm
- [ ] IR drop ≤ 3%
- [ ] Densidad routing ≤ 500/mm

### Estructural
- [ ] Área interposer ≤ 2500 mm²
- [ ] Warpage simulado ≤ 200 μm
- [ ] Keep-out zones respetadas

### ATDI
- [ ] Score ATDI < 0.3
- [ ] Zero ciclos de dependencia
- [ ] Zero hubs > 8 conexiones sin aprobación
```

---

*Documento CoWoS v1.0 | Silicon Synthesis Corp*
