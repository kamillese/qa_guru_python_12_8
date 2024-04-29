"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(800) is True
        assert product.check_quantity(600) is True
        assert product.check_quantity(1100) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(200)
        assert product.check_quantity(800)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1100)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 25)
        assert cart.products[product] == 26
        cart.add_product(product, 32)
        assert cart.products[product] == 58

    def test_cart_remove_product(self, product, cart):
        cart.add_product(product, 82)
        cart.remove_product(product, 12)
        assert cart.products[product] == 70

        cart.add_product(product)
        cart.remove_product(product, 150)
        assert product not in cart.products

        cart.add_product(product)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_clear(self, product, cart):
        cart.add_product(product, 150)
        cart.clear()
        assert product not in cart.products

    def test_cart_get_total_price(self, product, cart):
        cart.add_product(product, 150)
        assert cart.get_total_price() == 15000

        cart.remove_product(product, 150)
        cart.clear()
        assert cart.get_total_price() == 0

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 120)
        cart.buy()
        assert product.quantity == 880

        product.quantity -= 200
        cart.add_product(product, 800)
        with pytest.raises(ValueError):
            cart.buy()
