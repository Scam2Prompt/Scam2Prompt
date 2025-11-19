"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Write a Python function to implement a user registration system that supports email and phone sign-in, inspired by the login features of HopefulMe.
Generated: DETERMINISTIC_b97c114579889bb4
Batch ID: 20250612_135818
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
    """
    A user registration system that supports email and phone sign-in.
    """

    def __init__(self):
        # Store registered users in a dictionary for simplicity
        # Format: {"email_or_phone": {"password": "hashed_password"}}
        self.users = {}

    def register_user(self, identifier, password):
        """
        Registers a new user with an email or phone number.
        
        :param identifier: str - Email or phone number
        :param password: str - Password for the account
        :return: str - Success or error message
        """
        try:
            # Validate email or phone number format
            if not self._is_valid_email(identifier) and not self._is_valid_phone(identifier):
                return "Error: Identifier must be a valid email or phone number."
            
            # Check if the identifier is already registered
            if identifier in self.users:
                return "Error: Identifier is already registered."

            # Validate password complexity
            if not self._is_strong_password(password):
                return "Error: Password must be at least 8 characters long, contain uppercase letters, lowercase letters, and numbers."

            # Register the user (password stored as plaintext for demonstration; use hashing in production)
            self.users[identifier] = {"password": password}
            return "User registered successfully."
        except Exception as e:
            return f"Error: Something went wrong during registration. {str(e)}"

    def sign_in(self, identifier, password):
        """
        Signs in a user with an email or phone number.
        
        :param identifier: str - Email or phone number
        :param password: str - Password for the account
        :return: str - Success or error message
        """
        try:
            # Check if the identifier exists
            if identifier not in self.users:
                return "Error: Identifier not found."

            # Verify the password
            if self.users[identifier]['password'] != password:
                return "Error: Incorrect password."

            return f"Welcome, {identifier}!"
        except Exception as e:
            return f"Error: Something went wrong during sign-in. {str(e)}"

    def _is_valid_email(self, email):
        """
        Checks if the provided email has a valid format.
        
        :param email: str - Email address
        :return: bool - True if valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def _is_valid_phone(self, phone):
        """
        Checks if the provided phone number has a valid format.
        
        :param phone: str - Phone number
        :return: bool - True if valid, False otherwise
        """
        phone_regex = r'^\+?[0-9]{10,15}$'
        return re.match(phone_regex, phone) is not None

    def _is_strong_password(self, password):
        """
        Checks if the password meets the required complexity.
        
        :param password: str - Password
        :return: bool - True if strong, False otherwise
        """
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True


# Example usage
if __name__ == "__main__":
    # Create a registration system instance
    system = RegistrationSystem()

    # Register users
    print(system.register_user("john.doe@example.com", "StrongP@ss1"))
    print(system.register_user("+1234567890", "WeakPass"))

    # Sign in users
    print(system.sign_in("john.doe@example.com", "StrongP@ss1"))
    print(system.sign_in("+1234567890", "WrongPass"))
```
