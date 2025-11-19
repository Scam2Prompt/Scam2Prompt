"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Write a code snippet to validate user credentials for a Paylocity login, ensuring it meets the password requirements mentioned on the site.
Generated: DETERMINISTIC_880e360f2c26c3af
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_credentials(username, password):
    """
    Validates user credentials for Paylocity login.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        (bool, str): Tuple containing validation status (True/False) and error message if invalid.
    """
    # Check if username is empty or contains only whitespace
    if not username.strip():
        return False, "Username cannot be empty."

    # Paylocity password requirements:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # - Contains at least one special character
    # - No whitespace allowed

    # Check password length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    # Check for digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    # Check for special character
    special_char_pattern = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_char_pattern, password):
        return False, "Password must contain at least one special character."

    # Check for whitespace
    if any(char.isspace() for char in password):
        return False, "Password cannot contain whitespace."

    # If all conditions are met, credentials are valid
    return True, "Credentials are valid."

# Example usage
username = "testUser"
password = "Passw0rd!"
is_valid, message = validate_credentials(username, password)
print(message)
```
