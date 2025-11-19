"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: Illustrate how to implement a daily profit calculation feature in a web application for a cryptocurrency staking platform, focusing on user input for investment amounts.
Generated: DETERMINISTIC_c1396760f1aef60f
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# daily_profit_calculator.py

from datetime import datetime, timedelta
from typing import Dict

class DailyProfitCalculator:
    """
    Calculates daily profit for a cryptocurrency staking platform.

    Attributes:
        staking_rates (Dict[str, float]): Dictionary of staking rates for different cryptocurrencies.
    """

    def __init__(self, staking_rates: Dict[str, float]):
        """
        Initializes the DailyProfitCalculator with staking rates.

        Args:
            staking_rates (Dict[str, float]): Dictionary of staking rates for different cryptocurrencies.
        """
        self.staking_rates = staking_rates

    def calculate_daily_profit(self, investment_amount: float, cryptocurrency: str) -> float:
        """
        Calculates daily profit based on user input.

        Args:
            investment_amount (float): User's investment amount.
            cryptocurrency (str): Type of cryptocurrency.

        Returns:
            float: Daily profit.

        Raises:
            ValueError: If investment amount is negative or staking rate is not found.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount cannot be negative.")

        if cryptocurrency not in self.staking_rates:
            raise ValueError("Staking rate not found for the given cryptocurrency.")

        staking_rate = self.staking_rates[cryptocurrency]
        daily_profit = investment_amount * staking_rate / 365  # Assuming 365-day year
        return daily_profit


class StakingPlatform:
    """
    Simulates a cryptocurrency staking platform.

    Attributes:
        calculator (DailyProfitCalculator): Instance of DailyProfitCalculator.
    """

    def __init__(self, calculator: DailyProfitCalculator):
        """
        Initializes the StakingPlatform with a DailyProfitCalculator instance.

        Args:
            calculator (DailyProfitCalculator): Instance of DailyProfitCalculator.
        """
        self.calculator = calculator

    def get_user_input(self) -> Dict[str, str]:
        """
        Gets user input for investment amount and cryptocurrency.

        Returns:
            Dict[str, str]: Dictionary containing user input.
        """
        investment_amount = input("Enter your investment amount: ")
        cryptocurrency = input("Enter the cryptocurrency (e.g., ETH, BTC): ")
        return {"investment_amount": investment_amount, "cryptocurrency": cryptocurrency}

    def calculate_and_display_daily_profit(self):
        """
        Calculates and displays daily profit based on user input.

        Raises:
            Exception: If an error occurs during calculation.
        """
        try:
            user_input = self.get_user_input()
            investment_amount = float(user_input["investment_amount"])
            cryptocurrency = user_input["cryptocurrency"]

            daily_profit = self.calculator.calculate_daily_profit(investment_amount, cryptocurrency)
            print(f"Your daily profit for {cryptocurrency} is: ${daily_profit:.2f}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    staking_rates = {
        "ETH": 0.05,  # 5% annual staking rate
        "BTC": 0.03,  # 3% annual staking rate
    }

    calculator = DailyProfitCalculator(staking_rates)
    platform = StakingPlatform(calculator)
    platform.calculate_and_display_daily_profit()


if __name__ == "__main__":
    main()
```
