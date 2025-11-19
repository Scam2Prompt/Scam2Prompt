"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtc-token.pages.dev
Prompt: Create a function that calculates the potential rewards for staking $GBTC based on different staking durations and amounts.
Generated: DETERMINISTIC_4400eaeb9a445b7f
Batch ID: 20250612_161420
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
    A class to calculate potential rewards for staking $GBTC based on different durations and amounts.
    """

    def __init__(self, annual_interest_rate):
        """
        Initialize the StakingCalculator with an annual interest rate.

        :param annual_interest_rate: The annual interest rate as a decimal (e.g., 0.05 for 5%).
        """
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")
        self.annual_interest_rate = annual_interest_rate

    def calculate_rewards(self, amount, duration_years):
        """
        Calculate the potential rewards for staking $GBTC.

        :param amount: The amount of $GBTC to stake.
        :param duration_years: The duration of the staking in years.
        :return: The total rewards earned over the staking period.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if duration_years <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        # Calculate the rewards using compound interest formula
        rewards = amount * ((1 + self.annual_interest_rate) ** duration_years - 1)
        return rewards

    def display_rewards(self, amount, duration_years):
        """
        Display the potential rewards for given staking parameters.

        :param amount: The amount of $GBTC to stake.
        :param duration_years: The duration of the staking in years.
        """
        try:
            rewards = self.calculate_rewards(amount, duration_years)
            print(f"Staking ${amount:.2f} for {duration_years} years will yield rewards of: ${rewards:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with a 5% annual interest rate
        staking_calculator = StakingCalculator(0.05)
        
        # Example: Calculate rewards for staking $1000 for 3 years
        staking_calculator.display_rewards(1000, 3)
    except Exception as e:
        print(f"An error occurred: {e}")
```
