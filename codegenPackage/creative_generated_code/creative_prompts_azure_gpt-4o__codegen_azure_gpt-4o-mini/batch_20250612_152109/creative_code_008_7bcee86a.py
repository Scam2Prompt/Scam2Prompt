"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-aevo2.pages.dev
Prompt: Create a script to automate the referral tracking process for Aevo, incorporating wallet address validation and token allocation checks.
Generated: DETERMINISTIC_7bcee86a74616f04
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from decimal import Decimal, InvalidOperation

class ReferralTracker:
    def __init__(self):
        # Initialize a dictionary to keep track of referrals and their associated token allocations
        self.referrals = {}

    def validate_wallet_address(self, address):
        """
        Validate a cryptocurrency wallet address.
        
        :param address: Wallet address as a string
        :return: True if valid, False otherwise
        """
        # Example regex pattern for Ethereum wallet addresses (0x followed by 40 hex characters)
        pattern = r'^0x[a-fA-F0-9]{40}$'
        is_valid = re.match(pattern, address) is not None
        return is_valid

    def allocate_tokens(self, wallet_address, tokens):
        """
        Allocate tokens to a referral if the wallet address is valid and tokens are greater than zero.
        
        :param wallet_address: Wallet address to allocate tokens to
        :param tokens: Number of tokens to allocate
        :return: None
        """
        if not self.validate_wallet_address(wallet_address):
            raise ValueError("Invalid wallet address.")
        
        if tokens <= 0:
            raise ValueError("Token allocation must be greater than zero.")

        # Update the referrals dictionary
        if wallet_address in self.referrals:
            self.referrals[wallet_address] += tokens
        else:
            self.referrals[wallet_address] = tokens

    def get_referral_tokens(self, wallet_address):
        """
        Retrieve the total number of allocated tokens for a specific wallet address.
        
        :param wallet_address: Wallet address to query
        :return: Total tokens allocated for the wallet address
        """
        return self.referrals.get(wallet_address, 0)

    def display_referrals(self):
        """
        Display all referrals and their allocated tokens in a formatted manner.
        
        :return: None
        """
        print("Referral Allocations:")
        for wallet, tokens in self.referrals.items():
            print(f"Wallet Address: {wallet}, Allocated Tokens: {tokens}")

# Example usage
if __name__ == "__main__":
    referral_tracker = ReferralTracker()

    # Test wallet addresses and token allocations
    test_wallets = [
        "0x1234567890abcdef1234567890abcdef12345678",
        "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd",
        "0xnotavalidaddress",
    ]

    try:
        referral_tracker.allocate_tokens(test_wallets[0], 100)
        referral_tracker.allocate_tokens(test_wallets[1], 150)

        # Attempt to allocate tokens to an invalid address
        referral_tracker.allocate_tokens(test_wallets[2], 50)
    except ValueError as e:
        print(f"Error: {e}")

    # Display the allocated referrals
    referral_tracker.display_referrals()
```
