from src.item import Item


class MixinLog:

    """Создан Мixin класс для инициализации атрибутов класса Item и добавляем новый атрибут language"""
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):

        """Проверяет, какой язык сейчас стоит на клавиатуре и изменяет его на другой"""

        if self.__language == "EN":
            self.__language = "RU"
            return self
        elif self.__language == "RU":
            self.__language = "EN"
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLog, Item):
    """Создаем класс с цепочкой наследования"""
    pass
