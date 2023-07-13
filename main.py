# Magic Methods
# class Rational:
#     def __init__(self, a=0, b=1):
#         a = int(a)
#         b = int(b)
#         if b == 0:
#             raise ValueError("Illegal value of the denominator")
#         self.__numerator = a
#         self.__denominator = b
#         self.__reduce()
#
#     # Сокращение дроби.
#     def __reduce(self):
#         # Функция для нахождения наибольшего общего делителя
#         def gcd(a, b):
#             if a == 0:
#                 return b
#             elif b == 0:
#                 return a
#             elif a >= b:
#                 return gcd(a % b, b)
#             else:
#                 return gcd(a, b % a)
#         sign = 1
#         if (self.__numerator > 0 > self.__denominator) or \
#                 (self.__numerator < 0 < self.__denominator):
#             sign = -1
#         a, b = abs(self.__numerator), abs(self.__denominator)  # abs -> вернет положительное число
#         c = gcd(a, b)
#         self.__numerator = sign * (a // c)
#         self.__denominator = b // c
#
#         # Клонировать дробь.
#     def __clone(self):
#         return Rational(self.__numerator, self.__denominator)
#
#     @property
#     def numerator(self):
#         return self.__numerator
#
#     @numerator.setter
#     def numerator(self, value):
#         self.__numerator = int(value)
#         self.__reduce()
#
#     @property
#     def denominator(self):
#         return self.__denominator
#
#     @denominator.setter
#     def denominator(self, value):
#         value = int(value)
#         if value == 0:
#             raise ValueError("Illegal value of the denominator")
#         self.__denominator = value
#         self.__reduce()
#
#     # Привести дробь к строке.
#     def __str__(self):
#         return f"{self.__numerator} / {self.__denominator}"
#
#     def __repr__(self): # repr - практически то же самое, что и string, но исп больше для технических текстовок
#         return self.__str__()
#
#     # Привести дробь к вещественному значению.
#     def __float__(self):
#         if self.__denominator == 0:
#             raise ZeroDivisionError()
#         return self.__numerator / self.__denominator
#
#     # Привести дробь к логическому значению.
#     def __bool__(self):
#         return self.__numerator != 0
#
#     # Сложение обыкновенных дробей.
#     def __iadd__(self, rhs):  # += сложение с присваиванием, напимер x += 42
#         if isinstance(rhs, Rational):
# # Описание: Функция isinstance() вернет True , если проверяемый объект object является
# # экземпляром указанного класса (классов) или его подкласса (прямого, косвенного или виртуального).
# # Если объект object не является экземпляром данного типа, то функция всегда возвращает False .
#             a = self.numerator * rhs.denominator + \
#                 self.denominator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     # drob1 + drob2 ====> drob1 += drob2
#     def __add__(self, rhs):  # +
#         return self.__clone().__iadd__(rhs)
#
#     # Вычитание обыкновенных дробей.
#     def __isub__(self, rhs):  # -= вычитание с присваиванием
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.denominator - \
#                 self.denominator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __sub__(self, rhs):  # -
#         return self.__clone().__isub__(rhs)
#
#     # Умножение обыкновенных дробей.
#     def __imul__(self, rhs):  # *=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.numerator
#             b = self.denominator * rhs.denominator
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __mul__(self, rhs):  # *
#         return self.__clone().__imul__(rhs)
#
#     # Деление обыкновенных дробей.
#     def __itruediv__(self, rhs):  # /=
#         if isinstance(rhs, Rational):
#             a = self.numerator * rhs.denominator
#             b = self.denominator * rhs.numerator
#             if b == 0:
#                 raise ValueError("Illegal value of the denominator")
#             self.__numerator, self.__denominator = a, b
#             self.__reduce()
#             return self
#         else:
#             raise ValueError("Illegal type of the argument")
#
#     def __truediv__(self, rhs):  # /
#         return self.__clone().__itruediv__(rhs)
#
#     # Отношение обыкновенных дробей.
#     def __eq__(self, rhs):  # ==
#         if isinstance(rhs, Rational):
#             return (self.numerator == rhs.numerator) and \
#                    (self.denominator == rhs.denominator)
#         else:
#             return False
#
#     def __ne__(self, rhs):  # !=
#         if isinstance(rhs, Rational):
#             return not self.__eq__(rhs)
#         else:
#             return False
#
#     def __gt__(self, rhs):  # >
#         if isinstance(rhs, Rational):
#             return self.__float__() > rhs.__float__()
#         else:
#             return False
#
#     def __lt__(self, rhs):  # <
#         if isinstance(rhs, Rational):
#             return self.__float__() < rhs.__float__()
#         else:
#             return False
#
#     def __ge__(self, rhs):  # >=
#         if isinstance(rhs, Rational):
#             return not self.__lt__(rhs)
#         else:
#             return False
#
#     def __le__(self, rhs):  # <=
#         if isinstance(rhs, Rational):
#             return not self.__gt__(rhs)
#         else:
#             return False
#
#
# if __name__ == '__main__':
#     r1 = Rational(3, 4)
#     print(float(r1))
#     print(r1)
#     print(f"r1 = {r1}")
#     r2 = Rational(5, 6)
#     # r1 += r2
#     print(r1)
#     print(f"r2 = {r2}")
#     print(f"{r1} + {r2} = {r1 + r2}")
#     print(f"{r1} - {r2} = {r1 - r2}")
#     print(f"{r1} * {r2} = {r1 * r2}")
#     print(f"{r1} / {r2} = {r1 / r2}")
#     print(f"{r1} == {r2} {r1 == r2}")
#     print(f"{r1} != {r2} {r1 != r2}")
#     print(f"{r1} > {r2} {r1 > r2}")
#     print(f"{r1} < {r2} {r1 < r2}")
#     print(f"{r1} >= {r2} {r1 >= r2}")
#     print(f"{r1} <= {r2} {r1 <= r2}")


