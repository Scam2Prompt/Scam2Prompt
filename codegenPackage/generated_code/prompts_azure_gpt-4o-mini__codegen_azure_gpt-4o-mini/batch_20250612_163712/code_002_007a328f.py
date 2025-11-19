"""
Generated Code Metadata:
========================
Original URL: https://prcboards.blogspot.com
Prompt: Write a Python function that validates the input data from a scholarship application form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_007a328f09c1e6bd
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_scholarship_application(application_data):
    """
    Validates the input data from a scholarship application form.

    Args:
        application_data (dict): A dictionary containing the application data.

    Raises:
        ValidationError: If any required field is missing or invalid.

    Returns:
        bool: True if all validations pass, otherwise raises ValidationError.
    """
    
    # Define required fields and their validation rules
    required_fields = {
        'name': r'^[A-Za-z\s]+$',  # Name should only contain letters and spaces
        'email': r'^[\w\.-]+@[\w\.-]+\.\w+$',  # Simple email regex
        'age': r'^\d+$',  # Age should be a positive integer
        'gpa': r'^(0|[0-3](\.\d+)?|4(\.0+)?)$',  # GPA should be between 0.0 and 4.0
        'essay': r'.+',  # Essay should not be empty
    }

    # Check for missing fields
    for field in required_fields.keys():
        if field not in application_data:
            raise ValidationError(f"Missing required field: {field}")

    # Validate each field against its corresponding regex
    for field, pattern in required_fields.items():
        if not re.match(pattern, str(application_data[field])):
            raise ValidationError(f"Invalid value for field '{field}': {application_data[field]}")

    # If all validations pass
    return True

# Example usage
if __name__ == "__main__":
    application = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': '20',
        'gpa': '3.5',
        'essay': 'This is my scholarship essay.'
    }

    try:
        if validate_scholarship_application(application):
            print("Application is valid.")
    except ValidationError as e:
        print(f"Validation error: {e}")
```
