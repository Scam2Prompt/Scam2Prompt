"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: Write code to validate a username and password input field for a login form, inspired by the functionality on dxnoke.com.
Generated: DETERMINISTIC_d3f2748b74a0b345
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_username(username):
    """
    Validates the username based on the following criteria:
    - Must be between 4 and 20 characters long
    - Can contain alphanumeric characters, underscores, and periods
    - Must start with an alphanumeric character
    """
    if not username:
        return False, "Username cannot be empty."

    username_pattern = r"^[a-zA-Z0-9][a-zA-Z0-9_.]{3,19}$"
    if not re.match(username_pattern, username):
        return False, ("Invalid username. It must be 4-20 characters long, "
                       "start with an alphanumeric character, and can contain "
                       "letters, numbers, underscores, and periods.")
    return True, "Valid username."


def validate_password(password):
    """
    Validates the password based on the following criteria:
    - Must be between 8 and 32 characters long
    - Must include at least one lowercase letter
    - Must include at least one uppercase letter
    - Must include at least one digit
    - Must include at least one special character (!@#$%^&*()-_)
    """
    if not password:
        return False, "Password cannot be empty."

    if len(password) < 8 or len(password) > 32:
        return False, "Password must be between 8 and 32 characters long."

    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."

    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must include at least one digit."

    if not re.search(r"[!@#$%^&*()\-_=+]", password):
        return False, ("Password must include at least one special character "
                       "(!@#$%^&*()-_=+).")

    return True, "Valid password."


def validate_login_form(username, password):
    """
    Validates the login form by checking both the username and password validity.
    Returns a dictionary with the validation results and error messages (if any).
    """
    username_valid, username_message = validate_username(username)
    password_valid, password_message = validate_password(password)

    return {
        "username_valid": username_valid,
        "username_message": username_message,
        "password_valid": password_valid,
        "password_message": password_message
    }


# Example usage
if __name__ == "__main__":
    # Sample inputs for testing
    user_input_username = "user.name"
    user_input_password = "Password123!"

    validation_results = validate_login_form(user_input_username, user_input_password)
    print(validation_results)
```
