"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Create a Python tutorial for basic programming concepts, incorporating ideas from the "Presentaciones Talento Tech" section of https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_f2426b19c63a5e5b
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python Tutorial for Basic Programming Concepts
Inspired by "Presentaciones Talento Tech" from ejecutortecnico.github.io
"""

# Section 1: Variables and Data Types
def variables_and_data_types():
    # Integer
    age = 25
    print(f"Age: {age}, Type: {type(age)}")
    
    # Float
    height = 1.75
    print(f"Height: {height}, Type: {type(height)}")
    
    # String
    name = "Alice"
    print(f"Name: {name}, Type: {type(name)}")
    
    # Boolean
    is_student = True
    print(f"Is student: {is_student}, Type: {type(is_student)}")
    
    # List
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits: {fruits}, Type: {type(fruits)}")
    
    # Tuple
    coordinates = (10.0, 20.0)
    print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
    
    # Dictionary
    person = {"name": "Bob", "age": 30}
    print(f"Person: {person}, Type: {type(person)}")

# Section 2: Control Structures
def control_structures():
    # If-elif-else
    temperature = 22
    if temperature > 30:
        print("It's hot")
    elif temperature > 20:
        print("It's warm")
    else:
        print("It's cold")
    
    # For loop
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)
    
    # While loop
    print("\nCountdown from 5:")
    count = 5
    while count > 0:
        print(count)
        count -= 1
    
    # Break and continue
    print("\nOdd numbers up to 10:")
    for num in range(1, 11):
        if num % 2 == 0:
            continue
        if num > 10:
            break
        print(num)

# Section 3: Functions
def functions_section():
    # Basic function
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("Alice"))
    
    # Function with default parameter
    def power(base, exponent=2):
        return base ** exponent
    
    print(f"5 squared is {power(5)}")
    print(f"2 cubed is {power(2, 3)}")
    
    # Lambda function
    square = lambda x: x * x
    print(f"Square of 4 is {square(4)}")

# Section 4: Error Handling
def error_handling():
    # Basic try-except
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
    # Multiple exceptions
    try:
        num = int("abc")
    except ValueError:
        print("Invalid number format")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Finally block
    try:
        file = open("nonexistent.txt", "r")
    except FileNotFoundError:
        print("File not found")
    finally:
        print("This always executes")

# Section 5: File Operations
def file_operations():
    import os
    
    # Writing to a file
    try:
        with open("example.txt", "w") as file:
            file.write("Hello, World!\nThis is a test file.")
        print("File written successfully")
    except IOError as e:
        print(f"Error writing file: {e}")
    
    # Reading from a file
    try:
        with open("example.txt", "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except IOError as e:
        print(f"Error reading file: {e}")
    
    # Clean up
    if os.path.exists("example.txt"):
        os.remove("example.txt")

# Section 6: Object-Oriented Programming
def oop_section():
    # Class definition
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def greet(self):
            return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Creating objects
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    
    print(person1.greet())
    print(person2.greet())

# Main function to run all sections
def main():
    print("=== Python Basic Concepts Tutorial ===")
    print("\nSection 1: Variables and Data Types")
    variables_and_data_types()
    
    print("\nSection 2: Control Structures")
    control_structures()
    
    print("\nSection 3: Functions")
    functions_section()
    
    print("\nSection 4: Error Handling")
    error_handling()
    
    print("\nSection 5: File Operations")
    file_operations()
    
    print("\nSection 6: Object-Oriented Programming")
    oop_section()

if __name__ == "__main__":
    main()
```
