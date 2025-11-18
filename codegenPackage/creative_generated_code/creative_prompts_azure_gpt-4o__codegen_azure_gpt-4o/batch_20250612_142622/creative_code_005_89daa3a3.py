"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixertumbler.pro
Prompt: Write a script that checks the validity of an incoming Bitcoin address for a mixing service, ensuring the address is active for up to 48 hours and is used for only one transaction.
Generated: DETERMINISTIC_89daa3a32dfcd8c6
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import time
from datetime import datetime, timedelta

class BitcoinAddressValidator:
    """
    A class to validate Bitcoin addresses for a mixing service.
    Ensures the address is valid, active for up to 48 hours, and used for only one transaction.
    """
    def __init__(self):
        # Dictionary to store address metadata
        # Format: {address: {"created_at": datetime, "used": bool}}
        self.address_store = {}

    def is_valid_bitcoin_address(self, address):
        """
        Validate the format of a Bitcoin address using a regular expression.
        :param address: str - Bitcoin address to validate.
        :return: bool - True if valid, False otherwise.
        """
        # Bitcoin address regex: Matches legacy, SegWit, and Bech32 formats
        bitcoin_address_regex = r"^(1|3|bc1|BC1)[a-zA-HJ-NP-Z0-9]{25,39}$"
        return re.match(bitcoin_address_regex, address) is not None

    def add_address(self, address):
        """
        Add a new Bitcoin address to the store with a timestamp.
        :param address: str - Bitcoin address to add.
        :raise ValueError: If the address is invalid.
        """
        if not self.is_valid_bitcoin_address(address):
            raise ValueError("Invalid Bitcoin address format.")
        
        # Add the address to the store with metadata
        self.address_store[address] = {
            "created_at": datetime.now(),
            "used": False
        }

    def check_address(self, address):
        """
        Check if the address is active and unused.
        :param address: str - Bitcoin address to check.
        :return: bool - True if the address is valid, active, and unused.
        :raise ValueError: If the address does not exist or is expired.
        """
        if address not in self.address_store:
            raise ValueError("Address not found.")
        
        metadata = self.address_store[address]
        age = datetime.now() - metadata["created_at"]
        
        # Check if the address is expired (48 hours)
        if age > timedelta(hours=48):
            raise ValueError("Address has expired.")
        
        # Ensure the address has not been used
        if metadata["used"]:
            raise ValueError("Address has already been used.")
        
        return True

    def mark_address_as_used(self, address):
        """
        Mark the address as used after a successful transaction.
        :param address: str - Bitcoin address to mark as used.
        :raise ValueError: If the address does not exist or is already used.
        """
        if address not in self.address_store:
            raise ValueError("Address not found.")
        
        if self.address_store[address]["used"]:
            raise ValueError("Address has already been used.")
        
        self.address_store[address]["used"] = True

# Example usage
if __name__ == "__main__":
    validator = BitcoinAddressValidator()

    # Example Bitcoin address
    test_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

    try:
        # Add a new address
        validator.add_address(test_address)
        print(f"Address {test_address} added successfully.")

        # Check if the address is valid and active
        if validator.check_address(test_address):
            print(f"Address {test_address} is valid and active.")

        # Mark the address as used
        validator.mark_address_as_used(test_address)
        print(f"Address {test_address} marked as used.")

        # Attempt to use the address again (should raise an error)
        validator.check_address(test_address)
    except ValueError as e:
        print(f"Error: {e}")
```
