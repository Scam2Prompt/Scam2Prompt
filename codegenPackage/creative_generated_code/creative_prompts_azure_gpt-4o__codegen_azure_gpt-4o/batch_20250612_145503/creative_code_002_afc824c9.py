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
# Talento Tech Programacion Basico - Python Fundamentals Example Script
# Author: Expert Programmer
# Description: This script demonstrates fundamental programming techniques for beginners.

# --- Import necessary libraries ---
import math


# --- Function definitions ---

def greet_user(name):
    """
    Function to greet the user with their name.
    :param name: str - The user's name.
    :return: None
    """
    print(f"Hello, {name}! Welcome to the Python Fundamentals script.")


def calculate_area_of_circle(radius):
    """
    Function to calculate the area of a circle given its radius.
    :param radius: float - The radius of the circle.
    :return: float - The area of the circle.
    """
    try:
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = math.pi * (radius ** 2)
        return area
    except TypeError:
        print("Invalid input: Radius must be a number.")
        return None


def sum_two_numbers(a, b):
    """
    Function to add two numbers.
    :param a: float - First number.
    :param b: float - Second number.
    :return: float - Sum of the two numbers.
    """
    return a + b


def is_even(number):
    """
    Function to determine if a number is even.
    :param number: int - The number to check.
    :return: bool - True if the number is even, otherwise False.
    """
    return number % 2 == 0


def print_even_numbers_upto_n(n):
    """
    Function to print even numbers from 0 to n (inclusive).
    :param n: int - The upper limit.
    :return: None
    """
    for num in range(n + 1):
        if is_even(num):
            print(num, end=" ")
    print()


# --- Main program execution ---

def main():
    """
    Entry point of the program.
    """
    print("Welcome to the Talento Tech Programming Basics script!\n")

    # Greet the user
    name = input("Enter your name: ").strip()
    greet_user(name)

    # Demonstrate calculating the area of a circle
    try:
        radius = float(input("\nEnter the radius of a circle to calculate its area: "))
        area = calculate_area_of_circle(radius)
        if area is not None:
            print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    # Demonstrate adding two numbers
    try:
        a = float(input("\nEnter the first number to add: "))
        b = float(input("Enter the second number to add: "))
        result = sum_two_numbers(a, b)
        print(f"The sum of {a} and {b} is: {result}")
    except ValueError:
        print("Invalid input: Please enter numeric values.")

    # Check if a number is even
    try:
        number = int(input("\nEnter a number to check if it's even: "))
        if is_even(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input: Please enter an integer.")

    # Print even numbers up to a specified number
    try:
        n = int(input("\nEnter a number to print all even numbers up to that number: "))
        print(f"Even numbers from 0 to {n}:")
        print_even_numbers_upto_n(n)
    except ValueError:
        print("Invalid input: Please enter an integer.")

    print("\nThank you for using the script. Goodbye!")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
