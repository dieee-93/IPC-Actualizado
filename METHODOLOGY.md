# Metodología (v0.1 — decisiones tomadas y abiertas)

## Decidido (provisorio)
- **Fórmula:** canasta fija tipo Lowe/Laspeyres: `I(t) = 100 · Σ qᵢ·pᵢ(t) / Σ qᵢ·pᵢ(base)`. Igual que el INDEC, para poder comparar. No mide "costo de vida" (no captura sustitución).
- **Hogar de referencia:** 2 adultos (30–60 años), CABA/GBA, depto 2 ambientes en alquiler, auto gama media, 1 mascota (Actualizada) o 2 (Premium).
- **Dos variantes:** *Actualizada* (necesidades corregidas, incluye alquiler) y *Premium* (más consumo discrecional + capa digital).
- **Exclusiones** (igual que el IPC oficial): impuestos, aportes, cuotas de préstamos, ahorro/inversión.

## Abierto — hay que decidir antes de escalar
1. **Población objetivo:** ¿hogar de referencia o promedio nacional? Son índices distintos.
2. **Ponderadores:** ¿ENGHo 2017-18? **Pendiente verificar** si INDEC publica microdatos utilizables y a qué nivel de desagregación.
3. **Agregación elemental:** el INDEC usa media geométrica por variedad (Jevons); conviene igualar.
4. **Fórmula v2:** Fisher/Törnqvist (efecto sustitución) requiere cantidades mes a mes.
5. **Calidad y servicios:** salud (método indirecto para seguros), educación, recreación.
6. **Precios faltantes, sustitución de productos, estacionalidad.**
7. **Cambio de canasta:** reglas de empalme y período base.
8. **Recolección:** fuentes (Precios Claros u otras) y **términos de uso** antes de automatizar.
9. **Exposición cambiaria:** columna por ítem y serie en USD como métrica secundaria.

## Hallazgos que condicionan el diseño
- Los precios pasados no se pueden reconstruir: **hay que guardar el crudo cada mes**.
- Precio de lista de medicamentos ≠ costo para el afiliado tras recortes de cobertura (PAMI): no mezclar en un índice de precios.
- Amortizar bienes durables a su vida útil real baja el costo mensual respecto de una suposición plana.
