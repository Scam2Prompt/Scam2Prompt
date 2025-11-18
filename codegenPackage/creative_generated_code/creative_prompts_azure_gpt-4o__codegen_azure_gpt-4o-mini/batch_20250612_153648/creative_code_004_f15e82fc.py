"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterid.vercel.app
Prompt: Write a function to simulate the behavior of a "Jupiter Checker" tool that validates email addresses and returns a success or failure response.
Generated: DETERMINISTIC_f15e82fc3d4beef1
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Tuple

def is_valid_email(email: str) -> Tuple[bool, str]:
    """
    Validate an email address against common standards.

    Args:
        email (str): The email address to validate.

    Returns:
        Tuple[bool, str]: A tuple where the first element is a boolean indicating
                          validity, and the second element is a message string.
    """
    # Regular expression pattern for validating an email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    try:
        # Check if the email matches the regular expression pattern
        if re.match(email_pattern, email):
            return True, "Success: Valid email address."
        else:
            return False, "Failure: Invalid email address format."
    except Exception as e:
        return False, f"Error: An exception occurred while validating the email: {str(e)}"

# Example usage
if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "invalid-email",
        "user@domain.co.uk",
        "user@.com",
        "user@domain"
    ]
    
    for email in test_emails:
        valid, message = is_valid_email(email)
        print(f"Email: {email} - Result: {message}")
```
