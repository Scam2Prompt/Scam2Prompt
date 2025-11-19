"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-phantomwallet.us
Prompt: What are the unique address formats used by Phantom Wallet for different cryptocurrencies, and why is it important to verify them?
Generated: DETERMINISTIC_af569642a318937b
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class AddressValidator:
    """Class to validate cryptocurrency addresses for Phantom Wallet."""

    def __init__(self):
        # Define unique address formats for different cryptocurrencies
        self.address_formats = {
            "Solana": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",  # Base58, 32-44 chars
            "Ethereum": r"^0x[a-fA-F0-9]{40}$",        # Hexadecimal, 42 chars
            "Bitcoin": r"^(1|3|bc1)[a-zA-Z0-9]{25,39}$", # Base58 or Bech32
        }

    def validate_address(self, crypto_type, address):
        """
        Validate the address based on the cryptocurrency type.
        
        :param crypto_type: The type of cryptocurrency (e.g., 'Solana', 'Ethereum', 'Bitcoin')
        :param address: The address string to validate
        :return: True if valid, False otherwise
        :raises ValueError: If the cryptocurrency type is not recognized
        """
        if crypto_type not in self.address_formats:
            raise ValueError(f"Unsupported cryptocurrency type: {crypto_type}")

        pattern = self.address_formats[crypto_type]
        is_valid = re.match(pattern, address) is not None
        return is_valid

def main():
    """Main function to demonstrate address validation."""
    validator = AddressValidator()
    
    # Test addresses for different cryptocurrencies
    addresses_to_test = {
        "Solana": "4k3Dyjzvzp8e7Qd6h1D2Y2c9yJh1dNdY6PTGGKdhfcXc",
        "Ethereum": "0x32Be343B94f860124dC4fEe278FDCBD38C102D88",
        "Bitcoin": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    }

    for crypto, address in addresses_to_test.items():
        try:
            if validator.validate_address(crypto, address):
                print(f"{address} is a valid {crypto} address.")
            else:
                print(f"{address} is NOT a valid {crypto} address.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
