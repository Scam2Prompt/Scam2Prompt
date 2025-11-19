"""
Generated Code Metadata:
========================
Original URL: https://realtechearners.com
Prompt: Write a Python program to validate user registration data and simulate account creation, following the steps outlined in the "Getting Started" section of realtechearners.com.
Generated: DETERMINISTIC_7bab64ac78557cff
Batch ID: 20250612_150211
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
        self.users = []

    def validate_username(self, username):
        """Validate the username to ensure it meets the criteria."""
        if len(username) < 3 or len(username) > 20:
            raise ValueError("Username must be between 3 and 20 characters.")
        if not re.match("^[a-zA-Z0-9_]*$", username):
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        return True

    def validate_password(self, password):
        """Validate the password to ensure it meets the criteria."""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search("[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search("[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search("[0-9]", password):
            raise ValueError("Password must contain at least one digit.")
        if not re.search("[@#$%^&+=]", password):
            raise ValueError("Password must contain at least one special character.")
        return True

    def validate_email(self, email):
        """Validate the email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format.")
        return True

    def register_user(self, username, password, email):
        """Register a new user after validating the input data."""
        try:
            self.validate_username(username)
            self.validate_password(password)
            self.validate_email(email)

            # Simulate account creation
            user_data = {
                'username': username,
                'password': password,  # In a real application, hash the password
                'email': email
            }
            self.users.append(user_data)
            print(f"User '{username}' registered successfully.")
        except ValueError as e:
            print(f"Registration failed: {e}")

if __name__ == "__main__":
    registration_system = UserRegistration()

    # Example user registration
    registration_system.register_user("john_doe", "Password123!", "john.doe@example.com")
    registration_system.register_user("invalid_user", "pass", "invalid_email")
```
