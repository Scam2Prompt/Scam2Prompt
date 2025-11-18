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


class UserRegistrationError(Exception):
    """Custom exception for user registration errors."""
    pass


class User:
    """Class representing a user in the registration system."""

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserRegistration:
    """Class handling user registration with validation rules."""

    def __init__(self):
        self.users = []

    def validate_username(self, username):
        """Validate username according to specific criteria."""
        if len(username) < 3 or len(username) > 15:
            raise UserRegistrationError("Username must be between 3 and 15 characters.")
        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise UserRegistrationError("Username can only contain letters, numbers, and underscores.")
        if any(user.username == username for user in self.users):
            raise UserRegistrationError("Username already taken.")

    def validate_password(self, password):
        """Validate password according to specific criteria."""
        if len(password) < 8:
            raise UserRegistrationError("Password must be at least 8 characters long.")
        if not re.search("[A-Z]", password):
            raise UserRegistrationError("Password must contain at least one uppercase letter.")
        if not re.search("[a-z]", password):
            raise UserRegistrationError("Password must contain at least one lowercase letter.")
        if not re.search("[0-9]", password):
            raise UserRegistrationError("Password must contain at least one number.")
        if not re.search("[@#$%^&+=]", password):
            raise UserRegistrationError("Password must contain at least one special character.")

    def register_user(self, username, password):
        """Register a new user after validating username and password."""
        self.validate_username(username)
        self.validate_password(password)
        
        new_user = User(username, password)
        self.users.append(new_user)
        return new_user


if __name__ == "__main__":
    registration_system = UserRegistration()

    # Example usage
    try:
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")
        
        user = registration_system.register_user(username_input, password_input)
        print(f"User '{user.username}' registered successfully!")
    except UserRegistrationError as e:
        print(f"Registration failed: {e}")
```
