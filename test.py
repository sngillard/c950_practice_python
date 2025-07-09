""" USE TRIPLE QUOTES TO COMMENT OUT BLOCKS OF CODE
USE HASHTAG TO COMMENT OUT LINES

# Comment with hashtag
print("Learn python")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome.")
# Greets name entered by user

# Learning variables
# print(f)- the f means formatted string or f-string 
# f-string allows you to insert variables or expressions inside a string with using concatination symbols +
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.") # sums 2 numbers entered by user

#  If-Else Conditionals in Python
age = int(input("How old are you? "))
if age >= 18:
    print("You're an adult!")
else:
    print("You're a minor!")
    #asks user to enter their name then tells if they're an adult or miner

# Lists and for loops in Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")
    #prints "I like apple. I like banana. I like cherry." in terminal.

# Functions in Python
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

# Call the greet_user function
# DO NOT INDENT OR PYTHON THINKS THIS IS PART OF THE FUNCTION, NOT A FUNCTION CALL
greet_user(name)

# Print messages with Strings
message = "hello world"
print(message.upper()) # Prints HELLO WORLD
print(message.capitalize()) # Prints Hello world
print(message.replace("world", "Python")) # Print hello Python

"""

# Lists in Python
# Python lists are like Java ArrayLists but can hold mixed types and do NOT need a declared size.
my_python_list = [1, "pink", 3.45]
print(my_python_list[0]) # Prints 1
print(my_python_list[-2]) # Prints pink
print(my_python_list[1]) # Prints pink
print(my_python_list[2]) # Prints 3.45

colors = ["yellow", "pink", "purple"]
print(colors[0]) # Prints yellow
print(colors[-1]) # Prints purple (the last item)
print(colors[2]) # Prints purple
print(colors[1]) # Prints pink

# Loop through a list
colors = ["yellow", "pink", "purple"]
for color in colors:
    print(f"I like the color {color}.")

# Add items to a list
fruits = ["apple", "banana"]
fruits.append("cherry") # Add item
print(fruits) # ['apple', 'banana', 'cherry']
# Python's append() is like Java's ArrayList.add()

# Remove item from a list
fruits.remove("banana") # Remove item
print(fruits) # Prints ['apple', 'cherry']

# Dictionaries- in Python a dictionary is like a HashMap in Java
# Python dictionaries are more flexible than Java HashMaps- they can have keys of any type
student = {"name": "Lola", "age": 24, "major": "CS"}
print(student["name"]) # Prints Lola
student["age"] = 25 # Update a value (age)
print(student) # Prints {'name': 'Lola', 'age': 25, 'major': 'CS'}

# Loop through a Python dictionary (like looking through a HashMap in Java)
for key, value in student.items():
    print(f"{key}: {value}")

# Backspace to remove indent for new function

# Function with a list
def print_items(item_list):
    for item in item_list:
        print(f"Item: {item}")

# Call to print function
print_items(["pen", "notebook", "eraser"])

# In terminal, run python3 test.py to test code