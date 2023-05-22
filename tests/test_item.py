"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def product():
    return Item("Утюг", 5000, 25)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 125000


def test_apply_discount(product):
    assert product.apply_discount() is None
