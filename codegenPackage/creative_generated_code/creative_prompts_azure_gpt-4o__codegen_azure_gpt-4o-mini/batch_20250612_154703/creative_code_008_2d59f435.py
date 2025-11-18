"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Write a function to validate hosting package activation using a unique activation key.
Generated: DETERMINISTIC_2d59f435fb3db832
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ActivationKeyError(Exception):
    """Custom exception for activation key validation errors."""
    pass

def validate_activation_key(activation_key: str) -> bool:
    """
    Validates the given activation key.

    Args:
        activation_key (str): The activation key to validate.

    Returns:
        bool: True if the activation key is valid, False otherwise.

    Raises:
        ActivationKeyError: If the activation key format is invalid.
    """
    
    # Define the regex pattern for a valid activation key
    pattern = r'^[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}$'
    
    # Check if the activation key matches the expected format
    if not isinstance(activation_key, str):
        raise ActivationKeyError("Activation key must be a string.")
    
    if not re.match(pattern, activation_key):
        raise ActivationKeyError("Invalid activation key format. Expected format: XXXXX-XXXXX-XXXXX")
    
    # If the key is valid, return True
    return True

# Example usage:
if __name__ == "__main__":
    try:
        key = "ABCDE-FGHIJ-KLMNO"  # Sample activation key
        if validate_activation_key(key):
            print("Activation key is valid.")
    except ActivationKeyError as e:
        print(f"Error: {e}")
```
