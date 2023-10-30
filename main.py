#ФАБРИКА
from abc import ABC, abstractmethod


class Povedenie(ABC):  # интерфейс управления
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Enemy(Povedenie):  # суперкласс
    def __init__(self, a, b):
        self.weapon = a
        self.speed = b

    def run(self):
        print('run with speed', self.speed)

    def attack(self):
        print('attack with', self.weapon)


class Goblin(Enemy):  #  подкласс
    def __init__(self):  # при созлании объекта
        super().__init__('knife', 'fast')  # запускается инит из родительского класса


class Troll(Enemy):
    def __init__(self):
        super().__init__('bet', 'slow')


class Factory():  # фабрика, создаёт объекты
    def create(self, name):
        if name == 'goblin':
            return Goblin()
        elif name == 'troll':
            return Troll()
        else:
            return 'unknown type'

myfactory = Factory()
gob1 = myfactory.create('goblin')
tro1 = myfactory.create('troll')
gob1.run()
tro1.attack()