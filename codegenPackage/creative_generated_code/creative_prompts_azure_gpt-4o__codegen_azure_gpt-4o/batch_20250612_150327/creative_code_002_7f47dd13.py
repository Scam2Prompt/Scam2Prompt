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

def validate_and_format_contact_form(data):
    """
    Validates and formats user input for a contact form.
    
    Args:
        data (dict): A dictionary containing the following keys:
            - name (str): User's name
            - email (str): User's email
            - subject (str): Subject of the message
            - message (str): Message content
    
    Returns:
        dict: A dictionary with validated and formatted data.
    
    Raises:
        ValueError: If any of the fields fail validation.
    """
    
    # Validation helper functions
    def validate_name(name):
        """
        Validates the name field.
        Must be non-empty and contain only alphabetic characters and spaces.
        """
        if not name or not re.match(r"^[a-zA-Z\s]+$", name):
            raise ValueError("Invalid name. Only alphabetic characters and spaces are allowed.")
        return name.strip().title()  # Format: Remove leading/trailing spaces, capitalize first letters.

    def validate_email(email):
        """
        Validates the email field using a regular expression.
        """
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not email or not re.match(email_pattern, email):
            raise ValueError("Invalid email address.")
        return email.strip().lower()  # Format: Remove leading/trailing spaces and convert to lowercase.

    def validate_subject(subject):
        """
        Validates the subject field.
        Must be non-empty and less than or equal to 100 characters.
        """
        if not subject or len(subject) > 100:
            raise ValueError("Invalid subject. Must be non-empty and at most 100 characters.")
        return subject.strip().capitalize()  # Format: Remove leading/trailing spaces, capitalize first letter.

    def validate_message(message):
        """
        Validates the message field.
        Must be non-empty and less than or equal to 1000 characters.
        """
        if not message or len(message) > 1000:
            raise ValueError("Invalid message. Must be non-empty and at most 1000 characters.")
        return message.strip()  # Format: Remove leading/trailing spaces.

    try:
        # Validate and format each field
        validated_data = {
            "name": validate_name(data.get("name", "")),
            "email": validate_email(data.get("email", "")),
            "subject": validate_subject(data.get("subject", "")),
            "message": validate_message(data.get("message", "")),
        }
        return validated_data
    except ValueError as e:
        # Handle validation errors
        raise ValueError(f"Validation error: {str(e)}") from e


# Example usage
if __name__ == "__main__":
    contact_form_data = {
        "name": " john doe ",
        "email": "John.Doe@example.COM ",
        "subject": "   Hello world   ",
        "message": "   This is a test message for validation and formatting.   ",
    }

    try:
        formatted_data = validate_and_format_contact_form(contact_form_data)
        print("Validated and formatted data:", formatted_data)
    except ValueError as error:
        print("Error:", error)
```
