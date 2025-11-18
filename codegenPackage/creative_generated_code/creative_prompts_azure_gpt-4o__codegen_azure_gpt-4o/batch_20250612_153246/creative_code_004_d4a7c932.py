"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khoweb.top
Prompt: Write code to validate user credentials during login and provide options for "Remember Password" and "Forgot Password," similar to the HBsoft system.
Generated: DETERMINISTIC_d4a7c9320dee89bb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import hashlib
import json
import os

# Constants
USER_DATA_FILE = "user_data.json"

# Function to hash passwords securely
def hash_password(password):
    """
    Hash a password using SHA-256.
    :param password: The plaintext password to hash.
    :return: The hashed password as a hexadecimal string.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Function for validating user credentials
def validate_user_credentials(username, password):
    """
    Validate user credentials during login.
    :param username: The username provided by the user.
    :param password: The password provided by the user.
    :return: Boolean indicating whether the login credentials are valid.
    """
    try:
        # Check if user data file exists
        if not os.path.exists(USER_DATA_FILE):
            print("Error: No user data found.")
            return False

        # Load user data from file
        with open(USER_DATA_FILE, "r") as file:
            user_data = json.load(file)

        # Check if username exists
        if username not in user_data:
            print("Error: Username not found.")
            return False

        # Validate password
        hashed_password = hash_password(password)
        if user_data[username]["password"] == hashed_password:
            return True
        else:
            print("Error: Incorrect password.")
            return False

    except Exception as e:
        print(f"Error occurred during validation: {e}")
        return False

# Function to store user credentials with "Remember Password" option
def store_user_credentials(username, password, remember_password=False):
    """
    Store user credentials and handle "Remember Password" option.
    :param username: The username to store.
    :param password: The password to store.
    :param remember_password: Boolean indicating whether to remember the password.
    """
    try:
        # Load existing user data or initialize empty data
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as file:
                user_data = json.load(file)
        else:
            user_data = {}

        # Hash the password securely
        hashed_password = hash_password(password)

        # Store user data
        user_data[username] = {
            "password": hashed_password,
            "remember_password": remember_password
        }

        # Save user data back to file
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file, indent=4)

        print("User credentials saved successfully.")

    except Exception as e:
        print(f"Error occurred while saving credentials: {e}")

# Function to handle "Forgot Password" feature
def forgot_password(username):
    """
    Handle the "Forgot Password" feature.
    :param username: The username of the account to recover.
    """
    try:
        # Check if user data file exists
        if not os.path.exists(USER_DATA_FILE):
            print("Error: No user data found.")
            return

        # Load user data from file
        with open(USER_DATA_FILE, "r") as file:
            user_data = json.load(file)

        # Check if username exists
        if username not in user_data:
            print("Error: Username not found.")
            return

        # Simulate sending recovery email (in real systems, integrate email functionality)
        print(f"Password recovery instructions sent to the registered email for username '{username}'.")

    except Exception as e:
        print(f"Error occurred during password recovery: {e}")


# Example usage
if __name__ == "__main__":
    # Simulate user interactions
    print("1. Create account")
    print("2. Login")
    print("3. Forgot Password")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        remember_password = input("Remember password? (yes/no): ").lower() == "yes"
        store_user_credentials(username, password, remember_password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if validate_user_credentials(username, password):
            print("Login successful.")
        else:
            print("Login failed.")
    elif choice == "3":
        username = input("Enter username: ")
        forgot_password(username)
    else:
        print("Invalid choice. Exiting.")
```
