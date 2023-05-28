"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def product():
    return Item("Утюг", 5000, 25)


@pytest.fixture
def product_1():
    return Item("Холодильник", 5000, 25)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 125000


def test_apply_discount(product):
    assert product.apply_discount() is None


def test_name(product):
    assert product.name == "Утюг"


def test_exception_long_name(product_1):
    with pytest.raises(Exception):
        product_1.name = "Длина наименования товара превышает 10 символов"


def test_string_to_number():
    assert Item.string_to_number("0.5") == 0


def test_string_with_symbols():
    with pytest.raises(ValueError):
        Item.string_to_number("0w2")


def test_repr(product):
    assert repr(product) == "Item('Утюг', 5000, 25)"


def test_str(product):
    assert str(product) == "Утюг"
