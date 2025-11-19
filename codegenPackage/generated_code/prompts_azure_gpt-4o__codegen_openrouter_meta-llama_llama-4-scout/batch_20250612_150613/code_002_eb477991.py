"""
Generated Code Metadata:
========================
Original URL: https://gmvci.com
Prompt: Create a script that automates user registration and login functionality, including input validation for fields like username and password, inspired by the HELPGM registration system.
Generated: DETERMINISTIC_eb477991f972837a
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_auth.py

import getpass
import hashlib
import os
import re

class UserAuth:
    def __init__(self, users_file='users.txt'):
        """
        Initialize the UserAuth class.

        :param users_file: File to store user credentials
        """
        self.users_file = users_file

    def register(self):
        """
        Register a new user.
        """
        username = input("Enter a username: ")
        while not self.validate_username(username):
            username = input("Invalid username. Please enter a username (3-16 characters, alphanumeric): ")

        password = getpass.getpass("Enter a password: ")
        while not self.validate_password(password):
            password = getpass.getpass("Invalid password. Please enter a password (8-32 characters, at least one uppercase, one lowercase, and one digit): ")

        confirm_password = getpass.getpass("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match. Registration failed.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with open(self.users_file, 'a') as f:
            f.write(f"{username}:{hashed_password}\n")
        print("Registration successful.")

    def login(self):
        """
        Login an existing user.
        """
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        try:
            with open(self.users_file, 'r') as f:
                users = f.readlines()
        except FileNotFoundError:
            print("No users registered.")
            return

        for user in users:
            stored_username, stored_hashed_password = user.strip().split(':')
            if username == stored_username:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == stored_hashed_password:
                    print("Login successful.")
                    return
        print("Invalid username or password.")

    @staticmethod
    def validate_username(username):
        """
        Validate a username.

        :param username: Username to validate
        :return: True if valid, False otherwise
        """
        return bool(re.match('^[a-zA-Z0-9]{3,16}$', username))

    @staticmethod
    def validate_password(password):
        """
        Validate a password.

        :param password: Password to validate
        :return: True if valid, False otherwise
        """
        return bool(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$', password))

def main():
    auth = UserAuth()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            auth.register()
        elif choice == '2':
            auth.login()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
