from src.phone import Phone
import pytest


@pytest.fixture
def product():
    return Phone("Samsung", 25000, 15, 5)


def test_repr(product):
    assert repr(product) == "Phone('Samsung', 25000, 15, 5)"


