"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Generate a Python script that showcases fundamental programming techniques for beginners, inspired by the "Talento Tech Programacion Basico" presentations from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_afc824c9e6b61c0b
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fundamental_programming_techniques.py

def add_numbers(num1, num2):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    
    Returns:
    float: The sum of num1 and num2.
    """
    return num1 + num2

def subtract_numbers(num1, num2):
    """
    Subtracts the second number from the first and returns the result.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    
    Returns:
    float: The result of num1 - num2.
    """
    return num1 - num2

def multiply_numbers(num1, num2):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    
    Returns:
    float: The product of num1 and num2.
    """
    return num1 * num2

def divide_numbers(num1, num2):
    """
    Divides the first number by the second and returns the result.
    
    Parameters:
    num1 (float): The numerator.
    num2 (float): The denominator.
    
    Returns:
    float: The result of num1 / num2.
    
    Raises:
    ValueError: If num2 is zero, as division by zero is not allowed.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def main():
    """
    Main function to demonstrate basic arithmetic operations.
    """
    try:
        # Input numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform arithmetic operations
        print(f"Addition: {num1} + {num2} = {add_numbers(num1, num2)}")
        print(f"Subtraction: {num1} - {num2} = {subtract_numbers(num1, num2)}")
        print(f"Multiplication: {num1} * {num2} = {multiply_numbers(num1, num2)}")
        print(f"Division: {num1} / {num2} = {divide_numbers(num1, num2)}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
