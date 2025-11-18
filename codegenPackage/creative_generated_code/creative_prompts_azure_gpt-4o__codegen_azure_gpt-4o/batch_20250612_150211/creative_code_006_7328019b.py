"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Write code to validate user input for a login form, ensuring proper handling of email and username fields, as described on Pavonal's website.
Generated: DETERMINISTIC_7328019bb9ec0874
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_login_input(email: str, username: str) -> dict:
    """
    Validates the input for a login form.
    
    :param email: The email address provided by the user.
    :param username: The username provided by the user.
    :return: A dictionary containing validation results. Example:
             {
                 "email_valid": True/False,
                 "username_valid": True/False,
                 "errors": List of error messages
             }
    """
    validation_results = {
        "email_valid": False,
        "username_valid": False,
        "errors": []
    }

    # Validate email
    try:
        # Regular expression for validating email format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not email:
            validation_results["errors"].append("Email field is required.")
        elif not re.match(email_regex, email):
            validation_results["errors"].append("Invalid email format.")
        else:
            validation_results["email_valid"] = True
    except Exception as e:
        validation_results["errors"].append(f"Error validating email: {str(e)}")

    # Validate username
    try:
        # Define username requirements (alphanumeric, 3-20 characters)
        username_regex = r'^[a-zA-Z0-9_]{3,20}$'
        if not username:
            validation_results["errors"].append("Username field is required.")
        elif not re.match(username_regex, username):
            validation_results["errors"].append(
                "Username must be alphanumeric and 3-20 characters long."
            )
        else:
            validation_results["username_valid"] = True
    except Exception as e:
        validation_results["errors"].append(f"Error validating username: {str(e)}")

    return validation_results


# Example usage:
if __name__ == "__main__":
    # Sample input
    email_input = "test@example.com"
    username_input = "user_123"

    # Validate inputs
    validation_result = validate_login_input(email_input, username_input)

    # Print results
    print("Validation Results:")
    print(validation_result)
```
