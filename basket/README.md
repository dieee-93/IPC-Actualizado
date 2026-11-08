# Esquema de `basket_YYYY-MM.csv`

| Columna | Significado |
|---|---|
| `basket` | `actualizada`, `premium` o `actualizada;premium` (ítem compartido) |
| `category` | Rubro tal como figura en la planilla original (aún sin código COICOP) |
| `item` | Descripción del ítem (única dentro de cada canasta) |
| `quantity`, `unit` | Cantidad mensual del hogar de referencia y su unidad |
| `unit_price_ars` | Precio unitario en pesos |
| `price_month` | Mes del precio (`AAAA-MM`) |
| `source` | Fuente del precio o explicación del supuesto |
| `verification` | `verified` (fuente puntual) o `estimate` (supuesto propio) |

Pendiente: agregar `coicop` y `specification` (abierta/cerrada), y `weight_source`.
Nota: en la Premium, las cantidades "compartidas" salen de la Actualizada.
