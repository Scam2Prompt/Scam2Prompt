"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Design a user registration form for an online clothing store that captures essential details like email, password, and preferences, reflecting the user account setup process on Multan Designs.
Generated: DETERMINISTIC_a4b04577cc416662
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration.py

import re
import hashlib
import secrets

class UserRegistration:
    def __init__(self):
        self.email = None
        self.password = None
        self.preferences = {}

    def validate_email(self, email):
        # Regular expression for email validation
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True
        return False

    def validate_password(self, password):
        # Password requirements: at least 8 characters, 1 uppercase, 1 lowercase, 1 digit
        if (len(password) >= 8 and 
            any(char.isupper() for char in password) and 
            any(char.islower() for char in password) and 
            any(char.isdigit() for char in password)):
            return True
        return False

    def register_user(self, email, password, preferences):
        if not self.validate_email(email):
            raise ValueError("Invalid email address")

        if not self.validate_password(password):
            raise ValueError("Password must be at least 8 characters, contain 1 uppercase, 1 lowercase, and 1 digit")

        # Hash password for secure storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        salt = secrets.token_hex(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)

        self.email = email
        self.password = hashed_password.hex()
        self.preferences = preferences

        return {
            "email": self.email,
            "password": self.password,
            "preferences": self.preferences
        }

def main():
    try:
        registration = UserRegistration()
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        size_preference = input("Enter your preferred size (S, M, L, XL): ")
        color_preference = input("Enter your preferred color: ")

        user_data = registration.register_user(email, password, {
            "size": size_preference,
            "color": color_preference
        })

        print("User registered successfully!")
        print("User Data:")
        print(user_data)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
