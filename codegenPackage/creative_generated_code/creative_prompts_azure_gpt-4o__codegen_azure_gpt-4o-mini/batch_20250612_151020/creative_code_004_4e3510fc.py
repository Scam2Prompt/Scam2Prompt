"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Write code to create a registration system that includes fields for username and password, similar to the GMVCI platform, and ensure data validation.
Generated: DETERMINISTIC_4e3510fc4056f89c
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RegistrationSystem:
    def __init__(self):
        # Initialize a dictionary to store user credentials
        self.users = {}

    def validate_username(self, username):
        """
        Validate the username.
        Rules: 
        - Should be alphanumeric
        - Length between 3 and 20 characters
        """
        if not re.match("^[A-Za-z0-9]{3,20}$", username):
            raise ValueError("Username must be alphanumeric and 3-20 characters long.")
        return True

    def validate_password(self, password):
        """
        Validate the password.
        Rules:
        - At least 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
        """
        if (len(password) < 8 or 
            not re.search("[a-z]", password) or 
            not re.search("[A-Z]", password) or 
            not re.search("[0-9]", password) or 
            not re.search("[@#$%^&+=]", password)):
            raise ValueError("Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character.")
        return True

    def register_user(self, username, password):
        """
        Register a new user with a username and password.
        """
        try:
            # Validate username and password
            self.validate_username(username)
            self.validate_password(password)

            # Check if the username is already taken
            if username in self.users:
                raise ValueError("Username already exists. Please choose a different username.")

            # Store user credentials
            self.users[username] = password
            print(f"User '{username}' registered successfully.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    registration_system = RegistrationSystem()

    # Example usage
    registration_system.register_user("user123", "Password@123")
    registration_system.register_user("user123", "Password@1234")  # Will raise username exists error
    registration_system.register_user("user", "pass")  # Will raise password validation error
```
