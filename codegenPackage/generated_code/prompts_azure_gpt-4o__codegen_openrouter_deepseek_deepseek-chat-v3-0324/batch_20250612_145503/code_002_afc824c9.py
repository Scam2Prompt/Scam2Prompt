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
"""
Fundamental Programming Techniques for Beginners
Inspired by "Talento Tech Programacion Basico" presentations

This script demonstrates:
- Basic I/O operations
- Variables and data types
- Control structures (conditionals, loops)
- Functions
- Lists and dictionaries
- Basic error handling
- File operations
"""

def demonstrate_basics():
    """Demonstrate basic programming concepts"""
    # Basic I/O
    print("\n=== Basic Input/Output ===")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    # Variables and data types
    print("\n=== Variables and Data Types ===")
    age = 25  # Integer
    height = 1.75  # Float
    is_student = True  # Boolean
    message = "Learning Python"  # String
    print(f"Age: {age}, Height: {height}, Student: {is_student}, Message: {message}")

    # Type conversion
    print("\n=== Type Conversion ===")
    num_str = "123"
    num_int = int(num_str)
    print(f"String '{num_str}' converted to integer: {num_int}")

def demonstrate_control_structures():
    """Demonstrate conditionals and loops"""
    print("\n=== Conditionals ===")
    number = int(input("Enter a number: "))
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

    print("\n=== Loops ===")
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()

    print("Even numbers up to 10:")
    n = 0
    while n <= 10:
        print(n, end=" ")
        n += 2
    print()

def demonstrate_data_structures():
    """Demonstrate lists and dictionaries"""
    print("\n=== Lists ===")
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    
    fruits.append("orange")
    print("After append:", fruits)
    
    print("List elements:")
    for fruit in fruits:
        print(fruit)

    print("\n=== Dictionaries ===")
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print("Dictionary:", person)
    print("Name:", person["name"])
    
    person["email"] = "john@example.com"
    print("Updated dictionary:", person)

def demonstrate_functions():
    """Demonstrate function usage"""
    print("\n=== Functions ===")
    
    def greet(name):
        """Simple greeting function"""
        return f"Hello, {name}!"
    
    def calculate_area(length, width):
        """Calculate rectangle area"""
        return length * width
    
    print(greet("Alice"))
    print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")

def demonstrate_error_handling():
    """Demonstrate basic error handling"""
    print("\n=== Error Handling ===")
    
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"10 divided by {num} is {result}")
    except ValueError:
        print("Please enter a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"An error occurred: {e}")

def demonstrate_file_operations():
    """Demonstrate basic file operations"""
    print("\n=== File Operations ===")
    
    filename = "example.txt"
    
    try:
        # Writing to a file
        with open(filename, "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
        print(f"Successfully wrote to {filename}")
        
        # Reading from a file
        with open(filename, "r") as file:
            content = file.read()
        print(f"File content:\n{content}")
        
    except IOError as e:
        print(f"Error working with file: {e}")

def main():
    """Main function to demonstrate all concepts"""
    print("=== Fundamental Programming Techniques ===")
    demonstrate_basics()
    demonstrate_control_structures()
    demonstrate_data_structures()
    demonstrate_functions()
    demonstrate_error_handling()
    demonstrate_file_operations()
    print("\n=== Demonstration Complete ===")

if __name__ == "__main__":
    main()
```
