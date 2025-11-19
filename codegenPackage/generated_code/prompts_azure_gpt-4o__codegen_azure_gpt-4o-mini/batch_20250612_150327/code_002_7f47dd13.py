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

class ContactFormValidator:
    """A class to validate and format user input for a contact form."""

    def __init__(self, name: str, email: str, subject: str, message: str):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def validate_name(self) -> bool:
        """Validate the name field."""
        if not self.name or len(self.name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        return True

    def validate_email(self) -> bool:
        """Validate the email field using a regex pattern."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, self.email):
            raise ValueError("Invalid email address format.")
        return True

    def validate_subject(self) -> bool:
        """Validate the subject field."""
        if not self.subject or len(self.subject) < 3:
            raise ValueError("Subject must be at least 3 characters long.")
        return True

    def validate_message(self) -> bool:
        """Validate the message field."""
        if not self.message or len(self.message) < 10:
            raise ValueError("Message must be at least 10 characters long.")
        return True

    def format_input(self) -> dict:
        """Format the validated input for further processing."""
        return {
            'name': self.name.strip(),
            'email': self.email.strip().lower(),
            'subject': self.subject.strip(),
            'message': self.message.strip()
        }

    def validate_all(self) -> dict:
        """Validate all fields and return formatted input if valid."""
        try:
            self.validate_name()
            self.validate_email()
            self.validate_subject()
            self.validate_message()
            return self.format_input()
        except ValueError as e:
            raise ValueError(f"Validation error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Sample user input
        user_input = {
            'name': 'John Doe',
            'email': 'John.Doe@example.com',
            'subject': 'Inquiry',
            'message': 'I would like to know more about your services.'
        }

        # Create a validator instance
        validator = ContactFormValidator(**user_input)

        # Validate and format input
        formatted_input = validator.validate_all()
        print("Validated and formatted input:", formatted_input)

    except ValueError as e:
        print(e)
```
