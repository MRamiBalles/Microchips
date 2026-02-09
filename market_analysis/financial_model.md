# Modelo Financiero - Silicon Synthesis Corp
## Análisis de Viabilidad Económica y TCO

> **Tipo:** Proyección a 5 años  
> **Escenario:** Instalación piloto en Países Bajos  
> **Fecha:** 2026-02-09

---

## 1. Supuestos Clave

### 1.1 Parámetros de Mercado

| Variable | Valor | Fuente |
|----------|-------|--------|
| Precio CoWoS wafer (2026) | $8,000-12,000 | Industry estimates |
| Crecimiento demanda AI packaging | 25% CAGR | Market reports |
| Premium "AI Trustworthy" | +15-25% | Estimación |
| Margen bruto target | 35-45% | Industry benchmark |

### 1.2 Parámetros Operativos

| Variable | Valor | Notas |
|----------|-------|-------|
| Capacidad inicial | 5,000 wafers/mes | Línea piloto |
| Capacidad objetivo Y5 | 20,000 wafers/mes | Expansión |
| Utilización Y1 | 40% | Ramp-up |
| Utilización Y3+ | 75% | Madurez |
| Yield inicial | 70% | Conservador |
| Yield maduro | 90% | Objetivo |

---

## 2. Inversión Inicial (CAPEX)

### 2.1 Desglose de Inversión

| Categoría | Monto (€M) | % Total |
|-----------|------------|---------|
| Equipos packaging (bonders, etc.) | 180 | 45% |
| Instalaciones cleanroom | 80 | 20% |
| Infraestructura IT/EDA | 25 | 6% |
| Testing equipment | 35 | 9% |
| Certificaciones (ISO, etc.) | 5 | 1% |
| Capital de trabajo | 50 | 12% |
| Contingencia | 25 | 6% |
| **Total CAPEX** | **400** | 100% |

### 2.2 Financiación

| Fuente | Monto (€M) | % | Costo |
|--------|------------|---|-------|
| Subsidio EU Chips Act | 140 | 35% | 0% |
| Préstamo BEI | 100 | 25% | 2% |
| Equity (Series A) | 120 | 30% | Dilución |
| Deuda bancaria | 40 | 10% | 5% |
| **Total** | **400** | 100% | |

---

## 3. Proyección de Ingresos

### 3.1 Modelo de Revenue

```
Revenue = Wafers_vendidos × Precio_promedio × (1 + Premium_compliance)
```

### 3.2 Proyección 5 Años

| Año | Capacidad | Utilización | Wafers | Precio (€) | Revenue (€M) |
|-----|-----------|-------------|--------|------------|--------------|
| Y1 | 5,000/mes | 40% | 24,000 | 9,500 | 228 |
| Y2 | 8,000/mes | 55% | 52,800 | 10,000 | 528 |
| Y3 | 12,000/mes | 70% | 100,800 | 10,500 | 1,058 |
| Y4 | 16,000/mes | 75% | 144,000 | 11,000 | 1,584 |
| Y5 | 20,000/mes | 80% | 192,000 | 11,500 | 2,208 |

### 3.3 Desglose por Segmento

| Segmento | Mix Y1 | Mix Y5 | Comentario |
|----------|--------|--------|------------|
| AI/HPC | 60% | 50% | Nvidia, AMD, startups |
| Defensa/Gov | 15% | 25% | Premium por compliance |
| Automotriz | 15% | 15% | ADAS chips |
| Otros | 10% | 10% | Networking, etc. |

---

## 4. Estructura de Costos (OPEX)

### 4.1 Costos Variables (por wafer)

| Componente | Costo (€) | % |
|------------|-----------|---|
| Materiales (interposer, bumps) | 2,200 | 35% |
| HBM procurement | 2,500 | 40% |
| Consumibles | 300 | 5% |
| Energía | 200 | 3% |
| Testing | 500 | 8% |
| Embalaje/logística | 100 | 2% |
| Depreciación equipos | 400 | 6% |
| **Total COGS/wafer** | **6,200** | 100% |

### 4.2 Costos Fijos Anuales

| Categoría | Y1 (€M) | Y5 (€M) | Notas |
|-----------|---------|---------|-------|
| Salarios (100→300 emp) | 12 | 36 | €120k avg |
| I+D / Neuro-Weave | 8 | 15 | 7% revenue |
| IT/Cloud/Agents | 3 | 8 | Software stack |
| Legal/Compliance | 2 | 4 | ISO audits |
| Ventas/Marketing | 3 | 10 | |
| G&A | 4 | 8 | |
| **Total OPEX Fijo** | **32** | **81** | |

---

## 5. P&L Proyectado

