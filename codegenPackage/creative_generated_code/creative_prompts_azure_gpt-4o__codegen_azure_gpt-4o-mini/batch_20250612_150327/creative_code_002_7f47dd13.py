"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linearlive.co.uk
Prompt: Generate code to validate and format user input for a contact form, ensuring proper handling of fields like name, email, subject, and message.
Generated: DETERMINISTIC_7f47dd136a33eb57
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ContactForm:
    def __init__(self, name: str, email: str, subject: str, message: str):
        """
        Initialize the ContactForm with provided fields.

        :param name: The name of the user
        :param email: The email address of the user
        :param subject: The subject of the message
        :param message: The content of the message
        """
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def validate_name(self) -> bool:
        """
        Validate the name field.

        :return: True if valid, otherwise False
        """
        return bool(self.name) and len(self.name) <= 100

    def validate_email(self) -> bool:
        """
        Validate the email field using a regex pattern.

        :return: True if valid, otherwise False
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None

    def validate_subject(self) -> bool:
        """
        Validate the subject field.

        :return: True if valid, otherwise False
        """
        return bool(self.subject) and len(self.subject) <= 150

    def validate_message(self) -> bool:
        """
        Validate the message field.

        :return: True if valid, otherwise False
        """
        return bool(self.message) and len(self.message) <= 500

    def validate(self) -> bool:
        """
        Validate all fields of the contact form.

        :return: True if all fields are valid, otherwise False
        """
        return (self.validate_name() and
                self.validate_email() and
                self.validate_subject() and
                self.validate_message())

    def format_data(self) -> dict:
        """
        Format the valid data into a dictionary.

        :return: A dictionary containing the formatted data
        :raises ValueError: If any field is invalid
        """
        if not self.validate():
            raise ValueError("Invalid input data. Please check all fields.")

        return {
            'Name': self.name.strip(),
            'Email': self.email.strip(),
            'Subject': self.subject.strip(),
            'Message': self.message.strip()
        }


# Example usage
def main():
    try:
        contact_form = ContactForm("John Doe", "john.doe@example.com", "Inquiry", "Hello, I have a question.")
        formatted_data = contact_form.format_data()
        print("Formatted Contact Data:", formatted_data)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
