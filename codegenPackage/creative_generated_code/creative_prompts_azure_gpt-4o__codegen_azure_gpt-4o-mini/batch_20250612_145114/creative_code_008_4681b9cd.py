"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Write a function to validate a Habbo username before initiating any NFT-related operations, ensuring it meets the requirements specified on the webpage.
Generated: DETERMINISTIC_4681b9cdd23e5fde
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UsernameValidationError(Exception):
    """Custom exception for username validation errors."""
    pass

def validate_habbo_username(username: str) -> bool:
    """
    Validates a Habbo username based on specific criteria.
    
    The username must:
    - Be between 3 and 16 characters long.
    - Contain only alphanumeric characters (letters and digits).
    - Not start with a number.
    
    Args:
        username (str): The username to validate.
    
    Raises:
        UsernameValidationError: If the username does not meet the criteria.
    
    Returns:
        bool: True if the username is valid, False otherwise.
    """
    # Check for length
    if not (3 <= len(username) <= 16):
        raise UsernameValidationError("Username must be between 3 and 16 characters long.")
    
    # Check for alphanumeric characters and starting character
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', username):
        raise UsernameValidationError("Username can only contain letters and numbers, and must start with a letter.")
    
    # If all checks pass, the username is valid
    return True

# Example usage:
try:
    username = "Habbo123"
    if validate_habbo_username(username):
        print(f"'{username}' is a valid Habbo username.")
except UsernameValidationError as e:
    print(f"Invalid username: {e}")
```
