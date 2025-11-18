"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write code to calculate staking rewards for BTCETF tokens based on the tokenomics provided (total supply: 2,100,000,000; staking allocation: 25%).
Generated: DETERMINISTIC_1f6e257bc9834411
Batch ID: 20250612_152109
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
    A class to calculate staking rewards for BTCETF tokens based on the tokenomics provided.
    """

    def __init__(self, total_supply: int, staking_allocation_percentage: float):
        """
        Initializes the StakingRewardsCalculator with total supply and staking allocation percentage.

        :param total_supply: Total supply of BTCETF tokens.
        :param staking_allocation_percentage: Percentage of total supply allocated for staking.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        if not (0 <= staking_allocation_percentage <= 100):
            raise ValueError("Staking allocation percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.staking_allocation_percentage = staking_allocation_percentage

    def calculate_staking_allocation(self) -> float:
        """
        Calculates the total amount of tokens allocated for staking.

        :return: The total staking allocation in tokens.
        """
        staking_allocation = (self.staking_allocation_percentage / 100) * self.total_supply
        return staking_allocation

    def calculate_rewards(self, user_staked_amount: float, total_staked_amount: float) -> float:
        """
        Calculates the user's staking rewards based on their staked amount and total staked amount.

        :param user_staked_amount: The amount of tokens the user has staked.
        :param total_staked_amount: The total amount of tokens currently staked.
        :return: The user's staking rewards.
        """
        if user_staked_amount < 0:
            raise ValueError("User staked amount cannot be negative.")
        if total_staked_amount <= 0:
            raise ValueError("Total staked amount must be a positive number.")

        # Calculate user's share of the total staked amount
        user_share = user_staked_amount / total_staked_amount
        staking_allocation = self.calculate_staking_allocation()

        # Calculate user's rewards based on their share of the staking allocation
        user_rewards = user_share * staking_allocation
        return user_rewards


# Example usage:
if __name__ == "__main__":
    try:
        # Tokenomics values
        total_supply = 2_100_000_000  # Total supply of BTCETF tokens
        staking_allocation_percentage = 25  # Staking allocation percentage

        # Instantiate the calculator
        rewards_calculator = StakingRewardsCalculator(total_supply, staking_allocation_percentage)

        # Example staking amounts
        user_staked_amount = 1_000_000  # Amount user has staked
        total_staked_amount = 10_000_000  # Total amount staked in the system

        # Calculate user rewards
        rewards = rewards_calculator.calculate_rewards(user_staked_amount, total_staked_amount)
        print(f"User's staking rewards: {rewards:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
