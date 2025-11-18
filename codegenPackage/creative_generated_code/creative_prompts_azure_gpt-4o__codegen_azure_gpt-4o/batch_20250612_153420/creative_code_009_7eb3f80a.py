"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad-allybuildapp.pages.dev
Prompt: Generate code for linking a user's social media accounts (Twitter and Discord) and cryptocurrency wallets in a blockchain-based alliance platform.
Generated: DETERMINISTIC_7eb3f80af7f4431e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserProfile:
    """
    A class to represent a user's profile for linking social media accounts and cryptocurrency wallets.
    """
    def __init__(self, username):
        """
        Initialize a new user profile.
        :param username: Unique identifier for the user
        """
        self.username = username
        self.twitter_handle = None
        self.discord_id = None
        self.crypto_wallets = []

    def link_twitter(self, twitter_handle):
        """
        Link a Twitter account to the user profile.
        :param twitter_handle: The user's Twitter handle (e.g., @example)
        """
        if not re.match(r"^@[A-Za-z0-9_]{1,15}$", twitter_handle):
            raise ValueError("Invalid Twitter handle format. Must start with @ and be 1-15 characters long.")
        self.twitter_handle = twitter_handle

    def link_discord(self, discord_id):
        """
        Link a Discord account to the user profile.
        :param discord_id: The user's Discord ID (e.g., username#1234)
        """
        if not re.match(r"^[A-Za-z0-9_]{2,32}#[0-9]{4}$", discord_id):
            raise ValueError("Invalid Discord ID format. Must be in the format username#1234.")
        self.discord_id = discord_id

    def link_crypto_wallet(self, wallet_address):
        """
        Link a cryptocurrency wallet to the user profile.
        :param wallet_address: The user's cryptocurrency wallet address
        """
        if not re.match(r"^(0x)?[A-Fa-f0-9]{40}$", wallet_address):  # Example validation for Ethereum addresses
            raise ValueError("Invalid wallet address. Must be a 40-character hexadecimal string.")
        if wallet_address in self.crypto_wallets:
            raise ValueError("Wallet address already linked.")
        self.crypto_wallets.append(wallet_address)

    def get_profile_summary(self):
        """
        Get a summary of the user's linked accounts and wallets.
        :return: Dictionary containing profile information
        """
        return {
            "username": self.username,
            "twitter_handle": self.twitter_handle,
            "discord_id": self.discord_id,
            "crypto_wallets": self.crypto_wallets,
        }


# Example usage
try:
    user = UserProfile("alliance_user")
    user.link_twitter("@CryptoAlliance")
    user.link_discord("AllianceBot#1234")
    user.link_crypto_wallet("0x1234567890abcdef1234567890abcdef12345678")
    user.link_crypto_wallet("0xabcdef1234567890abcdef1234567890abcdef12")

    print("User Profile Linked Data:")
    print(user.get_profile_summary())
except ValueError as e:
    print(f"Error: {e}")
```
