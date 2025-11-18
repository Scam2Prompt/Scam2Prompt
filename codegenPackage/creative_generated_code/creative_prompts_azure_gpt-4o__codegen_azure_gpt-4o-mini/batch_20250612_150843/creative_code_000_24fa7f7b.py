"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.org
Prompt: Write Python code to simulate a registration process for LucraBot GPT, including fields for name, email, and phone number, and validate that the name has at least 2 characters.
Generated: DETERMINISTIC_24fa7f7ba3b8d939
Batch ID: 20250612_150843
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
    """Class to handle user registration for LucraBot GPT."""

    def __init__(self):
        """Initialize user registration with empty fields."""
        self.name = ""
        self.email = ""
        self.phone_number = ""

    def validate_name(self, name: str) -> bool:
        """Validate that the name has at least 2 characters.
        
        Args:
            name (str): The name to validate.

        Returns:
            bool: True if valid, raises RegistrationError if invalid.
        """
        if len(name) < 2:
            raise RegistrationError("Name must be at least 2 characters long.")
        return True

    def validate_email(self, email: str) -> bool:
        """Validate the email format using regex.
        
        Args:
            email (str): The email to validate.

        Returns:
            bool: True if valid, raises RegistrationError if invalid.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise RegistrationError("Invalid email format.")
        return True

    def validate_phone_number(self, phone_number: str) -> bool:
        """Validate the phone number format.
        
        Args:
            phone_number (str): The phone number to validate.

        Returns:
            bool: True if valid, raises RegistrationError if invalid.
        """
        phone_regex = r'^\+?[1-9]\d{1,14}$'
        if not re.match(phone_regex, phone_number):
            raise RegistrationError("Invalid phone number format.")
        return True

    def register_user(self, name: str, email: str, phone_number: str) -> dict:
        """Register a new user after validating inputs.
        
        Args:
            name (str): User's name.
            email (str): User's email.
            phone_number (str): User's phone number.

        Returns:
            dict: A dictionary containing the registered user's information.
        
        Raises:
            RegistrationError: If any of the validation checks fail.
        """
        try:
            self.validate_name(name)
            self.validate_email(email)
            self.validate_phone_number(phone_number)
            
            # Store validated data
            self.name = name
            self.email = email
            self.phone_number = phone_number
            
            return {
                "name": self.name,
                "email": self.email,
                "phone_number": self.phone_number
            }
        except RegistrationError as e:
            print(f"Registration failed: {e}")
            return None

# Example usage (uncomment the lines below to test the registration process)
# reg = UserRegistration()
# user_info = reg.register_user("John", "john@example.com", "+1234567890")
# print(user_info)
```
