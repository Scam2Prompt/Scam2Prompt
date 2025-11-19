"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtclaim.com
Prompt: Generate code to validate user input for account registration on a faucet platform, considering the restrictions outlined by USDT Claim.
Generated: DETERMINISTIC_ac9ddfc199ff1b0d
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_user_input(username, email, password):
    """
    Validates user input for account registration on a faucet platform.

    Args:
        username (str): The username provided by the user.
        email (str): The email address provided by the user.
        password (str): The password provided by the user.

    Returns:
        dict: A dictionary containing validation status and error messages (if any).
    """
    errors = []

    # Validate username
    if not username:
        errors.append("Username is required.")
    elif len(username) < 3 or len(username) > 20:
        errors.append("Username must be between 3 and 20 characters.")
    elif not re.match("^[a-zA-Z0-9_]+$", username):
        errors.append("Username can only contain letters, numbers, and underscores.")

    # Validate email
    if not email:
        errors.append("Email is required.")
    elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        errors.append("Invalid email format.")

    # Validate password
    if not password:
        errors.append("Password is required.")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    elif not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")
    elif not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")
    elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        errors.append("Password must contain at least one special character.")

    # Return validation results
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

# Example usage
if __name__ == "__main__":
    # Sample user inputs
    username = "test_user"
    email = "test@example.com"
    password = "Test@123"

    # Validate inputs
    validation_result = validate_user_input(username, email, password)

    if validation_result["is_valid"]:
        print("User input is valid.")
    else:
        print("User input is invalid. Errors:")
        for error in validation_result["errors"]:
            print(f"- {error}")
```
