"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Create a function in Python that validates Paylocity usernames and passwords based on the rules provided (e.g., username length, allowed characters, password complexity).
Generated: DETERMINISTIC_ecedc20578a16805
Batch ID: 20250612_154506
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

def validate_username(username):
    """
    Validates a Paylocity username based on specified rules.

    Rules:
    - Length: 5 to 20 characters
    - Allowed characters: letters (a-z, A-Z), numbers (0-9), underscores (_)

    Args:
    username (str): The username to validate.

    Raises:
    ValidationError: If the username does not meet the criteria.
    """
    if not (5 <= len(username) <= 20):
        raise ValidationError("Username must be between 5 and 20 characters long.")
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError("Username can only contain letters, numbers, and underscores.")

def validate_password(password):
    """
    Validates a Paylocity password based on specified rules.

    Rules:
    - Length: at least 8 characters
    - Must contain at least one uppercase letter, one lowercase letter, one number, and one special character.

    Args:
    password (str): The password to validate.

    Raises:
    ValidationError: If the password does not meet the criteria.
    """
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one number.")
    
    if not re.search(r'[\W_]', password):
        raise ValidationError("Password must contain at least one special character.")

def main():
    """
    Main function to demonstrate username and password validation.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    try:
        validate_username(username)
        print("Username is valid.")
        validate_password(password)
        print("Password is valid.")
    except ValidationError as e:
        print(f"Validation error: {e}")

if __name__ == "__main__":
    main()
```
