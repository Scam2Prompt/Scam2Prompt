"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Generate a Python script that demonstrates basic programming concepts as outlined in the "Programacion Basico" section of the Ejecutor Tecnico website.
Generated: DETERMINISTIC_c9b5ff86c2e370ca
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# basic_programming_concepts.py

"""
A Python script demonstrating basic programming concepts such as variables,
data types, control structures, functions, and error handling.
"""

# Import necessary modules
import random

# Function to demonstrate variable declaration and data types
def demonstrate_variables():
    """Demonstrates variable declaration and data types."""
    integer_var = 10          # Integer
    float_var = 10.5          # Float
    string_var = "Hello, World!"  # String
    boolean_var = True        # Boolean

    print("Integer:", integer_var)
    print("Float:", float_var)
    print("String:", string_var)
    print("Boolean:", boolean_var)


# Function to demonstrate control structures: if-else
def demonstrate_if_else(age):
    """Demonstrates if-else control structure."""
    if age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")


# Function to demonstrate loops: for loop
def demonstrate_loops():
    """Demonstrates a for loop for iterating through a range."""
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)


# Function to demonstrate functions
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Function to demonstrate error handling
def divide_numbers(num1, num2):
    """Divides two numbers and handles division by zero error."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result


# Main function to run the demonstrations
def main():
    """Main function to execute the basic programming concepts demonstration."""
    print("Demonstrating Variables:")
    demonstrate_variables()
    
    print("\nDemonstrating If-Else:")
    age = random.randint(10, 70)  # Generate a random age for demonstration
    print(f"Random Age: {age}")
    demonstrate_if_else(age)
    
    print("\nDemonstrating Loops:")
    demonstrate_loops()
    
    print("\nDemonstrating Functions:")
    sum_result = add_numbers(5, 10)
    print("Sum of 5 and 10:", sum_result)
    
    print("\nDemonstrating Error Handling:")
    division_result = divide_numbers(10, 0)  # Attempt to divide by zero
    print("Division Result:", division_result)


# Entry point of the script
if __name__ == "__main__":
    main()
```
