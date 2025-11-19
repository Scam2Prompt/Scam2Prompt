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
# Import necessary libraries
from typing import List, Dict, Optional

class StakingTier:
    """
    Represents a staking tier with its associated rewards and requirements.
    """
    def __init__(self, name: str, min_stake: float, reward_multiplier: float):
        self.name = name
        self.min_stake = min_stake
        self.reward_multiplier = reward_multiplier

class NFTBoost:
    """
    Represents an NFT boost that can enhance staking rewards.
    """
    def __init__(self, name: str, boost_multiplier: float):
        self.name = name
        self.boost_multiplier = boost_multiplier

class User:
    """
    Represents a user in the staking system.
    """
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.staked_amount = 0.0
        self.current_tier: Optional[StakingTier] = None
        self.nft_boosts: List[NFTBoost] = []

    def stake(self, amount: float, tier: StakingTier):
        """
        Stake a specified amount of tokens and assign a tier.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if amount < tier.min_stake:
            raise ValueError(f"Stake amount must be at least {tier.min_stake} for tier {tier.name}.")
        
        self.staked_amount += amount
        self.current_tier = tier

    def add_nft_boost(self, nft_boost: NFTBoost):
        """
        Add an NFT boost to the user's account.
        """
        self.nft_boosts.append(nft_boost)

    def calculate_rewards(self) -> float:
        """
        Calculate the total rewards based on the staked amount, current tier, and NFT boosts.
        """
        if self.current_tier is None:
            return 0.0
        
        base_reward = self.staked_amount * self.current_tier.reward_multiplier
        total_boost = 1.0
        
        for boost in self.nft_boosts:
            total_boost *= boost.boost_multiplier
        
        return base_reward * total_boost

class StakingSystem:
    """
    Represents the staking system that manages users and tiers.
    """
    def __init__(self):
        self.tiers: List[StakingTier] = []
        self.users: Dict[str, User] = {}

    def add_tier(self, tier: StakingTier):
        """
        Add a new staking tier to the system.
        """
        self.tiers.append(tier)

    def register_user(self, user_id: str) -> User:
        """
        Register a new user in the staking system.
        """
        if user_id in self.users:
            raise ValueError("User already registered.")
        
        user = User(user_id)
        self.users[user_id] = user
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by their ID.
        """
        return self.users.get(user_id)

# Example usage
if __name__ == "__main__":
    # Initialize the staking system
    staking_system = StakingSystem()

    # Define staking tiers
    tier1 = StakingTier("Bronze", 100, 0.05)
    tier2 = StakingTier("Silver", 500, 0.1)
    tier3 = StakingTier("Gold", 1000, 0.15)

    # Add tiers to the system
    staking_system.add_tier(tier1)
    staking_system.add_tier(tier2)
    staking_system.add_tier(tier3)

    # Register a user
    user = staking_system.register_user("user123")

    # User stakes tokens
    user.stake(600, tier2)

    # User adds an NFT boost
    nft_boost = NFTBoost("Rare NFT", 1.2)
    user.add_nft_boost(nft_boost)

    # Calculate rewards
    rewards = user.calculate_rewards()
    print(f"User {user.user_id} has earned rewards: {rewards:.2f} AITECH tokens")
```
