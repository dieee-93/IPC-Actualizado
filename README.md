# IPC-Actualizado

Proyecto para construir, de forma transparente y reproducible, un índice de precios al consumidor propio para Argentina, apoyado en el estándar internacional (*Manual del IPC: Teoría y Práctica*, OIT/FMI/OCDE/Eurostat/ONU/Banco Mundial) y contrastado contra el IPC y las canastas oficiales del INDEC.

> **Estado: v0.1 (julio 2026).** Un único mes de precios (la base). Todavía **no hay una tasa de inflación propia**: hace falta al menos un segundo snapshot mensual. Ver `METHODOLOGY.md`.

## Por qué existe

El IPC oficial usa ponderadores de la ENGHo 2004/05 y las canastas de pobreza (CBA/CBT) de la ENGHo 1996/97; la CBT no incluye alquiler; y la lista de las 609 variedades con su ponderación no es pública. Este proyecto no pretende "reemplazar" al INDEC: busca hacer explícito qué se mide, con qué datos y con qué supuestos.

## Estructura

```
basket/            definición de la canasta (CSV): ítem, cantidad, precio, fuente, nivel de verificación
data/raw/          snapshots mensuales de precios, con fecha (NO se pueden reconstruir después)
data/processed/    series calculadas
src/               cálculo del índice
tests/             pruebas (los totales deben coincidir con la planilla original)
docs/              metodología, decisiones y referencias
```

## Uso rápido

```bash
pip install pytest
python -m pytest -q
python src/compute_index.py basket/basket_2026-07.csv actualizada
# con un segundo mes (CSV con columnas item,unit_price_ars):
python src/compute_index.py basket/basket_2026-07.csv actualizada data/raw/precios_2026-08.csv
```

## Reglas del proyecto

1. **No se inventan datos.** Cada precio lleva su fuente y una marca `verified` / `estimate`.
2. **Las estimaciones se dicen como tales** y se reemplazan cuando hay dato real.
3. **Se guarda el precio crudo de cada mes**, con fecha.
4. Todo cambio de método queda en `CHANGELOG.md` con el motivo.

## Limitaciones conocidas

- El hogar de referencia (2 adultos, CABA/GBA, depto 2 amb. en alquiler, auto propio) **no representa al promedio nacional**.
- No se replican las 609 variedades del INDEC (no son públicas).
- Hay ítems en `estimate` en `basket/basket_2026-07.csv`; se pueden listar con `grep estimate`.
- Las cantidades son supuestos de consumo, no gasto relevado (falta una fuente de ponderadores real).
