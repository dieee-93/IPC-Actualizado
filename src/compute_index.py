"""Calcula el costo de una canasta y el índice entre dos snapshots de precios.

Fórmula (v0.1): índice de canasta fija tipo Lowe/Laspeyres.
    I(t) = 100 * sum(q_i * p_i(t)) / sum(q_i * p_i(base))
Las cantidades q_i se fijan en el período base (basket/basket_YYYY-MM.csv).
Ver METHODOLOGY.md para las decisiones abiertas.
"""
import csv
import sys
from pathlib import Path


def load_basket(path, basket):
    with open(path, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if basket in r["basket"].split(";")]
    if not rows:
        raise ValueError(f"No hay ítems para la canasta '{basket}' en {path}")
    return rows


def basket_cost(rows, prices=None):
    """Costo mensual. `prices` es opcional: {item: precio} para otro mes."""
    total = 0.0
    for r in rows:
        p = float(r["unit_price_ars"]) if prices is None else float(prices[r["item"]])
        total += float(r["quantity"]) * p
    return total


def load_prices(path):
    with open(path, encoding="utf-8") as f:
        return {r["item"]: float(r["unit_price_ars"]) for r in csv.DictReader(f)}


def lowe_index(rows, prices_t):
    """Índice (base = 100) de la canasta `rows` con los precios del mes t."""
    return 100.0 * basket_cost(rows, prices_t) / basket_cost(rows)


def by_category(rows, prices=None):
    out = {}
    for r in rows:
        p = float(r["unit_price_ars"]) if prices is None else float(prices[r["item"]])
        out[r["category"]] = out.get(r["category"], 0.0) + float(r["quantity"]) * p
    return out


if __name__ == "__main__":
    # uso: python src/compute_index.py basket/basket_2026-07.csv actualizada [data/raw/precios_2026-08.csv]
    basket_file, name = sys.argv[1], sys.argv[2]
    rows = load_basket(basket_file, name)
    print(f"Costo base ({name}): ${basket_cost(rows):,.2f}")
    if len(sys.argv) > 3:
        idx = lowe_index(rows, load_prices(sys.argv[3]))
        print(f"Índice vs. base: {idx:.2f}  (variación: {idx - 100:+.2f}%)")