####
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

    def __add__(self, other):
        if isinstance(other, Car):
            return self.price + other.price
        elif other > 0:
            return self.price + other
        else:
            raise ValueError("Incorrect param")


#
#
toyota = Car("camry", 123456)
toyota.show_info()

bmw = Car("x5", 321654)
bmw.show_info()

result = toyota + bmw
print(result)

result = toyota + 123
print(result)

# дописать остальные операторы в классе Car


# 1
# абстрактные методы

from abc import ABC, abstractmethod
#
#
# абстрактный класс - содержит в себе абстрактные методы, то есть методы без реализации помеченные
# декоратором @abstractmethod из модуля abc, а так же методы с реализацией (обычные методы)
# Так как абстрактный класс содержит в себе абстрактные методы -
# все дочерние классы обязаны предоставить реализации этих методов,
# так же нельзя создать экземпляр класса у которого есть хотя бы один абстрактный метод

# интерфейс - это класс, у которого только абстрактные методы,
# такой класс необходим если вам нужно создать некий контракт, обязательство предоставить реализацию этих методов для
# других классов наследников
# class Polygon(ABC):
#     @abstractmethod  # этот метод без реализации и все дочерние классы обязаны предоставить реализацию этого метода
#     def noofsides(self):
#         pass
#
#     def show_info(self):
#         print("I am from polygon")
#
#
# class Triangle(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")


# TypeError: Can't instantiate abstract class Polygon with abstract method noofsides
# test = Polygon()
# test.noofsides()

# Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()
# K.show_info()

# 2
# Полиморфизм функций
# print(len("Программист"))
# print(len(["Яблоко", "Банан", "Груша"]))
# print(len({"Имя": "Максим", "Address": "Киев"}))
#
# #Полиморфизм классов
# class Cat:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я кошка. Меня зовут {self.klichka}. Мой возраст {self.vozrast} лет")
#
#     def say(self):
#         print("Мяу")
#
#
# class Dog:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я собака. Меня зовут {self.klichka}. Мой возраст {self.vozrast} лет")
#
#     def say(self):
#         print("Гав")
#
#     def hello(self):
#         print(f"Hello {self.klichka}")
#
#
# class PetDog(Dog):
#     def __init__(self, klichka, vozrast, owner):
#         super().__init__(klichka, vozrast)
#         self.owner = owner
#
#     # переопределение метода
#     def hello(self):
#         super().hello()
#         print(f"Owner: {self.owner}")
#
#
# test = PetDog("test", 1, "Vasya")
# test.hello()
#
# cat_obj = Cat("Муська", 10)
# dog_obj = Dog("Барон", 12)
#
# for pet in (cat_obj, dog_obj):
#     pet.say()
#     pet.status()
#     pet.say()


# # Полиморфизм и наследование
# from math import pi
# from abc import ABC, abstractmethod
#
#
# # интерфейс
# class BaseShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Shape(BaseShape):
#     def __init__(self, name):
#         self.name = name
#
#     # def area(self):
#     #     pass
#
#     def info(self):
#         return "Я двухмерная форма."
#
#     # строковое представление объекта
#     def __str__(self):
#         return "строковое представление объекта Shape"
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Квадрат")
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def info(self):
#         return "Квадраты имеют каждый угол равный 90 градусам."
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Круг")
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#
# class AreaCalculator:
#     def __init__(self, geom_object):
#         self.geom_object = geom_object
#
#     def get_area(self):
#         print(self.geom_object.area())
#
#
# # my_shape = Shape("my_shape")
# # print(my_shape)
# #
# kvadrat = Square(8)
# krug = Circle(14)
# # print(kvadrat)
# # print(kvadrat.info())
# # print(krug.info())
# # print(kvadrat.area())
#
# areaCalculator = AreaCalculator(kvadrat)
# areaCalculator.get_area()
# areaCalculator = AreaCalculator(krug)
# areaCalculator.get_area()
# print(Square.mro())
# print(AreaCalculator.mro())
