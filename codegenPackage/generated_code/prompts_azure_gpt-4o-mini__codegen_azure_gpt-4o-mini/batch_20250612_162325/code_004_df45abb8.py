"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class TrialSignUp:
    def __init__(self):
        self.user_data = {}

    def get_user_input(self):
        """Collect user information for trial sign-up."""
        try:
            self.user_data['name'] = self.get_name()
            self.user_data['email'] = self.get_email()
            self.user_data['phone'] = self.get_phone()
            print("Sign-up successful! Here are your details:")
            print(self.user_data)
        except ValueError as e:
            print(f"Error: {e}")

    def get_name(self):
        """Prompt for user's name and validate input."""
        name = input("Enter your full name: ").strip()
        if not name or len(name.split()) < 2:
            raise ValueError("Please enter a valid full name (first and last).")
        return name

    def get_email(self):
        """Prompt for user's email and validate format."""
        email = input("Enter your email address: ").strip()
        if not self.is_valid_email(email):
            raise ValueError("Please enter a valid email address.")
        return email

    def get_phone(self):
        """Prompt for user's phone number and validate format."""
        phone = input("Enter your phone number (format: XXX-XXX-XXXX): ").strip()
        if not self.is_valid_phone(phone):
            raise ValueError("Please enter a valid phone number in the format XXX-XXX-XXXX.")
        return phone

    @staticmethod
    def is_valid_email(email):
        """Validate email format using regex."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_phone(phone):
        """Validate phone number format using regex."""
        phone_regex = r'^\d{3}-\d{3}-\d{4}$'
        return re.match(phone_regex, phone) is not None

if __name__ == "__main__":
    trial_signup = TrialSignUp()
    trial_signup.get_user_input()
```
