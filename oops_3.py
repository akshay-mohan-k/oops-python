# INHERITANCE

# Base Class
class Animal:
  
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class

class Dog(Animal):
    def speak(self):
        return super().speak()

animal = Animal("Generic Animal")
print(animal.speak())

dog = Dog("Dogesh")
print(dog.speak())