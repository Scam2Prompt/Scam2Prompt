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
"""
Python Script: Basic Programming Concepts Demonstration
This script covers fundamental programming concepts:
- Variables and data types
- Control structures (if/else, loops)
- Functions
- Error handling
- Basic use of data structures (list, dictionary)
- File I/O
"""

# Import necessary modules
import os

def main():
    """
    Main function to demonstrate basic programming concepts.
    """
    # 1. Variables and Data Types
    name = "John Doe"  # String
    age = 30           # Integer
    balance = 1250.75  # Float
    is_active = True   # Boolean

    print(f"Name: {name}, Age: {age}, Balance: ${balance}, Active: {is_active}")

    # 2. Control Structures
    # If/Else
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    # Loop - For loop
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    # Loop - While loop
    print("Countdown from 5 to 1:")
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1

    # 3. Functions
    def greet_user(name):
        """
        Function to greet a user.
        :param name: str - Name of the user.
        :return: None
        """
        print(f"Hello, {name}!")

    greet_user(name)

    # 4. Error Handling
    try:
        # Simulating an exception
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError as e:
        print("Error: Please enter a valid integer.")
        print(f"Exception details: {e}")

    # 5. Data Structures
    # List demonstration
    fruits = ["Apple", "Banana", "Cherry"]
    print("Fruits list:")
    for fruit in fruits:
        print(fruit)

    # Dictionary demonstration
    user_profile = {
        "name": name,
        "age": age,
        "balance": balance,
        "is_active": is_active
    }

    print("User profile dictionary:")
    for key, value in user_profile.items():
        print(f"{key}: {value}")

    # 6. File I/O
    try:
        # Writing to a file
        with open("output.txt", "w") as file:
            file.write("User Profile:\n")
            for key, value in user_profile.items():
                file.write(f"{key}: {value}\n")
        print("User profile written to 'output.txt'.")

        # Reading from a file
        if os.path.exists("output.txt"):
            with open("output.txt", "r") as file:
                print("Reading from 'output.txt':")
                print(file.read())
        else:
            print("'output.txt' does not exist.")
    except IOError as e:
        print("Error performing file operations.")
        print(f"Exception details: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
