"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Design a staking system with multiple tiers, including NFT boosts and tier boosts, to incentivize users to stake more AITECH tokens.
Generated: DETERMINISTIC_6ff88ad6eeed42c8
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_system.py

from enum import Enum
from typing import Dict, List

class Tier(Enum):
    """Staking tier enumeration"""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4

class NFT:
    """NFT class"""
    def __init__(self, id: int, boost: float):
        """
        Initialize an NFT

        Args:
        id (int): Unique NFT identifier
        boost (float): NFT boost value
        """
        self.id = id
        self.boost = boost

class StakingSystem:
    """Staking system class"""
    def __init__(self):
        """
        Initialize the staking system
        """
        self.tiers: Dict[Tier, int] = {
            Tier.BRONZE: 100,
            Tier.SILVER: 500,
            Tier.GOLD: 1000,
            Tier.PLATINUM: 5000
        }
        self.nfts: Dict[int, NFT] = {}
        self.user_stakes: Dict[int, Dict[str, float]] = {}

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the system

        Args:
        nft (NFT): NFT to add
        """
        self.nfts[nft.id] = nft

    def stake(self, user_id: int, amount: float, nft_ids: List[int] = None):
        """
        Stake AITECH tokens

        Args:
        user_id (int): User ID
        amount (float): Amount to stake
        nft_ids (List[int], optional): List of NFT IDs. Defaults to None.

        Raises:
        ValueError: If the stake amount is less than the tier requirement
        """
        if user_id not in self.user_stakes:
            self.user_stakes[user_id] = {"stake": 0, "boost": 1.0}

        # Calculate the total boost
        boost = 1.0
        if nft_ids:
            for nft_id in nft_ids:
                if nft_id in self.nfts:
                    boost += self.nfts[nft_id].boost
                else:
                    raise ValueError("Invalid NFT ID")

        # Determine the tier
        tier = self.determine_tier(amount)
        tier_boost = self.calculate_tier_boost(tier)

        # Update the user's stake and boost
        self.user_stakes[user_id]["stake"] += amount
        self.user_stakes[user_id]["boost"] = boost * tier_boost

    def unstake(self, user_id: int, amount: float):
        """
        Unstake AITECH tokens

        Args:
        user_id (int): User ID
        amount (float): Amount to unstake

        Raises:
        ValueError: If the unstake amount exceeds the user's stake
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has no stake")

        if self.user_stakes[user_id]["stake"] < amount:
            raise ValueError("Unstake amount exceeds user's stake")

        self.user_stakes[user_id]["stake"] -= amount

    def determine_tier(self, amount: float) -> Tier:
        """
        Determine the staking tier based on the amount

        Args:
        amount (float): Staked amount

        Returns:
        Tier: The determined tier
        """
        if amount < self.tiers[Tier.BRONZE]:
            return Tier.BRONZE
        elif amount < self.tiers[Tier.SILVER]:
            return Tier.SILVER
        elif amount < self.tiers[Tier.GOLD]:
            return Tier.GOLD
        else:
            return Tier.PLATINUM

    def calculate_tier_boost(self, tier: Tier) -> float:
        """
        Calculate the tier boost

        Args:
        tier (Tier): The tier

        Returns:
        float: The tier boost
        """
        tier_boosts: Dict[Tier, float] = {
            Tier.BRONZE: 1.0,
            Tier.SILVER: 1.2,
            Tier.GOLD: 1.5,
            Tier.PLATINUM: 2.0
        }
        return tier_boosts[tier]

def main():
    staking_system = StakingSystem()

    nft1 = NFT(1, 0.1)
    nft2 = NFT(2, 0.2)
    staking_system.add_nft(nft1)
    staking_system.add_nft(nft2)

    staking_system.stake(1, 1000, [1, 2])
    print(staking_system.user_stakes)

    staking_system.unstake(1, 500)
    print(staking_system.user_stakes)

if __name__ == "__main__":
    main()
```
