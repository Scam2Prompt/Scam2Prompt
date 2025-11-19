"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Write a function that validates user input for a telephone quote request form, ensuring all fields are filled correctly.
Generated: DETERMINISTIC_7db5ee5acb6b37c5
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class TelephoneQuoteRequestValidator:
    """
    A class to validate user input for a telephone quote request form.
    """

    def __init__(self, name: str, phone: str, email: str):
        """
        Initializes the validator with user input.

        :param name: The name of the user.
        :param phone: The user's phone number.
        :param email: The user's email address.
        """
        self.name = name
        self.phone = phone
        self.email = email

    def validate(self):
        """
        Validates the user input for the quote request.

        :raises ValueError: If any validation fails.
        :return: True if all inputs are valid.
        """
        if not self._is_name_valid(self.name):
            raise ValueError("Invalid name: Name must be alphabetic and not empty.")
        
        if not self._is_phone_valid(self.phone):
            raise ValueError("Invalid phone number: Must be 10 digits long.")
        
        if not self._is_email_valid(self.email):
            raise ValueError("Invalid email: Must be a valid email format.")
        
        return True

    def _is_name_valid(self, name: str) -> bool:
        """
        Checks if the name is valid.

        :param name: The name to validate.
        :return: True if valid, otherwise False.
        """
        return bool(name) and name.isalpha()

    def _is_phone_valid(self, phone: str) -> bool:
        """
        Checks if the phone number is valid.

        :param phone: The phone number to validate.
        :return: True if valid, otherwise False.
        """
        return bool(re.fullmatch(r'\d{10}', phone))

    def _is_email_valid(self, email: str) -> bool:
        """
        Checks if the email is valid.

        :param email: The email to validate.
        :return: True if valid, otherwise False.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))


# Example usage
if __name__ == "__main__":
    try:
        validator = TelephoneQuoteRequestValidator("JohnDoe", "1234567890", "john.doe@example.com")
        if validator.validate():
            print("All inputs are valid.")
    except ValueError as e:
        print(f"Validation error: {e}")
```
