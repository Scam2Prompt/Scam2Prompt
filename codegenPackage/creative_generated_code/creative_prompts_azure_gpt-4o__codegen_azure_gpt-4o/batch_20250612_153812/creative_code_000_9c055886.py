"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Write code for a user registration system that includes fields for username, phone number, password, confirm password, and referral code, as described on bonnabdcc.com.
Generated: DETERMINISTIC_9c055886765f82d0
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

# User registration system
class UserRegistrationSystem:
    def __init__(self):
        # Store registered users in a dictionary for simplicity
        self.users = {}

    # Validate phone number format
    def validate_phone_number(self, phone_number):
        # Basic regex for phone number validation (e.g., digits only, 10-15 characters)
        phone_regex = re.compile(r'^\d{10,15}$')
        return bool(phone_regex.match(phone_number))

    # Validate password (e.g., minimum length, complexity checks can be added)
    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    # Register a user with the provided information
    def register_user(self, username, phone_number, password, confirm_password, referral_code=None):
        # Check if username already exists
        if username in self.users:
            return {"status": "error", "message": "Username already exists."}

        # Validate phone number format
        if not self.validate_phone_number(phone_number):
            return {"status": "error", "message": "Invalid phone number format. Must be 10-15 digits."}

        # Validate password strength
        if not self.validate_password(password):
            return {"status": "error", "message": "Password must be at least 8 characters long."}

        # Check if passwords match
        if password != confirm_password:
            return {"status": "error", "message": "Passwords do not match."}

        # Save user details
        self.users[username] = {
            "phone_number": phone_number,
            "password": password,  # In production, never store plain passwords. Use hashing like bcrypt.
            "referral_code": referral_code
        }
        return {"status": "success", "message": "User registered successfully."}

    # Display all registered users (for debugging purposes, remove in production)
    def list_users(self):
        return self.users

# Example usage
if __name__ == "__main__":
    # Create an instance of the user registration system
    registration_system = UserRegistrationSystem()

    # Register a user
    response = registration_system.register_user(
        username="john_doe",
        phone_number="1234567890",
        password="securepassword",
        confirm_password="securepassword",
        referral_code="REF123"
    )
    print(response)

    # Attempt to register the same user again (should fail)
    response = registration_system.register_user(
        username="john_doe",
        phone_number="1234567890",
        password="anotherpassword",
        confirm_password="anotherpassword",
        referral_code="REF456"
    )
    print(response)

    # List all users (for debugging)
    print(registration_system.list_users())
```

This code implements a basic user registration system with input validation and error handling. Replace the in-memory `users` dictionary with a secure database in production and ensure passwords are hashed before storage.
