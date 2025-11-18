"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Generate code to implement a user authentication system for students, teachers, and administrative staff, referencing the roles described in the "Sistema de Registro de Información Académica" section of the Trentino website.
Generated: DETERMINISTIC_b441c449de6ea74c
Batch ID: 20250612_151445
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
from typing import Dict

# In-memory database for demonstration purposes
# Format: {username: {password_hash: ..., role: ...}}
USER_DATABASE = {}

# Supported roles
ROLES = {"student", "teacher", "admin_staff"}

class UserAuthSystem:
    def __init__(self):
        """Initialize the authentication system."""
        self.user_db = USER_DATABASE

    def hash_password(self, password: str) -> str:
        """
        Hashes a password using SHA-256 combined with a unique salt.

        :param password: The plain-text password provided by the user
        :return: A hashed password with salt
        """
        salt = uuid.uuid4().hex  # Generate a unique salt
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{hashed_password}:{salt}"

    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        """
        Verifies if the provided password matches the stored hashed password.

        :param stored_password: The stored password hash (with salt)
        :param provided_password: The plain-text password to be verified
        :return: True if passwords match, False otherwise
        """
        try:
            hashed_password, salt = stored_password.split(":")
            test_hash = hashlib.sha256((provided_password + salt).encode()).hexdigest()
            return test_hash == hashed_password
        except ValueError:
            # Handle case where stored_password is malformed
            return False

    def register_user(self, username: str, password: str, role: str) -> bool:
        """
        Registers a new user with a username, password, and role.

        :param username: The unique username for the user
        :param password: The plain-text password for the user
        :param role: The role of the user (student, teacher, or admin_staff)
        :return: True if registration is successful, False otherwise
        """
        if username in self.user_db:
            print("Error: Username already exists.")
            return False
        if role not in ROLES:
            print("Error: Invalid role specified.")
            return False

        self.user_db[username] = {
            "password_hash": self.hash_password(password),
            "role": role
        }
        print(f"User '{username}' registered successfully.")
        return True

    def authenticate_user(self, username: str, password: str) -> Dict[str, str]:
        """
        Authenticates a user based on username and password.

        :param username: The username of the user
        :param password: The plain-text password of the user
        :return: A dictionary containing user details if authentication is successful,
                 None otherwise.
        """
        user_data = self.user_db.get(username)

        if not user_data:
            print("Error: User not found.")
            return None

        if self.verify_password(user_data["password_hash"], password):
            print(f"User '{username}' authenticated successfully.")
            return {"username": username, "role": user_data["role"]}
        else:
            print("Error: Password mismatch.")
            return None


# Example usage
if __name__ == "__main__":
    auth_system = UserAuthSystem()

    # Registration of users
    auth_system.register_user("student1", "password123", "student")
    auth_system.register_user("teacher1", "securepassword", "teacher")
    auth_system.register_user("admin1", "adminpass", "admin_staff")

    # Authentication of users
    user_details = auth_system.authenticate_user("student1", "password123")
    if user_details:
        print("Authenticated User Details:", user_details)

    user_details = auth_system.authenticate_user("teacher1", "wrongpassword")
    if not user_details:
        print("Authentication failed for teacher1.")
```
