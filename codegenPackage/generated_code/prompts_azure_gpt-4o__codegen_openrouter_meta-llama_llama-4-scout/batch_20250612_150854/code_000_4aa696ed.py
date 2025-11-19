"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: Write Python code to simulate a registration form for Trade GPT, including validation for first name, last name, and email as described on the website.
Generated: DETERMINISTIC_4aa696edaaa7818f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import email.utils

class TradeGPTRegistrationForm:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def validate_first_name(self):
        """Validate first name. It should not be empty and have a maximum length of 50 characters."""
        if not self.first_name:
            raise ValueError("First name is required")
        if len(self.first_name) > 50:
            raise ValueError("First name should not exceed 50 characters")

    def validate_last_name(self):
        """Validate last name. It should not be empty and have a maximum length of 50 characters."""
        if not self.last_name:
            raise ValueError("Last name is required")
        if len(self.last_name) > 50:
            raise ValueError("Last name should not exceed 50 characters")

    def validate_email(self):
        """Validate email. It should be a valid email address."""
        try:
            email.utils.parseaddr(self.email)[1]
        except Exception:
            raise ValueError("Invalid email address")

        # Additional email validation using regex
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, self.email):
            raise ValueError("Invalid email address")

    def validate(self):
        """Validate all fields."""
        self.validate_first_name()
        self.validate_last_name()
        self.validate_email()

    @staticmethod
    def register(first_name, last_name, email):
        """Register a new user."""
        try:
            user = TradeGPTRegistrationForm(first_name, last_name, email)
            user.validate()
            # If validation succeeds, you can add the user to your database here
            return {"success": True, "message": "Registration successful"}
        except ValueError as e:
            return {"success": False, "message": str(e)}

def main():
    # Example usage
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"
    result = TradeGPTRegistrationForm.register(first_name, last_name, email)
    print(result)

    # Test error handling
    first_name = ""
    last_name = "Doe"
    email = "john.doe@example.com"
    result = TradeGPTRegistrationForm.register(first_name, last_name, email)
    print(result)

if __name__ == "__main__":
    main()
```
