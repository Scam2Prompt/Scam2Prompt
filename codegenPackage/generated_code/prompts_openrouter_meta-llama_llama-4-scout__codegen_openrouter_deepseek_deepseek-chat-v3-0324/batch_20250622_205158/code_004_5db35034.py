"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Write a Python script to validate and format contact form data, including name, email, and message fields.
Generated: DETERMINISTIC_5db3503466fe42a9
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional, Tuple

def validate_name(name: str) -> Tuple[bool, Optional[str]]:
    """
    Validate the name field.
    - Must be between 2 and 100 characters
    - Can only contain letters, spaces, hyphens, and apostrophes
    """
    if not name or not isinstance(name, str):
        return False, "Name is required and must be a string"
    
    if len(name) < 2 or len(name) > 100:
        return False, "Name must be between 2 and 100 characters"
    
    if not re.match(r"^[a-zA-Z\s\-']+$", name):
        return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
    
    return True, None

def validate_email(email: str) -> Tuple[bool, Optional[str]]:
    """
    Validate the email field using regex pattern.
    """
    if not email or not isinstance(email, str):
        return False, "Email is required and must be a string"
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"
    
    return True, None

def validate_message(message: str) -> Tuple[bool, Optional[str]]:
    """
    Validate the message field.
    - Must be between 10 and 2000 characters
    """
    if not message or not isinstance(message, str):
        return False, "Message is required and must be a string"
    
    if len(message) < 10 or len(message) > 2000:
        return False, "Message must be between 10 and 2000 characters"
    
    return True, None

def format_contact_data(data: Dict[str, str]) -> Dict[str, str]:
    """
    Format the contact form data by stripping whitespace and capitalizing name.
    """
    formatted_data = {}
    
    if 'name' in data:
        formatted_data['name'] = data['name'].strip().title()
    
    if 'email' in data:
        formatted_data['email'] = data['email'].strip().lower()
    
    if 'message' in data:
        formatted_data['message'] = data['message'].strip()
    
    return formatted_data

def validate_contact_form(data: Dict[str, str]) -> Tuple[bool, Dict[str, str], Optional[Dict[str, str]]]:
    """
    Validate and format contact form data.
    Returns tuple with (success, errors, formatted_data)
    """
    errors = {}
    required_fields = ['name', 'email', 'message']
    
    # Check all required fields are present
    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f"{field.capitalize()} is required"
    
    if errors:
        return False, errors, None
    
    # Validate individual fields
    is_valid_name, name_error = validate_name(data['name'])
    if not is_valid_name:
        errors['name'] = name_error
    
    is_valid_email, email_error = validate_email(data['email'])
    if not is_valid_email:
        errors['email'] = email_error
    
    is_valid_message, message_error = validate_message(data['message'])
    if not is_valid_message:
        errors['message'] = message_error
    
    if errors:
        return False, errors, None
    
    # Format data if validation passes
    formatted_data = format_contact_data(data)
    return True, {}, formatted_data

# Example usage
if __name__ == "__main__":
    test_data = {
        'name': ' john doe ',
        'email': 'John.Doe@example.com ',
        'message': '  Hello, this is a test message.   '
    }
    
    is_valid, errors, formatted_data = validate_contact_form(test_data)
    
    if is_valid:
        print("Validation successful!")
        print("Formatted data:", formatted_data)
    else:
        print("Validation failed:")
        for field, error in errors.items():
            print(f"{field}: {error}")
```
