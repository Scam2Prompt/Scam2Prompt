"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Write a Python function that validates the input data from a scholarship application form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_007a328f09c1e6bd
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_scholarship_application(form_data):
    """
    Validates the input data from a scholarship application form.
    
    Args:
        form_data (dict): A dictionary containing the form fields and their values.
                          Expected keys: 'full_name', 'email', 'age', 'phone_number', 'essay'
    
    Returns:
        dict: A dictionary containing validation results with the following keys:
              - 'is_valid' (bool): Indicates whether the form is valid.
              - 'errors' (dict): A dictionary containing error messages for invalid fields.
    """
    errors = {}
    
    # Validate 'full_name' - Required and must be at least 2 characters long
    if not form_data.get('full_name'):
        errors['full_name'] = "Full name is required."
    elif len(form_data['full_name'].strip()) < 2:
        errors['full_name'] = "Full name must be at least 2 characters long."
    
    # Validate 'email' - Required and must be a valid email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not form_data.get('email'):
        errors['email'] = "Email is required."
    elif not re.match(email_regex, form_data['email']):
        errors['email'] = "Invalid email format."
    
    # Validate 'age' - Required and must be an integer between 18 and 100
    if not form_data.get('age'):
        errors['age'] = "Age is required."
    else:
        try:
            age = int(form_data['age'])
            if age < 18 or age > 100:
                errors['age'] = "Age must be between 18 and 100."
        except ValueError:
            errors['age'] = "Age must be a valid integer."
    
    # Validate 'phone_number' - Required and must be a valid phone number format
    phone_regex = r'^\+?[0-9]{10,15}$'  # Supports international format with optional '+' sign
    if not form_data.get('phone_number'):
        errors['phone_number'] = "Phone number is required."
    elif not re.match(phone_regex, form_data['phone_number']):
        errors['phone_number'] = "Invalid phone number format."
    
    # Validate 'essay' - Required and must be at least 100 characters long
    if not form_data.get('essay'):
        errors['essay'] = "Essay is required."
    elif len(form_data['essay'].strip()) < 100:
        errors['essay'] = "Essay must be at least 100 characters long."
    
    # Return validation results
    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }


# Example usage:
# form_data = {
#     "full_name": "John Doe",
#     "email": "john.doe@example.com",
#     "age": "20",
#     "phone_number": "+1234567890",
#     "essay": "This is my scholarship essay, which is over 100 characters long."
# }
# result = validate_scholarship_application(form_data)
# print(result)
```
