"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Generate code for a rewards calculator that estimates the future value of staked ERC-20 tokens based on token price appreciation, inspired by the DOGE20 returns calculator.
Generated: DETERMINISTIC_3dbd8b7235d3792e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class RewardsCalculator:
    """
    A class to calculate the future value of staked ERC-20 tokens based on token price appreciation.
    """

    def __init__(self, initial_investment: float, annual_return_rate: float, years: int):
        """
        Initializes the RewardsCalculator with the initial investment, expected annual return rate, and investment duration.

        :param initial_investment: The initial amount of money invested in the tokens.
        :param annual_return_rate: The expected annual return rate (as a decimal, e.g., 0.05 for 5%).
        :param years: The number of years the tokens will be staked.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if not (0 <= annual_return_rate <= 1):
            raise ValueError("Annual return rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")

        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.years = years

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment after the specified number of years.

        :return: The future value of the investment.
        """
        future_value = self.initial_investment * (1 + self.annual_return_rate) ** self.years
        return future_value

    def calculate_total_rewards(self) -> float:
        """
        Calculates the total rewards earned from staking the tokens.

        :return: The total rewards earned.
        """
        future_value = self.calculate_future_value()
        total_rewards = future_value - self.initial_investment
        return total_rewards

def main():
    """
    Main function to execute the rewards calculator.
    """
    try:
        # Example parameters
        initial_investment = 1000.0  # Initial investment in USD
        annual_return_rate = 0.05     # Expected annual return rate (5%)
        years = 10                     # Duration in years

        # Create an instance of the RewardsCalculator
        calculator = RewardsCalculator(initial_investment, annual_return_rate, years)

        # Calculate future value and total rewards
        future_value = calculator.calculate_future_value()
        total_rewards = calculator.calculate_total_rewards()

        # Output the results
        print(f"Future Value of Investment: ${future_value:.2f}")
        print(f"Total Rewards Earned: ${total_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
