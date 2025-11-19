"""
Generated Code Metadata:
========================
Original URL: https://doge20claim-dashboard.pages.dev
Prompt: "Design a staking rewards system for a new cryptocurrency project, taking into account dynamic rewards rates and token supply distribution over a 2-year period."
Generated: DETERMINISTIC_ad3dbd3b73637a0e
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsSystem:
    """
    A class to represent a staking rewards system for a cryptocurrency project.
    
    Attributes:
        total_supply (float): The total supply of tokens available for staking.
        staking_duration (int): The duration for staking rewards in days.
        reward_rate (float): The dynamic reward rate for staking.
        rewards_distribution (dict): A dictionary to track rewards distribution over time.
    """

    def __init__(self, total_supply: float, staking_duration: int):
        """
        Initializes the StakingRewardsSystem with total supply and staking duration.

        Args:
            total_supply (float): The total supply of tokens.
            staking_duration (int): The duration for staking rewards in days.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        self.total_supply = total_supply
        self.staking_duration = staking_duration
        self.reward_rate = self.calculate_dynamic_reward_rate()
        self.rewards_distribution = {}

    def calculate_dynamic_reward_rate(self) -> float:
        """
        Calculates the dynamic reward rate based on the total supply.

        Returns:
            float: The calculated reward rate.
        """
        # Example logic for dynamic reward rate based on total supply
        if self.total_supply < 1_000_000:
            return 0.15  # 15% reward rate for low supply
        elif self.total_supply < 10_000_000:
            return 0.10  # 10% reward rate for medium supply
        else:
            return 0.05  # 5% reward rate for high supply

    def stake_tokens(self, amount: float, days: int) -> float:
        """
        Stakes a specified amount of tokens for a given number of days.

        Args:
            amount (float): The amount of tokens to stake.
            days (int): The number of days to stake the tokens.

        Returns:
            float: The total rewards earned from staking.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if days <= 0 or days > self.staking_duration:
            raise ValueError("Staking days must be within the staking duration.")

        # Calculate rewards based on the amount staked and the reward rate
        rewards = amount * self.reward_rate * (days / self.staking_duration)
        self.rewards_distribution[days] = self.rewards_distribution.get(days, 0) + rewards
        return rewards

    def get_total_rewards(self) -> float:
        """
        Returns the total rewards distributed over the staking period.

        Returns:
            float: The total rewards distributed.
        """
        return sum(self.rewards_distribution.values())

    def display_rewards_distribution(self):
        """
        Displays the rewards distribution over the staking period.
        """
        print("Rewards Distribution Over Time:")
        for days, rewards in self.rewards_distribution.items():
            print(f"Days: {days}, Rewards: {rewards:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        staking_system = StakingRewardsSystem(total_supply=5_000_000, staking_duration=730)
        rewards_1 = staking_system.stake_tokens(amount=1000, days=30)
        print(f"Rewards earned for 30 days: {rewards_1:.2f}")
        
        rewards_2 = staking_system.stake_tokens(amount=2000, days=60)
        print(f"Rewards earned for 60 days: {rewards_2:.2f}")

        staking_system.display_rewards_distribution()
        print(f"Total rewards distributed: {staking_system.get_total_rewards():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
