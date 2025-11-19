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
# tier_system.py

from enum import Enum
from typing import Dict, List

class Tier(Enum):
    """ Enum representing the different tiers in the system """
    BASIC = 1
    PREMIUM = 2
    ELITE = 3
    LEGEND = 4

class NFT:
    """ Class representing a non-fungible token """
    def __init__(self, id: int, name: str, rarity: str):
        """
        Initialize an NFT

        Args:
        id (int): Unique identifier for the NFT
        name (str): Name of the NFT
        rarity (str): Rarity of the NFT (e.g., common, uncommon, rare)
        """
        self.id = id
        self.name = name
        self.rarity = rarity

class User:
    """ Class representing a user in the digital community """
    def __init__(self, id: int, nft_holdings: List[NFT], token_holdings: float):
        """
        Initialize a user

        Args:
        id (int): Unique identifier for the user
        nft_holdings (List[NFT]): List of NFTs held by the user
        token_holdings (float): Number of tokens held by the user
        """
        self.id = id
        self.nft_holdings = nft_holdings
        self.token_holdings = token_holdings

class TierSystem:
    """ Class representing the tier system """
    def __init__(self):
        """
        Initialize the tier system
        """
        self.tier_requirements = {
            Tier.BASIC: {"nft_count": 0, "token_holdings": 0},
            Tier.PREMIUM: {"nft_count": 1, "token_holdings": 100},
            Tier.ELITE: {"nft_count": 3, "token_holdings": 500},
            Tier.LEGEND: {"nft_count": 5, "token_holdings": 1000},
        }

    def get_user_tier(self, user: User) -> Tier:
        """
        Determine the tier of a user based on their NFT holdings and token holdings

        Args:
        user (User): The user to determine the tier for

        Returns:
        Tier: The tier of the user
        """
        nft_count = len(user.nft_holdings)
        token_holdings = user.token_holdings

        for tier, requirements in self.tier_requirements.items():
            if nft_count >= requirements["nft_count"] and token_holdings >= requirements["token_holdings"]:
                return tier

        return Tier.BASIC

    def validate_user(self, user: User) -> bool:
        """
        Validate a user's holdings and return True if they meet the requirements for their tier

        Args:
        user (User): The user to validate

        Returns:
        bool: True if the user's holdings are valid, False otherwise
        """
        user_tier = self.get_user_tier(user)
        nft_count = len(user.nft_holdings)
        token_holdings = user.token_holdings

        requirements = self.tier_requirements[user_tier]
        return nft_count >= requirements["nft_count"] and token_holdings >= requirements["token_holdings"]

def main():
    # Example usage
    nft1 = NFT(1, "NFT 1", "common")
    nft2 = NFT(2, "NFT 2", "uncommon")
    nft3 = NFT(3, "NFT 3", "rare")

    user1 = User(1, [nft1, nft2], 500)
    user2 = User(2, [nft1, nft2, nft3], 1500)

    tier_system = TierSystem()

    print(f"User 1 Tier: {tier_system.get_user_tier(user1).name}")
    print(f"User 2 Tier: {tier_system.get_user_tier(user2).name}")

    print(f"User 1 Valid: {tier_system.validate_user(user1)}")
    print(f"User 2 Valid: {tier_system.validate_user(user2)}")

if __name__ == "__main__":
    main()
```
