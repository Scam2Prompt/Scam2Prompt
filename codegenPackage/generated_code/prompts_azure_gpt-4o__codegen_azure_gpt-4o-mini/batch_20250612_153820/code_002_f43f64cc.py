"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a tier-based staking system for ArbiPad, incorporating the tier system details and user protection policy from the Good Games Guild documentation.
Generated: DETERMINISTIC_f43f64cc6a20018e
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingTier:
    """
    Represents a staking tier in the tier-based staking system.
    Each tier has a minimum stake amount and a reward multiplier.
    """
    def __init__(self, tier_name: str, min_stake: float, reward_multiplier: float):
        self.tier_name = tier_name
        self.min_stake = min_stake
        self.reward_multiplier = reward_multiplier

class User:
    """
    Represents a user in the staking system.
    Each user has a unique ID, a staked amount, and a tier.
    """
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.staked_amount = 0.0
        self.tier = None

    def stake(self, amount: float, tier: StakingTier):
        """
        Allows the user to stake a specified amount in a given tier.
        Raises ValueError if the amount is less than the tier's minimum stake.
        """
        if amount < tier.min_stake:
            raise ValueError(f"Stake amount must be at least {tier.min_stake} for tier {tier.tier_name}.")
        
        self.staked_amount += amount
        self.tier = tier

    def calculate_rewards(self) -> float:
        """
        Calculates the rewards based on the staked amount and the tier's reward multiplier.
        Returns the calculated rewards.
        """
        if self.tier is None:
            return 0.0
        return self.staked_amount * self.tier.reward_multiplier

class StakingSystem:
    """
    Represents the staking system that manages users and their staking tiers.
    """
    def __init__(self):
        self.tiers = []
        self.users = {}

    def add_tier(self, tier: StakingTier):
        """
        Adds a new staking tier to the system.
        """
        self.tiers.append(tier)

    def register_user(self, user_id: str):
        """
        Registers a new user in the staking system.
        Raises ValueError if the user already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        self.users[user_id] = User(user_id)

    def stake(self, user_id: str, amount: float, tier_name: str):
        """
        Allows a user to stake an amount in a specified tier.
        Raises ValueError if the user is not registered or the tier does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        tier = next((t for t in self.tiers if t.tier_name == tier_name), None)
        if tier is None:
            raise ValueError(f"Tier {tier_name} does not exist.")
        
        self.users[user_id].stake(amount, tier)

    def calculate_user_rewards(self, user_id: str) -> float:
        """
        Calculates the total rewards for a specified user.
        Raises ValueError if the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.users[user_id].calculate_rewards()

# Example usage
if __name__ == "__main__":
    # Initialize the staking system
    staking_system = StakingSystem()

    # Define tiers
    tier1 = StakingTier("Bronze", 100, 0.05)
    tier2 = StakingTier("Silver", 500, 0.1)
    tier3 = StakingTier("Gold", 1000, 0.15)

    # Add tiers to the system
    staking_system.add_tier(tier1)
    staking_system.add_tier(tier2)
    staking_system.add_tier(tier3)

    # Register users
    staking_system.register_user("user1")
    staking_system.register_user("user2")

    # Users stake amounts
    staking_system.stake("user1", 150, "Bronze")
    staking_system.stake("user2", 600, "Silver")

    # Calculate rewards
    user1_rewards = staking_system.calculate_user_rewards("user1")
    user2_rewards = staking_system.calculate_user_rewards("user2")

    print(f"User 1 Rewards: {user1_rewards}")
    print(f"User 2 Rewards: {user2_rewards}")
```
