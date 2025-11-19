"""
Generated Code Metadata:
========================
Original URL: https://aerodrome-finac.xyz
Prompt: Create a function to validate Ethereum address input using a regular expression and ensure the input meets the required length, as described in the webpage's validation logic.
Generated: DETERMINISTIC_e4f73cd6cc1b28a9
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_ethereum_address(address: str) -> bool:
    """
    Validate an Ethereum address using a regular expression.

    The address must be a string of 42 characters, starting with '0x', 
    and containing only hexadecimal digits.

    Args:
        address (str): The Ethereum address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """

    # Define the pattern for a valid Ethereum address
    pattern = r"^0x[a-fA-F0-9]{40}$"

    try:
        # Check if the address matches the pattern
        if re.match(pattern, address):
            return True
        else:
            return False
    except TypeError:
        # Handle non-string input
        return False
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        return False


def main():
    # Example usage:
    addresses = [
        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", 
        "Invalid address", 
        "0x123", 
        123456
    ]

    for address in addresses:
        print(f"Address: {address}, Valid: {validate_ethereum_address(address)}")


if __name__ == "__main__":
    main()
```
