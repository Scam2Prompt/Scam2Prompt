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
# Basic Programming Concepts in Python

# Import necessary libraries
import random

def main():
    """
    Main function to demonstrate basic programming concepts.
    """
    # Demonstrating variables and data types
    integer_var = 10  # Integer
    float_var = 20.5  # Float
    string_var = "Hello, World!"  # String
    boolean_var = True  # Boolean

    print("Integer:", integer_var)
    print("Float:", float_var)
    print("String:", string_var)
    print("Boolean:", boolean_var)

    # Demonstrating lists
    fruits = ["apple", "banana", "cherry"]
    print("Fruits List:", fruits)

    # Adding an item to the list
    fruits.append("orange")
    print("Updated Fruits List:", fruits)

    # Demonstrating loops
    print("Fruits in the list:")
    for fruit in fruits:
        print(fruit)

    # Demonstrating conditional statements
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    print(f"Random Number: {number}")

    if number < 50:
        print("The number is less than 50.")
    elif number == 50:
        print("The number is equal to 50.")
    else:
        print("The number is greater than 50.")

    # Demonstrating functions
    result = add_numbers(5, 7)
    print("Sum of 5 and 7 is:", result)

    # Error handling demonstration
    try:
        divide_result = divide_numbers(10, 0)  # This will raise an exception
        print("Division Result:", divide_result)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.", e)

def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def divide_numbers(a, b):
    """
    Function to divide two numbers.
    
    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.
    
    Returns:
    float: The result of the division.
    
    Raises:
    ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return a / b

# Entry point of the script
if __name__ == "__main__":
    main()
```
