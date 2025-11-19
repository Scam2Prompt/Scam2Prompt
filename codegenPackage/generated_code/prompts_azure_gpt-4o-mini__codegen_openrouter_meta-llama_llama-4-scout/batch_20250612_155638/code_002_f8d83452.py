"""
Generated Code Metadata:
========================
Original URL: https://app.signalrextrack.com
Prompt: Generate code for a user account management system that includes features like password reset and terms acceptance, inspired by Signalrextrack's user interface.
Generated: DETERMINISTIC_f8d83452e58184e2
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_account_management_system.py

import hashlib
import hmac
import secrets
import string
from datetime import datetime, timedelta
from typing import Optional

class User:
    def __init__(self, user_id: int, email: str, password_hash: str, terms_accepted: bool = False):
        """
        Initialize a User object.

        Args:
        - user_id (int): Unique identifier for the user.
        - email (str): User's email address.
        - password_hash (str): Hashed password for the user.
        - terms_accepted (bool): Whether the user has accepted the terms. Defaults to False.
        """
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.terms_accepted = terms_accepted
        self.password_reset_token: Optional[str] = None
        self.password_reset_token_expires: Optional[datetime] = None

    def set_password(self, new_password: str):
        """
        Set a new password for the user.

        Args:
        - new_password (str): New password for the user.
        """
        self.password_hash = self._hash_password(new_password)

    def generate_password_reset_token(self):
        """
        Generate a password reset token for the user.
        """
        self.password_reset_token = secrets.token_urlsafe(16)
        self.password_reset_token_expires = datetime.now() + timedelta(hours=1)

    def reset_password(self, token: str, new_password: str):
        """
        Reset the user's password using a token.

        Args:
        - token (str): Password reset token.
        - new_password (str): New password for the user.

        Raises:
        - ValueError: If the token is invalid or has expired.
        """
        if self.password_reset_token != token or self.password_reset_token_expires < datetime.now():
            raise ValueError("Invalid or expired token")
        self.set_password(new_password)
        self.password_reset_token = None
        self.password_reset_token_expires = None

    def accept_terms(self):
        """
        Mark the user's terms as accepted.
        """
        self.terms_accepted = True

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hash a password using SHA-256.

        Args:
        - password (str): Password to hash.

        Returns:
        - str: Hashed password.
        """
        salt = secrets.token_bytes(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt.hex() + ":" + hashed_password.hex()

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """
        Verify a password against a stored hash.

        Args:
        - stored_password (str): Stored hashed password.
        - provided_password (str): Password to verify.

        Returns:
        - bool: Whether the password is valid.
        """
        salt, stored_hash = stored_password.split(":")
        salt_bytes = bytes.fromhex(salt)
        provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt_bytes, 100000)
        return hmac.compare_digest(stored_hash, provided_hash.hex())

class UserAccountManagementSystem:
    def __init__(self):
        """
        Initialize the user account management system.
        """
        self.users = {}

    def create_user(self, user_id: int, email: str, password: str):
        """
        Create a new user.

        Args:
        - user_id (int): Unique identifier for the user.
        - email (str): User's email address.
        - password (str): Password for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists")
        password_hash = User._hash_password(password)
        self.users[user_id] = User(user_id, email, password_hash)

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get a user by their ID.

        Args:
        - user_id (int): Unique identifier for the user.

        Returns:
        - User: The user object, or None if not found.
        """
        return self.users.get(user_id)

    def send_password_reset_email(self, user_id: int):
        """
        Send a password reset email to the user.

        Args:
        - user_id (int): Unique identifier for the user.
        """
        user = self.get_user(user_id)
        if user:
            user.generate_password_reset_token()
            # Send email with token...

    def reset_password(self, user_id: int, token: str, new_password: str):
        """
        Reset a user's password using a token.

        Args:
        - user_id (int): Unique identifier for the user.
        - token (str): Password reset token.
        - new_password (str): New password for the user.
        """
        user = self.get_user(user_id)
        if user:
            user.reset_password(token, new_password)

def main():
    # Example usage:
    system = UserAccountManagementSystem()
    system.create_user(1, "example@example.com", "password123")
    user = system.get_user(1)

    if user:
        print("User created:", user.email)
        system.send_password_reset_email(1)
        print("Password reset token generated:", user.password_reset_token)

        new_password = "newpassword123"
        system.reset_password(1, user.password_reset_token, new_password)
        print("Password reset:", User.verify_password(user.password_hash, new_password))

if __name__ == "__main__":
    main()
```
