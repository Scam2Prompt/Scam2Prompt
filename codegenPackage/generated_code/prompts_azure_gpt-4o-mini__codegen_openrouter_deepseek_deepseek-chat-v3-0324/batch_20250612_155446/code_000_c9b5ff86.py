"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Generate a Python script that demonstrates basic programming concepts as outlined in the "Programacion Basico" section of the Ejecutor Tecnico website.
Generated: DETERMINISTIC_c9b5ff86c2e370ca
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Programming Concepts Demonstration
This script covers fundamental programming concepts as outlined in the "Programacion Basico" section.
Includes: variables, data types, operators, control structures, functions, and basic I/O.
"""

# 1. Variables and Data Types
def demonstrate_variables():
    """Demonstrate variable declaration and basic data types"""
    # Integer
    age = 25
    # Float
    temperature = 36.5
    # String
    name = "Juan Pérez"
    # Boolean
    is_active = True
    # List
    fruits = ["apple", "banana", "orange"]
    # Tuple
    coordinates = (10.5, -66.9)
    # Dictionary
    person = {"name": "Maria", "age": 30, "city": "Bogotá"}

    print("\n--- Variables and Data Types ---")
    print(f"Integer: {age}")
    print(f"Float: {temperature}")
    print(f"String: {name}")
    print(f"Boolean: {is_active}")
    print(f"List: {fruits}")
    print(f"Tuple: {coordinates}")
    print(f"Dictionary: {person}")

# 2. Operators
def demonstrate_operators():
    """Demonstrate arithmetic, comparison, and logical operators"""
    a = 10
    b = 3
    
    print("\n--- Operators ---")
    # Arithmetic
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponent: {a} ** {b} = {a ** b}")
    print(f"Floor division: {a} // {b} = {a // b}")
    
    # Comparison
    print(f"Equal: {a} == {b} -> {a == b}")
    print(f"Not equal: {a} != {b} -> {a != b}")
    print(f"Greater than: {a} > {b} -> {a > b}")
    print(f"Less than: {a} < {b} -> {a < b}")
    
    # Logical
    x = True
    y = False
    print(f"AND: {x} and {y} -> {x and y}")
    print(f"OR: {x} or {y} -> {x or y}")
    print(f"NOT: not {x} -> {not x}")

# 3. Control Structures
def demonstrate_control_structures():
    """Demonstrate if-else, for, and while loops"""
    print("\n--- Control Structures ---")
    
    # If-elif-else
    grade = 85
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
    
    # For loop
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)
    
    # While loop
    print("\nCountdown from 5:")
    counter = 5
    while counter > 0:
        print(counter)
        counter -= 1

# 4. Functions
def demonstrate_functions():
    """Demonstrate function definition and usage"""
    print("\n--- Functions ---")
    
    # Simple function
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("Ana"))
    
    # Function with default parameter
    def power(base, exponent=2):
        return base ** exponent
    
    print(f"5 squared is {power(5)}")
    print(f"2 to the 3rd power is {power(2, 3)}")

# 5. Basic I/O
def demonstrate_io():
    """Demonstrate basic input/output operations"""
    print("\n--- Basic I/O ---")
    
    try:
        # Input
        user_name = input("Enter your name: ")
        user_age = int(input("Enter your age: "))
        
        # Output
        print(f"\nHello {user_name}! You are {user_age} years old.")
        
        # File I/O
        with open("output.txt", "w") as file:
            file.write(f"Name: {user_name}\nAge: {user_age}")
        print("Data written to output.txt")
        
    except ValueError:
        print("Error: Please enter a valid age (number).")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main function to run all demonstrations
def main():
    """Main function to execute all demonstrations"""
    print("Basic Programming Concepts Demonstration\n")
    
    demonstrate_variables()
    demonstrate_operators()
    demonstrate_control_structures()
    demonstrate_functions()
    demonstrate_io()
    
    print("\nDemonstration complete!")

if __name__ == "__main__":
    main()
```
