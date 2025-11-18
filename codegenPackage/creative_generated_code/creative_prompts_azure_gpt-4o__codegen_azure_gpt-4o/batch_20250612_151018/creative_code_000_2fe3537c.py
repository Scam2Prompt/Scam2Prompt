"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Write code for a user authentication system that includes features like login, password recovery, and new user registration, similar to the functionality described on the Diverbox website.
Generated: DETERMINISTIC_2fe3537c4b593a78
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_auth_system.py

import hashlib
import uuid
import re


class UserAuthenticationSystem:
    """A User Authentication System that supports registration, login, and password recovery."""

    def __init__(self):
        # Dictionary to store user data (For production, use a proper database)
        self.user_data = {}

    def hash_password(self, password):
        """Hashes a password using SHA-256 and a unique salt."""
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        return hashed_password, salt

    def verify_password(self, password, hashed_password, salt):
        """Verifies if the given password matches the stored hashed password."""
        return hashlib.sha256((password + salt).encode()).hexdigest() == hashed_password

    def register_user(self, username, password, email):
        """
        Registers a new user with a username, password, and email.
        Returns True if successful, otherwise False.
        """
        # Validate username
        if username in self.user_data:
            print("Error: Username already exists.")
            return False

        # Validate password (minimum 8 characters, alphanumeric)
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            print("Error: Password must be at least 8 characters long and contain both letters and numbers.")
            return False

        # Validate email
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            print("Error: Invalid email format.")
            return False

        # Hash password and create user entry
        hashed_password, salt = self.hash_password(password)
        self.user_data[username] = {
            'hashed_password': hashed_password,
            'salt': salt,
            'email': email
        }

        print("User registered successfully.")
        return True

    def login_user(self, username, password):
        """
        Logs in a user with a username and password.
        Returns True if successful, otherwise False.
        """
        if username not in self.user_data:
            print("Error: Username not found.")
            return False

        user_info = self.user_data[username]
        if self.verify_password(password, user_info['hashed_password'], user_info['salt']):
            print("Login successful.")
            return True
        else:
            print("Error: Incorrect password.")
            return False

    def recover_password(self, username, email):
        """
        Initiates password recovery for a user by verifying their email.
        Sends a password recovery link (simulated here).
        """
        if username not in self.user_data:
            print("Error: Username not found.")
            return False

        user_info = self.user_data[username]
        if user_info['email'] == email:
            # Simulate sending recovery link
            print(f"Password recovery link sent to {email}.")
            return True
        else:
            print("Error: Email does not match our records.")
            return False


# Example usage of the UserAuthenticationSystem
if __name__ == "__main__":
    auth_system = UserAuthenticationSystem()

    print("\n--- Registration ---")
    auth_system.register_user("testuser", "password123", "testuser@example.com")

    print("\n--- Login ---")
    auth_system.login_user("testuser", "password123")

    print("\n--- Password Recovery ---")
    auth_system.recover_password("testuser", "testuser@example.com")
```

This implementation adheres to the requirements described in the prompt, providing a simple and clean user authentication system in Python. It uses SHA-256 for password hashing and includes features for registration, login, and password recovery. For production, replace the in-memory storage (`self.user_data`) with a secure database, and implement real email functionality for password recovery.
