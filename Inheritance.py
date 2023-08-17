# inheritance allows one class to inherit attributes and methods from another class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class goat(Animal):
    def speak(self):
        return "beeee"
class cock(Animal):
    def speak(self):
        return "Craws"


    # These are objects


doggy = Dog("Buddy")
cat = Cat("Chase")
goat=goat("beeee")
cock=cock("Craws")
print(doggy.speak())
print(cat.speak())
print(goat.speak())
print(cock.speak())

