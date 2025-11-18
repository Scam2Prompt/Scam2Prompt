"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lens-airdrop.pages.dev
Prompt: Create a function that validates a user-selected handle for Lens Protocol, ensuring it meets specific criteria before submission.
Generated: DETERMINISTIC_8cffacce8c9f6c91
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class HandleValidationError(Exception):
    """Custom exception for handle validation errors."""
    pass

def validate_handle(handle: str) -> bool:
    """
    Validates a user-selected handle for the Lens Protocol.

    A valid handle must meet the following criteria:
    - Length between 3 and 15 characters
    - Only contains alphanumeric characters and underscores
    - Cannot start with a number

    Args:
        handle (str): The user-selected handle to validate.

    Returns:
        bool: True if the handle is valid, False otherwise.

    Raises:
        HandleValidationError: If the handle is invalid, raises an error with a descriptive message.
    """
    # Check if handle length is within the specified range
    if len(handle) < 3 or len(handle) > 15:
        raise HandleValidationError("Handle must be between 3 and 15 characters long.")
    
    # Check if handle starts with a letter
    if not handle[0].isalpha():
        raise HandleValidationError("Handle must start with a letter.")
    
    # Check if handle contains only valid characters (alphanumeric and underscores)
    if not re.match("^[A-Za-z0-9_]+$", handle):
        raise HandleValidationError("Handle can only contain alphanumeric characters and underscores.")
    
    return True

# Example usage
if __name__ == "__main__":
    user_handle = input("Enter your handle for Lens Protocol: ")
    try:
        if validate_handle(user_handle):
            print("Handle is valid!")
    except HandleValidationError as e:
        print(f"Error: {e}")
```
