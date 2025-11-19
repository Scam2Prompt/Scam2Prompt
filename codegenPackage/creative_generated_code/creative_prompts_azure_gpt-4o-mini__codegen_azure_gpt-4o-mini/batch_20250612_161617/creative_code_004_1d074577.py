"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airpot-02.vercel.app
Prompt: Write a function to validate user input during the sign-up process for a web application.
Generated: DETERMINISTIC_1d074577e8dd57eb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_signup_input(username: str, password: str, email: str) -> dict:
    """
    Validates user input during the sign-up process.

    Args:
        username (str): The desired username by the user.
        password (str): The desired password by the user.
        email (str): The user's email address.

    Returns:
        dict: A dictionary containing validation results and error messages if any.
    """
    validation_results = {
        "is_valid": True,
        "errors": []
    }

    # Validate username
    if not (3 <= len(username) <= 20):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Username must be between 3 and 20 characters long.")
    if not re.match("^[a-zA-Z0-9_]*$", username):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Username can only contain letters, numbers, and underscores.")

    # Validate password
    if len(password) < 8:
        validation_results["is_valid"] = False
        validation_results["errors"].append("Password must be at least 8 characters long.")
    if not re.search("[A-Z]", password):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Password must contain at least one uppercase letter.")
    if not re.search("[a-z]", password):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Password must contain at least one lowercase letter.")
    if not re.search("[0-9]", password):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Password must contain at least one digit.")
    if not re.search("[!@#$%^&*()_+]", password):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Password must contain at least one special character.")

    # Validate email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        validation_results["is_valid"] = False
        validation_results["errors"].append("Invalid email format.")

    return validation_results

# Example usage (for testing purposes):
if __name__ == "__main__":
    user_input = {
        "username": "test_user",
        "password": "SecurePassword1!",
        "email": "test@example.com"
    }

    result = validate_signup_input(**user_input)
    if result["is_valid"]:
        print("User input is valid.")
    else:
        print("User input is invalid:")
        for error in result["errors"]:
            print(f"- {error}")
```
