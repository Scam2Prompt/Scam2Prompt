"""
Generated Code Metadata:
========================
Original URL: https://nextearths-ap.web.app
Prompt: Design a tier system for a digital community like Next Earth, incorporating NFT ownership and token holdings as key factors.
Generated: DETERMINISTIC_2606316102dfc57f
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from typing import List, Dict

class Tier(Enum):
    """Enumeration for user tiers based on NFT ownership and token holdings."""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class User:
    """Class representing a user in the digital community."""
    
    def __init__(self, username: str, nft_count: int, token_balance: float):
        """
        Initialize a new user with a username, NFT count, and token balance.
        
        :param username: The username of the user.
        :param nft_count: The number of NFTs owned by the user.
        :param token_balance: The amount of tokens held by the user.
        """
        self.username = username
        self.nft_count = nft_count
        self.token_balance = token_balance
        self.tier = self.calculate_tier()

    def calculate_tier(self) -> Tier:
        """
        Calculate the user's tier based on NFT ownership and token balance.
        
        :return: The user's tier.
        """
        if self.nft_count >= 10 and self.token_balance >= 1000:
            return Tier.PLATINUM
        elif self.nft_count >= 5 and self.token_balance >= 500:
            return Tier.GOLD
        elif self.nft_count >= 1 and self.token_balance >= 100:
            return Tier.SILVER
        else:
            return Tier.BRONZE

    def update_nft_count(self, new_count: int):
        """
        Update the user's NFT count and recalculate the tier.
        
        :param new_count: The new NFT count.
        """
        if new_count < 0:
            raise ValueError("NFT count cannot be negative.")
        self.nft_count = new_count
        self.tier = self.calculate_tier()

    def update_token_balance(self, new_balance: float):
        """
        Update the user's token balance and recalculate the tier.
        
        :param new_balance: The new token balance.
        """
        if new_balance < 0:
            raise ValueError("Token balance cannot be negative.")
        self.token_balance = new_balance
        self.tier = self.calculate_tier()

class Community:
    """Class representing the digital community."""
    
    def __init__(self):
        """Initialize an empty community."""
        self.users: Dict[str, User] = {}

    def add_user(self, username: str, nft_count: int, token_balance: float):
        """
        Add a new user to the community.
        
        :param username: The username of the new user.
        :param nft_count: The number of NFTs owned by the new user.
        :param token_balance: The amount of tokens held by the new user.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, nft_count, token_balance)

    def get_user_tier(self, username: str) -> Tier:
        """
        Get the tier of a user by username.
        
        :param username: The username of the user.
        :return: The user's tier.
        """
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        return user.tier

# Example usage
if __name__ == "__main__":
    community = Community()
    
    # Adding users to the community
    community.add_user("Alice", 10, 1500)
    community.add_user("Bob", 3, 300)

    # Retrieving user tiers
    print(f"Alice's tier: {community.get_user_tier('Alice')}")
    print(f"Bob's tier: {community.get_user_tier('Bob')}")
    
    # Updating user data
    community.users["Bob"].update_nft_count(5)
    community.users["Bob"].update_token_balance(600)
    
    print(f"Bob's new tier: {community.get_user_tier('Bob')}")
```
