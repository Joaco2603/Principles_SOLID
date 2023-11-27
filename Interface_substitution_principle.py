
#Interface Segregation Principle - ISP:
#A client should not be forced to implement interfaces it does not use, promoting the creation of specific, focused interfaces rather than large, general ones.

from abc import ABC, abstractmethod

class Worker(ABC):    
    @abstractmethod
    def work(self):
        pass
    

class Sleep(ABC):
    @abstractmethod
    def sleep(self):
        pass
    
    
class Eat(ABC):
    @abstractmethod
    def eat(self,food):
        pass
    
    
class Human(Worker,Sleep,Eat):
    def work(self):
        print("Working")
    def sleep(self):
        print("Sleeping");
    def eat(self):
        print("Eating");
    
    
class Robot(Worker):
    def work(self):
        print("Working")

robot = Robot();
robot.work();

human = Human();
human.work();
human.eat();
human.sleep();