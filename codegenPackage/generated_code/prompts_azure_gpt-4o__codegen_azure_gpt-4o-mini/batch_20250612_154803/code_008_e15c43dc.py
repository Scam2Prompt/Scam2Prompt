"""
Generated Code Metadata:
========================
Original URL: https://sheout.vip
Prompt: Write code to implement a user registration system with validation rules (e.g., username and password requirements) similar to the login functionality described on Sheout.vip.
Generated: DETERMINISTIC_e15c43dceea4aff2
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class UserRegistration:
    def __init__(self):
        # Initialize an empty list to store registered users
        self.users = []

    def validate_username(self, username):
        """
        Validate the username based on specific rules:
        - Must be between 3 and 20 characters
        - Can contain letters, numbers, and underscores
        - Must start with a letter
        """
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$', username):
            raise ValueError("Username must be 3-20 characters long and start with a letter.")

    def validate_password(self, password):
        """
        Validate the password based on specific rules:
        - Must be at least 8 characters long
        - Must contain at least one uppercase letter, one lowercase letter, one number, and one special character
        """
        if (len(password) < 8 or
                not re.search(r'[A-Z]', password) or
                not re.search(r'[a-z]', password) or
                not re.search(r'[0-9]', password) or
                not re.search(r'[\W_]', password)):
            raise ValueError("Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.")

    def register_user(self, username, password):
        """
        Register a new user after validating the username and password.
        If the username is already taken, raise an error.
        """
        # Validate username and password
        self.validate_username(username)
        self.validate_password(password)

        # Check if the username is already taken
        if any(user['username'] == username for user in self.users):
            raise ValueError("Username is already taken.")

        # Register the user
        self.users.append({'username': username, 'password': password})
        return "User registered successfully."

    def get_users(self):
        """Return the list of registered users (for testing purposes)."""
        return self.users


# Example usage
if __name__ == "__main__":
    registration_system = UserRegistration()

    try:
        print(registration_system.register_user("user1", "Password123!"))
        print(registration_system.register_user("user2", "AnotherPass1@"))
        print(registration_system.get_users())
    except ValueError as e:
        print(f"Error: {e}")
```
