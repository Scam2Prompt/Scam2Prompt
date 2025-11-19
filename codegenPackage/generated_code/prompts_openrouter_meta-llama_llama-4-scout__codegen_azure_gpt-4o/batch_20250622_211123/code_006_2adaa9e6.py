"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Implement a MetaKey staking system, including features for highTable tier systems and secret deal programs, using a programming language of your choice.
Generated: DETERMINISTIC_2adaa9e6385e54d9
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
MetaKey Staking System Implementation
Features:
1. HighTable Tier System
2. Secret Deal Programs

Language: Python
"""

import time
from typing import Dict, List

class MetaKeyStakingSystem:
    """
    A class to represent the MetaKey staking system.
    """

    def __init__(self):
        # Dictionary to store user staking information
        self.stakers: Dict[str, Dict] = {}
        # HighTable tier thresholds (in tokens staked)
        self.high_table_tiers = {
            "Bronze": 100,
            "Silver": 500,
            "Gold": 1000,
            "Platinum": 5000
        }
        # Secret deal programs (only accessible to certain tiers)
        self.secret_deals: Dict[str, str] = {
            "Gold": "Access to exclusive NFT drops.",
            "Platinum": "Private investment opportunities."
        }

    def stake_tokens(self, user_id: str, amount: int):
        """
        Allows a user to stake tokens.
        :param user_id: Unique identifier for the user.
        :param amount: Number of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if user_id not in self.stakers:
            self.stakers[user_id] = {
                "staked_tokens": 0,
                "stake_time": time.time()
            }

        self.stakers[user_id]["staked_tokens"] += amount
        self.stakers[user_id]["stake_time"] = time.time()

        print(f"User {user_id} staked {amount} tokens. Total: {self.stakers[user_id]['staked_tokens']} tokens.")

    def unstake_tokens(self, user_id: str, amount: int):
        """
        Allows a user to unstake tokens.
        :param user_id: Unique identifier for the user.
        :param amount: Number of tokens to unstake.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        if amount <= 0 or amount > self.stakers[user_id]["staked_tokens"]:
            raise ValueError("Invalid unstake amount.")

        self.stakers[user_id]["staked_tokens"] -= amount

        print(f"User {user_id} unstaked {amount} tokens. Remaining: {self.stakers[user_id]['staked_tokens']} tokens.")

        # Remove user from stakers if no tokens are left
        if self.stakers[user_id]["staked_tokens"] == 0:
            del self.stakers[user_id]

    def get_user_tier(self, user_id: str) -> str:
        """
        Determines the HighTable tier of a user based on staked tokens.
        :param user_id: Unique identifier for the user.
        :return: Tier name as a string.
        """
        if user_id not in self.stakers:
            return "No Tier"

        staked_tokens = self.stakers[user_id]["staked_tokens"]

        for tier, threshold in sorted(self.high_table_tiers.items(), key=lambda x: x[1], reverse=True):
            if staked_tokens >= threshold:
                return tier

        return "No Tier"

    def get_secret_deals(self, user_id: str) -> List[str]:
        """
        Provides secret deals available to the user based on their tier.
        :param user_id: Unique identifier for the user.
        :return: List of secret deals.
        """
        user_tier = self.get_user_tier(user_id)

        if user_tier in self.secret_deals:
            return [self.secret_deals[user_tier]]

        return []

    def get_staking_info(self, user_id: str) -> Dict:
        """
        Retrieves staking information for a user.
        :param user_id: Unique identifier for the user.
        :return: Dictionary containing staking details.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        return self.stakers[user_id]


# Example usage
if __name__ == "__main__":
    staking_system = MetaKeyStakingSystem()

    try:
        # Stake tokens
        staking_system.stake_tokens("user1", 1200)
        staking_system.stake_tokens("user2", 300)

        # Get user tier
        print("User1 Tier:", staking_system.get_user_tier("user1"))
        print("User2 Tier:", staking_system.get_user_tier("user2"))

        # Get secret deals
        print("User1 Secret Deals:", staking_system.get_secret_deals("user1"))
        print("User2 Secret Deals:", staking_system.get_secret_deals("user2"))

        # Unstake tokens
        staking_system.unstake_tokens("user1", 200)
        print("User1 Tier after unstaking:", staking_system.get_user_tier("user1"))

        # Get staking info
        print("User1 Staking Info:", staking_system.get_staking_info("user1"))

    except Exception as e:
        print("Error:", e)
```
