"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RiskFreeTrialSignUp:
    def __init__(self):
        self.user_data = {}

    def get_user_input(self):
        """Collects and validates user input for trial sign-up."""
        try:
            self.user_data['name'] = self.get_name()
            self.user_data['email'] = self.get_email()
            self.user_data['phone'] = self.get_phone()
            self.user_data['address'] = self.get_address()
            print("Sign-up successful! Your trial details are:")
            print(self.user_data)
        except ValueError as e:
            print(f"Error: {e}")

    def get_name(self):
        """Prompts for user's name and validates input."""
        name = input("Enter your full name: ").strip()
        if not name or len(name.split()) < 2:
            raise ValueError("Name must contain at least first and last name.")
        return name

    def get_email(self):
        """Prompts for user's email and validates format."""
        email = input("Enter your email address: ").strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        return email

    def get_phone(self):
        """Prompts for user's phone number and validates format."""
        phone = input("Enter your phone number (format: XXX-XXX-XXXX): ").strip()
        if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            raise ValueError("Phone number must be in format: XXX-XXX-XXXX.")
        return phone

    def get_address(self):
        """Prompts for user's address and validates input."""
        address = input("Enter your address: ").strip()
        if not address:
            raise ValueError("Address cannot be empty.")
        return address

if __name__ == "__main__":
    sign_up = RiskFreeTrialSignUp()
    sign_up.get_user_input()
```
