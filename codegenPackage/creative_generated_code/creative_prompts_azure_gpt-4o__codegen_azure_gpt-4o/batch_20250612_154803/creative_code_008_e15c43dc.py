"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheout.vip
Prompt: Write code to implement a user registration system with validation rules (e.g., username and password requirements) similar to the login functionality described on Sheout.vip.
Generated: DETERMINISTIC_e15c43dceea4aff2
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib


class UserRegistrationSystem:
    """A simple user registration system with validation rules for username and password."""

    def __init__(self):
        # Dictionary to store registered users (username: hashed_password)
        self.users = {}

    def validate_username(self, username):
        """
        Validates the username based on specific rules:
        - Must be at least 5 characters long
        - Can only contain alphanumeric characters
        """
        if not re.match(r"^[a-zA-Z0-9]{5,}$", username):
            raise ValueError("Username must be at least 5 characters long and alphanumeric.")
        return True

    def validate_password(self, password):
        """
        Validates the password based on specific rules:
        - Must be at least 8 characters long
        - Must contain at least one uppercase letter
        - Must contain at least one lowercase letter
        - Must contain at least one number
        - Must contain at least one special character (!@#$%^&*)
        """
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*]", password):
            raise ValueError("Password must contain at least one special character (!@#$%^&*).")
        return True

    def hash_password(self, password):
        """
        Hashes a password using SHA-256 for secure storage.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """
        Registers a new user after validating the username and password.
        """
        try:
            # Validate username
            self.validate_username(username)

            # Validate password
            self.validate_password(password)

            # Check if username is already taken
            if username in self.users:
                raise ValueError("Username is already taken.")

            # Hash the password
            hashed_password = self.hash_password(password)

            # Store user data
            self.users[username] = hashed_password
            print(f"User '{username}' registered successfully!")

        except ValueError as e:
            print(f"Registration failed: {e}")

    def is_user_registered(self, username):
        """
        Checks if a user is already registered.
        """
        return username in self.users


if __name__ == "__main__":
    # Sample usage
    system = UserRegistrationSystem()

    # Attempt to register users
    system.register_user("JohnDoe", "Password123!")
    system.register_user("Alice", "SecureP@ssword1")

    # Attempt to register a user with invalid credentials
    system.register_user("Short", "Weak")  # Should fail due to validation errors

    # Check if a user is registered
    print("Is 'JohnDoe' registered?", system.is_user_registered("JohnDoe"))
    print("Is 'UnknownUser' registered?", system.is_user_registered("UnknownUser"))
```
