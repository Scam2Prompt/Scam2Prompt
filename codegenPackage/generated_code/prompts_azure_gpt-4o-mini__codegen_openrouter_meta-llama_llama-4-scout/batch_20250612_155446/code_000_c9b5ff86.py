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
# basic_programming_concepts.py

def greet_user(name: str) -> None:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The user's name.
    """
    try:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        print(f"Hello, {name}!")
    except TypeError as e:
        print(f"Error: {e}")

def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    try:
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        return length * width
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

def main() -> None:
    # Variables and Data Types
    print("# Variables and Data Types")
    name = "John Doe"
    age = 30
    height = 1.75
    print(f"Name: {name}, Age: {age}, Height: {height}")

    # Basic Operators
    print("\n# Basic Operators")
    num1 = 10
    num2 = 5
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division: {num1} / {num2} = {num1 / num2}")

    # Control Structures
    print("\n# Control Structures")
    greet_user("Alice")
    area = calculate_area(4, 5)
    if area is not None:
        print(f"Area: {area}")

    # Loops
    print("\n# Loops")
    for i in range(5):
        print(f"Iteration {i+1}")

    # Functions
    print("\n# Functions")
    greet_user("Bob")

if __name__ == "__main__":
    main()
```