| Concepto | Y1 | Y2 | Y3 | Y4 | Y5 |
|----------|-----|-----|------|------|------|
| **Revenue (€M)** | 228 | 528 | 1,058 | 1,584 | 2,208 |
| COGS | (149) | (327) | (625) | (893) | (1,190) |
| **Gross Profit** | 79 | 201 | 433 | 691 | 1,018 |
| *Gross Margin* | *35%* | *38%* | *41%* | *44%* | *46%* |
| OPEX Fijo | (32) | (45) | (58) | (70) | (81) |
| **EBITDA** | 47 | 156 | 375 | 621 | 937 |
| *EBITDA Margin* | *21%* | *30%* | *35%* | *39%* | *42%* |
| Deprec. & Amort. | (20) | (25) | (30) | (35) | (40) |
| **EBIT** | 27 | 131 | 345 | 586 | 897 |
| Intereses | (5) | (5) | (4) | (3) | (2) |
| Impuestos (25%) | (6) | (32) | (85) | (146) | (224) |
| **Net Income** | 16 | 94 | 256 | 437 | 671 |

---

## 6. TCO de Empleados Digitales

### 6.1 Costo de Infraestructura Agéntica

| Componente | Costo Anual (€) | Escalabilidad |
|------------|-----------------|---------------|
| LLM API (inference) | 180,000 | Por uso |
| Cloud compute (agents) | 120,000 | Fijo |
| Storage (audit logs) | 24,000 | Lineal |
| Licencias EDA | 200,000 | Por seat |
| Mantenimiento Neuro-Weave | 150,000 | Equipo interno |
| **Total "Digital Workforce"** | **674,000** | |

### 6.2 Comparación: Humanos vs Agentes

| Actividad | FTE Humano | Costo/año (€) | Agente | Costo/año (€) | Ahorro |
|-----------|------------|---------------|--------|---------------|--------|
| Generación specs | 2 | 240,000 | AI-Doc | 40,000 | 83% |
| Optimización layout | 3 | 360,000 | AI-Opt | 80,000 | 78% |
| Verificación DRC | 2 | 240,000 | AI-Ver | 30,000 | 88% |
| Documentación ISO | 1 | 120,000 | AI-Doc | 20,000 | 83% |
| **Total** | **8 FTE** | **960,000** | **4 agents** | **170,000** | **82%** |

### 6.3 ROI de Automatización

```
ROI = (Ahorro_anual - Costo_infraestructura) / Costo_infraestructura
ROI = (790,000 - 674,000) / 674,000 = 17%
```

> [!NOTE]
> El ROI mejora significativamente en Y3+ cuando el volumen justifica mayor automatización.

---

## 7. Análisis de Riesgos Financieros

### 7.1 Sensibilidad

| Variable | Cambio | Impacto EBITDA Y5 |
|----------|--------|-------------------|
| Precio wafer | -10% | -€221M (-24%) |
| Utilización | -10pp | -€138M (-15%) |
| Costo HBM | +20% | -€95M (-10%) |
| Yield | -5pp | -€65M (-7%) |

### 7.2 Escenarios

| Escenario | Prob. | EBITDA Y5 | IRR |
|-----------|-------|-----------|-----|
| **Optimista** | 20% | €1.2B | 45% |
| **Base** | 60% | €937M | 35% |
| **Pesimista** | 20% | €450M | 18% |

---

## 8. Métricas de Inversión

| Métrica | Valor | Benchmark |
|---------|-------|-----------|
| Payback Period | 3.2 años | 3-5 años OK |
| IRR (5 años) | 35% | >25% target |
| NPV (10%, 5Y) | €580M | Positivo ✅ |
| Revenue/Employee Y5 | €7.4M | >€5M good |

---

## 9. Deuda Organizacional (Costo Oculto)

### 9.1 Riesgos de "Atrofia Digital"

| Riesgo | Probabilidad | Costo Potencial | Mitigación |
|--------|--------------|-----------------|------------|
| Deuda técnica code | Media | €2M rework | ATDI < 0.3 |
| Tool sprawl | Alta | €500K/año | Consolidación |
| Knowledge loss | Media | €1M por salida | Documentación |
| Skill gap | Alta | €300K training | Formación continua |

### 9.2 Presupuesto de Mitigación

| Partida | % Revenue | Y5 (€M) |
|---------|-----------|---------|
| Formación continua | 0.5% | 11 |
| Refactoring técnico | 1% | 22 |
| Auditorías externas | 0.3% | 7 |
| **Total prevención** | **1.8%** | **40** |

---

## 10. Conclusión

| Criterio | Evaluación |
|----------|------------|
| Viabilidad financiera | ✅ IRR 35%, NPV positivo |
| Riesgo de mercado | 🟠 Dependencia TSMC/HBM |
| Diferenciación | ✅ Compliance como moat |
| Escalabilidad | ✅ Modelo validado |

### Recomendación

**PROCEDER** con captación de Series A y aplicación EU Chips Act.

Factores críticos de éxito:
1. Asegurar subsidio ≥€120M
2. Contratos LTA con HBM supplier
3. Primera fab calificada operativa en 24 meses

---

*Modelo financiero v1.0 | Silicon Synthesis Corp*
*Sujeto a revisión con datos de mercado actualizados*
