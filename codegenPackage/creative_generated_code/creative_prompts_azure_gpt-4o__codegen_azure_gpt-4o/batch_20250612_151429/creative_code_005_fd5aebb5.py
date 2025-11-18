"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Write a Python script to simulate user authentication and registration processes, inspired by the Lulu Malls website.
Generated: DETERMINISTIC_fd5aebb5f1bb620c
Batch ID: 20250612_151429
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
import json

# Constants for file storage
USER_DATA_FILE = "user_data.json"

# Helper Functions
def hash_password(password: str, salt: str) -> str:
    """
    Hashes the password using SHA-256 along with a salt.
    :param password: The plain text password
    :param salt: A randomly generated salt
    :return: Hashed password
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()

def load_user_data() -> dict:
    """
    Loads user data from the JSON file.
    :return: Dictionary containing user data
    """
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

def save_user_data(user_data: dict):
    """
    Saves user data to the JSON file.
    :param user_data: Dictionary containing user data
    """
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file, indent=4)

# Core Functions
def register_user(username: str, password: str) -> str:
    """
    Registers a new user with a username and password.
    :param username: The desired username
    :param password: The desired password
    :return: Success or failure message
    """
    user_data = load_user_data()

    if username in user_data:
        return "Error: Username already exists."

    # Generate a unique salt for the user
    salt = os.urandom(16).hex()
    hashed_password = hash_password(password, salt)

    # Store user details
    user_data[username] = {
        "salt": salt,
        "hashed_password": hashed_password
    }
    save_user_data(user_data)

    return "Success: User registered successfully."

def authenticate_user(username: str, password: str) -> str:
    """
    Authenticates an existing user with their username and password.
    :param username: The username of the user
    :param password: The password of the user
    :return: Success or failure message
    """
    user_data = load_user_data()

    if username not in user_data:
        return "Error: Username not found."

    # Retrieve stored salt and hashed password
    salt = user_data[username]["salt"]
    stored_hashed_password = user_data[username]["hashed_password"]

    # Hash the provided password with the stored salt
    hashed_password = hash_password(password, salt)

    if hashed_password == stored_hashed_password:
        return "Success: Authentication successful."
    return "Error: Incorrect password."

# CLI interface
def main():
    print("Welcome to Lulu Mall User Authentication System")
    print("Select an option:")
    print("1. Register")
    print("2. Authenticate")
    option = input("Enter your choice (1/2): ")

    if option == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        result = register_user(username, password)
        print(result)
    elif option == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        result = authenticate_user(username, password)
        print(result)
    else:
        print("Error: Invalid option.")

if __name__ == "__main__":
    main()
```
