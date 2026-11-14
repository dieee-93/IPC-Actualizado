# Bloque 3 — Ponderadores (borrador v0)

Capítulo de referencia: Manual 2020, Cap. 3 (*Expenditure weights*), con complementos del Cap. 1 y Cap. 9.
Convención de citas: ver `00_registro_de_decisiones.md`. `ENGHo-IG` = INDEC, *ENGHo 2017-18. Informe de gastos*; `NT4` = *Nota técnica N°4*.

## 1. Qué es un ponderador y por qué es el punto crítico

El ponderador de un producto es su participación en el gasto de consumo de la población de referencia. Define cuánto pesa cada variación de precio en el índice total. El manual indica que los ponderadores **deben ser de acceso público**, para generar confianza y transparencia (¶3.1).

## 2. Lo que establece el manual (verificado en el texto)

| Tema | Criterio del manual | Cita |
|---|---|---|
| Plutocrático vs. democrático | Plutocrático: participación en el gasto total. Democrático: promedio de participaciones por hogar. | ¶3.16-3.18 |
| Peso de un agregado elemental | Refleja el gasto total en todo el agregado, no solo en las variedades muestreadas. | ¶3.22 |
| Hogares rurales | Si hay datos, ponderar con hogares urbanos y rurales aunque los precios sean urbanos. | ¶3.26 |
| Subdeclaración en la encuesta | Se debe corregir o evaluar. | ¶3.41, ¶3.61-3.63 |
| Precisión de la encuesta | Usar coeficientes de variación para evaluar la calidad de las participaciones. | ¶3.42 |
| Fuentes | Encuesta de gastos (al menos cada 5 años) y cuentas nacionales como alternativa o complemento. | ¶3.43-3.46 |
| Mercados que cambian rápido | Ajustar con otras fuentes cuando la encuesta quedó vieja. | ¶3.67 |
| Productos poco importantes | Pueden excluirse del muestreo si su peso se reasigna a otros similares. | ¶3.68-3.70 |
| Actualización por precios | Los ponderadores **pueden** actualizarse por precios, pero eso **no los hace reflejar el consumo actual**: nuevos ponderadores solo salen de datos nuevos. | ¶3.75 |
| Frecuencia | Actualizar tan seguido como sea posible y **como mínimo cada cinco años**, con un calendario planificado. | ¶3.76 |
| Ponderadores fijos mucho tiempo | El índice deja de responder a la sustitución y a los cambios de preferencias. | ¶3.77 |
| Encuesta infrecuente | Aun así, revisar los pesos entre encuestas. | ¶3.78 |

## 3. Lo que hace el INDEC (Metod. §4.1-4.2)

1. **Fuente:** gasto de los hogares urbanos de la ENGHo 2004/05 por región, para las variedades que se relevaban en diciembre de 2015. Se estimó el *gasto promedio de los hogares por variedad*.
2. **Actualización por precios** hasta dic. 2015: se emparejaron las variedades del IPC-GBA base 1999 con las de 2015 y se usaron los relativos de precio de las variedades de especificación similar, **los mismos para todas las regiones**. Para agua, gas y electricidad se usaron los tarifarios provinciales de 2005 y de 2015.
3. **Ajuste ad hoc:** se redistribuyó el peso de telefonía fija, móvil e internet según facturación a dic. 2015, **manteniendo el total del grupo** estimado con la ENGHo.
4. El propio INDEC describe los ponderadores como *"híbridos"*: cantidades de la encuesta y precios del período base.

**No indica** de qué serie provienen los relativos de precio entre 2005 y 2015 usados en el paso 2, ni si los ponderadores son plutocráticos o democráticos. Queda como pendiente.

## 4. Lo que ofrece la ENGHo 2017-18 (verificado en ENGHo-MU, ENGHo-IG y NT4)

