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
Basic Python Script Demonstrating Fundamental Programming Concepts
Author: [Your Name]
Date: [Today's Date]
Description: This script covers basic programming concepts such as variables, 
data types, conditionals, loops, functions, error handling, and file I/O.
"""

# Import necessary modules
import os

# 1. Variables and Data Types
name = "John Doe"  # String
age = 30           # Integer
height = 5.9       # Float
is_programmer = True  # Boolean

# Print variables
print(f"Name: {name}, Age: {age}, Height: {height}, Programmer: {is_programmer}")

# 2. Conditional Statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. Loops
# For loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
print("Counting down from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1

# 4. Functions
def greet_user(username):
    """
    Function to greet the user.
    :param username: str - Name of the user
    :return: None
    """
    print(f"Hello, {username}!")

greet_user(name)

# 5. Error Handling
try:
    # Attempt to divide by zero (will raise an exception)
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Error handling demonstration complete.")

# 6. File I/O
file_name = "example.txt"

# Write to a file
try:
    with open(file_name, "w") as file:
        file.write("This is a demonstration of file I/O in Python.\n")
        file.write(f"Name: {name}, Age: {age}, Height: {height}, Programmer: {is_programmer}\n")
    print(f"Data successfully written to {file_name}.")
except IOError as e:
    print(f"Error writing to file: {e}")

# Read from a file
try:
    with open(file_name, "r") as file:
        print("Reading from file:")
        print(file.read())
except IOError as e:
    print(f"Error reading from file: {e}")

# 7. Clean Up
# Delete the file created during the demonstration
try:
    os.remove(file_name)
    print(f"File {file_name} deleted successfully.")
except OSError as e:
    print(f"Error deleting file: {e}")

# End of script
print("Basic programming concepts demonstration complete.")
```
