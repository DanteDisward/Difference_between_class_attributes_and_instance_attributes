def type_int_or_house(value):
    if isinstance(value, House):
        value = value.number_of_floors
    return value


class House:
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > 1 and not new_floor > self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == type_int_or_house(other)

    def __lt__(self, other):
        return self.number_of_floors < type_int_or_house(other)

    def __le__(self, other):
        return self.number_of_floors <= type_int_or_house(other)

    def __gt__(self, other):
        return self.number_of_floors > type_int_or_house(other)

    def __ge__(self, other):
        return self.number_of_floors >= type_int_or_house(other)

    def __ne__(self, other):
        return self.number_of_floors != type_int_or_house(other)

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + type_int_or_house(
            value)  # По идее не правильно, так как значение меняется без операта '='
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    houses_history = []


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
