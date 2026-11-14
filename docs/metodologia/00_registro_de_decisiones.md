# Registro de decisiones metodológicas

Cada decisión se documenta con tres columnas: **qué recomienda el manual (2020)**, **qué hace hoy el INDEC** y **qué adoptamos**. Cada celda lleva su cita. Si algo no pudo verificarse en las fuentes, figura como *pendiente*, nunca como dato.

**Convención de citas**
- `Manual ¶x.y` = *Consumer Price Index Manual: Concepts and Methods* (2020), párrafo x.y. (`docs/fuentes/nucleo/`).
- `Metod. §x.y` = INDEC, *Metodología N°32* del IPC base dic. 2016 (`docs/fuentes/argentina/metodologia_ipc_nacional_2019.pdf`).
- `ENGHo-MU` = INDEC, *ENGHo 2017-2018. Manual de uso de la base usuario*.

**Estados:** `abierto` · `provisorio` (decidido, sujeto a lectura del capítulo indicado) · `cerrado`.

## Mapa: bloques de la metodología ↔ capítulos del manual 2020

| Bloque | Tema | Capítulo del manual | Archivo | Estado |
|---|---|---|---|---|
| 1 | Propósito y alcance | Cap. 1 (§C-D) y Cap. 2 | `01_proposito_y_alcance.md` | borrador v0 |
| 2 | Clasificación (COICOP 2018) | Cap. 2 | — | pendiente |
| 3 | Ponderadores (fuentes) | Cap. 3 | `03_ponderadores.md` | borrador v0 |
| 4 | Muestreo de productos y comercios | Cap. 4 | — | pendiente |
| 5 | Recolección y validación de precios | Cap. 5 (+ Apéndice F, web scraping) | — | pendiente |
| 6 | Precios faltantes y cambio de calidad | Cap. 6 | — | pendiente |
| 7 | Mantenimiento de la muestra | Cap. 7 | — | pendiente |
| 8 | Fórmulas y cálculo | Cap. 8 | — | pendiente |
| 9 | Actualización de ponderadores y empalme | Cap. 9 | — | pendiente |
| 10 | Scanner data | Cap. 10 | — | pendiente |
| 11 | Casos especiales (vivienda, seguros, etc.) | Cap. 11 | — | pendiente |

Números de capítulo y de página: verificados contra el índice del PDF del manual 2020 (la página del PDF coincide con la impresa).

## Hallazgos documentales relevantes

1. **Nota INDEC de febrero de 2011** (`argentina/ipc_metodologia_02_11.pdf`, 3 págs.): *"Implementación de índices encadenados en el IPC-GBA base abril 2008=100"*. Cita el manual de 2004 para sostener que no se pueden usar las mismas ponderaciones indefinidamente. Valor documental: el propio INDEC reconocía ese criterio. **Cautela:** corresponde al IPC-GBA del período de la intervención (2007-2015), por lo que no se toma como modelo de implementación.
2. **El INDEC ya parcheó ponderadores con fuentes distintas de la encuesta** en la base 2016: reponderó telefonía fija, móvil e internet según facturación, para corregir una estructura de gasto más antigua (Metod. §4.2). Es un precedente interno de uso de datos administrativos para actualizar pesos.
3. **El alquiler pesa 5,0% del gasto de consumo del total de hogares, pero 21,0% entre inquilinos** (ENGHo-IG, ENGHo 2017-18). Es la evidencia primaria detrás del problema de la CBT sin alquiler.
4. **La ENGHo 2017-18 es utilizable**: bases públicas de hogares, personas, gastos, artículos, equipamiento, hábitos y réplicas bootstrap; campo noviembre 2017 a noviembre 2018 (ENGHo-MU §1 y §2.1).

## Decisiones

Ver los archivos por bloque. Resumen del estado actual:

| ID | Decisión | Estado |
|---|---|---|
| D1.1 | Índice principal ("headline") | provisorio |
| D1.2 | Tipo de índice y enfoque de adquisición | provisorio |
| D1.3 | Cobertura geográfica y población de referencia | provisorio |
| D1.4 | Tipo de ponderadores (plutocráticos / democráticos) | abierto |
| D1.5 | Exclusiones | provisorio |
| D1.6 | Transacciones imputadas (vivienda propia, autoconsumo) | abierto (Cap. 3 y 11) |
| D1.7 | Compras por internet y servicios digitales | provisorio |
| D1.8 | Frecuencia de actualización de ponderadores | provisorio |

## Decisiones del bloque 3 (detalle en `03_ponderadores.md`)

| ID | Decisión | Estado |
|---|---|---|
| D3.1 | Fuente: microdatos ENGHo 2017-18 | provisorio |
| D3.2 | Alcance: localidades de 2.000 o más habitantes | cerrado por disponibilidad |
| D3.3 | Plutocrático (principal) y democrático (sensibilidad) | provisorio |
| D3.4 | Desagregación a nivel artículo y umbrales de inclusión | abierto |
| D3.5 | Alcance del IPC y subdeclaración | abierto |
| D3.6 | Actualización por precios: evaluar ambas variantes | abierto |
| D3.7 | Pesos por región y tipo de negocio | provisorio |
| D3.8 | Servicios digitales y telecomunicaciones | abierto |
| D3.9 | CV con réplicas y publicación de pesos | provisorio |
| D3.10 | Frecuencia de actualización (Cap. 9) | abierto |
