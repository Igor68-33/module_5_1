# Атрибуты и методы объекта
class House:
    """
    атрибут:
    name - имя,
    number_of_floors - кол-во этажей
    метод:
    go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
    """

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
