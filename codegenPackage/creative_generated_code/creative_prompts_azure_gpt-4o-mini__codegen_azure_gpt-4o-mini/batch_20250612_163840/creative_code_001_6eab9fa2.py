"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Write a function that validates user input for an event checkout form, ensuring fields like email and full name are required, as seen in the AI Crypto Summit registration process.
Generated: DETERMINISTIC_6eab9fa2f4270e33
Batch ID: 20250612_163840
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
    """Validate the given email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email format is invalid.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format.")

def validate_full_name(full_name: str) -> None:
    """Validate the user's full name.

    Args:
        full_name (str): The full name to validate.

    Raises:
        ValidationError: If the full name is empty.
    """
    if not full_name.strip():
        raise ValidationError("Full name is required.")

def validate_event_checkout_form(email: str, full_name: str) -> None:
    """Validate the event checkout form inputs.

    Args:
        email (str): The user's email address.
        full_name (str): The user's full name.

    Raises:
        ValidationError: If any of the required fields are invalid.
    """
    try:
        validate_email(email)
        validate_full_name(full_name)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Test the validation function with example inputs
    try:
        validate_event_checkout_form("test@example.com", "John Doe")
        print("Validation passed.")
    except ValidationError:
        print("Validation failed.")
```
