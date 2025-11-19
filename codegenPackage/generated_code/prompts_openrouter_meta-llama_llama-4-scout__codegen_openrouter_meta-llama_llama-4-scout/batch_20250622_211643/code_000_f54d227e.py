"""
Generated Code Metadata:
========================
Original URL: https://microlab.world
Prompt: Implement a simple user login system using username and password authentication in Python.
Generated: DETERMINISTIC_f54d227e25717e22
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_login_system.py

import getpass
import hashlib
import os

class User:
    def __init__(self, username, password_hash):
        """
        Initialize a User object.

        Args:
            username (str): The username chosen by the user.
            password_hash (str): The hashed password for the user.
        """
        self.username = username
        self.password_hash = password_hash

class UserLoginSystem:
    def __init__(self):
        """
        Initialize the UserLoginSystem.

        This system stores users in a dictionary where the key is the username and
        the value is a User object.
        """
        self.users = {}

    def register_user(self, username, password):
        """
        Register a new user.

        Args:
            username (str): The username chosen by the user.
            password (str): The password chosen by the user.

        Raises:
            ValueError: If the username is already taken.
        """
        if username in self.users:
            raise ValueError("Username already taken")

        password_hash = self._hash_password(password)
        self.users[username] = User(username, password_hash)

    def login_user(self, username, password):
        """
        Login a user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is successful, False otherwise.

        Raises:
            ValueError: If the username does not exist.
        """
        if username not in self.users:
            raise ValueError("Username does not exist")

        user = self.users[username]
        password_hash = self._hash_password(password)
        return user.password_hash == password_hash

    @staticmethod
    def _hash_password(password):
        """
        Hash a password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        # Use a salt to prevent rainbow table attacks
        salt = os.urandom(32)
        # Use SHA-256 for password hashing
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Store the salt and hashed password as a single string
        return salt.hex() + ':' + hashed_password.hex()

    @staticmethod
    def _check_password(stored_password, provided_password):
        """
        Check if a provided password matches a stored password.

        Args:
            stored_password (str): The stored password (salt and hashed password).
            provided_password (str): The provided password.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        salt, stored_hash = stored_password.split(':')
        salt_bytes = bytes.fromhex(salt)
        provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt_bytes, 100000)
        return provided_hash.hex() == stored_hash

def main():
    login_system = UserLoginSystem()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = getpass.getpass("Enter a password: ")
            try:
                login_system.register_user(username, password)
                print("User registered successfully")
            except ValueError as e:
                print(e)
        elif choice == '2':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            try:
                if login_system.login_user(username, password):
                    print("Login successful")
                else:
                    print("Invalid password")
            except ValueError as e:
                print(e)
        elif choice == '3':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
