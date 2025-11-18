"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babysamocoin-nft.web.app
Prompt: Generate a script that validates wallet addresses against the whitelist criteria for Baby SAMO Coin NFT minting and provides feedback to the user.
Generated: DETERMINISTIC_205c856689479827
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class WalletValidator:
    def __init__(self, whitelist):
        """
        Initialize the WalletValidator with a whitelist of valid wallet addresses.

        :param whitelist: A set of valid wallet addresses.
        """
        self.whitelist = set(whitelist)

    def is_valid_wallet(self, wallet_address):
        """
        Validate the wallet address against the criteria.

        :param wallet_address: The wallet address to validate.
        :return: True if valid, False otherwise.
        """
        # Check if the wallet address matches the expected format (example format).
        wallet_pattern = r'^(0x)?[0-9a-fA-F]{40}$'
        return re.match(wallet_pattern, wallet_address) is not None

    def validate_wallet(self, wallet_address):
        """
        Validate the given wallet address against whitelist criteria.

        :param wallet_address: The wallet address to validate.
        :return: Feedback message indicating the validation result.
        """
        try:
            if not self.is_valid_wallet(wallet_address):
                return "Invalid wallet address format."

            if wallet_address in self.whitelist:
                return "Wallet address is valid and whitelisted."
            else:
                return "Wallet address is valid but not on the whitelist."
        except Exception as e:
            return f"An error occurred during validation: {str(e)}"

# Sample whitelist of valid wallet addresses
whitelist_addresses = [
    "0x1234567890abcdef1234567890abcdef12345678",
    "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd",
]

# Instantiate the WalletValidator with the whitelist
validator = WalletValidator(whitelist_addresses)

# Example usage
wallet_to_check = input("Enter the wallet address to validate: ")
result = validator.validate_wallet(wallet_to_check)
print(result)
```
