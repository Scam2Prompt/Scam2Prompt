"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heist-nana.web.app
Prompt: Write a function to verify recipient addresses (e.g., AE17aa..2YC) before initiating payments via Helio's platform on Solana.
Generated: DETERMINISTIC_1cd6bea0ba78f0dc
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from solana.publickey import PublicKey
from solana.rpc.api import Client

# Define a regular expression pattern for Solana addresses
ADDRESS_PATTERN = r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'

def is_valid_solana_address(address: str) -> bool:
    """
    Verify if the provided address is a valid Solana address.
    
    Args:
        address (str): The recipient address to verify.
        
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    if not isinstance(address, str):
        raise ValueError("Address must be a string.")

    # Check if the address matches the Solana address pattern
    address_is_valid = re.match(ADDRESS_PATTERN, address) is not None

    # Further validate using the PublicKey class from solana library
    try:
        PublicKey(address)
    except Exception as e:
        print(f"Validation error: {e}")
        return False

    return address_is_valid

def verify_recipient_address(address: str) -> None:
    """
    Verify the recipient address before initiating a payment.
    
    Args:
        address (str): The recipient address to verify.
        
    Raises:
        ValueError: If the address is invalid.
    """
    if not is_valid_solana_address(address):
        raise ValueError(f"Invalid recipient address: {address}")

    print(f"Recipient address {address} is valid.")

# Example usage
if __name__ == "__main__":
    try:
        recipient_address = "AE17aa...2YC"  # Replace with an actual address
        verify_recipient_address(recipient_address)
    except ValueError as ve:
        print(ve)
```

Make sure to install the `solana` library if you haven't done so already:

```bash
pip install solana
```
