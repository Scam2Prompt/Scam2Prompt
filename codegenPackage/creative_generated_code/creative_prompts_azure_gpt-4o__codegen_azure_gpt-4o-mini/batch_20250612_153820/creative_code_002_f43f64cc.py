"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a tier-based staking system for ArbiPad, incorporating the tier system details and user protection policy from the Good Games Guild documentation.
Generated: DETERMINISTIC_f43f64cc6a20018e
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    """
    Represents a tier in the staking system.
    Each tier has a minimum stake, a reward percentage, and a name.
    """
    
    def __init__(self, name: str, min_stake: float, reward_percentage: float):
        self.name = name
        self.min_stake = min_stake
        self.reward_percentage = reward_percentage

class User:
    """
    Represents a user in the staking system.
    Each user has a balance and a tier based on their stake.
    """
    
    def __init__(self, address: str):
        self.address = address
        self.stake_amount = 0.0
        self.tier = None

    def stake(self, amount: float):
        """
        Allows a user to stake a specified amount.
        :param amount: The amount to stake
        :raises ValueError: If the staking amount is invalid
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        self.stake_amount += amount
        print(f"User {self.address} has staked {amount}. Total stake: {self.stake_amount}")

    def calculate_rewards(self) -> float:
        """
        Calculates the rewards for the user based on their current tier.
        :return: The calculated rewards
        :raises ValueError: If the user has not yet staked
        """
        if self.tier is None:
            raise ValueError("User is not in a staking tier.")
        return self.stake_amount * (self.tier.reward_percentage / 100)

class StakingSystem:
    """
    A tier-based staking system that allows users to stake and earn rewards.
    """
    
    def __init__(self):
        self.tiers = []
        self.users = {}

    def add_tier(self, name: str, min_stake: float, reward_percentage: float):
        """
        Adds a new tier to the staking system.
        :param name: The name of the tier
        :param min_stake: The minimum stake required for the tier
        :param reward_percentage: The reward percentage for the tier
        """
        tier = StakingTier(name, min_stake, reward_percentage)
        self.tiers.append(tier)
        print(f"Tier added: {name}")

    def get_user_tier(self, user: User):
        """
        Determines the user's tier based on their stake amount.
        :param user: The user to evaluate
        :raises ValueError: If no tiers are available in the system
        """
        if not self.tiers:
            raise ValueError("No tiers available in the staking system.")
        
        for tier in sorted(self.tiers, key=lambda t: t.min_stake):
            if user.stake_amount >= tier.min_stake:
                user.tier = tier
                print(f"User {user.address} is now in tier: {tier.name}")
                return
        user.tier = None
        print(f"User {user.address} does not qualify for any tier.")

    def register_user(self, address: str):
        """
        Registers a new user in the staking system.
        :param address: The user's address
        """
        if address in self.users:
            raise ValueError("User already registered.")
        self.users[address] = User(address)
        print(f"User registered: {address}")

    def stake_for_user(self, address: str, amount: float):
        """
        Allows a registered user to stake an amount.
        :param address: The user's address
        :param amount: The amount to stake
        :raises ValueError: If the user is not registered
        """
        if address not in self.users:
            raise ValueError("User not registered.")
        
        user = self.users[address]
        user.stake(amount)
        self.get_user_tier(user)

# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    staking_system.add_tier("Bronze", 100, 5)
    staking_system.add_tier("Silver", 500, 10)
    staking_system.add_tier("Gold", 1000, 15)

    staking_system.register_user("0x123abc")
    staking_system.stake_for_user("0x123abc", 600)

    user = staking_system.users["0x123abc"]
    rewards = user.calculate_rewards()
    print(f"Rewards for user {user.address}: {rewards}")
```
