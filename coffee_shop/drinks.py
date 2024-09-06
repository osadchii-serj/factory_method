from interfaces import Drink


class HoneyRiff(Drink):

    def __init__(self) -> None:
        self.__type_of_drink = "Кофейные коктейли"
        self.__name = "Медовый рафф"
        self.__espresso = "Эспрессо"
        self.__cinnamon = "Корица"
        self.__cream = "Сливки"
        self.__honey = "Мед"

    def __make_a_drink(self, espresso, cream, honey, cinnamon):
        ingredients = {
            cinnamon: "(по вкусу)",
            espresso: 30,
            cream: 100,
            honey: 1,
        }

        heating = f"Подогрев {cream} - {ingredients[cream]} мл, 10-15% жирности до 60 градусов."
        brewing = f"Заваривание {espresso} - {ingredients[espresso]} мл и добавление {honey} - {ingredients[honey]} ч.ложка, размешивание до растворения."
        compound = f"Соединение {espresso} и {cream}, взбивание до появления пены, посыпав {cinnamon} {ingredients[cinnamon]}\n"

        return f"{heating}\n{brewing}\n{compound}"

    def get_a_drink(self):
        print(f"\n{self.__type_of_drink}")
        print(f"{self.__name}\n")
        print("Приготовление ...")
        print(
            self.__make_a_drink(
                self.__espresso, self.__cream, self.__honey, self.__cinnamon
            )
        )
        return f"Напиток {self.__name} готов!\n"


class CoffeeMulledWineWithRaspberry(Drink):

    def __init__(self) -> None:
        self.__name = "Кофейный глинтвейн с малиной"
        self.__type_of_drink = "Кофейные коктейли"
        self.__espresso = "Эспрессо"
        self.__raspberry = "Малина"
        self.__spices = "Пряности"
        self.__sugar = "Сахар"
        self.__water = "Вода"

    def __make_a_drink(self, espresso, raspberry, sugar, water, spices):
        ingredients = {
            spices: "(корица, кардамон, бадьян)",
            espresso: 200,
            raspberry: 3,
            sugar: 1,
            water: 2,
        }

        mixing = f" Смешивание {sugar} {ingredients[sugar]} ст. ложки, {spices} - {ingredients[spices]}, {raspberry} - {ingredients[raspberry]} ст. ложки и\n немного {water} - {ingredients[water]} ст. ложки, доведение до загустения.\n"
        cup = f"Заливание {espresso} - {ingredients[espresso]} мл\n"

        return f"{mixing} {cup}"

    def get_a_drink(self):
        print(f"\n=== {self.__type_of_drink} ===")
        print(f"=== {self.__name} ===\n")
        print(" Приготовление ...")
        print(
            self.__make_a_drink(
                self.__espresso,
                self.__raspberry,
                self.__sugar,
                self.__water,
                self.__spices,
            )
        )
        return f"=== Напиток {self.__name} готов! ===\n"


class GingerAndOrangeTea(Drink):

    def __init__(self) -> None:
        self.__name = "Чай с имбирем и апельсином"
        self.__type_of_drink = "Чайные коктейли"
        self.__apple_juice = "Яблочный сок"
        self.__orange = "Апельсин"
        self.__ginger = "Имбирь"
        self.__syrups = "Сиропы"
        self.__tea = "Чай"

    def __make_a_drink(self, apple_juice, orange, ginger, syrups, tea):
        ingredients = {
            apple_juice: "(подогретый)",
            syrups: "(по желанию)",
            orange: "(по вкусу)",
            ginger: "(по вкусу)",
            tea: 100,
        }

        brewing_tea = f"@@@ заваривание {self.__tea} - {ingredients[tea]} мл @@@"
        mixing_whipping = f">>> смешивание {self.__ginger} - {self.__orange} взбивание >>>"
        adding_to_tea_syrups = f"добавление в {self.__tea} - {self.__syrups} {ingredients[syrups]}"
        adding_to_tea_apple_juice = f"добавление в {self.__tea} - {self.__apple_juice} {ingredients[apple_juice]}"

        return f"{brewing_tea}\n{mixing_whipping}\n{adding_to_tea_syrups}\n{adding_to_tea_apple_juice}\n"
    
    def get_a_drink(self):
        print(f"\n{self.__type_of_drink}")
        print(f"{self.__name}\n")
        print(" Приготовление ...")
        presenter = "Пироженки"
        print(self.__make_a_drink(
            self.__apple_juice, 
            self.__orange, 
            self.__ginger, 
            self.__syrups, 
            self.__tea)
            )
        print("Презент от заведения")
        print("-" * 13)
        print(f"| {presenter} |")
        print("-" * 13)
        return f"(--- Напиток {self.__name} готов! ---)\n"
