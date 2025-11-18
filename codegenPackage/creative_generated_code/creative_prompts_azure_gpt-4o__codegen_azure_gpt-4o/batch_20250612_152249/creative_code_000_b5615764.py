"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Write code to simulate a user registration process for the 8KBet platform, including validation for promotional offers like the 88k bonus.
Generated: DETERMINISTIC_b56157641e7b2335
Batch ID: 20250612_152249
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

class EightKBetRegistration:
    def __init__(self):
        # Simulated database for registered users
        self.registered_users = set()

    def is_valid_email(self, email):
        """
        Validate the email format using regex.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def is_valid_password(self, password):
        """
        Validate the password format. Must be at least 8 characters long with a mix of letters and numbers.
        """
        if len(password) < 8:
            return False
        has_letter = any(char.isalpha() for char in password)
        has_number = any(char.isdigit() for char in password)
        return has_letter and has_number

    def is_eligible_for_bonus(self, promo_code):
        """
        Check if the user is eligible for the 88k bonus based on the promotional code.
        """
        return promo_code == "88KBONUS"

    def register_user(self, email, password, promo_code=None):
        """
        Simulate user registration with validation and optional promotional offer.
        """
        # Validate email
        if not self.is_valid_email(email):
            raise RegistrationError("Invalid email address format.")

        # Validate password
        if not self.is_valid_password(password):
            raise RegistrationError("Password must be at least 8 characters long and include both letters and numbers.")

        # Check if email is already registered
        if email in self.registered_users:
            raise RegistrationError("Email is already registered.")

        # Process promotional code
        bonus_message = None
        if promo_code:
            if self.is_eligible_for_bonus(promo_code):
                bonus_message = "Congratulations! You are eligible for the 88k bonus."
            else:
                raise RegistrationError("Invalid promotional code.")

        # Simulate adding user to database
        self.registered_users.add(email)

        # Return successful registration message
        success_message = f"User {email} successfully registered."
        if bonus_message:
            success_message += f" {bonus_message}"
        return success_message


# Example Usage
if __name__ == "__main__":
    # Initialize registration system
    registration_system = EightKBetRegistration()

    try:
        # User inputs
        email = "user@example.com"
        password = "password123"
        promo_code = "88KBONUS"

        # Register user
        result = registration_system.register_user(email, password, promo_code)
        print(result)
    except RegistrationError as e:
        print(f"Registration failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
