"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Write Python code to simulate the registration process described on Immediate Peak, including form validation for fields like name, email, and phone number.
Generated: DETERMINISTIC_0527be240762218f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

class UserRegistration:
    """Class to handle user registration."""

    def __init__(self):
        self.users = []  # List to store registered users

    def register_user(self, name: str, email: str, phone: str):
        """
        Register a new user with the provided name, email, and phone number.

        :param name: User's full name
        :param email: User's email address
        :param phone: User's phone number
        :raises RegistrationError: If any validation fails
        """
        self.validate_name(name)
        self.validate_email(email)
        self.validate_phone(phone)

        # Create a user dictionary and add to users list
        user = {'name': name, 'email': email, 'phone': phone}
        self.users.append(user)

    @staticmethod
    def validate_name(name: str):
        """Validate the name field."""
        if not name or not isinstance(name, str) or len(name) < 3:
            raise RegistrationError("Name must be at least 3 characters long.")

    @staticmethod
    def validate_email(email: str):
        """Validate the email field."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise RegistrationError("Invalid email format.")

    @staticmethod
    def validate_phone(phone: str):
        """Validate the phone number field."""
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        if not re.match(phone_regex, phone):
            raise RegistrationError("Invalid phone number format.")

    def get_users(self):
        """Returns the list of registered users."""
        return self.users


if __name__ == "__main__":
    registration_system = UserRegistration()

    # Example registration process
    try:
        registration_system.register_user("John Doe", "john@example.com", "+1234567890")
        registration_system.register_user("Jane Smith", "jane@example.com", "+0987654321")
        print("Registered users:", registration_system.get_users())
    except RegistrationError as e:
        print(f"Registration failed: {e}")
```
