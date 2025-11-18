"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiosis-dashboard.pages.dev
Prompt: Provide code examples for validating ZetaChain addresses when using multisig contracts, as described in the Symbiosis Bridge documentation.
Generated: DETERMINISTIC_e8040128f54114fd
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# zeta_chain_validator.py

import re
from typing import List, Tuple

class ZetaChainAddressValidator:
    """
    A class to validate ZetaChain addresses specifically for use in multisig contracts.
    """

    # Regular expression to validate ZetaChain addresses
    ADDRESS_PATTERN = r'^(0x)?[0-9a-fA-F]{40}$'

    def __init__(self, addresses: List[str]):
        """
        Initializes the ZetaChainAddressValidator with a list of addresses.

        :param addresses: A list of addresses to validate.
        """
        self.addresses = addresses

    def validate_addresses(self) -> Tuple[List[str], List[str]]:
        """
        Validates all provided addresses and categorizes them into valid and invalid addresses.

        :return: A tuple containing two lists: valid addresses and invalid addresses.
        """
        valid_addresses = []
        invalid_addresses = []

        for address in self.addresses:
            if self.is_valid_address(address):
                valid_addresses.append(address)
            else:
                invalid_addresses.append(address)

        return valid_addresses, invalid_addresses

    @classmethod
    def is_valid_address(cls, address: str) -> bool:
        """
        Checks if a given address is valid according to the ZetaChain address pattern.

        :param address: The address to validate.
        :return: True if valid, False otherwise.
        """
        if not isinstance(address, str):
            raise ValueError("Address must be a string.")

        return bool(re.match(cls.ADDRESS_PATTERN, address))

# Example usage
if __name__ == "__main__":
    # List of addresses to validate
    addresses_to_validate = [
        "0x1234567890abcdef1234567890abcdef12345678",  # Valid address
        "0x1234567890abcdef1234567890abcdef1234567g",  # Invalid address (contains 'g')
        "1234567890abcdef1234567890abcdef12345678",    # Valid address without '0x'
        "0x123",                                          # Invalid address (too short)
    ]

    # Create a validator instance
    validator = ZetaChainAddressValidator(addresses_to_validate)

    try:
        valid, invalid = validator.validate_addresses()
        print("Valid Addresses:", valid)
        print("Invalid Addresses:", invalid)
    except ValueError as e:
        print(f"Error: {e}")
```
