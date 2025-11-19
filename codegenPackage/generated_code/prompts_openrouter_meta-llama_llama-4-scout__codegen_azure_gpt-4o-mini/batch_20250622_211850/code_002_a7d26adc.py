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
import hashlib
import os

class User:
    """Class to represent a user in the authentication system."""
    
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verifies a given password against the stored password hash."""
        return self.password_hash == self.hash_password(password)


class AuthSystem:
    """Class to manage user authentication."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, password):
        """Registers a new user with a user ID and password."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, password)
        print(f"User {user_id} registered successfully.")

    def login(self, user_id, password):
        """Logs in a user by verifying their user ID and password."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User ID not found.")
        if not user.verify_password(password):
            raise ValueError("Invalid password.")
        print(f"User {user_id} logged in successfully.")


def main():
    """Main function to demonstrate the authentication system."""
    auth_system = AuthSystem()

    # Register a user
    try:
        auth_system.register_user("client123", "securePassword!")
    except ValueError as e:
        print(f"Registration error: {e}")

    # Attempt to log in
    try:
        auth_system.login("client123", "securePassword!")
    except ValueError as e:
        print(f"Login error: {e}")

    # Attempt to log in with an incorrect password
    try:
        auth_system.login("client123", "wrongPassword")
    except ValueError as e:
        print(f"Login error: {e}")

    # Attempt to log in with a non-existent user
    try:
        auth_system.login("nonExistentUser", "somePassword")
    except ValueError as e:
        print(f"Login error: {e}")


if __name__ == "__main__":
    main()
```
