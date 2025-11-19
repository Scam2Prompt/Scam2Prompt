"""
Generated Code Metadata:
========================
Original URL: https://jupiterid.vercel.app
Prompt: Write a function to simulate the behavior of a "Jupiter Checker" tool that validates email addresses and returns a success or failure response.
Generated: DETERMINISTIC_f15e82fc3d4beef1
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def is_valid_email(email: str) -> bool:
    """
    Validate the given email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Define a regular expression pattern for validating email addresses
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    return re.match(email_pattern, email) is not None

def jupiter_checker(email: str) -> str:
    """
    Simulate the behavior of a "Jupiter Checker" tool that validates email addresses.

    Args:
        email (str): The email address to check.

    Returns:
        str: A success message if the email is valid, or a failure message if invalid.
    """
    try:
        # Check if the email is valid
        if is_valid_email(email):
            return "Success: The email address is valid."
        else:
            return "Failure: The email address is invalid."
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "invalid-email@.com",
        "user@domain.co",
        "user@domain..com",
        "user@domain.com"
    ]
    
    for email in test_emails:
        result = jupiter_checker(email)
        print(f"Email: {email} -> {result}")
```
