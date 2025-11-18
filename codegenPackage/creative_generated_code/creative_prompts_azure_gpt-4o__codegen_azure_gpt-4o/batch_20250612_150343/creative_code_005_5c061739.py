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

def validate_email_and_password(email: str, password: str) -> dict:
    """
    Validates email and password inputs for a login system.

    Args:
        email (str): The email address to validate.
        password (str): The password to validate.

    Returns:
        dict: A dictionary containing success status and error messages (if any).
    """

    errors = {
        "email": None,
        "password": None
    }

    # Validate email using a regular expression
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str) or not re.match(email_regex, email):
        errors['email'] = "Invalid email format."

    # Validate password (minimum 8 characters, at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character)
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not isinstance(password, str) or not re.match(password_regex, password):
        errors['password'] = ("Password must be at least 8 characters long, "
                              "contain one uppercase letter, one lowercase letter, "
                              "one digit, and one special character.")

    # Check if there are any errors
    success = not any(errors.values())
    return {
        "success": success,
        "errors": errors if not success else None
    }

# Example Usage
if __name__ == "__main__":
    result = validate_email_and_password("test@example.com", "Password123!")
    print(result)
```
