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

def validate_quote_request(data):
    """
    Validates the user input for a telephone quote request form.

    :param data: dict containing form fields and their values
    :return: tuple (bool, str) - (is_valid, error_message or success_message)
    """
    try:
        # Validate that all required fields exist
        required_fields = ['name', 'email', 'phone', 'address', 'zip_code']
        missing_fields = [field for field in required_fields if field not in data or not data[field].strip()]
        
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"

        # Validate name (must be alphabetic and non-empty)
        if not re.match(r'^[A-Za-z\s]+$', data['name']):
            return False, "Invalid name. Name should only contain alphabetic characters."

        # Validate email (basic regex pattern)
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, data['email']):
            return False, "Invalid email address."

        # Validate phone number (US phone number format: (xxx) xxx-xxxx or xxx-xxx-xxxx)
        phone_regex = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
        if not re.match(phone_regex, data['phone']):
            return False, "Invalid phone number. Accepted formats: (123) 456-7890 or 123-456-7890."

        # Validate address (non-empty)
        if not data['address']:
            return False, "Invalid address. Address cannot be empty."

        # Validate zip code (5 or 9 digits)
        zip_code_regex = r'^\d{5}(?:-\d{4})?$'
        if not re.match(zip_code_regex, data['zip_code']):
            return False, "Invalid zip code. Accepted formats: 12345 or 12345-6789."

        # If all validations pass
        return True, "Form is valid."
    
    except Exception as e:
        # General error handling
        return False, f"An error occurred during validation: {str(e)}"

# Example usage:
form_data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'phone': '(123) 456-7890',
    'address': '123 Main St',
    'zip_code': '12345'
}

is_valid, message = validate_quote_request(form_data)
print(message)
```
