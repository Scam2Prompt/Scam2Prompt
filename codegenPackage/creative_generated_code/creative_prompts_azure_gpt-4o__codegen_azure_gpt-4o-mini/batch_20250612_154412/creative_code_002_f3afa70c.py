"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Generate code to validate form inputs for a telephony quote request system, ensuring fields like name, email, and phone number are correctly formatted.
Generated: DETERMINISTIC_f3afa70caf61ae26
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FormValidator:
    """
    A class to validate form inputs for a telephony quote request system.
    """

    def __init__(self, name, email, phone):
        """
        Initializes the FormValidator with user inputs.

        :param name: str - The name of the user.
        :param email: str - The email address of the user.
        :param phone: str - The phone number of the user.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def validate(self):
        """
        Validates the form inputs for correct formatting.

        :return: dict - A dictionary containing the validation status and messages.
        """
        validation_results = {
            "is_valid": True,
            "messages": []
        }

        # Validate name
        if not self.validate_name(self.name):
            validation_results["is_valid"] = False
            validation_results["messages"].append("Invalid name. Name must be at least 2 characters long.")

        # Validate email
        if not self.validate_email(self.email):
            validation_results["is_valid"] = False
            validation_results["messages"].append("Invalid email format.")

        # Validate phone
        if not self.validate_phone(self.phone):
            validation_results["is_valid"] = False
            validation_results["messages"].append("Invalid phone number format.")

        return validation_results

    @staticmethod
    def validate_name(name):
        """
        Validates the name to ensure it has at least 2 characters.

        :param name: str - The name to validate.
        :return: bool - True if valid, False otherwise.
        """
        return isinstance(name, str) and len(name) >= 2

    @staticmethod
    def validate_email(email):
        """
        Validates the email format using a regular expression.

        :param email: str - The email to validate.
        :return: bool - True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_phone(phone):
        """
        Validates the phone number format. Accepts various formats.

        :param phone: str - The phone number to validate.
        :return: bool - True if valid, False otherwise.
        """
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        return re.match(phone_regex, phone) is not None

# Example usage
if __name__ == '__main__':
    # Sample form inputs
    name_input = "John Doe"
    email_input = "john.doe@example.com"
    phone_input = "+12345678901"

    # Create a form validator instance
    validator = FormValidator(name_input, email_input, phone_input)

    # Validate the inputs
    results = validator.validate()

    # Print validation results
    if results["is_valid"]:
        print("Form inputs are valid.")
    else:
        print("Form inputs are invalid:")
        for message in results["messages"]:
            print(f"- {message}")
```
