"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-exodus.com
Prompt: Can you provide code examples for a password-protected entry system for an online store, inspired by the features of secure-exodus.com?
Generated: DETERMINISTIC_d305dd5034404fcf
Batch ID: 20250612_135736
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
from getpass import getpass

class PasswordManager:
    """
    A class to handle password storage and verification.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using SHA256.

        Parameters:
        password (str): The password to hash.

        Returns:
        str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password: str, provided_password: str) -> bool:
        """
        Check if the provided password matches the stored password.

        Parameters:
        stored_password (str): The hashed password.
        provided_password (str): The password to check.

        Returns:
        bool: True if the passwords match, False otherwise.
        """
        return stored_password == PasswordManager.hash_password(provided_password)

class User:
    """
    A class to represent a user in the password-protected entry system.
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = PasswordManager.hash_password(password)

class EntrySystem:
    """
    A simple entry system for password-protected access.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, username: str, password: str):
        """
        Register a new user with a username and password.

        Parameters:
        username (str): The user's username.
        password (str): The user's password.

        Raises:
        ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)
        print(f"User '{username}' registered successfully.")

    def login_user(self, username: str, password: str) -> bool:
        """
        Attempt to log in a user with the provided credentials.

        Parameters:
        username (str): The user's username.
        password (str): The user's password.

        Returns:
        bool: True if login is successful, False otherwise.
        """
        user = self.users.get(username)
        if user and PasswordManager.check_password(user.password_hash, password):
            print(f"User '{username}' logged in successfully.")
            return True
        else:
            print("Invalid username or password.")
            return False

def main():
    """
    Main function to run the password-protected entry system.
    """
    entry_system = EntrySystem()

    while True:
        action = input("Would you like to (register/login)? ").strip().lower()
        
        if action == 'register':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            try:
                entry_system.register_user(username, password)
            except ValueError as e:
                print(e)

        elif action == 'login':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            entry_system.login_user(username, password)

        else:
            print("Invalid action. Please choose 'register' or 'login'.")

if __name__ == "__main__":
    main()
```
