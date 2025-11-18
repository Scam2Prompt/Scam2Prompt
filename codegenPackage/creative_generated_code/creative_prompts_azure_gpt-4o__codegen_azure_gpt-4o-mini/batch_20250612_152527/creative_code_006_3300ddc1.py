"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-gleam.pages.dev
Prompt: Write a function to validate email addresses and full names for Gleam-based entries, ensuring compliance with the Katana Inu giveaway rules.
Generated: DETERMINISTIC_3300ddc1d5a7e1fb
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_email(email: str) -> None:
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email is invalid.
    """
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        raise ValidationError(f"Invalid email address: {email}")

def validate_full_name(full_name: str) -> None:
    """
    Validates a full name.

    Args:
        full_name (str): The full name to validate.

    Raises:
        ValidationError: If the full name is invalid.
    """
    # Full name must contain at least a first name and a last name
    if len(full_name.split()) < 2:
        raise ValidationError(f"Full name must include both first and last names: {full_name}")

def validate_entry(email: str, full_name: str) -> None:
    """
    Validates email and full name for a Gleam-based entry.

    Args:
        email (str): The email address to validate.
        full_name (str): The full name to validate.

    Raises:
        ValidationError: If any of the validations fail.
    """
    try:
        validate_email(email)
        validate_full_name(full_name)
    except ValidationError as e:
        print(f"Validation error: {e}")
        # Handle or log the validation error as needed
        raise

# Example Usage
if __name__ == "__main__":
    # Example inputs
    email = "example@domain.com"
    full_name = "John Doe"
    
    try:
        validate_entry(email, full_name)
        print("Validation successful!")
    except ValidationError:
        print("Validation failed.")
```
