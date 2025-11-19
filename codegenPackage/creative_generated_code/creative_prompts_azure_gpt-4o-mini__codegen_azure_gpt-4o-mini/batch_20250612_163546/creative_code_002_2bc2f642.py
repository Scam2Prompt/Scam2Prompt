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

class InputValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

def validate_client_number(client_number: str) -> None:
    """
    Validate the client number.
    
    Args:
        client_number (str): The client number to validate.

    Raises:
        InputValidationError: If the client number is invalid.
    """
    if not client_number.isdigit() or len(client_number) != 8:
        raise InputValidationError("Client number must be an 8-digit number.")

def validate_date_of_birth(dob: str) -> None:
    """
    Validate the date of birth.

    Args:
        dob (str): The date of birth in 'YYYY-MM-DD' format.

    Raises:
        InputValidationError: If the date of birth is invalid or indicates an age under 18.
    """
    try:
        date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        raise InputValidationError("Date of birth must be in 'YYYY-MM-DD' format.")
    
    # Check if the user is at least 18 years old
    age = (datetime.now() - date_of_birth).days // 365
    if age < 18:
        raise InputValidationError("User must be at least 18 years old.")

def validate_user_input(client_number: str, dob: str) -> None:
    """
    Validate user input for client number and date of birth.

    Args:
        client_number (str): The client number to validate.
        dob (str): The date of birth to validate.

    Raises:
        InputValidationError: If any of the inputs are invalid.
    """
    validate_client_number(client_number)
    validate_date_of_birth(dob)

# Example usage
if __name__ == "__main__":
    try:
        # Example client number and date of birth
        client_number = "12345678"
        dob = "2000-01-01"
        
        # Validate inputs
        validate_user_input(client_number, dob)
        print("All inputs are valid.")
    except InputValidationError as e:
        print(f"Input validation error: {e}")
```
