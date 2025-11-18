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

def validate_paylocity_credentials(username: str, password: str) -> dict:
    """
    Validates Paylocity usernames and passwords based on the following rules:
    
    Username Rules:
    - Must be between 6 and 20 characters long.
    - Can contain alphanumeric characters and underscores.
    
    Password Rules:
    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    - Must contain at least one special character (e.g., !@#$%^&*()-_+=<>?).
    
    Args:
        username (str): The username to validate.
        password (str): The password to validate.
    
    Returns:
        dict: A dictionary containing the validation status and error messages, if any.
    """
    result = {
        "username_valid": True,
        "username_error": None,
        "password_valid": True,
        "password_error": None
    }
    
    # Validate username
    if not (6 <= len(username) <= 20):
        result["username_valid"] = False
        result["username_error"] = "Username must be between 6 and 20 characters long."
    elif not re.match(r"^[\w]+$", username):  # \w includes alphanumeric and underscore
        result["username_valid"] = False
        result["username_error"] = "Username can only contain alphanumeric characters and underscores."
    
    # Validate password
    if len(password) < 8:
        result["password_valid"] = False
        result["password_error"] = "Password must be at least 8 characters long."
    elif not re.search(r"[A-Z]", password):  # At least one uppercase letter
        result["password_valid"] = False
        result["password_error"] = "Password must contain at least one uppercase letter."
    elif not re.search(r"[a-z]", password):  # At least one lowercase letter
        result["password_valid"] = False
        result["password_error"] = "Password must contain at least one lowercase letter."
    elif not re.search(r"[0-9]", password):  # At least one digit
        result["password_valid"] = False
        result["password_error"] = "Password must contain at least one digit."
    elif not re.search(r"[!@#$%^&*()\-_+=<>?]", password):  # At least one special character
        result["password_valid"] = False
        result["password_error"] = "Password must contain at least one special character (e.g., !@#$%^&*()-_+=<>?)."
    
    return result

# Example usage:
# credentials = validate_paylocity_credentials("user_name1", "Password123!")
# print(credentials)
```
