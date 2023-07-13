# class Car:
#     def __init__(self, name, price):
#         self.__name = "no name"
#         self.__price = 0
#         # инкапсуляция
#         self.name = name
#         self.price = price
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 1:
#             self.__name = name
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price
#
#     def show_info(self):
#         print(f"Name: {self.__name}")
#         print(f"Price: {self.__price}")
#
#     def __str__(self):
#         return f"Name: {self.__name}, price: {self.__price}"
#
#     def __add__(self, other):
#         if isinstance(other, Car):
#             return self.__price + other.price
#         elif other > 0:
#             return self.__price + other
#         else:
#             raise ValueError("Incorrect param")
#
#     def __sub__(self, other):
#         if isinstance(other, Car):
#             return self.__price - other.price
#         elif other > 0:
#             return self.__price - other
#         else:
#             return ValueError("Incorrect param")
#
#     def __mul__(self, other):
#         if isinstance(other, Car):
#             return self.__price * other.price
#         elif other > 0:
#             return self.__price * other
#         else:
#             return ValueError("Incorrect param")
#
#     def __truediv__(self, other):
#         if isinstance(other, Car):
#             return self.__price / other.price
#         elif other > 0:
#             return self.__price / other
#         else:
#             return ValueError("Incorrect param")
#
#     def __eq__(self, other):
#         if isinstance(other, Car):
#             return self.__price == other.price
#         elif other > 0:
#             return self.__price == other
#         else:
#             return ValueError("Incorrect param")
#
#     def __ne__(self, other):
#         if isinstance(other, Car):
#             return not self.__eq__(other)
#         else:
#             return False
#
#     def __lt__(self, other):
#         if isinstance(other, Car):
#             return self.__price < other.__price
#         elif other > 0:
#             return self.__price < other
#         else:
#             return False
#
#     def __gt__(self, other):
#         if isinstance(other, Car):
#             return self.__price > other.__price
#         elif other > 0:
#             return self.__price > other
#         else:
#             return False
#
#     def __ge__(self, other):
#         if isinstance(other, Car):
#             return not self.__lt__(other)
#         else:
#             return False
#
#     def __le__(self, other):
#         if isinstance(other, Car):
#             return not self.__gt__(other)
#         else:
#             return False
#
#
# # mycar = Car("c", -24)
# # mycar.show_info()
# #
# toyota = Car("camry", 123456)
# toyota.show_info()
#
# bmw = Car("x5", 321654)
# bmw.show_info()
#
# result = toyota + bmw
# print(result)
#
# result = toyota + 123
# print(result)
#
# # дописать остальные операторы в классе Car
#
# another_result = toyota - bmw
# print(another_result)
#
# result = toyota * 2
# print(result)
#
# result = toyota * bmw / 10
# print(result)
#
# result = bmw / toyota
# print(result)
#
# print(f"{bmw} == {toyota}: {bmw == toyota}")
# print(f"{bmw} != {toyota} {bmw != toyota}")
# print(f"{bmw} < {toyota} {bmw < toyota}")
# print(f"{bmw} > {toyota} {bmw > toyota}")
# print(f"{bmw} >= {toyota} {bmw >= toyota}")
# print(f"{bmw} <= {toyota} {bmw <= toyota}")

class X:
    def hello(self):
        print("Hello, I`m X")


class Y:
    def hello(self):
        print("Hello, I`m Y")


class A(X, Y):
    # def hello(self):
    #     print("Hello, I`m A")
    pass


class B(X, Y):
    def hello(self):
        print("Hello, I`m B")

class C(A, B):
    def bye (self):
        print("Bye")
    # def hello(self):
    #     pass

test = C()
test.hello()

print(C.mro())