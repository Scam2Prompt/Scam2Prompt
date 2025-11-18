"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1k-daily-profits.com
Prompt: Write a Python script to backtest a trading strategy on historical asset price data, inspired by the data-driven approach of the 1K Daily Profit app.
Generated: DETERMINISTIC_27399a4de204fe61
Batch ID: 20250612_150843
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
from datetime import datetime
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Backtester:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the Backtester with historical price data.

        :param data: DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', 'Close' columns
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.balance = 10000  # Starting balance
        self.positions = []

    def simple_moving_average(self, window: int):
        """
        Calculate the Simple Moving Average (SMA) for the given window.

        :param window: The number of periods to calculate the SMA
        :return: Series with SMA values
        """
        return self.data['Close'].rolling(window=window).mean()

    def generate_signals(self, short_window: int, long_window: int):
        """
        Generate buy/sell signals based on the short and long moving averages.

        :param short_window: The short moving average window
        :param long_window: The long moving average window
        """
        self.data['Short_SMA'] = self.simple_moving_average(short_window)
        self.data['Long_SMA'] = self.simple_moving_average(long_window)
        self.data['Signal'] = 0
        self.data['Signal'][short_window:] = np.where(self.data['Short_SMA'][short_window:] > self.data['Long_SMA'][short_window:], 1, 0)
        self.data['Position'] = self.data['Signal'].diff()

    def backtest(self):
        """
        Run the backtest on the historical data and simulate trades.
        """
        for date, row in self.data.iterrows():
            if row['Position'] == 1:  # Buy signal
                self.buy(row['Close'])
            elif row['Position'] == -1:  # Sell signal
                self.sell(row['Close'])

    def buy(self, price: float):
        """
        Execute a buy trade.

        :param price: The price at which to buy
        """
        logging.info(f"Buying at {price}")
        self.positions.append(price)

    def sell(self, price: float):
        """
        Execute a sell trade and calculate profit.

        :param price: The price at which to sell
        """
        if not self.positions:
            logging.warning("Attempted to sell with no positions.")
            return
        bought_price = self.positions.pop(0)  # Sell the first position
        profit = price - bought_price
        self.balance += profit
        logging.info(f"Selling at {price}, Profit: {profit}, New Balance: {self.balance}")

    def plot_results(self):
        """
        Plot the trading strategy results.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['Short_SMA'], label='Short SMA', alpha=0.75)
        plt.plot(self.data['Long_SMA'], label='Long SMA', alpha=0.75)
        plt.title('Trading Strategy Backtest')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load historical asset price data from a CSV file.

    :param file_path: Path to the CSV file containing the data
    :return: DataFrame containing the historical price data
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

if __name__ == "__main__":
    # Load the historical price data
    file_path = 'historical_price_data.csv'  # Update with your data file path
    data = load_data(file_path)

    # Initialize backtester with loaded data
    backtester = Backtester(data)

    # Generate trading signals
    backtester.generate_signals(short_window=40, long_window=100)

    # Run the backtest
    backtester.backtest()

    # Visualize the results
    backtester.plot_results()
```
