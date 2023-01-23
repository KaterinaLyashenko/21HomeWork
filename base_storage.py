from typing import Dict

from abstract_storage import AbstarctStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstarctStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:  #amount- кол-во товара, который хотим добавить
    #Проверить что места достаточно
        if self.get_free_space() < amount:
            raise NotEnoughSpace

    #Добавить товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
    #Есть ли такой товар и хватает ли его на складе
        if name not in self.__items[name] or self.__items[name] < amount:
            raise NotEnoughProduct
    #Вычесть необходимое число товара.Если товара станет 0 - удалить его из списка
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)


    def get_free_space(self) -> int:
    #Посчитать сумму значений в словаре __items. Вычесть ее из __capacity
        return self.__capacity - sum(self.__items.values())

    #def get_items(self) -> Dict:
    #Возвращает items
    #    return self.__items

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, new_data):
        self.__items = new_data

    def get_unique_items_count(self):
    # Возвращает кол-во уникального товара
        return len(self.__items)