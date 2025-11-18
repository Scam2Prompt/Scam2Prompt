"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Create a function to validate Ethereum address input using a regular expression and ensure the input meets the required length, as described in the webpage's validation logic.
Generated: DETERMINISTIC_e4f73cd6cc1b28a9
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_valid_ethereum_address(address: str) -> bool:
    """
    Validate an Ethereum address.

    An Ethereum address is a 42-character hexadecimal string that starts with '0x'.
    The address must have a length of 42 characters and consist only of hexadecimal digits.

    Args:
        address (str): The Ethereum address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.

    Raises:
        ValueError: If the address is not a string or is None.
    """

    # Check if the input is a string
    if not isinstance(address, str):
        raise ValueError("Input must be a string.")

    # Define the regular expression pattern for a valid Ethereum address
    pattern = r"^0x[a-fA-F0-9]{40}$"

    # Check the length of the address and validate using regex
    if len(address) == 42 and re.match(pattern, address):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_address = "0x32Be343B9427c958c8e5b59729B0B0D2D8C4c2F"
    try:
        if is_valid_ethereum_address(test_address):
            print(f"{test_address} is a valid Ethereum address.")
        else:
            print(f"{test_address} is not a valid Ethereum address.")
    except ValueError as ve:
        print(f"Error: {ve}")
```
