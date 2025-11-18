"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Write a Python program to validate user registration data and simulate account creation, following the steps outlined in the "Getting Started" section of realtechearners.com.
Generated: DETERMINISTIC_7bab64ac78557cff
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserRegistration:
    def __init__(self):
        self.users = []

    def validate_username(self, username: str) -> bool:
        """Validate the username to ensure it meets criteria."""
        if len(username) < 3 or len(username) > 20:
            print("Username must be between 3 and 20 characters long.")
            return False
        if not re.match("^[a-zA-Z0-9_]*$", username):
            print("Username can only contain letters, numbers, and underscores.")
            return False
        return True

    def validate_email(self, email: str) -> bool:
        """Validate the email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            print("Invalid email format.")
            return False
        return True

    def validate_password(self, password: str) -> bool:
        """Validate the password to ensure it meets criteria."""
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        if not re.search("[A-Z]", password):
            print("Password must contain at least one uppercase letter.")
            return False
        if not re.search("[0-9]", password):
            print("Password must contain at least one number.")
            return False
        if not re.search("[@#$%^&+=]", password):
            print("Password must contain at least one special character.")
            return False
        return True

    def register_user(self, username: str, email: str, password: str) -> bool:
        """Register a new user if all validations pass."""
        if self.validate_username(username) and \
           self.validate_email(email) and \
           self.validate_password(password):
            self.users.append({
                'username': username,
                'email': email,
                'password': password  # In a real application, do not store plain passwords.
            })
            print("User registered successfully!")
            return True
        return False

if __name__ == "__main__":
    registration_system = UserRegistration()

    # Simulating user input
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        registration_system.register_user(username, email, password)
    except Exception as e:
        print(f"An error occurred during registration: {e}")
```
