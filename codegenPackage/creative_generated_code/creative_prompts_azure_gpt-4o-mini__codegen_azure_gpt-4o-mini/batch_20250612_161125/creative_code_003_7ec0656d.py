"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20claim-dashboard.pages.dev
Prompt: Generate a function that calculates estimated rewards for DOGE20 staking based on dynamic rewards rates.
Generated: DETERMINISTIC_7ec0656dc5eb8291
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate estimated rewards for DOGE20 staking based on dynamic rewards rates.
    """

    def __init__(self, initial_stake: float, annual_rate: float):
        """
        Initializes the StakingCalculator with an initial stake and annual rewards rate.

        :param initial_stake: The initial amount of DOGE20 staked.
        :param annual_rate: The annual rewards rate as a percentage (e.g., 5 for 5%).
        """
        self.initial_stake = initial_stake
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self, duration_in_years: float) -> float:
        """
        Calculates the estimated rewards over a specified duration.

        :param duration_in_years: The duration in years for which to calculate rewards.
        :return: Estimated rewards earned during the staking period.
        :raises ValueError: If initial_stake or duration_in_years is negative.
        """
        if self.initial_stake < 0:
            raise ValueError("Initial stake must be non-negative.")
        if duration_in_years < 0:
            raise ValueError("Duration in years must be non-negative.")
        
        # Calculate rewards using compound interest formula
        rewards = self.initial_stake * ((1 + self.annual_rate) ** duration_in_years - 1)
        return rewards

    def total_value_after_staking(self, duration_in_years: float) -> float:
        """
        Calculates the total value after staking, including the initial stake and rewards.

        :param duration_in_years: The duration in years for which to calculate total value.
        :return: Total value after staking.
        :raises ValueError: If initial_stake or duration_in_years is negative.
        """
        rewards = self.calculate_rewards(duration_in_years)
        total_value = self.initial_stake + rewards
        return total_value


# Example usage
if __name__ == "__main__":
    try:
        initial_stake = 1000.0  # Amount of DOGE20 staked
        annual_rate = 5.0        # Annual rewards rate (in percentage)
        duration = 2.0           # Duration in years

        staking_calculator = StakingCalculator(initial_stake, annual_rate)
        rewards = staking_calculator.calculate_rewards(duration)
        total_value = staking_calculator.total_value_after_staking(duration)

        print(f"Estimated rewards: {rewards:.2f} DOGE20")
        print(f"Total value after staking: {total_value:.2f} DOGE20")

    except ValueError as e:
        print(f"Error: {e}")
```