- **Cobertura:** hogares particulares de aglomerados o localidades de **2.000 habitantes o más**, en todo el país. **No cubre población rural dispersa ni localidades menores**; es una limitación a documentar frente a ¶3.26.
- **Campo:** noviembre de 2017 a noviembre de 2018.
- **Archivos:** hogares, personas, gastos (901.804 registros), artículos, equipamiento, hábitos y réplicas bootstrap.
- **Base de gastos:** una fila por artículo, con `pondera` (factor de expansión), `monto`, `cantidad`, `unmed`, `r_imputado` (gasto imputado o no), `forma_pago`, `tipo_negocio` (incluye *Internet*), `modo_adq` (en el negocio, internet, teléfono), `lugar_adq` (hasta *otro país*), región (6) y subregión (12).
- **Clasificación:** COICOP Argentina 2019 en cuatro niveles (división, grupo, clase, subclase) y el código de **artículo**, un nivel más fino que lo que el INDEC publica en el IPC.
- **Precisión:** las réplicas bootstrap permiten calcular errores de muestreo de cualquier participación (NT4).
- **Estructura de gasto, total país urbano (ENGHo-IG):** Alimentos y bebidas no alcohólicas 22,7%; Vivienda, agua, electricidad, gas y otros combustibles 14,5%; Transporte 14,3%.
- **Alquiler (ENGHo-IG):** 5,0% del gasto de consumo del total de hogares. Entre los **inquilinos**, el alquiler efectivo es 21,0% del gasto y la división Vivienda llega a 28,2%, contra 10,5% en los propietarios.

> Estas participaciones corresponden a la definición de gasto de consumo de la ENGHo, no necesariamente al alcance del IPC (que excluye, por ejemplo, el alquiler imputado). Hay que reconstruirlas con el alcance del IPC antes de compararlas.

## 5. Precedente argentino: IPCBA (Ciudad de Buenos Aires)

- Usó la ENGHo 2017-18 como fuente principal: 522 productos, de los cuales **438 se mantuvieron y 84 son nuevos** (16%).
- **Criterios de inclusión:** el producto debe representar **más de 0,02% del gasto total** o ser declarado por **más del 2,0% de los hogares**. El gasto de los productos excluidos se **reasigna** a productos similares.
- **No actualizó los ponderadores por precios**, citando el manual 2020. Su argumento: actualizar solo los precios deja fijas las cantidades, lo que generaría más sesgo.
- Ejemplo de cambio de peso: la telefonía móvil aumentó su ponderación respecto de la canasta anterior.

El INDEC sí actualizó por precios en 2016, y el manual dice que se **puede** hacerlo (¶3.75). El pasaje al que remite el IPCBA no está identificado todavía.

## 6. Decisiones del bloque

| ID | Decisión | Propuesta provisoria | Estado |
|---|---|---|---|
| D3.1 | Fuente principal | Microdatos de la ENGHo 2017-18 | provisorio |
| D3.2 | Alcance poblacional de los pesos | Hogares particulares de localidades de 2.000 o más habitantes. Documentar la exclusión rural. | cerrado por disponibilidad |
| D3.3 | Tipo de ponderador | Plutocrático para el índice principal (D1.4); democrático como análisis de sensibilidad, usando `pondera` | provisorio |
| D3.4 | Nivel de desagregación | Código de artículo (COICOP Argentina 2019). Umbrales de inclusión como en el IPCBA (0,02% del gasto o 2,0% de hogares) para evaluar. | abierto |
| D3.5 | Alcance y subdeclaración | Alinear con las exclusiones del IPC (D1.5) usando `r_imputado`. Evaluar subdeclaración contra cuentas nacionales (¶3.41, ¶3.44-3.46). | abierto |
| D3.6 | Actualización por precios | Evaluar **ambas** variantes y documentar el efecto. | abierto |
| D3.7 | Pesos por región y por tipo de negocio | Calcular por región y subregión; usar `tipo_negocio` para ponderar canales | provisorio |
| D3.8 | Ajustes por mercados cambiantes (¶3.67) | Servicios digitales y telecomunicaciones: la ENGHo 2017-18 es previa a la adopción actual; requiere fuente complementaria | abierto |
| D3.9 | Precisión y publicación | Calcular el CV de cada participación con las réplicas y publicar todos los ponderadores (¶3.1) | provisorio |
| D3.10 | Frecuencia de actualización | Se define en el Cap. 9. La ENGHo se hace cada 5 a 7 años, por lo que hacen falta fuentes intermedias. | abierto |

## 7. Pendientes de verificación (no inventar)

- [ ] **Descarga y licencia de los microdatos.** Los archivos existen y otros trabajos los usan, pero no verifiqué el enlace de descarga directa ni las condiciones de uso.
- [ ] Origen de los relativos de precio 2005-2015 en Metod. §4.2.
- [ ] Tipo de ponderador del INDEC (¶3.16-3.18 vs. su práctica).
- [ ] Pasaje del manual 2020 al que remite el IPCBA (nota 3) sobre no actualizar por precios.
- [ ] Reconstruir la estructura de la ENGHo 2017-18 con el alcance del IPC.
