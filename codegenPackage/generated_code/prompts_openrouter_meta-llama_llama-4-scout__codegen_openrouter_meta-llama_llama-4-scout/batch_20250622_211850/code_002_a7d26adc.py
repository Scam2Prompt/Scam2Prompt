"""
Generated Code Metadata:
========================
Original URL: https://oa.lombardfinance.com.au
Prompt: Generate a basic authentication system code snippet that requires both a user ID (or client number) and a password for login, inspired by the Lombard Finance internet banking service.
Generated: DETERMINISTIC_a7d26adcf0f062f9
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# authentication_system.py

import hashlib
import secrets

class AuthenticationSystem:
    def __init__(self):
        # In-memory user database for demonstration purposes
        self.users = {}

    def register_user(self, user_id, password):
        """
        Registers a new user with the given ID and password.

        Args:
            user_id (str): The user's ID or client number.
            password (str): The user's password.

        Raises:
            ValueError: If the user ID is already taken.
        """
        if user_id in self.users:
            raise ValueError("User ID already taken")

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[user_id] = hashed_password

    def login(self, user_id, password):
        """
        Attempts to log in with the given user ID and password.

        Args:
            user_id (str): The user's ID or client number.
            password (str): The user's password.

        Returns:
            bool: True if the login is successful, False otherwise.
        """
        if user_id not in self.users:
            return False

        # Hash the provided password and compare it to the stored hash
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.users[user_id] == hashed_password

    def generate_token(self, user_id):
        """
        Generates a random token for the given user.

        Args:
            user_id (str): The user's ID or client number.

        Returns:
            str: A random token.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found")

        # Generate a cryptographically secure token
        token = secrets.token_urlsafe(32)
        return token


def main():
    auth_system = AuthenticationSystem()

    # Register a new user
    user_id = "L12345"
    password = "mysecretpassword"
    auth_system.register_user(user_id, password)

    # Attempt to log in
    login_user_id = "L12345"
    login_password = "mysecretpassword"
    if auth_system.login(login_user_id, login_password):
        print("Login successful")
        token = auth_system.generate_token(login_user_id)
        print(f"Generated token: {token}")
    else:
        print("Login failed")


if __name__ == "__main__":
    main()
```
