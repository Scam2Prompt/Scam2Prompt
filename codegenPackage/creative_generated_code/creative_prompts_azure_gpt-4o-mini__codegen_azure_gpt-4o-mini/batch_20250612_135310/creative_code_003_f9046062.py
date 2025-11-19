"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-mixers.to
Prompt: Create a code snippet that validates BTC addresses entered by users in a mixing service to ensure they are correctly formatted before processing.
Generated: DETERMINISTIC_f904606235aa0eaa
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BTCAddressValidator:
    """
    A class to validate Bitcoin (BTC) addresses.

    Attributes
    ----------
    btc_address : str
        The Bitcoin address to be validated.
    """

    BTC_ADDRESS_REGEX = r'^(1|3|bc1)[a-zA-Z0-9]{25,39}$'

    def __init__(self, btc_address: str):
        """
        Initializes the BTCAddressValidator with a BTC address.

        Parameters
        ----------
        btc_address : str
            The BTC address to validate.
        """
        self.btc_address = btc_address

    def is_valid(self) -> bool:
        """
        Validates the BTC address format.

        Returns
        -------
        bool
            True if the address is valid, False otherwise.
        """
        if not isinstance(self.btc_address, str):
            raise ValueError("BTC address must be a string.")
        
        # Use regex to validate the BTC address
        is_match = re.match(self.BTC_ADDRESS_REGEX, self.btc_address)
        return bool(is_match)

def main():
    # Example usage of the BTCAddressValidator
    btc_address = input("Enter the BTC address to validate: ")
    
    try:
        validator = BTCAddressValidator(btc_address)
        if validator.is_valid():
            print("The BTC address is valid.")
        else:
            print("The BTC address is invalid.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
