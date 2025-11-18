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

class ReferralTracker:
    def __init__(self):
        # Dictionary to store referral information in the format:
        # {referrer_wallet: {'referrals': [list_of_wallet_addresses], 'allocated_tokens': int}}
        self.referral_data = {}

    @staticmethod
    def validate_wallet_address(wallet_address):
        """
        Validate wallet address using regex.
        For simplicity, assume Ethereum-style wallet addresses (starting with '0x' and 40 hexadecimal characters).
        """
        pattern = r'^0x[a-fA-F0-9]{40}$'
        if re.match(pattern, wallet_address):
            return True
        return False

    def add_referral(self, referrer_wallet, referred_wallet):
        """
        Add a referral relationship between referrer and referred wallet.
        """
        if not self.validate_wallet_address(referrer_wallet):
            raise ValueError(f"Invalid referrer wallet address: {referrer_wallet}")
        if not self.validate_wallet_address(referred_wallet):
            raise ValueError(f"Invalid referred wallet address: {referred_wallet}")

        if referrer_wallet not in self.referral_data:
            self.referral_data[referrer_wallet] = {'referrals': [], 'allocated_tokens': 0}

        if referred_wallet not in self.referral_data[referrer_wallet]['referrals']:
            self.referral_data[referrer_wallet]['referrals'].append(referred_wallet)
        else:
            raise ValueError(f"Referred wallet {referred_wallet} already exists for referrer {referrer_wallet}")

    def allocate_tokens(self, referrer_wallet, tokens):
        """
        Allocate tokens to a referrer based on their referral activity.
        """
        if not self.validate_wallet_address(referrer_wallet):
            raise ValueError(f"Invalid referrer wallet address: {referrer_wallet}")
        if tokens < 0:
            raise ValueError("Token allocation must be a non-negative value")

        if referrer_wallet in self.referral_data:
            self.referral_data[referrer_wallet]['allocated_tokens'] += tokens
        else:
            raise ValueError(f"Referrer wallet {referrer_wallet} not found in referral data")

    def get_referral_data(self, wallet_address):
        """
        Retrieve referral data for a specific wallet address.
        """
        if not self.validate_wallet_address(wallet_address):
            raise ValueError(f"Invalid wallet address: {wallet_address}")

        return self.referral_data.get(wallet_address, None)

    def display_referral_data(self):
        """
        Print the referral data in a readable format.
        """
        print("Referral Data:")
        for referrer, data in self.referral_data.items():
            print(f"Referrer Wallet: {referrer}")
            print(f"  Referrals: {', '.join(data['referrals']) if data['referrals'] else 'None'}")
            print(f"  Allocated Tokens: {data['allocated_tokens']}")
            print()

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()

    try:
        tracker.add_referral("0x1234567890abcdef1234567890abcdef12345678", "0xabcdef1234567890abcdef1234567890abcdef12")
        tracker.add_referral("0x1234567890abcdef1234567890abcdef12345678", "0x9876543210abcdef9876543210abcdef98765432")
        tracker.allocate_tokens("0x1234567890abcdef1234567890abcdef12345678", 100)

        tracker.display_referral_data()

    except ValueError as e:
        print(f"Error: {e}")
```
