"""
Generated Code Metadata:
========================
Original URL: https://capinvest.ltd
Prompt: Write Python code to simulate a trading strategy for CAPINVEST LTD's platform using leverage options (e.g., 1:20, 1:50, 1:100) and calculate daily returns based on the provided investment plans.
Generated: DETERMINISTIC_49ab93f9dec02b41
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class TradingStrategy:
    """
    A class to simulate a trading strategy for CAPINVEST LTD's platform using leverage options.
    """

    def __init__(self, initial_investment: float, leverage: float, daily_return_rate: float):
        """
        Initializes the trading strategy with the given parameters.

        :param initial_investment: The initial amount of money to invest.
        :param leverage: The leverage ratio (e.g., 20 for 1:20).
        :param daily_return_rate: The expected daily return rate as a decimal (e.g., 0.01 for 1%).
        """
        self.initial_investment = initial_investment
        self.leverage = leverage
        self.daily_return_rate = daily_return_rate
        self.daily_returns = []

    def simulate_trading_days(self, num_days: int):
        """
        Simulates the trading over a specified number of days.

        :param num_days: The number of trading days to simulate.
        """
        for day in range(num_days):
            daily_return = self.calculate_daily_return()
            self.daily_returns.append(daily_return)

    def calculate_daily_return(self) -> float:
        """
        Calculates the daily return based on the leveraged investment.

        :return: The daily return for the current day.
        """
        # Calculate the total investment with leverage
        leveraged_investment = self.initial_investment * self.leverage
        # Calculate the daily return
        daily_return = leveraged_investment * self.daily_return_rate
        return daily_return

    def get_total_returns(self) -> float:
        """
        Calculates the total returns after all simulated trading days.

        :return: The total returns from the trading strategy.
        """
        return sum(self.daily_returns)

    def get_daily_returns_dataframe(self) -> pd.DataFrame:
        """
        Returns a DataFrame containing the daily returns.

        :return: A pandas DataFrame with daily returns.
        """
        return pd.DataFrame(self.daily_returns, columns=['Daily Returns'])

def main():
    """
    Main function to run the trading strategy simulation.
    """
    try:
        # Parameters for the trading strategy
        initial_investment = 1000.0  # Initial investment amount
        leverage = 20.0                # Leverage ratio (1:20)
        daily_return_rate = 0.01       # Daily return rate (1%)

        # Create an instance of the TradingStrategy
        trading_strategy = TradingStrategy(initial_investment, leverage, daily_return_rate)

        # Simulate trading for 30 days
        trading_strategy.simulate_trading_days(num_days=30)

        # Get total returns
        total_returns = trading_strategy.get_total_returns()
        print(f"Total Returns after 30 days: ${total_returns:.2f}")

        # Get daily returns DataFrame
        daily_returns_df = trading_strategy.get_daily_returns_dataframe()
        print(daily_returns_df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
