"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Develop a script that allows users to log in or register for an online beauty store, inspired by the login features mentioned on the aquarelaesmalte site.
Generated: DETERMINISTIC_e43ad833d6b3c046
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for user login and registration for an online beauty store.

Features:
- Users can register with a username and password.
- Users can log in with their registered credentials.
- Passwords are securely hashed using bcrypt.
- Includes proper input validation and error handling.
"""

import bcrypt
import os
import json

# File to store user data
USER_DATA_FILE = "user_data.json"

def load_user_data():
    """
    Loads user data from a JSON file.
    Returns an empty dictionary if the file does not exist.
    """
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)

def save_user_data(user_data):
    """
    Saves user data to a JSON file.
    """
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)

def register_user(username, password):
    """
    Registers a new user.

    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.

    Raises:
        ValueError: If the username is already taken.
    """
    user_data = load_user_data()

    if username in user_data:
        raise ValueError("Username already taken. Please choose another one.")

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data[username] = hashed_password.decode('utf-8')

    save_user_data(user_data)
    print("Registration successful!")

def login_user(username, password):
    """
    Logs in a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Raises:
        ValueError: If the username does not exist or the password is incorrect.
    """
    user_data = load_user_data()

    if username not in user_data:
        raise ValueError("Username does not exist. Please register first.")

    hashed_password = user_data[username].encode('utf-8')

    # Validate the password
    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        raise ValueError("Incorrect password. Please try again.")

    print("Login successful!")

def main():
    """
    Main function to provide user options for login or registration.
    """
    while True:
        print("\nWelcome to the Online Beauty Store")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = input("Enter your choice (1/2/3): ").strip()

            if choice == '1':
                username = input("Enter a username: ").strip()
                password = input("Enter a password: ").strip()
                register_user(username, password)

            elif choice == '2':
                username = input("Enter your username: ").strip()
                password = input("Enter your password: ").strip()
                login_user(username, password)

            elif choice == '3':
                print("Thank you for visiting! Goodbye!")
                break

            else:
                print("Invalid option. Please select 1, 2, or 3.")
        
        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
