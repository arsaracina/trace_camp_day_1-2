#parent class:
class Pet:
    dog=[]
    def __init__(self, dog):
        self.dog = dog

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

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

print("I have {} dogs".format(len(mypets.dog)))
for dog in mypets.dog:
    dog.eat()
    print("{} is {}.".format(dog.name,dog.age))
print("And they're all {}s of course".format(Dog.species))
hungry_dogs= False
for dog in mypets.dog:
    if dog.is_hungry:
            hungry_dogs= True
if hungry_dogs:
        print("My dogs are hungry")
else:
        print("My dogs are not hungry")
