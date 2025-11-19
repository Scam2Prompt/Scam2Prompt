"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Write code to validate user input for a donation form, ensuring fields like first name, last name, and email are correctly formatted.
Generated: DETERMINISTIC_184c1ec73a4982b4
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class DonationFormValidator:
    """
    A class to validate user input for a donation form.
    """

    def __init__(self, first_name: str, last_name: str, email: str):
        """
        Initializes the DonationFormValidator with user input.

        :param first_name: The first name of the donor.
        :param last_name: The last name of the donor.
        :param email: The email address of the donor.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def validate(self) -> bool:
        """
        Validates the user input for the donation form.

        :return: True if all fields are valid, False otherwise.
        """
        return (self.validate_name(self.first_name) and
                self.validate_name(self.last_name) and
                self.validate_email(self.email))

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validates the name field to ensure it contains only alphabetic characters.

        :param name: The name to validate.
        :return: True if valid, False otherwise.
        """
        if not name or not name.isalpha():
            print(f"Invalid name: '{name}'. Name must contain only alphabetic characters.")
            return False
        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates the email field to ensure it is in the correct format.

        :param email: The email to validate.
        :return: True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            print(f"Invalid email: '{email}'. Please enter a valid email address.")
            return False
        return True

# Example usage
if __name__ == "__main__":
    # Sample user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")

    # Create a validator instance
    validator = DonationFormValidator(first_name, last_name, email)

    # Validate the input
    if validator.validate():
        print("All inputs are valid. Thank you for your donation!")
    else:
        print("Please correct the errors in your input.")
```
