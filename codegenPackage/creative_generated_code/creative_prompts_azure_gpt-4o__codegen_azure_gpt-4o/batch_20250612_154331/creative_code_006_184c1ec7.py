"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Write code to validate user input for a donation form, ensuring fields like first name, last name, and email are correctly formatted.
Generated: DETERMINISTIC_184c1ec73a4982b4
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_donation_form(data):
    """
    Validates a donation form's input data.

    Args:
        data (dict): Dictionary containing form input values with keys:
            - 'first_name': str, the first name of the user
            - 'last_name': str, the last name of the user
            - 'email': str, the user's email address

    Returns:
        tuple: (bool, str) where the first value indicates success (True if valid, False otherwise),
               and the second value contains an error message if validation fails.
    """
    # Validate first name
    if not data.get('first_name') or not isinstance(data['first_name'], str):
        return False, "First name is required and must be a string."
    if not re.match(r"^[a-zA-Z\s'-]+$", data['first_name']):
        return False, "First name contains invalid characters."
    
    # Validate last name
    if not data.get('last_name') or not isinstance(data['last_name'], str):
        return False, "Last name is required and must be a string."
    if not re.match(r"^[a-zA-Z\s'-]+$", data['last_name']):
        return False, "Last name contains invalid characters."
    
    # Validate email
    if not data.get('email') or not isinstance(data['email'], str):
        return False, "Email is required and must be a string."
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, data['email']):
        return False, "Email is not valid."

    # All validations passed
    return True, "Validation successful."

# Example usage
if __name__ == "__main__":
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com'
    }

    is_valid, message = validate_donation_form(form_data)
    if is_valid:
        print("Form is valid.")
    else:
        print(f"Form is invalid: {message}")
```
