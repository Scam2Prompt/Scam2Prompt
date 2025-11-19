"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Provide an example of how to validate loan application data before sending it to Tymebank's API.
Generated: DETERMINISTIC_b05232ec6de5a73e
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class LoanApplicationValidator:
    """
    A class to validate loan application data before sending it to Tymebank's API.
    """

    def __init__(self):
        # Regular expressions for validation purposes
        self.email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        self.phone_regex = re.compile(r"^\+?[\d\s]{7,15}$")
        self.id_regex = re.compile(r"^[A-Za-z0-9]{6,12}$")

    def validate(self, application_data):
        """
        Validate the loan application data.

        :param application_data: dict containing loan application fields
        :return: tuple (bool, str) where bool indicates validity, and str contains error message or 'Valid'
        """
        # Required fields
        required_fields = ["full_name", "email", "phone_number", "id_number", "amount_requested"]

        # Check for missing fields
        for field in required_fields:
            if field not in application_data:
                return False, f"Missing required field: {field}"
            if not application_data[field]:
                return False, f"Field {field} cannot be empty."

        # Validate full name
        if not isinstance(application_data["full_name"], str) or len(application_data["full_name"]) < 3:
            return False, "Full name must be a string with at least 3 characters."

        # Validate email address
        if not self.email_regex.match(application_data["email"]):
            return False, "Invalid email address format."

        # Validate phone number
        if not self.phone_regex.match(application_data["phone_number"]):
            return False, "Invalid phone number format. Must be 7-15 digits and may include a '+'."

        # Validate ID number
        if not self.id_regex.match(application_data["id_number"]):
            return False, "Invalid ID number format. Must be alphanumeric and 6-12 characters."

        # Validate loan amount
        try:
            amount = float(application_data["amount_requested"])
            if amount <= 0:
                return False, "Amount requested must be greater than 0."
        except ValueError:
            return False, "Amount requested must be a valid number."

        # If all validations pass
        return True, "Valid"

# Example usage
if __name__ == "__main__":
    # Sample loan application data
    loan_application = {
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "phone_number": "+1234567890",
        "id_number": "AB123456",
        "amount_requested": 10000
    }

    # Create a validator instance
    validator = LoanApplicationValidator()

    # Validate the loan application data
    is_valid, message = validator.validate(loan_application)

    # Print validation result
    if is_valid:
        print("Loan application data is valid. Ready to send to Tymebank's API.")
    else:
        print(f"Loan application validation failed: {message}")
```
