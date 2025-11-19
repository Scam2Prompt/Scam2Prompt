"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: Explain how to calculate potential returns for DOGE20 investments based on its fixed supply and staking rewards.
Generated: DETERMINISTIC_e833942d64f5f3c4
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Doge20Investment:
    def __init__(self, initial_investment, staking_reward_rate, total_supply):
        """
        Initializes the Doge20Investment instance.

        :param initial_investment: The initial amount invested in DOGE20.
        :param staking_reward_rate: Annual staking reward rate as a decimal (e.g., 0.05 for 5%).
        :param total_supply: The total fixed supply of DOGE20.
        """
        self.initial_investment = initial_investment
        self.staking_reward_rate = staking_reward_rate
        self.total_supply = total_supply

    def calculate_future_value(self, years):
        """
        Calculates the future value of the investment based on the staking rewards.

        :param years: The number of years the investment is held.
        :return: The future value of the investment after the given number of years.
        """
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")
        
        future_value = self.initial_investment * (1 + self.staking_reward_rate) ** years
        return future_value

    def calculate_roi(self, years):
        """
        Calculates the return on investment (ROI) after a given number of years.

        :param years: The number of years the investment is held.
        :return: The ROI as a percentage.
        """
        future_value = self.calculate_future_value(years)
        roi = ((future_value - self.initial_investment) / self.initial_investment) * 100
        return roi

    def display_investment_summary(self, years):
        """
        Displays a summary of the investment's potential returns.

        :param years: The number of years the investment is held.
        """
        try:
            future_value = self.calculate_future_value(years)
            roi = self.calculate_roi(years)
            print(f"Initial Investment: ${self.initial_investment:.2f}")
            print(f"Total Supply of DOGE20: {self.total_supply}")
            print(f"Years Held: {years}")
            print(f"Future Value: ${future_value:.2f}")
            print(f"Return on Investment (ROI): {roi:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    investment = Doge20Investment(initial_investment=1000, staking_reward_rate=0.05, total_supply=1000000)
    investment.display_investment_summary(years=5)
```
