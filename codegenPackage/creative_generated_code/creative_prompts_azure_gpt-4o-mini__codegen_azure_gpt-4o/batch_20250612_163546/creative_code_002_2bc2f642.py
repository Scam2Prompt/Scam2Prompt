"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Write a function that validates user input for a form that includes fields like client number and date of birth, as seen in the Proximus client form.
Generated: DETERMINISTIC_2bc2f642e5445ec0
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

def validate_form_input(client_number, date_of_birth):
    """
    Validates user input for a form.

    Parameters:
    - client_number (str): Client number, expected to be a numeric string of exactly 8 digits.
    - date_of_birth (str): Date of birth in the format 'YYYY-MM-DD'.

    Returns:
    - dict: Contains `is_valid` (bool) and `errors` (list of validation error messages).
    """
    errors = []

    # Validate client number: must be an 8-digit numeric string
    if not re.match(r'^\d{8}$', client_number):
        errors.append("Client number must be an 8-digit numeric string.")

    # Validate date of birth: must match 'YYYY-MM-DD' format and be a valid date
    try:
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
        if dob > datetime.now():
            errors.append("Date of birth cannot be in the future.")
    except ValueError:
        errors.append("Date of birth must be in the format 'YYYY-MM-DD' and a valid date.")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

# Example usage
if __name__ == '__main__':
    # Test the function with sample data
    test_client_number = "12345678"
    test_date_of_birth = "2000-01-01"
    result = validate_form_input(test_client_number, test_date_of_birth)
    if result["is_valid"]:
        print("Validation successful!")
    else:
        print("Validation failed with errors:", result["errors"])
```
