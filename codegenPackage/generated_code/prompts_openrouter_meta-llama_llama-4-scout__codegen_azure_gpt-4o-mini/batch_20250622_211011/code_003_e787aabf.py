"""
Generated Code Metadata:
========================
Original URL: https://stake-aevo.pages.dev
Prompt: Design a function to calculate the total AEVO staked and the corresponding rewards based on the provided staking APR.
Generated: DETERMINISTIC_e787aabf2d4a8b49
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingCalculator:
    """
    A class to calculate the total AEVO staked and the corresponding rewards
    based on the provided staking Annual Percentage Rate (APR).
    """

    def __init__(self, total_staked: float, apr: float):
        """
        Initializes the StakingCalculator with the total staked amount and APR.

        :param total_staked: The total amount of AEVO staked (in currency units).
        :param apr: The annual percentage rate (APR) for staking (as a percentage).
        """
        if total_staked < 0:
            raise ValueError("Total staked amount cannot be negative.")
        if apr < 0:
            raise ValueError("APR cannot be negative.")

        self.total_staked = total_staked
        self.apr = apr / 100  # Convert APR from percentage to decimal

    def calculate_rewards(self, years: float) -> float:
        """
        Calculates the total rewards earned over a specified number of years.

        :param years: The number of years for which to calculate rewards.
        :return: The total rewards earned (in currency units).
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")

        # Calculate rewards using the formula: rewards = staked * (1 + apr) ** years - staked
        rewards = self.total_staked * ((1 + self.apr) ** years - 1)
        return rewards

    def total_value_after_rewards(self, years: float) -> float:
        """
        Calculates the total value after rewards are added.

        :param years: The number of years for which to calculate rewards.
        :return: The total value after rewards (in currency units).
        """
        rewards = self.calculate_rewards(years)
        total_value = self.total_staked + rewards
        return total_value


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with total staked amount and APR
        staking_calculator = StakingCalculator(total_staked=1000.0, apr=5.0)

        # Calculate rewards for 3 years
        years = 3
        rewards = staking_calculator.calculate_rewards(years)
        total_value = staking_calculator.total_value_after_rewards(years)

        print(f"Total rewards earned over {years} years: {rewards:.2f}")
        print(f"Total value after {years} years: {total_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
