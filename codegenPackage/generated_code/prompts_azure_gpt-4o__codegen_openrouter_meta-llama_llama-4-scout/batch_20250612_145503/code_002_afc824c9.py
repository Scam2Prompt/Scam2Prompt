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
# Fundamental Programming Techniques in Python

# Section 1: Variables and Data Types

def variables_example():
    """
    Demonstrates the use of variables and basic data types in Python.
    """
    # Integer variable
    my_int = 10
    print(f"Integer: {my_int}")

    # Float variable
    my_float = 3.14
    print(f"Float: {my_float}")

    # String variable
    my_string = "Hello, World!"
    print(f"String: {my_string}")

    # Boolean variable
    my_bool = True
    print(f"Boolean: {my_bool}")

    # List variable
    my_list = [1, 2, 3, 4, 5]
    print(f"List: {my_list}")

    # Tuple variable
    my_tuple = (1, 2, 3, 4, 5)
    print(f"Tuple: {my_tuple}")


# Section 2: Control Structures

def control_structures_example():
    """
    Demonstrates the use of control structures in Python.
    """
    # If-Else Statement
    age = 25
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    # For Loop
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:")
    for fruit in fruits:
        print(fruit)

    # While Loop
    i = 0
    print("Counting to 5:")
    while i < 5:
        print(i)
        i += 1


# Section 3: Functions

def greet(name: str) -> None:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The person's name.
    """
    print(f"Hello, {name}!")


# Section 4: Error Handling

def error_handling_example():
    """
    Demonstrates basic error handling in Python.
    """
    try:
        # Attempt to divide by zero
        x = 5 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Section 5: Lists and Tuples

def lists_tuples_example():
    """
    Demonstrates the use of lists and tuples in Python.
    """
    # List operations
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)
    my_list.append(6)
    print("List after append:", my_list)
    my_list.remove(4)
    print("List after remove:", my_list)

    # Tuple operations
    my_tuple = (1, 2, 3, 4, 5)
    print("Original Tuple:", my_tuple)
    # Tuples are immutable, so we can't modify them directly


# Main function
def main():
    print("Fundamental Programming Techniques in Python")
    print("-------------------------------------------")

    variables_example()
    print()

    control_structures_example()
    print()

    greet("John")
    print()

    error_handling_example()
    print()

    lists_tuples_example()


if __name__ == "__main__":
    main()
```
