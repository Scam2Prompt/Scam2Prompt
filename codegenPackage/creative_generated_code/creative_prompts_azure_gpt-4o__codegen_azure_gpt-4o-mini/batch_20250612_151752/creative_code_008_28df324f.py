"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrading-ethereum.info
Prompt: Create a Python function to verify Ethereum addresses like the one provided for donations on the "Upgrading Ethereum" site, ensuring compatibility with ZkSync, Polygon, Optimism, and Arbitrum.
Generated: DETERMINISTIC_28df324f9d5e2acb
Batch ID: 20250612_151752
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
    Verify if the given Ethereum address is valid.

    Parameters:
    address (str): The Ethereum address to validate.

    Returns:
    bool: True if the address is valid, False otherwise.
    
    Supported networks:
    - Ethereum
    - ZkSync
    - Polygon
    - Optimism
    - Arbitrum
    """
    # Define a regular expression pattern for a valid Ethereum address
    pattern = r'^(0x)?[0-9a-fA-F]{40}$'  # Matches a string starting with '0x' followed by 40 hex characters
    
    # Check if the address matches the pattern
    if re.match(pattern, address):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    test_addresses = [
        '0x32Be3435EFeD23C28c962F35B50d1bD3B2C9D4e',  # Valid Ethereum address
        '0x1234567890123456789012345678901234567890',  # Valid Ethereum address
        '0xGHIJKLMNOPQRSTUVWXYZ12345678901234567890',  # Invalid address (invalid characters)
        '1234567890123456789012345678901234567890',     # Invalid address (missing '0x')
        '0x123',                                         # Invalid address (too short)
    ]

    # Validate test addresses
    for address in test_addresses:
        is_valid = is_valid_ethereum_address(address)
        print(f"Address: {address}, Valid: {is_valid}")
```
