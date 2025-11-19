"""
Generated Code Metadata:
========================
Original URL: https://jellynfts.web.app
Prompt: Develop a staking rewards calculator for Jelly token holders based on the project's staking utilities.
Generated: DETERMINISTIC_08c2af5c7ac87e53
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for Jelly token holders based on the amount staked,
    the staking duration, and the annual percentage yield (APY).
    """

    def __init__(self, apy: float):
        """
        Initializes the StakingRewardsCalculator with the given annual percentage yield (APY).

        :param apy: Annual Percentage Yield as a decimal (e.g., 0.05 for 5%)
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy

    def calculate_rewards(self, amount_staked: float, duration_years: float) -> float:
        """
        Calculates the staking rewards based on the amount staked and the duration.

        :param amount_staked: The amount of Jelly tokens staked.
        :param duration_years: The duration for which the tokens are staked, in years.
        :return: The total rewards earned over the staking period.
        """
        if amount_staked < 0:
            raise ValueError("Amount staked must be a non-negative value.")
        if duration_years < 0:
            raise ValueError("Duration must be a non-negative value.")

        # Calculate the total rewards using the formula for compound interest
        total_rewards = amount_staked * ((1 + self.apy) ** duration_years - 1)
        return total_rewards

    def display_rewards(self, amount_staked: float, duration_years: float) -> None:
        """
        Displays the calculated staking rewards in a user-friendly format.

        :param amount_staked: The amount of Jelly tokens staked.
        :param duration_years: The duration for which the tokens are staked, in years.
        """
        try:
            rewards = self.calculate_rewards(amount_staked, duration_years)
            print(f"Staking {amount_staked} Jelly tokens for {duration_years} years will yield "
                  f"{rewards:.2f} Jelly tokens in rewards.")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APY of 5%
        calculator = StakingRewardsCalculator(apy=0.05)

        # Example values for amount staked and duration
        amount_staked = 1000.0  # Amount of Jelly tokens
        duration_years = 2.0     # Duration in years

        # Display the rewards
        calculator.display_rewards(amount_staked, duration_years)
    except Exception as e:
        print(f"An error occurred: {e}")
```
