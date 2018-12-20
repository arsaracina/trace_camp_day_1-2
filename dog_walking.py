#parent class:
class Pet:
    dog=[]
    def __init__(self, dog):
        self.dog = dog

    def walk(self):
        for dog in self.dog:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry= True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    #instance method
    def eat(self):
        self.is_hungry= False

    #instance method

    def walk(self):
        return "{} is walking!" .format(self.name)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#now need Instance
mydogs=[ RussellTerrier('Tom',6), Bulldog('Fletcher',7), RussellTerrier('Larry',9)]
mypets=Pet(mydogs)

#output

mypets.walk()
