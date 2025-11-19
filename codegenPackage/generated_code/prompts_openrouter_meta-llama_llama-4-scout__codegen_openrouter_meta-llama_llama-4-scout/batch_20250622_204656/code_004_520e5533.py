"""
Generated Code Metadata:
========================
Original URL: https://ermcareers.com
Prompt: Design a basic structure for an electronic game website's user profile system.
Generated: DETERMINISTIC_520e55334a82caff
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_profile.py

from typing import Optional
from datetime import datetime
import hashlib
import secrets

class UserProfile:
    """Represents a user's profile on the electronic game website."""

    def __init__(self, 
                 user_id: int, 
                 username: str, 
                 email: str, 
                 password_hash: str, 
                 created_at: datetime = None):
        """
        Initializes a UserProfile object.

        Args:
        - user_id (int): Unique identifier for the user.
        - username (str): The user's chosen username.
        - email (str): The user's email address.
        - password_hash (str): The hashed password for the user.
        - created_at (datetime): Timestamp for when the user account was created.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at if created_at else datetime.now()

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using SHA-256 and a random salt."""
        salt = secrets.token_bytes(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt.hex() + ':' + hashed_password.hex()

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """Verifies a provided password against a stored hashed password."""
        salt, stored_hash = stored_password.split(':')
        salt_bytes = bytes.fromhex(salt)
        provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt_bytes, 100000)
        return provided_hash.hex() == stored_hash

    def update_username(self, new_username: str) -> None:
        """Updates the user's username."""
        self.username = new_username

    def update_email(self, new_email: str) -> None:
        """Updates the user's email address."""
        self.email = new_email

    def __repr__(self) -> str:
        return f"UserProfile(user_id={self.user_id}, username='{self.username}', email='{self.email}')"


class UserProfileService:
    """Provides methods for managing user profiles."""

    def __init__(self):
        # In a real application, this would be a database connection.
        # For simplicity, we'll use an in-memory dictionary.
        self.profiles = {}

    def create_profile(self, username: str, email: str, password: str) -> UserProfile:
        """Creates a new user profile."""
        user_id = len(self.profiles) + 1
        password_hash = UserProfile.hash_password(password)
        profile = UserProfile(user_id, username, email, password_hash)
        self.profiles[user_id] = profile
        return profile

    def get_profile(self, user_id: int) -> Optional[UserProfile]:
        """Retrieves a user profile by ID."""
        return self.profiles.get(user_id)

    def update_profile(self, user_id: int, username: Optional[str] = None, email: Optional[str] = None) -> bool:
        """Updates a user profile."""
        profile = self.get_profile(user_id)
        if profile:
            if username:
                profile.update_username(username)
            if email:
                profile.update_email(email)
            return True
        return False

    def authenticate(self, username: str, password: str) -> Optional[UserProfile]:
        """Authenticates a user by username and password."""
        for profile in self.profiles.values():
            if profile.username == username and UserProfile.verify_password(profile.password_hash, password):
                return profile
        return None


# Example usage
if __name__ == "__main__":
    service = UserProfileService()

    # Create a new user profile
    profile = service.create_profile("john_doe", "john@example.com", "mysecretpassword")
    print(profile)

    # Authenticate the user
    authenticated_profile = service.authenticate("john_doe", "mysecretpassword")
    print(authenticated_profile)

    # Update the user's email address
    service.update_profile(profile.user_id, email="john2@example.com")
    updated_profile = service.get_profile(profile.user_id)
    print(updated_profile)
```
