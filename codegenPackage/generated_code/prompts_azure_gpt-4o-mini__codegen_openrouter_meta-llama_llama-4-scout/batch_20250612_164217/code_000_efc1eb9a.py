"""
Generated Code Metadata:
========================
Original URL: https://sin88.makeup
Prompt: Generate code for a secure user login system for an online betting platform like SIN88.
Generated: DETERMINISTIC_efc1eb9a8c784a8d
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import hmac
import secrets
import string
import time
from typing import Dict

class User:
    def __init__(self, username: str, email: str, password: str):
        """
        Initialize a User object.

        Args:
        - username (str): The username chosen by the user.
        - email (str): The email address of the user.
        - password (str): The password chosen by the user.
        """
        self.username = username
        self.email = email
        self.password_hash = self._hash_password(password)
        self.salt = secrets.token_bytes(16)
        self.password_reset_token = None
        self.account_locked = False
        self.last_login = None

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password with a random salt.

        Args:
        - password (str): The password to be hashed.

        Returns:
        - bytes: The hashed password.
        """
        # Generate a random salt
        salt = secrets.token_bytes(16)
        # Use PBKDF2HMAC to hash the password
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password

    def verify_password(self, password: str) -> bool:
        """
        Verify if a provided password matches the stored hash.

        Args:
        - password (str): The password to be verified.

        Returns:
        - bool: True if the password matches, False otherwise.
        """
        # Extract the salt and hashed password
        salt = self.password_hash[:16]
        stored_hash = self.password_hash[16:]
        # Hash the provided password with the same salt
        provided_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Compare the two hashes
        return hmac.compare_digest(stored_hash, provided_hash)

    def generate_reset_token(self) -> str:
        """
        Generate a password reset token.

        Returns:
        - str: A password reset token.
        """
        self.password_reset_token = secrets.token_urlsafe(32)
        return self.password_reset_token

    def reset_password(self, new_password: str, token: str) -> bool:
        """
        Reset the user's password.

        Args:
        - new_password (str): The new password.
        - token (str): The password reset token.

        Returns:
        - bool: True if the password was reset successfully, False otherwise.
        """
        if self.password_reset_token == token:
            self.password_hash = self._hash_password(new_password)
            self.password_reset_token = None
            return True
        return False

class Authenticator:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register(self, username: str, email: str, password: str) -> bool:
        """
        Register a new user.

        Args:
        - username (str): The username chosen by the user.
        - email (str): The email address of the user.
        - password (str): The password chosen by the user.

        Returns:
        - bool: True if the user was registered successfully, False otherwise.
        """
        if username in self.users:
            return False
        self.users[username] = User(username, email, password)
        return True

    def login(self, username: str, password: str) -> bool:
        """
        Login a user.

        Args:
        - username (str): The username of the user.
        - password (str): The password of the user.

        Returns:
        - bool: True if the login was successful, False otherwise.
        """
        if username not in self.users:
            return False
        user = self.users[username]
        if user.account_locked:
            return False
        if user.verify_password(password):
            user.last_login = time.time()
            return True
        # Implement rate limiting and account locking here
        return False

    def request_password_reset(self, username: str) -> str:
        """
        Request a password reset for a user.

        Args:
        - username (str): The username of the user.

        Returns:
        - str: A password reset token if the user exists, None otherwise.
        """
        if username not in self.users:
            return None
        user = self.users[username]
        return user.generate_reset_token()

def main():
    auth = Authenticator()
    auth.register("user123", "user@example.com", "password123")
    print(auth.login("user123", "password123"))  # Should print: True
    print(auth.login("user123", "wrongpassword"))  # Should print: False
    token = auth.request_password_reset("user123")
    user = auth.users["user123"]
    print(user.reset_password("newpassword", token))  # Should print: True

if __name__ == "__main__":
    main()
```
