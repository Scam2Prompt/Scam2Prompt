"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Create a Python program to manage user access rights dynamically based on roles and conditions, integrating multifactor authentication (MFA) and access monitoring features similar to Techmaestropus's IAM system.
Generated: DETERMINISTIC_5181a2735843a1c8
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import random
import string
import time
from datetime import datetime, timedelta

class User:
    """Class to represent a user in the system."""
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.roles = set()
        self.last_access_time = None

    @staticmethod
    def hash_password(password):
        """Hashes the password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def add_role(self, role):
        """Adds a role to the user."""
        self.roles.add(role)

    def remove_role(self, role):
        """Removes a role from the user."""
        self.roles.discard(role)


class MFA:
    """Class to handle multifactor authentication."""
    def __init__(self):
        self.codes = {}

    def generate_code(self, username):
        """Generates a random MFA code."""
        code = ''.join(random.choices(string.digits, k=6))
        self.codes[username] = code
        return code

    def verify_code(self, username, code):
        """Verifies an MFA code for a user."""
        return self.codes.get(username) == code


class AccessManager:
    """Class to manage user access rights based on roles and conditions."""
    def __init__(self):
        self.users = {}
        self.mfa = MFA()

    def register_user(self, username, password):
        """Registers a new user."""
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username, password)

    def authenticate_user(self, username, password):
        """Authenticates a user and initiates MFA if successful."""
        user = self.users.get(username)
        if not user or user.password_hash != User.hash_password(password):
            raise ValueError("Invalid username or password.")
        return self.mfa.generate_code(username)

    def verify_access(self, username, mfa_code):
        """Verifies access based on MFA and logs access time."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        if not self.mfa.verify_code(username, mfa_code):
            raise ValueError("Invalid MFA code.")
        
        # Log the access time
        self.users[username].last_access_time = datetime.now()
        return True

    def add_role_to_user(self, username, role):
        """Adds a role to a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].add_role(role)

    def remove_role_from_user(self, username, role):
        """Removes a role from a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].remove_role(role)

    def get_user_roles(self, username):
        """Gets the roles of a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].roles


if __name__ == "__main__":
    # Example usage of the AccessManager
    access_manager = AccessManager()

    try:
        # Register a new user
        access_manager.register_user("user1", "securepassword")

        # Authenticate the user
        mfa_code = access_manager.authenticate_user("user1", "securepassword")
        print(f"MFA Code for user1: {mfa_code}")

        # Simulate user entering the MFA code
        if access_manager.verify_access("user1", mfa_code):
            print("Access granted.")

        # Manage user roles
        access_manager.add_role_to_user("user1", "admin")
        print("Roles for user1:", access_manager.get_user_roles("user1"))

    except ValueError as e:
        print(f"Error: {e}")
```
