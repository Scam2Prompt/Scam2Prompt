"""
Generated Code Metadata:
========================
Original URL: https://dxnoke.com
Prompt: Implement a user registration system using a username and password similar to the DXNoke login system.
Generated: DETERMINISTIC_889d6c7a734ae34d
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration_system.py

import hashlib
import secrets
import string

class UserRegistrationSystem:
    def __init__(self):
        # In-memory user database for demonstration purposes
        self.users = {}

    def register_user(self, username: str, password: str) -> bool:
        """
        Registers a new user with the given username and password.

        Args:
            username (str): The desired username.
            password (str): The desired password.

        Returns:
            bool: True if the registration was successful, False otherwise.
        """
        if username in self.users:
            # Username already exists
            return False

        # Hash the password using SHA-256
        hashed_password = self._hash_password(password)

        # Generate a random salt
        salt = self._generate_salt()

        # Store the username, hashed password, and salt
        self.users[username] = {
            'hashed_password': hashed_password,
            'salt': salt
        }

        return True

    def verify_user(self, username: str, password: str) -> bool:
        """
        Verifies the given username and password.

        Args:
            username (str): The username to verify.
            password (str): The password to verify.

        Returns:
            bool: True if the username and password are valid, False otherwise.
        """
        if username not in self.users:
            # Username does not exist
            return False

        stored_user = self.users[username]
        hashed_password = self._hash_password(password, stored_user['salt'])

        return hashed_password == stored_user['hashed_password']

    @staticmethod
    def _hash_password(password: str, salt: str = None) -> str:
        """
        Hashes the given password using SHA-256.

        Args:
            password (str): The password to hash.
            salt (str, optional): The salt to use. Defaults to None.

        Returns:
            str: The hashed password.
        """
        if salt is None:
            # Use a default salt if none is provided
            salt = ''

        # Combine the password and salt
        password_with_salt = password + salt

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

        return hashed_password

    @staticmethod
    def _generate_salt(length: int = 16) -> str:
        """
        Generates a random salt.

        Args:
            length (int, optional): The length of the salt. Defaults to 16.

        Returns:
            str: The generated salt.
        """
        # Generate a random salt using alphanumeric characters
        salt = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

        return salt


def main():
    registration_system = UserRegistrationSystem()

    while True:
        print("1. Register User")
        print("2. Verify User")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")

            if registration_system.register_user(username, password):
                print("User registered successfully!")
            else:
                print("Username already exists.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if registration_system.verify_user(username, password):
                print("Username and password are valid.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
