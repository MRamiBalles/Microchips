# Template: Especificación de Herramienta (SDD)

> Usar este template para documentar nuevas herramientas siguiendo Spec-Driven Development.

---

## Metadata

```yaml
tool_name: "[NOMBRE]"
version: "0.1.0"
status: "draft|review|approved"
owner_accountable: "[ROL HUMANO]"
owner_responsible: "[AGENTE IA]"
last_updated: "YYYY-MM-DD"
```

---

## 1. Resumen Ejecutivo

_Descripción de 2-3 líneas del propósito de la herramienta._

---

## 2. Goals (Objetivos)

| ID | Objetivo | Métrica de Éxito | Prioridad |
|----|----------|------------------|-----------|
| G-01 | ... | ... | P0/P1/P2 |

---

## 3. Constraints (Restricciones)

### 3.1 Restricciones de Constitution.md

_Listar reglas físicas/éticas que aplican._

### 3.2 Restricciones Técnicas

_Listar limitaciones técnicas (memoria, CPU, etc.)._

---

## 4. User Journey

_Diagrama de secuencia o descripción paso a paso._

---

## 5. Stack Tecnológico

| Capa | Tecnología | Justificación |
|------|------------|---------------|
| ... | ... | ... |

---

## 6. Interfaces

### 6.1 CLI Commands

```bash
# Ejemplos de comandos
```

### 6.2 Input Files

```yaml
# Schema de archivos de entrada
```

### 6.3 Output Files

| Archivo | Formato | Descripción |
|---------|---------|-------------|
| ... | ... | ... |

---

## 7. Quality Gates

| Gate | Umbral | Acción si Falla |
|------|--------|-----------------|
| ... | ... | ... |

---

## 8. Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| ... | ... | ... | ... |

---

## 9. Roadmap

| Milestone | Entregable | Fecha Objetivo |
|-----------|------------|----------------|
| ... | ... | ... |

---

## Checklist de Aprobación

- [ ] Spec revisado por CPO
- [ ] Constraints verificados contra constitution.md
- [ ] Riesgos evaluados por Ethics Officer
- [ ] Aprobación formal del CTO

---

*Template v1.0 | Silicon Synthesis Corp*
