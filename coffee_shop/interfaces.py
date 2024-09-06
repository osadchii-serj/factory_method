from abc import ABC, abstractmethod


class Drink(ABC):

    @abstractmethod
    def get_a_drink(self):
        """
        Фабричный метод
        """
        pass
