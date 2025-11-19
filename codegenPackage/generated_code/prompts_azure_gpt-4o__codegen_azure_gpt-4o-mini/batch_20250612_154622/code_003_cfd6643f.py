"""
Generated Code Metadata:
========================
Original URL: https://syncexperttrade.com
Prompt: Write a script to simulate recurrent buying patterns for assets, as described in SyncExpertTrade's trading strategy, using historical price data.
Generated: DETERMINISTIC_cfd6643fae4f44d1
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AssetTrader:
    """
    A class to simulate recurrent buying patterns for assets based on historical price data.
    """

    def __init__(self, historical_data: pd.DataFrame, initial_investment: float, buy_threshold: float):
        """
        Initializes the AssetTrader with historical data, initial investment, and buy threshold.

        :param historical_data: DataFrame containing historical price data with a 'Date' and 'Close' column.
        :param initial_investment: Initial amount of money to invest.
        :param buy_threshold: Percentage drop in price to trigger a buy.
        """
        self.historical_data = historical_data
        self.initial_investment = initial_investment
        self.buy_threshold = buy_threshold
        self.current_balance = initial_investment
        self.assets_owned = 0

    def simulate_trading(self):
        """
        Simulates the trading strategy based on historical price data.
        """
        # Ensure the historical data is sorted by date
        self.historical_data.sort_values('Date', inplace=True)

        # Iterate through the historical price data
        for index, row in self.historical_data.iterrows():
            current_price = row['Close']
            date = row['Date']

            # Check if we can buy assets
            if self.assets_owned == 0 and self.current_balance > 0:
                # Calculate the price drop percentage
                if index > 0:
                    previous_price = self.historical_data.iloc[index - 1]['Close']
                    price_drop_percentage = ((previous_price - current_price) / previous_price) * 100

                    # Buy if the price drop exceeds the threshold
                    if price_drop_percentage >= self.buy_threshold:
                        # Calculate how many assets can be bought
                        assets_to_buy = self.current_balance // current_price
                        if assets_to_buy > 0:
                            self.assets_owned += assets_to_buy
                            self.current_balance -= assets_to_buy * current_price
                            print(f"Bought {assets_to_buy} assets on {date} at {current_price:.2f}")

        # Final balance and assets owned
        self.final_balance = self.current_balance + (self.assets_owned * self.historical_data.iloc[-1]['Close'])
        print(f"Final balance: {self.final_balance:.2f}")
        print(f"Assets owned: {self.assets_owned}")

    def plot_results(self):
        """
        Plots the historical price data and marks the buy points.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.historical_data['Date'], self.historical_data['Close'], label='Price', color='blue')

        # Mark buy points
        buy_dates = self.historical_data[self.historical_data['Close'].shift(1) * (1 - self.buy_threshold / 100) >= self.historical_data['Close']]
        plt.scatter(buy_dates['Date'], buy_dates['Close'], color='green', label='Buy Points', marker='^', s=100)

        plt.title('Asset Price and Buy Points')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

def load_historical_data(file_path: str) -> pd.DataFrame:
    """
    Loads historical price data from a CSV file.

    :param file_path: Path to the CSV file containing historical price data.
    :return: DataFrame containing the historical price data.
    """
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'])
        if 'Date' not in data.columns or 'Close' not in data.columns:
            raise ValueError("CSV must contain 'Date' and 'Close' columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Load historical data
    historical_data = load_historical_data('historical_prices.csv')

    if not historical_data.empty:
        # Initialize the trader with historical data, initial investment, and buy threshold
        trader = AssetTrader(historical_data, initial_investment=10000, buy_threshold=5)

        # Simulate trading
        trader.simulate_trading()

        # Plot results
        trader.plot_results()
```
