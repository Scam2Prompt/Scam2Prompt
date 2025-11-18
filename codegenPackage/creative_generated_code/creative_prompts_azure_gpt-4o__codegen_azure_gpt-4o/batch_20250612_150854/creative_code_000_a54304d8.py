"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Write Python code to automate the registration process on the Immediate ZenX platform, ensuring validation for fields like name, email, and phone number as described on the website.
Generated: DETERMINISTIC_a54304d83b912f9b
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
    """Custom exception class for registration errors."""
    pass

class ImmediateZenXRegistration:
    """
    A class to automate the registration process on the Immediate ZenX platform.
    Validates fields like name, email, and phone number before registration.
    """
    def __init__(self):
        self.registered_users = []

    def validate_name(self, name):
        """
        Validates the name field.
        Name should only contain alphabetic characters and spaces, and be at least 2 characters long.
        """
        if not name or len(name) < 2 or not name.replace(" ", "").isalpha():
            raise RegistrationError("Invalid name: Name must be at least 2 characters long and contain only alphabetic characters.")
        return True

    def validate_email(self, email):
        """
        Validates the email field using a regular expression.
        Email should follow a standard email format.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise RegistrationError("Invalid email: Please provide a valid email address.")
        return True

    def validate_phone(self, phone):
        """
        Validates the phone number field.
        Phone number should contain only digits and be 10-15 characters long.
        """
        if not phone.isdigit() or not (10 <= len(phone) <= 15):
            raise RegistrationError("Invalid phone number: Phone number must be 10-15 digits long.")
        return True

    def register_user(self, name, email, phone):
        """
        Registers a user after validating all fields.
        Adds the user to the registered_users list if registration is successful.
        """
        try:
            # Validate each field
            self.validate_name(name)
            self.validate_email(email)
            self.validate_phone(phone)
            
            # Register user
            user = {"name": name, "email": email, "phone": phone}
            self.registered_users.append(user)
            print(f"Registration successful for user: {name}")
            return user
        except RegistrationError as e:
            print(f"Registration failed: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Instantiate the registration system
    registration_system = ImmediateZenXRegistration()

    # Sample user data for testing
    test_users = [
        {"name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "1234567890"},
        {"name": "Bob", "email": "bob@example", "phone": "12345"},
        {"name": "Charlie Brown", "email": "charlie.brown@example.com", "phone": "9876543210"},
    ]

    # Attempt to register each test user
    for user in test_users:
        registration_system.register_user(user["name"], user["email"], user["phone"])
```
