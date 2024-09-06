from drinks import CoffeeMulledWineWithRaspberry
from drinks import GingerAndOrangeTea
from drinks import HoneyRiff
from interfaces import Drink
from random import choice

list_of_drinks = [
    CoffeeMulledWineWithRaspberry(),
    GingerAndOrangeTea(),
    HoneyRiff(),
]


def client_code(drink: Drink):
    print(drink.get_a_drink())


for _ in range(10):
    client_code(choice(list_of_drinks))
    print("***" * 30)
