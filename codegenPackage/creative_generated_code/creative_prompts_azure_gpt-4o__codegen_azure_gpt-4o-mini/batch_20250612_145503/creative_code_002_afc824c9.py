"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Generate a Python script that showcases fundamental programming techniques for beginners, inspired by the "Talento Tech Programacion Basico" presentations from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_afc824c9e6b61c0b
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# talento_tech_basico.py

def greet_user(name):
    """
    Greets the user with their name.

    Parameters:
    name (str): The name of the user.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the Talento Tech Programming Basics."

def add_numbers(num1, num2):
    """
    Adds two numbers and returns the result.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.

    Returns:
    int or float: The sum of num1 and num2.
    """
    return num1 + num2

def divide_numbers(num1, num2):
    """
    Divides the first number by the second number.

    Parameters:
    num1 (int or float): The numerator.
    num2 (int or float): The denominator.

    Returns:
    float: The result of the division.

    Raises:
    ValueError: If the denominator is zero.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def main():
    """
    Main function to execute the script.
    """
    try:
        # Greet the user
        name = input("Enter your name: ")
        print(greet_user(name))

        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Display addition result
        sum_result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {sum_result}")

        # Display division result
        try:
            division_result = divide_numbers(num1, num2)
            print(f"The result of dividing {num1} by {num2} is: {division_result}")
        except ValueError as e:
            print(e)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
```
