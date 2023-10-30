#ДЕКОРАТОР
from abc import ABC, abstractmethod


class Povedenie(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Animal(Povedenie):  # чертёж базового животного
    def move(self):
        print('I move')

    def eat(self):
        print('I eat food')



class AbsDecorator(Povedenie):  # декоратор для надевания декораторов на объекты
    def __init__(self, object):
        self.object = object

    def move(self):
        self.object.move()

    def eat(self):
        self.object.eat()



class Swim(AbsDecorator):  # декоратор
    def move(self):
        print('I swim')


class Fly(AbsDecorator):  # декоратор
    def move(self):
        print('I fly')


class Predator(AbsDecorator):  # декоратор
    def eat(self):
        print('I eat meat')


class Herbivorous(AbsDecorator):  # декоратор
    def eat(self):
        print('I eat grass')


ani = Animal()  # создали животное
ani.move()
ani.eat()
ani = Fly(ani)  # надели декоратор
ani = Predator(ani)  # надели декоратор
ani.move()
ani.eat()
