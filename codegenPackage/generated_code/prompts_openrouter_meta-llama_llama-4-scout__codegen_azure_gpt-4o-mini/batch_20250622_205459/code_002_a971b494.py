"""
Generated Code Metadata:
========================
Original URL: https://diamondtradingfx.com
Prompt: Develop a simple trading strategy using technical indicators for predicting the direction of financial market movements, specifically for beginners.
Generated: DETERMINISTIC_a971b49473541e44
Batch ID: 20250622_205459
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
import yfinance as yf

class SimpleTradingStrategy:
    """
    A simple trading strategy using moving averages to predict market movements.
    This strategy generates buy/sell signals based on the crossover of short and long-term moving averages.
    """

    def __init__(self, ticker, start_date, end_date, short_window=20, long_window=50):
        """
        Initializes the trading strategy with the given parameters.

        :param ticker: Stock ticker symbol (e.g., 'AAPL')
        :param start_date: Start date for historical data (e.g., '2020-01-01')
        :param end_date: End date for historical data (e.g., '2023-01-01')
        :param short_window: Short moving average window
        :param long_window: Long moving average window
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.short_window = short_window
        self.long_window = long_window
        self.data = None
        self.signals = None

    def fetch_data(self):
        """Fetch historical stock data from Yahoo Finance."""
        try:
            self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("No data fetched. Please check the ticker symbol and date range.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def compute_indicators(self):
        """Compute short and long moving averages and generate buy/sell signals."""
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")

        # Calculate moving averages
        self.data['Short_MA'] = self.data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        self.data['Long_MA'] = self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()

        # Generate signals
        self.data['Signal'] = 0
        self.data['Signal'][self.short_window:] = np.where(
            self.data['Short_MA'][self.short_window:] > self.data['Long_MA'][self.short_window:], 1, 0
        )
        self.data['Position'] = self.data['Signal'].diff()

    def plot_signals(self):
        """Plot the closing price along with the moving averages and buy/sell signals."""
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")

        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['Short_MA'], label=f'Short {self.short_window}-Day MA', alpha=0.75)
        plt.plot(self.data['Long_MA'], label=f'Long {self.long_window}-Day MA', alpha=0.75)

        # Plot buy signals
        plt.plot(self.data[self.data['Position'] == 1].index,
                 self.data['Short_MA'][self.data['Position'] == 1],
                 '^', markersize=10, color='g', lw=0, label='Buy Signal')

        # Plot sell signals
        plt.plot(self.data[self.data['Position'] == -1].index,
                 self.data['Short_MA'][self.data['Position'] == -1],
                 'v', markersize=10, color='r', lw=0, label='Sell Signal')

        plt.title(f'Trading Strategy for {self.ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

    def run_strategy(self):
        """Run the trading strategy by fetching data, computing indicators, and plotting signals."""
        self.fetch_data()
        self.compute_indicators()
        self.plot_signals()

# Example usage
if __name__ == "__main__":
    strategy = SimpleTradingStrategy(ticker='AAPL', start_date='2020-01-01', end_date='2023-01-01')
    strategy.run_strategy()
```
