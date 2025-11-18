"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://port-3000-metamask-portfolio-master-acess8203.preview.codeanywhere.com
Prompt: Write a function to validate email and password inputs for a login system, similar to the one described on Codeanywhere.
Generated: DETERMINISTIC_5c0617396601660c
Batch ID: 20250612_150343
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
    Validates the provided email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email is invalid.
    """
    # Define a regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format.")

def validate_password(password: str) -> None:
    """
    Validates the provided password.

    Args:
        password (str): The password to validate.

    Raises:
        ValidationError: If the password is invalid.
    """
    # Password must be at least 8 characters long and contain a mix of letters and numbers
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Password must contain at least one letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one number.")

def login(email: str, password: str) -> str:
    """
    Validates login credentials and returns a success message.

    Args:
        email (str): The email address for login.
        password (str): The password for login.

    Returns:
        str: Success message if validation passes.

    Raises:
        ValidationError: If email or password validation fails.
    """
    # Validate email and password
    validate_email(email)
    validate_password(password)
    
    return "Login successful."

# Example usage:
if __name__ == "__main__":
    try:
        user_email = input("Enter your email: ")
        user_password = input("Enter your password: ")
        result = login(user_email, user_password)
        print(result)
    except ValidationError as ve:
        print(f"Error: {ve}")
```
