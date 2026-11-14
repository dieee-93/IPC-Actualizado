# Bloque 1 — Propósito y alcance (borrador v0)

## 1. Propósito del proyecto

Proyecto **educativo, con nivel académico**: construir una metodología de medición de la inflación para Argentina que (a) siga la línea metodológica del INDEC, que se apoya en el manual internacional OIT/FMI/OCDE/Eurostat/ONU/Banco Mundial, (b) esté **actualizada** a los patrones de consumo actuales y (c) conserve los consumos que no cambiaron.

El manual establece que *"el propósito de un IPC debe guiar todos los aspectos de su construcción"*, que es poco probable que un único índice sirva igual para todos los usos, y que debe identificarse explícitamente un índice principal (*headline*) (Manual ¶1.8). Por eso este bloque fija primero qué se mide y para quién.

## 2. Usos que declara el INDEC

Medida de inflación del país (política económica, contratos, tasas, remuneraciones), indicador del poder de compra, deflactor de series económicas, comparación de subconjuntos de precios y variación promedio de precios de bienes y servicios representativos del consumo de los hogares (Metod. §1.1).

El manual enumera tres usos principales: indexación, deflación de cuentas nacionales y medición de inflación (Manual ¶1.7, ¶1.10).

## 3. Decisiones de alcance

| ID | Tema | Manual 2020 | INDEC (Metod. N°32) | Propuesta provisoria | Se confirma en |
|---|---|---|---|---|---|
| D1.1 | Índice principal | Un índice por propósito; identificar el *headline* (¶1.8). Para inflación general, cuanto más abarcativo, mejor (¶1.34). | IPC nacional urbano, único headline, más 6 índices regionales (§1). | **Headline:** IPC de hogares urbanos de todo el país. Variantes por grupo de hogares (ej. jubilados, quintiles) como índices **separados y nombrados**, no mezclados con el principal (¶1.36). | Cap. 2 |
| D1.2 | Tipo de índice | El ideal es un índice superlativo (Fisher); en la práctica casi todos usan ponderadores de un período anterior (¶1.11, ¶1.16). Debe declararse públicamente qué tipo se calcula (¶1.13). | Laspeyres, con ponderadores de ENGHo 2004/05 actualizados por precios a dic. 2015 (§4.2). | **Índice de canasta fija tipo Lowe/Laspeyres** (comparable con el INDEC), declarando que no es un Laspeyres puro (¶1.13). Un índice superlativo se calcula en forma retrospectiva como referencia (Cap. 8). | Cap. 8 |
| D1.2b | Enfoque de gasto | Adquisiciones, uso o pagos; la mayoría usa adquisiciones (¶1.21-1.22). | Adquisiciones a precios de contado, incluso para durables (§2.2). | **Adquisiciones**, igual que el INDEC. | Cap. 9 y 11 |
| D1.3 | Cobertura geográfica | Concepto nacional (hogares residentes) o doméstico (todo gasto en el territorio) (¶1.24). En principio, todo el territorio; el costo puede justificar acotar (¶1.27, ¶1.29). | Hogares particulares de áreas urbanas; precios en 39 aglomerados; 6 regiones (§2.5, §2.6). | **Urbano nacional, 39 aglomerados**, como el INDEC. Si la ENGHo permite, ponderar con hogares urbanos y rurales combinados aunque los precios sean urbanos (¶1.30). | Cap. 3 |
| D1.4 | Ponderadores | Plutocráticos (gasto total) para inflación general y deflactores; democráticos (promedio de participaciones por hogar) para el impacto en el hogar promedio, rara vez calculados (¶1.35-1.36). | **No declara** cuál usa (búsqueda de "plutocr/democr" sin resultados). | **Abierto.** Headline plutocrático por defecto. Calcular la variante democrática como análisis de sensibilidad. Verificar qué usa el INDEC. | Cap. 3 |
| D1.5 | Exclusiones | Se pueden excluir bienes ilegales o inmedibles; **no** excluir categorías por motivos no estadísticos (ej. alcohol y tabaco) en el índice total (¶1.37-1.39). | Excluye impuestos, aportes, cuotas de préstamos, donaciones, inversión física o financiera, alquiler imputado de propietarios y SIFMI; excluye intereses (§2.2). | **Mismas exclusiones que el INDEC.** Las variantes sin alcohol/tabaco, si existen, se publican aparte. | Cap. 2 |
| D1.6 | Transacciones imputadas | La elección entre adquisición, uso o pagos afecta sobre todo el peso de la vivienda ocupada por sus propietarios (¶1.22). El manual distingue además transacciones imputadas de precios imputados (¶1.41). | **Excluye** el alquiler imputado de propietarios (§2.2). | **Abierto.** Decidir en Cap. 3 y 11 (vivienda propia, autoconsumo, bienes gratuitos del Estado). | Cap. 3 y 11 |
| D1.7 | Compras por internet | Bajo concepto nacional, incluir compras en sitios del exterior y convertirlas al tipo de cambio relevante; bajo concepto doméstico, la mayoría de las oficinas incluye compras desde el hogar (¶1.25-1.26). | **Pendiente verificar** su tratamiento en la Metodología N°32. La ENGHo 2017-18 sí registra compras por internet y en otro país (`tipo_negocio`, `modo_adq`, `lugar_adq`). | **Incluir** servicios digitales y compras online, convertidos al tipo de cambio relevante. | Cap. 3 y 11 |
| D1.8 | Actualización de ponderadores | Como mínimo cada 5 años; muchas oficinas pasan a actualización anual o bianual (¶1.15). | Ponderadores de ENGHo 2004/05 (campo oct. 2004–dic. 2005) en la base 2016 (§4.2). | **Diseñar para actualización anual o bianual**; ponderadores base de la ENGHo 2017-18, con fuentes intermedias a definir. | Cap. 9 |

## 4. Observaciones que condicionan lo que sigue

1. **La vivienda propia es el punto que más afecta a la comparación con nuestras canastas.** Si el IPC excluye el alquiler imputado de propietarios (Metod. §2.2), el peso de vivienda refleja a la vez a inquilinos y propietarios. D1.6 se resuelve con evidencia del Cap. 3 y 11, no a priori.
2. **El headline no representa a cada hogar.** Cuanto más específico el propósito (jubilados, inquilinos, hogares de bajos ingresos), más conviene una variante propia con ponderadores propios (¶1.10, ¶1.36).
3. **Los pesos de la ENGHo 2017-18 tienen más de 8 años.** Eso ya supera el plazo de 5 años que el manual fija como mínimo de actualización (¶1.15). Es la mejor fuente disponible hoy, no una solución definitiva (ver Cap. 9).

## 5. Pendientes de verificación (no inventar)

- [ ] Qué tipo de ponderadores usa el INDEC (D1.4).
- [ ] Tratamiento de compras por internet en la Metodología N°32 (D1.7).
- [x] Cobertura de la ENGHo 2017-18: localidades de 2.000 o más habitantes; no cubre población rural dispersa (ver `03_ponderadores.md`).
- [x] Desagregación: código de artículo COICOP Argentina 2019, más fino que lo publicado en el IPC (ver `03_ponderadores.md`).
- [ ] Condiciones de uso y redistribución de los microdatos.
