"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Generate code for a rewards calculator that estimates the future value of staked ERC-20 tokens based on token price appreciation, inspired by the DOGE20 returns calculator.
Generated: DETERMINISTIC_3dbd8b7235d3792e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class RewardsCalculator:
    """
    A class to calculate the estimated future value of staked ERC-20 tokens
    based on token price appreciation.
    """

    def __init__(self, initial_investment: float, annual_growth_rate: float,
                 staking_period_years: int, staking_reward_rate: float):
        """
        Initialize the RewardsCalculator with initial investment, annual growth rate,
        staking period in years, and staking reward rate.

        :param initial_investment: The initial amount invested in the tokens.
        :param annual_growth_rate: The expected annual growth rate of the token price (in decimal).
        :param staking_period_years: The number of years the tokens will be staked.
        :param staking_reward_rate: The annual reward rate from staking (in decimal).
        """
        self.initial_investment = initial_investment
        self.annual_growth_rate = annual_growth_rate
        self.staking_period_years = staking_period_years
        self.staking_reward_rate = staking_reward_rate

    def calculate_future_value(self) -> float:
        """
        Calculate the future value of staked tokens after a certain period.

        :return: The estimated future value of staked tokens.
        """
        # Calculate future price appreciation
        future_price = self.initial_investment * (1 + self.annual_growth_rate) ** self.staking_period_years
        
        # Calculate rewards from staking
        staking_rewards = future_price * self.staking_reward_rate * self.staking_period_years
        
        # Calculate total future value
        total_future_value = future_price + staking_rewards
        
        return total_future_value

    def display_results(self) -> None:
        """
        Display the results of the future value calculation in a formatted way.
        """
        try:
            future_value = self.calculate_future_value()
            print(f"Initial Investment: ${self.initial_investment:.2f}")
            print(f"Annual Growth Rate: {self.annual_growth_rate * 100:.2f}%")
            print(f"Staking Period: {self.staking_period_years} years")
            print(f"Staking Reward Rate: {self.staking_reward_rate * 100:.2f}%")
            print(f"Estimated Future Value: ${future_value:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating future value: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        initial_investment = 1000.0  # Initial investment in USD
        annual_growth_rate = 0.15  # Expected annual growth rate (15%)
        staking_period_years = 5  # Number of years of staking
        staking_reward_rate = 0.05  # Staking reward rate (5%)

        calculator = RewardsCalculator(initial_investment, annual_growth_rate, staking_period_years, staking_reward_rate)
        calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
