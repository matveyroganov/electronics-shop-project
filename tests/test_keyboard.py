from src.keyboard import Keyboard
import pytest


@pytest.fixture
def product():
    return Keyboard("Клавиатура", 5000, 5)


@pytest.fixture
def product_1():
    return Keyboard("Российская Клавиатура", 4000, 5, "RU")


def test_change_lang(product, product_1):
    assert product.change_lang().language == "RU"
    assert product_1.change_lang().language == "EN"
