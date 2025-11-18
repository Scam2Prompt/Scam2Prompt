"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Develop code to calculate staking rewards for DOGE20 tokens based on the tokenomics provided (e.g., 15% of total supply allocated for staking rewards).
Generated: DETERMINISTIC_213fd701eb5cb2b7
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for DOGE20 tokens based on predefined tokenomics.
    """

    def __init__(self, total_supply: float, staking_allocation_percentage: float):
        """
        Initializes the StakingRewardsCalculator with the total supply and staking allocation percentage.

        :param total_supply: The total supply of DOGE20 tokens.
        :param staking_allocation_percentage: The percentage of total supply allocated for staking rewards.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= staking_allocation_percentage <= 100):
            raise ValueError("Staking allocation percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.staking_allocation_percentage = staking_allocation_percentage
        self.staking_rewards_pool = self.calculate_staking_rewards_pool()

    def calculate_staking_rewards_pool(self) -> float:
        """
        Calculates the total amount allocated for staking rewards.

        :return: The total staking rewards pool.
        """
        return (self.total_supply * self.staking_allocation_percentage) / 100

    def calculate_rewards(self, staked_amount: float, total_staked_amount: float) -> float:
        """
        Calculates the staking rewards for a user based on their staked amount.

        :param staked_amount: The amount of DOGE20 tokens staked by the user.
        :param total_staked_amount: The total amount of DOGE20 tokens staked in the pool.
        
        :return: The staking rewards for the user's staked amount.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if total_staked_amount <= 0:
            raise ValueError("Total staked amount must be greater than zero.")

        # Calculate user rewards proportionate to their stake
        user_reward = (staked_amount / total_staked_amount) * self.staking_rewards_pool
        return user_reward

# Example usage:
if __name__ == "__main__":
    try:
        # Define total supply and staking allocation percentage
        total_supply = 100_000_000  # Example total supply
        staking_allocation_percentage = 15.0  # 15% allocated for staking rewards

        # Create an instance of the StakingRewardsCalculator
        rewards_calculator = StakingRewardsCalculator(total_supply, staking_allocation_percentage)

        # Example staked amounts
        user_staked_amount = 10_000  # User's staked amount
        total_staked_amount = 1_000_000  # Total staked amount in the pool

        # Calculate user's staking rewards
        rewards = rewards_calculator.calculate_rewards(user_staked_amount, total_staked_amount)
        print(f"User's staking rewards: {rewards:.2f} DOGE20 tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
```
