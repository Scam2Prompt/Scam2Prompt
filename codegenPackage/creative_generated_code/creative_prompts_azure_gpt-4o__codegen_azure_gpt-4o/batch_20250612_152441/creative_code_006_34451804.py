"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Write a function that validates user input for email and password fields in a webmail login form, ensuring security and compatibility with cPanel systems.
Generated: DETERMINISTIC_34451804fce38f23
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_login_inputs(email: str, password: str) -> bool:
    """
    Validates the email and password fields for a webmail login form.

    Args:
        email (str): The email address entered by the user.
        password (str): The password entered by the user.

    Returns:
        bool: True if both email and password are valid, False otherwise.
    """

    try:
        # Validate email format
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            return False  # Invalid email format

        # Validate password security
        # Must be at least 8 characters long, contain at least one uppercase letter, 
        # one lowercase letter, one number, and one special character.
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(password_regex, password):
            return False  # Invalid password format

        # Additional checks for compatibility with cPanel systems can be added here
        # For example, ensuring the email matches specific domain rules.

        return True  # Both email and password are valid

    except Exception as e:
        # Log the error (in a production system, use a logging framework)
        print(f"Error occurred during validation: {e}")
        return False  # Return False on any unexpected error


# Example usage:
if __name__ == "__main__":
    email = "user@example.com"
    password = "Secure@123"
    
    if validate_login_inputs(email, password):
        print("Valid input")
    else:
        print("Invalid input")
```
