"""
Generated Code Metadata:
========================
Original URL: https://gmvci.com
Prompt: "Write a code snippet to implement a simple user authentication system with login, registration, and password features in Python."
Generated: DETERMINISTIC_53c9bf0321df6713
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_authentication.py

import hashlib
import secrets
import string

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.salt = secrets.token_bytes(16)

    def _hash_password(self, password):
        # Use PBKDF2HMAC for password hashing
        import hashlib
        import binascii
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)

    def verify_password(self, password):
        # Compare provided password with stored hash
        return self.password_hash == hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)


class AuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Register a new user."""
        if username in self.users:
            raise ValueError("Username already exists")
        if not self._validate_password(password):
            raise ValueError("Password does not meet requirements")
        
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Login an existing user."""
        if username not in self.users:
            raise ValueError("Username does not exist")
        
        user = self.users[username]
        if user.verify_password(password):
            return True
        else:
            raise ValueError("Incorrect password")

    def _validate_password(self, password):
        # Check if password meets requirements (at least 8 characters, 1 uppercase, 1 lowercase, 1 digit)
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True

    def change_password(self, username, old_password, new_password):
        """Change password for an existing user."""
        if username not in self.users:
            raise ValueError("Username does not exist")
        
        user = self.users[username]
        if user.verify_password(old_password):
            if not self._validate_password(new_password):
                raise ValueError("New password does not meet requirements")
            user.password_hash = user._hash_password(new_password)
        else:
            raise ValueError("Incorrect old password")


def main():
    auth_system = AuthenticationSystem()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                auth_system.register(username, password)
                print("User registered successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                auth_system.login(username, password)
                print("Login successful")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            try:
                auth_system.change_password(username, old_password, new_password)
                print("Password changed successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
