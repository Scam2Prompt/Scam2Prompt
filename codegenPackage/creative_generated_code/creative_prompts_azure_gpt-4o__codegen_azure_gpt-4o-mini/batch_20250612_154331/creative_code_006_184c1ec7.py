"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Write code to validate user input for a donation form, ensuring fields like first name, last name, and email are correctly formatted.
Generated: DETERMINISTIC_184c1ec73a4982b4
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class DonationFormValidator:
    """
    A class to validate user input for a donation form.
    Attributes:
        first_name (str): The first name of the donor.
        last_name (str): The last name of the donor.
        email (str): The email address of the donor.
    """

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def validate(self) -> bool:
        """
        Validate the donation form fields.
        
        Returns:
            bool: True if all fields are valid; False otherwise.
        """
        return (self.validate_name(self.first_name) and
                self.validate_name(self.last_name) and
                self.validate_email(self.email))

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validate name fields to ensure they contain only alphabetic characters.
        
        Args:
            name (str): The name to validate.

        Returns:
            bool: True if the name is valid; False otherwise.
        """
        if not name or not isinstance(name, str):
            return False
        return bool(re.match("^[A-Za-z]+$", name))

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate the email format using a regular expression.
        
        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email format is valid; False otherwise.
        """
        if not email or not isinstance(email, str):
            return False
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))

# Example Usage
if __name__ == "__main__":
    # Sample user input
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"

    # Create a validator instance
    validator = DonationFormValidator(first_name, last_name, email)

    # Validate input
    if validator.validate():
        print("All fields are valid.")
    else:
        print("Invalid input detected.")
```
