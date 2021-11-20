# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def hasBirthday(self):
        self.age += 1

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init User Object
brad = User('Brad Traversy', 'brad@gmail.com', 37)

# Init Customer object
janet = Customer('Janet Smith', 'janet@gmail.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.hasBirthday()

# print(brad)
# print(brad.name)
print(brad.greeting())