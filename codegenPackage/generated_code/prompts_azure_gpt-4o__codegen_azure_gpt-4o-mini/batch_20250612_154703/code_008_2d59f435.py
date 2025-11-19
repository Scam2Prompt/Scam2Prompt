"""
Generated Code Metadata:
========================
Original URL: https://zerion.be
Prompt: Write a function to validate hosting package activation using a unique activation key.
Generated: DETERMINISTIC_2d59f435fb3db832
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ActivationKeyError(Exception):
    """Custom exception for invalid activation keys."""
    pass

def validate_activation_key(activation_key: str) -> bool:
    """
    Validates the provided activation key.

    An activation key is considered valid if it meets the following criteria:
    - It is exactly 16 characters long.
    - It contains only alphanumeric characters (letters and digits).
    - It contains at least one uppercase letter, one lowercase letter, and one digit.

    Args:
        activation_key (str): The activation key to validate.

    Returns:
        bool: True if the activation key is valid, False otherwise.

    Raises:
        ActivationKeyError: If the activation key does not meet the validation criteria.
    """
    # Check if the activation key is exactly 16 characters long
    if len(activation_key) != 16:
        raise ActivationKeyError("Activation key must be exactly 16 characters long.")

    # Check if the activation key contains only alphanumeric characters
    if not re.match("^[a-zA-Z0-9]*$", activation_key):
        raise ActivationKeyError("Activation key must contain only alphanumeric characters.")

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    if (not re.search("[a-z]", activation_key) or
        not re.search("[A-Z]", activation_key) or
        not re.search("[0-9]", activation_key)):
        raise ActivationKeyError("Activation key must contain at least one uppercase letter, one lowercase letter, and one digit.")

    return True

# Example usage
if __name__ == "__main__":
    try:
        key = "Abc12345Def67890"  # Example activation key
        if validate_activation_key(key):
            print("Activation key is valid.")
    except ActivationKeyError as e:
        print(f"Invalid activation key: {e}")
```
