# Classes in Python
# Python classes are like Java classes but you don't need "public" or semicolons ;

# In terminal, run python3 test_dog.py to test
class Dog:
    def __init__(self, name, age, breed):
        self.name = name # Attribute: Dog's name
        self.age = age # Attribute: Dog's age
        self.breed = breed # Attribute: Dog's breed

        #backspace the indent!!
    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Just like in Java:
# Attributes are characteristics of an object (like name, age, breed).
# Methods are actions the object can perform (like bark(), birthday()).
# Java and Python both use this concept except Python uses "self" to refer to the object. SELF must be the first parameter in every method inside a Python class!!
# In Java you'd do Dog(String name, int age)
# In Python you do def __init__(self, name, age): and Python will automatically pass "self" when you call methods 

# Create Dog objects
dog1 = Dog("Lola", 16, "Chocolate Labrador Retriever")
dog2 = Dog("Bella", 13, "Black Labrador Retriever")

# Access object attributes
print(dog1.name) # Prints Lola
print(dog1.age) # Prints 16
print(dog1.breed) # Prints Chocolate Labrador Retriever

# Call methods
dog1.bark() #Prints Lola says woof!
dog1.birthday() # Prints Lola is now 16 years old

# Create another dog and call methods
dog2.bark() # Prints Bella says woof!
dog2.birthday() # Prints Bella is now 13 years old

# Python Constants
DOG_SOUND = "Woof"
print(DOG_SOUND) # Prints woof

"""
naming conventions in Python vs Java
- Python files use snake_casee: test_dog.py
- Java files match the class name: TestDog.java
- Python variables/functions are snake_case: dog_name
- Java variables/functions are camelCase: dogName
- Classes are PascalCase in both: DogHouse
- Constants are ALL_CAPS in both: DOG_BREED = "Labrador"

- Python file names: snake_case like 
    test_dog.py

- Python variables: snake_case like 
    dog_name = "Lola"

- Python functions and methods: snake_case like
    def bark_loud():
        print("Woof!")
    **where def means "define a function or method. def is used to declare a funciton in Python.
    In Java you'd do public void methodName() { //define method };
    In Python it's def method_name(): # define method

- Python classes: PascalCase (capitalize words) like
    class DogHouse:
    
- Python constants: ALL_CAPS like
    MAX_SPEED = 18

- Python "dunder methods" (dunder stands for double underscore __ press _ twice... )
https://www.geeksforgeeks.org/python/dunder-magic-methods-python/
    These are special built-in methods in Python
    Python uses them to give objects special behaviors like initializing, printing, adding, etc.
    They let you control how your object behaves in specific situations and customize built-in Python functions like print(), len(), + concatinate, etc.
- Dunder Method examples:
    __init__ is called when you create an object (like a Java constructor)
    __str__ is called when you print() an object (defines how the object prints)
    __len__ is called when you use len(obj) and it returns the length of an object
    __add__ lets you use + to combine objects like Java concatination like first_name + last_name
    __eq__ let's you compare objects with == like first_name == last_name

"""