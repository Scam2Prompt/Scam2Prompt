"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Create a script that automates user registration and login functionality, including input validation for fields like username and password, inspired by the HELPGM registration system.
Generated: DETERMINISTIC_eb477991f972837a
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Registration and Login System
----------------------------------

This script provides functionality for user registration and login. It includes input validation for fields like
username and password, as well as error handling to ensure robustness. The data is stored locally in a JSON file.

Requirements:
- Python 3.x
"""

import json
import re
import os

# Constants
DATA_FILE = "users.json"

# Helper Functions
def load_users():
    """
    Load user data from the JSON file.
    If the file doesn't exist, return an empty dictionary.

    Returns:
        dict: A dictionary containing user data.
    """
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_users(users):
    """
    Save user data to the JSON file.

    Args:
        users (dict): The user data to save.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"Error saving users: {e}")

def validate_username(username):
    """
    Validate the username based on specific criteria.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    # Username should be alphanumeric and between 3 to 20 characters
    return re.match("^[a-zA-Z0-9]{3,20}$", username) is not None

def validate_password(password):
    """
    Validate the password based on specific criteria.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Password should be at least 8 characters long and include at least one number
    return len(password) >= 8 and re.search("[0-9]", password) is not None

def register_user(username, password):
    """
    Register a new user if the username and password are valid and the username is not already taken.

    Args:
        username (str): The desired username.
        password (str): The desired password.

    Returns:
        str: A message indicating success or failure.
    """
    users = load_users()

    if username in users:
        return "Error: Username already exists."
    if not validate_username(username):
        return "Error: Invalid username. Must be alphanumeric and 3-20 characters."
    if not validate_password(password):
        return "Error: Invalid password. Must be at least 8 characters and include a number."

    users[username] = password
    save_users(users)
    return "Registration successful!"

def login_user(username, password):
    """
    Log in a user if the username exists and the password matches.

    Args:
        username (str): The username to authenticate.
        password (str): The password to authenticate.

    Returns:
        str: A message indicating success or failure.
    """
    users = load_users()

    if username not in users:
        return "Error: Username does not exist."
    if users[username] != password:
        return "Error: Incorrect password."

    return "Login successful!"

# Main Functionality
def main():
    """
    Main function to provide a menu for user registration and login.
    """
    while True:
        print("\nUser Registration and Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            print(register_user(username, password))
        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            print(login_user(username, password))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry Point
if __name__ == "__main__":
    main()
```
