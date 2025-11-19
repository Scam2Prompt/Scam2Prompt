"""
Generated Code Metadata:
========================
Original URL: https://polkadot-france.fr
Prompt: "Create a simple staking calculator for Polkadot, considering the current staking reward and inflation rate."
Generated: DETERMINISTIC_19f198436c8d4e81
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_calculator.py

class StakingCalculator:
    """
    A simple staking calculator for Polkadot.

    Attributes:
        staking_reward (float): The current staking reward.
        inflation_rate (float): The current inflation rate.
        total_staked (float): The total amount staked.
    """

    def __init__(self, staking_reward: float, inflation_rate: float, total_staked: float):
        """
        Initializes the StakingCalculator.

        Args:
            staking_reward (float): The current staking reward.
            inflation_rate (float): The current inflation rate.
            total_staked (float): The total amount staked.
        """
        self.staking_reward = staking_reward
        self.inflation_rate = inflation_rate
        self.total_staked = total_staked

    def calculate_staking_rewards(self, staked_amount: float) -> float:
        """
        Calculates the staking rewards based on the staked amount.

        Args:
            staked_amount (float): The amount staked.

        Returns:
            float: The staking rewards.

        Raises:
            ValueError: If the staked amount is negative.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative")

        # Calculate the staking rewards
        rewards = (staked_amount / self.total_staked) * self.staking_reward
        return rewards

    def calculate_inflation_based_rewards(self, staked_amount: float) -> float:
        """
        Calculates the inflation-based rewards.

        Args:
            staked_amount (float): The amount staked.

        Returns:
            float: The inflation-based rewards.

        Raises:
            ValueError: If the staked amount is negative.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative")

        # Calculate the inflation-based rewards
        rewards = staked_amount * self.inflation_rate
        return rewards

    def calculate_total_rewards(self, staked_amount: float) -> float:
        """
        Calculates the total rewards.

        Args:
            staked_amount (float): The amount staked.

        Returns:
            float: The total rewards.

        Raises:
            ValueError: If the staked amount is negative.
        """
        staking_rewards = self.calculate_staking_rewards(staked_amount)
        inflation_based_rewards = self.calculate_inflation_based_rewards(staked_amount)
        total_rewards = staking_rewards + inflation_based_rewards
        return total_rewards


def main():
    try:
        # Example usage
        staking_reward = 0.1  # 10%
        inflation_rate = 0.05  # 5%
        total_staked = 1000000  # 1,000,000 DOT

        calculator = StakingCalculator(staking_reward, inflation_rate, total_staked)

        staked_amount = 10000  # 10,000 DOT

        staking_rewards = calculator.calculate_staking_rewards(staked_amount)
        inflation_based_rewards = calculator.calculate_inflation_based_rewards(staked_amount)
        total_rewards = calculator.calculate_total_rewards(staked_amount)

        print(f"Staking Rewards: {staking_rewards:.2f} DOT")
        print(f"Inflation-based Rewards: {inflation_based_rewards:.2f} DOT")
        print(f"Total Rewards: {total_rewards:.2f} DOT")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
