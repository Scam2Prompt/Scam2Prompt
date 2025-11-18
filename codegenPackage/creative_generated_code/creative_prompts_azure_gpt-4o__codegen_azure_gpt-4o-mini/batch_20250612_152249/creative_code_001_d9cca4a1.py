"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Generate code to implement a referral system for MoonBag ($MBAG) tokens, where users can share referral codes to earn 10% extra tokens and track referrals using wallet addresses.
Generated: DETERMINISTIC_d9cca4a1a7997fa2
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # A dictionary to store user wallets and their referral codes
        self.users = {}
        # A dictionary to store referrals made by each user
        self.referrals = defaultdict(list)
        # A dictionary to keep track of user balances
        self.balances = defaultdict(float)

    def create_user(self, wallet_address):
        """
        Create a new user in the system with a unique referral code.
        
        :param wallet_address: The wallet address of the user
        :raises ValueError: If the user already exists
        """
        if wallet_address in self.users:
            raise ValueError("User already exists.")
        
        # Generate a unique referral code based on the wallet address
        referral_code = self.generate_referral_code(wallet_address)
        self.users[wallet_address] = referral_code
        self.balances[wallet_address] = 0  # Initialize balance to 0

    def generate_referral_code(self, wallet_address):
        """
        Generate a unique referral code by hashing the wallet address.
        
        :param wallet_address: The wallet address of the user
        :return: A unique referral code
        """
        return sha256(wallet_address.encode()).hexdigest()[:10]  # Shorten to 10 characters

    def refer_user(self, referrer_wallet, referred_wallet):
        """
        A user refers another user using a referral code.
        
        :param referrer_wallet: The wallet address of the referrer
        :param referred_wallet: The wallet address of the referred user
        :raises ValueError: If the referrer does not exist or if the referred user already exists
        """
        if referrer_wallet not in self.users:
            raise ValueError("Referrer does not exist.")
        
        if referred_wallet in self.users:
            raise ValueError("Referred user already exists.")
        
        # Create the referred user and add them to the referrer's referrals
        self.create_user(referred_wallet)
        self.referrals[referrer_wallet].append(referred_wallet)

        # Reward the referrer with 10% extra tokens
        self.balances[referrer_wallet] += 10  # Assuming a base reward of 100, this is 10%

    def get_balance(self, wallet_address):
        """
        Retrieve the balance of a user.
        
        :param wallet_address: The wallet address of the user
        :return: The balance of the user
        :raises ValueError: If the user does not exist
        """
        if wallet_address not in self.balances:
            raise ValueError("User does not exist.")
        
        return self.balances[wallet_address]

    def get_referrals(self, wallet_address):
        """
        Get the list of referrals made by a user.
        
        :param wallet_address: The wallet address of the user
        :return: A list of referred wallet addresses
        :raises ValueError: If the user does not exist
        """
        if wallet_address not in self.users:
            raise ValueError("User does not exist.")
        
        return self.referrals[wallet_address]


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        # Create users
        referral_system.create_user("0x1234567890abcdef")
        referral_system.create_user("0xfedcba0987654321")
        
        # Refer a user
        referral_system.refer_user("0x1234567890abcdef", "0xabcdef1234567890")
        
        # Fetch balances and referrals
        print(referral_system.get_balance("0x1234567890abcdef"))  # Should output 10
        print(referral_system.get_referrals("0x1234567890abcdef"))  # Should contain the referred address
    except ValueError as e:
        print(f"Error: {e}")
```
