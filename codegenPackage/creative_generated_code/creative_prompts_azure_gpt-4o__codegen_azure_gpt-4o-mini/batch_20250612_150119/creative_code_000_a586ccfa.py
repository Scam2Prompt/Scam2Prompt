"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Write code to create a VIP membership login system with username and password authentication, including a "Register" option, similar to the functionality described on the VIP Membership website.
Generated: DETERMINISTIC_a586ccfae89c36ac
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os

# Constants for the file storage of user credentials
USER_DATA_FILE = 'users.txt'

def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256 for secure storage.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register(username: str, password: str) -> bool:
    """
    Register a new user by storing their username and hashed password.

    Args:
        username (str): The username for the new user.
        password (str): The password for the new user.

    Returns:
        bool: True if registration was successful; False if the username already exists.
    """
    if username_exists(username):
        return False  # User already exists

    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{hashed_password}\n")
    return True

def username_exists(username: str) -> bool:
    """
    Check if a username already exists in the user data file.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the username exists; False otherwise.
    """
    try:
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(',', 1)
                if stored_username == username:
                    return True
    except FileNotFoundError:
        return False  # File does not exist, no users registered yet
    return False

def authenticate(username: str, password: str) -> bool:
    """
    Authenticate a user by checking their username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if authentication succeeds; False otherwise.
    """
    try:
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(',', 1)
                if stored_username == username and stored_hashed_password == hash_password(password):
                    return True
    except FileNotFoundError:
        return False  # File does not exist, no users registered yet
    return False

def main():
    """
    Main function to run the VIP membership login system.
    """
    while True:
        print("\nWelcome to the VIP Membership System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            if register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate(username, password):
                print("Login successful! Welcome to the VIP area!")
            else:
                print("Login failed! Invalid username or password.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
