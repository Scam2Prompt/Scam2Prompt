"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Create a function in Python that validates Paylocity usernames and passwords based on the rules provided (e.g., username length, allowed characters, password complexity).
Generated: DETERMINISTIC_ecedc20578a16805
Batch ID: 20250612_154506
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

def validate_username(username: str) -> bool:
    """
    Validates the Paylocity username.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, otherwise raises ValidationError.

    Raises:
        ValidationError: If the username does not meet the criteria.
    """
    if not (5 <= len(username) <= 20):
        raise ValidationError("Username must be between 5 and 20 characters long.")
    
    if not re.match("^[a-zA-Z0-9._-]+$", username):
        raise ValidationError("Username can only contain letters, numbers, dots, underscores, and hyphens.")
    
    return True

def validate_password(password: str) -> bool:
    """
    Validates the Paylocity password.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, otherwise raises ValidationError.

    Raises:
        ValidationError: If the password does not meet the criteria.
    """
    if not (8 <= len(password) <= 20):
        raise ValidationError("Password must be between 8 and 20 characters long.")
    
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one digit.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must contain at least one special character.")
    
    return True

def validate_credentials(username: str, password: str) -> bool:
    """
    Validates both username and password for Paylocity.

    Args:
        username (str): The username to validate.
        password (str): The password to validate.

    Returns:
        bool: True if both username and password are valid.

    Raises:
        ValidationError: If either username or password is invalid.
    """
    try:
        validate_username(username)
        validate_password(password)
    except ValidationError as e:
        print(f"Validation error: {e}")
        return False
    
    return True

# Example usage
if __name__ == "__main__":
    username_input = "user.name-123"
    password_input = "Password1!"

    if validate_credentials(username_input, password_input):
        print("Username and password are valid.")
    else:
        print("Invalid username or password.")
```
