import csv
import os

path = os.path.join('..', 'src', 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Добавлен метод repr, печатающий экземпляр класса"""
        return f"{self.__class__.__name__}{(self.__name, self.price, self.quantity)}"

    def __str__(self):
        """Добавлен метод str, печатающий название товара"""
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise AttributeError
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Классовые метод, который распаковывает csv файл и возвращает список продуктов из файла
        """
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for string in reader:
                name = string['name']
                price = string['price']
                quantity = string['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if isinstance(float(string), float):
            return int(float(string))
        else:
            raise ValueError("Строка содержит лишние символы")

    @property
    def name(self):
        """
        Геттер для приватного атрибута name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер name проверяет, что длина наименования товара не больше 10 символов
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")
