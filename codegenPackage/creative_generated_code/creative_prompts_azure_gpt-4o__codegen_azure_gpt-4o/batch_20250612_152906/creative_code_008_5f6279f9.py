"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtflashersoftwares.com
Prompt: Create a Python function that calculates the maximum daily USDT flash capacity based on the license type (Basic or Premium) of the Flash USDT software.
Generated: DETERMINISTIC_5f6279f94241537f
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

# Define constants for USDT flash capacity limits
BASIC_LICENSE_CAPACITY = 1000  # Maximum daily USDT capacity for Basic license
PREMIUM_LICENSE_CAPACITY = 10000  # Maximum daily USDT capacity for Premium license

def calculate_flash_capacity(license_type: str) -> Union[int, str]:
    """
    Calculate the maximum daily USDT flash capacity based on the license type.

    Args:
        license_type (str): The type of license. Accepted values are "Basic" or "Premium".

    Returns:
        Union[int, str]: Maximum USDT flash capacity if license type is valid, 
                         or an error message if license type is invalid.
    """
    try:
        # Convert license_type to lowercase for case-insensitive comparison
        license_type = license_type.strip().lower()
        
        # Match license type and return corresponding capacity
        if license_type == "basic":
            return BASIC_LICENSE_CAPACITY
        elif license_type == "premium":
            return PREMIUM_LICENSE_CAPACITY
        else:
            # Return error message for unsupported license type
            return "Error: Invalid license type. Please use 'Basic' or 'Premium'."
    except Exception as e:
        # Catch any unexpected exceptions and return an error message
        return f"Error: An unexpected error occurred. Details: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test the function with valid and invalid license types
    print(calculate_flash_capacity("Basic"))   # Expected output: 1000
    print(calculate_flash_capacity("Premium")) # Expected output: 10000
    print(calculate_flash_capacity("Unknown")) # Expected output: Error message
```
