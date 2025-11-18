"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixedfloatio.org
Prompt: Write a program to simulate yield farming and staking rewards on a platform similar to FixedFloat, using RAY tokens as an example.
Generated: DETERMINISTIC_595bacd274cd7e58
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class YieldFarmingPlatform:
    def __init__(self):
        """Initialize the yield farming platform with an empty pool."""
        self.pool = {}
    
    def stake(self, user: str, amount: float):
        """
        Allow a user to stake a specified amount of RAY tokens.

        :param user: The username of the user staking tokens.
        :param amount: The amount of RAY tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        
        if user not in self.pool:
            self.pool[user] = 0.0

        self.pool[user] += amount
        print(f"{amount} RAY tokens staked by {user}. Total staked: {self.pool[user]} RAY.")

    def calculate_rewards(self, user: str) -> float:
        """
        Calculate rewards based on the staked amount.

        :param user: The username of the user for whom to calculate rewards.
        :return: The calculated rewards as a float.
        """
        if user not in self.pool:
            return 0.0
        
        # For simplicity, assume a fixed reward rate of 10% per time unit (e.g., day)
        reward_rate = 0.10
        staked_amount = self.pool[user]
        # Assume each reward calculation is per unit time (e.g., per day)
        rewards = staked_amount * reward_rate
        return rewards

    def claim_rewards(self, user: str):
        """
        Allow a user to claim their rewards.

        :param user: The username of the user claiming rewards.
        :return: The amount of rewards claimed.
        """
        if user not in self.pool:
            raise ValueError(f"No stake found for user {user}.")
        
        rewards = self.calculate_rewards(user)
        print(f"{user} claimed {rewards:.2f} RAY tokens as rewards.")
        return rewards

    def unstake(self, user: str, amount: float):
        """
        Allow a user to unstake a specified amount of RAY tokens.

        :param user: The username of the user unstaking tokens.
        :param amount: The amount of RAY tokens to unstake.
        """
        if user not in self.pool or self.pool[user] < amount:
            raise ValueError(f"Insufficient balance for user {user}.")
        
        self.pool[user] -= amount
        print(f"{amount} RAY tokens unstaked by {user}. Total staked: {self.pool[user]} RAY.")

# Example usage:
if __name__ == "__main__":
    platform = YieldFarmingPlatform()

    # Users stake RAY tokens
    platform.stake("Alice", 100)
    platform.stake("Bob", 200)

    # Users claim rewards
    print(platform.claim_rewards("Alice"))
    print(platform.claim_rewards("Bob"))

    # Users unstake RAY tokens
    platform.unstake("Alice", 50)
    platform.unstake("Bob", 100)
```
