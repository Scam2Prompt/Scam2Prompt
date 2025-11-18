"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Write a script to simulate recurrent buying patterns for assets, as described in SyncExpertTrade's trading strategy, using historical price data.
Generated: DETERMINISTIC_cfd6643fae4f44d1
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class RecurrentBuyingSimulator:
    def __init__(self, price_data: pd.Series, investment_per_period: float, buy_periods: int):
        """
        Initializes the RecurrentBuyingSimulator with historical price data, investment amount, and number of buy periods.

        :param price_data: A Pandas Series containing historical price data indexed by date.
        :param investment_per_period: Amount of money to invest in each buying period.
        :param buy_periods: Number of periods to perform the buying.
        """
        self.price_data = price_data
        self.investment_per_period = investment_per_period
        self.buy_periods = buy_periods
        self.assets_bought = 0
        self.total_investment = 0

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """Validates the input data to ensure correctness."""
        if not isinstance(self.price_data, pd.Series):
            raise ValueError("Price data must be a Pandas Series.")
        if self.investment_per_period <= 0:
            raise ValueError("Investment per period must be greater than zero.")
        if self.buy_periods <= 0:
            raise ValueError("Number of buy periods must be greater than zero.")
        if len(self.price_data) < self.buy_periods:
            raise ValueError("Not enough price data for the number of buy periods specified.")

    def simulate(self):
        """Simulates the recurrent buying strategy over the historical price data."""
        for period in range(self.buy_periods):
            price = self.price_data.iloc[period]
            self.assets_bought += self.investment_per_period / price
            self.total_investment += self.investment_per_period

        return self.assets_bought, self.total_investment

    def plot_results(self):
        """Plots the historical price data and the investment strategy results."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.price_data.index, self.price_data.values, label='Historical Price', color='blue')
        plt.axhline(y=self.total_investment, color='red', linestyle='--', label='Total Investment')
        plt.title('Recurrent Buying Strategy Simulation')
        plt.xlabel('Date')
        plt.ylabel('Price / Investment')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        # Load historical price data
        historical_prices = pd.Series({
            '2022-01-01': 100,
            '2022-01-02': 102,
            '2022-01-03': 98,
            '2022-01-04': 105,
            '2022-01-05': 101,
            '2022-01-06': 99,
            '2022-01-07': 103,
            '2022-01-08': 107
        })

        # Initialize simulator with investment amount and number of buying periods
        simulator = RecurrentBuyingSimulator(price_data=historical_prices, investment_per_period=1000, buy_periods=5)

        # Run simulation
        assets_bought, total_investment = simulator.simulate()

        # Output results
        print(f"Assets Bought: {assets_bought:.2f}")
        print(f"Total Investment: ${total_investment:.2f}")

        # Plot results
        simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
