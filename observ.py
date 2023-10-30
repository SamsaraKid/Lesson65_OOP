#НАБЛЮДАТЕЛЬ
from abc import ABC, abstractmethod

class CameraSystem():
    def __init__(self):
        self.observers = set()

    def podkl(self, obs):
        self.observers.add(obs)

    def otkl(self, obs):
        self.observers.remove(obs)

    def signal(self):
        for obs in self.observers:
            # if 'камера' in obs.name:
            #     obs.photo()
            # elif 'турель' in obs.name:
            #     obs.fire()
            if isinstance(obs, Camera):
                obs.photo()
            if isinstance(obs, Turel):
                obs.fire()


class ActionCamera(ABC):
    @abstractmethod
    def photo(self):
        pass


class ActionTurel(ABC):
    @abstractmethod
    def fire(self):
        pass


class Camera(ActionCamera):
    def __init__(self, name):
        self.name = name

    def photo(self):
        print(self.name, 'make photo')


class Turel(ActionTurel):
    def __init__(self, name):
        self.name = name

    def fire(self):
        print(self.name, 'make tratata')


CamSys = CameraSystem()
cam1 = Camera('камера 1')
cam2 = Camera('камера 2')
cam3 = Camera('камера 3')
tur1 = Turel('турель 1')
tur2 = Turel('турель 2')
CamSys.podkl(cam1)
CamSys.podkl(cam2)
CamSys.podkl(cam3)
CamSys.podkl(tur1)
CamSys.podkl(tur2)
CamSys.signal()
