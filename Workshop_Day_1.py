#example problem 1
N = int(input())
if N%2==0 and N>2 and N<5:
        print("Not Weird")
elif N%2==0 and N>6 and N<20:
        print("Weird")
elif N %2==0 and N>20:
        print ("Not Weird")
else:
        print("Weird")

#example problem 2
if __name__ == '__main__':
    n = int(input())
for n in range(0,n):
    print (n**2)

#Object Example
#dog_isinstance
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

#dog walking

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
