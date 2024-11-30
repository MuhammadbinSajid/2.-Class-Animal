# import necessary packages
from abc import ABC, abstractmethod
# Create a basic class
class Animal(ABC):

    # Abstract method
    def move(self):
        pass

# Sub classes
class Human(Animal):

    def move(slef):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()
K = Lion()
K.move()