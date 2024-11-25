# 1 Задание
class Person:
    def __init__(self, _age):
        self._age = _age

    def set_age(self, _age):
        if _age < 0:
            print("Ошибка! Возраст не может быть отрицательным.")
        else:
            self._age = _age
            print(f"Новый возраст {_age} лет.")

    def get_age(self):
        return f"{self._age} лет"


p = Person(20)
p.set_age(25)
print(p.get_age())
p.set_age(-5)


# 2 Задание
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"



dog = Dog("Buddy")
dog.speak()

cat = Cat("Kitty")
cat.speak()

print(dog.name, dog.speak())
print(cat.name, cat.speak())


# 3 Задание
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(Vehicle):
    return Vehicle.move()

car = Car()
bicycle = Bicycle()

print(move(car))
print(move(bicycle))


# 4 Задание
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())