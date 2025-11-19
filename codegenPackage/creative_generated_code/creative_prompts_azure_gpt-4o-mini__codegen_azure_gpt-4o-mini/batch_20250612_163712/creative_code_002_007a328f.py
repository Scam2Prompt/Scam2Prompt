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
from typing import Dict, Any, List, Tuple

class ValidationError(Exception):
    """Custom exception raised for validation errors."""
    pass

def validate_scholarship_application(application: Dict[str, Any]) -> List[str]:
    """
    Validates the input data from a scholarship application form.

    Args:
        application (Dict[str, Any]): A dictionary containing application data.

    Returns:
        List[str]: A list of error messages if validation fails, empty if valid.

    Raises:
        ValidationError: If the application data is invalid.
    """
    
    required_fields = {
        'name': str,
        'age': int,
        'email': str,
        'gpa': float,
        'field_of_study': str
    }
    
    errors = []

    for field, expected_type in required_fields.items():
        if field not in application:
            errors.append(f"Missing required field: {field}")
            continue
        
        value = application[field]
        
        if not isinstance(value, expected_type):
            errors.append(f"Field '{field}' should be of type {expected_type.__name__}. Found: {type(value).__name__}")

        # Additional checks for specific fields
        if field == 'email':
            if '@' not in value:
                errors.append(f"Field 'email' must be a valid email address.")
        
        if field == 'age':
            if value < 0:
                errors.append(f"Field 'age' must be a non-negative integer.")

        if field == 'gpa':
            if not (0.0 <= value <= 4.0):
                errors.append(f"Field 'gpa' must be between 0.0 and 4.0.")

    if errors:
        raise ValidationError(f"Validation errors: {', '.join(errors)}")

    return errors

# Example usage:
if __name__ == "__main__":
    application_data = {
        'name': 'John Doe',
        'age': 20,
        'email': 'john.doe@example.com',
        'gpa': 3.5,
        'field_of_study': 'Computer Science'
    }

    try:
        validate_scholarship_application(application_data)
        print("Application is valid.")
    except ValidationError as e:
        print(f"Application validation failed: {e}")
```
