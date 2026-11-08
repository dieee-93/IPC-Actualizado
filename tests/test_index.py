import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from compute_index import load_basket, basket_cost, lowe_index

BASKET = Path(__file__).resolve().parents[1] / "basket" / "basket_2026-07.csv"


def test_totales_coinciden_con_planilla_original():
    assert round(basket_cost(load_basket(BASKET, "actualizada")), 2) == 2759341.42
    assert round(basket_cost(load_basket(BASKET, "premium")), 2) == 3506635.42


def test_indice_base_es_100():
    rows = load_basket(BASKET, "actualizada")
    prices = {r["item"]: float(r["unit_price_ars"]) for r in rows}
    assert abs(lowe_index(rows, prices) - 100.0) < 1e-9


def test_suba_uniforme_del_10_por_ciento():
    rows = load_basket(BASKET, "actualizada")
    prices = {r["item"]: float(r["unit_price_ars"]) * 1.10 for r in rows}
    assert abs(lowe_index(rows, prices) - 110.0) < 1e-6
