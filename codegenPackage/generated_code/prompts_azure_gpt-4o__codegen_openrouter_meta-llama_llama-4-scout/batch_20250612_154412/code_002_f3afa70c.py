"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: Generate code to validate form inputs for a telephony quote request system, ensuring fields like name, email, and phone number are correctly formatted.
Generated: DETERMINISTIC_f3afa70caf61ae26
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict

class TelephonyQuoteRequestValidator:
    """
    Validator for telephony quote request form inputs.
    """

    def __init__(self, form_data: Dict):
        """
        Initialize the validator with form data.

        Args:
        - form_data (Dict): A dictionary containing form inputs.
        """
        self.form_data = form_data

    def validate_name(self) -> bool:
        """
        Validate the name field.

        Returns:
        - bool: True if valid, False otherwise.
        """
        name = self.form_data.get('name')
        if not name:
            raise ValueError("Name is required")
        if len(name) < 2 or len(name) > 50:
            raise ValueError("Name must be between 2 and 50 characters")
        return True

    def validate_email(self) -> bool:
        """
        Validate the email field.

        Returns:
        - bool: True if valid, False otherwise.
        """
        email = self.form_data.get('email')
        if not email:
            raise ValueError("Email is required")
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return True

    def validate_phone_number(self) -> bool:
        """
        Validate the phone number field.

        Returns:
        - bool: True if valid, False otherwise.
        """
        phone_number = self.form_data.get('phone_number')
        if not phone_number:
            raise ValueError("Phone number is required")
        phone_regex = r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
        if not re.match(phone_regex, phone_number):
            raise ValueError("Invalid phone number format")
        return True

    def validate(self) -> bool:
        """
        Validate all form inputs.

        Returns:
        - bool: True if all fields are valid, False otherwise.
        """
        try:
            self.validate_name()
            self.validate_email()
            self.validate_phone_number()
            return True
        except ValueError as e:
            print(f"Validation error: {e}")
            return False


def main():
    # Example usage:
    form_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone_number': '(123) 456-7890'
    }

    validator = TelephonyQuoteRequestValidator(form_data)
    if validator.validate():
        print("Form is valid")
    else:
        print("Form is invalid")


if __name__ == "__main__":
    main()
```
