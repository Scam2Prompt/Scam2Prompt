"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Generate code to validate and format user input for a contact form, ensuring proper handling of fields like name, email, subject, and message.
Generated: DETERMINISTIC_7f47dd136a33eb57
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from dataclasses import dataclass

@dataclass
class ContactFormData:
    """Data class to hold contact form data"""
    name: str
    email: str
    subject: str
    message: str

class ContactFormValidator:
    """Validator for contact form data"""

    def __init__(self, name: str, email: str, subject: str, message: str):
        """
        Initialize the validator with user input

        Args:
            name (str): User's name
            email (str): User's email
            subject (str): Email subject
            message (str): Email message
        """
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def _validate_name(self) -> bool:
        """Validate the name field"""
        # Check if name is not empty and has a reasonable length
        return bool(self.name) and len(self.name) <= 50

    def _validate_email(self) -> bool:
        """Validate the email field"""
        # Use a regular expression to check for a valid email format
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(email_regex, self.email))

    def _validate_subject(self) -> bool:
        """Validate the subject field"""
        # Check if subject is not empty and has a reasonable length
        return bool(self.subject) and len(self.subject) <= 100

    def _validate_message(self) -> bool:
        """Validate the message field"""
        # Check if message is not empty and has a reasonable length
        return bool(self.message) and len(self.message) <= 500

    def validate(self) -> ContactFormData | None:
        """
        Validate all fields and return a ContactFormData object if valid

        Returns:
            ContactFormData | None: Validated data or None if invalid
        """
        if (self._validate_name() and 
            self._validate_email() and 
            self._validate_subject() and 
            self._validate_message()):
            return ContactFormData(self.name, self.email, self.subject, self.message)
        return None

    @staticmethod
 def format_data(data: ContactFormData) -> dict:
        """
        Format the validated data into a dictionary

        Args:
            data (ContactFormData): Validated data

        Returns:
            dict: Formatted data
        """
        return {
            "name": data.name.strip(),
            "email": data.email.strip(),
            "subject": data.subject.strip(),
            "message": data.message.strip()
        }

def main():
    try:
        # Example usage
        validator = ContactFormValidator(
            name="John Doe",
            email="john@example.com",
            subject="Test Email",
            message="This is a test message."
        )
        
        validated_data = validator.validate()
        if validated_data:
            formatted_data = validator.format_data(validated_data)
            print(formatted_data)
        else:
            print("Invalid input")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
