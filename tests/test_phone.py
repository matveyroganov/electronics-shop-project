from src.phone import Phone
import pytest


@pytest.fixture
def product():
    return Phone("Samsung", 25000, 15, 5)


@pytest.fixture
def product_1():
    return Phone("Xiaomi", 20000, 10, 0)


def test_repr(product):
    assert repr(product) == "Phone('Samsung', 25000, 15, 5)"


def test_number_of_sim(product):
    assert product.number_of_sim == 5


def test_null_number_of_sim(product_1):
    with pytest.raises(ValueError):
        product_1.number_of_sim = "Количество физических SIM-карт должно быть целым числом больше нуля."
