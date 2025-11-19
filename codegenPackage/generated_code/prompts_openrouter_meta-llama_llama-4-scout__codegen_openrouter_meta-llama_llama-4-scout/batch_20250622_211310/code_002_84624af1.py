"""
Generated Code Metadata:
========================
Original URL: https://immediatevortex.nl
Prompt: Generate a code example for a simple cryptocurrency trading strategy using Immediate Vortex's provided analytical tools and indicators, such as moving averages and Bollinger Bands.
Generated: DETERMINISTIC_84624af15c8301bf
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define a class for the trading strategy
class TradingStrategy:
    def __init__(self, symbol, short_window, long_window, bb_window, bb_std):
        """
        Initialize the trading strategy.

        Parameters:
        symbol (str): The stock symbol.
        short_window (int): The short window for the moving average.
        long_window (int): The long window for the moving average.
        bb_window (int): The window for Bollinger Bands.
        bb_std (int): The standard deviation for Bollinger Bands.
        """
        self.symbol = symbol
        self.short_window = short_window
        self.long_window = long_window
        self.bb_window = bb_window
        self.bb_std = bb_std

    def fetch_data(self):
        """
        Fetch historical data for the given symbol.
        """
        try:
            data = yf.download(self.symbol, period="1y")
            return data
        except Exception as e:
            print(f"Failed to fetch data: {e}")
            return None

    def calculate_indicators(self, data):
        """
        Calculate moving averages and Bollinger Bands.

        Parameters:
        data (pd.DataFrame): The historical data.

        Returns:
        pd.DataFrame: The data with indicators.
        """
        data['short_ma'] = data['Close'].rolling(window=self.short_window).mean()
        data['long_ma'] = data['Close'].rolling(window=self.long_window).mean()

        data['bb_middle'] = data['Close'].rolling(window=self.bb_window).mean()
        data['bb_upper'] = data['bb_middle'] + (data['Close'].rolling(window=self.bb_window).std() * self.bb_std)
        data['bb_lower'] = data['bb_middle'] - (data['Close'].rolling(window=self.bb_window).std() * self.bb_std)

        return data

    def generate_signals(self, data):
        """
        Generate buy and sell signals.

        Parameters:
        data (pd.DataFrame): The data with indicators.

        Returns:
        pd.DataFrame: The data with signals.
        """
        data['signal'] = 0.0

        # Generate buy signals
        data.loc[(data['short_ma'] > data['long_ma']) & (data['Close'] < data['bb_lower']), 'signal'] = 1.0

        # Generate sell signals
        data.loc[(data['short_ma'] < data['long_ma']) & (data['Close'] > data['bb_upper']), 'signal'] = -1.0

        return data

    def plot_strategy(self, data):
        """
        Plot the trading strategy.

        Parameters:
        data (pd.DataFrame): The data with signals.
        """
        plt.figure(figsize=(12,6))
        plt.plot(data['Close'], label='Close Price')
        plt.plot(data['short_ma'], label='Short MA')
        plt.plot(data['long_ma'], label='Long MA')
        plt.plot(data['bb_upper'], label='BB Upper')
        plt.plot(data['bb_middle'], label='BB Middle')
        plt.plot(data['bb_lower'], label='BB Lower')

        buy_signals = data[data['signal'] == 1.0]
        sell_signals = data[data['signal'] == -1.0]

        plt.scatter(buy_signals.index, buy_signals['Close'], label='Buy', marker='^', color='g')
        plt.scatter(sell_signals.index, sell_signals['Close'], label='Sell', marker='v', color='r')

        plt.legend(loc='upper left')
        plt.show()

# Usage
if __name__ == "__main__":
    strategy = TradingStrategy('BTC-USD', 20, 50, 20, 2)
    data = strategy.fetch_data()
    if data is not None:
        data = strategy.calculate_indicators(data)
        data = strategy.generate_signals(data)
        strategy.plot_strategy(data)
```
