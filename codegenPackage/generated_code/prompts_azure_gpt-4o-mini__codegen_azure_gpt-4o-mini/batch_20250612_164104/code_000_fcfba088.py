"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Generate a Python script that implements a trading strategy based on the "3 high-probability trading setups" discussed in the FinTrends trading courses.
Generated: DETERMINISTIC_fcfba088e0581969
Batch ID: 20250612_164104
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
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingStrategy:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the TradingStrategy with historical price data.

        :param data: A pandas DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', 'Close' columns.
        """
        self.data = data
        self.signals = pd.DataFrame(index=self.data.index)

    def moving_average_crossover(self, short_window=50, long_window=200):
        """
        Implement the Moving Average Crossover strategy.

        :param short_window: The short moving average window.
        :param long_window: The long moving average window.
        """
        logging.info("Calculating moving averages.")
        self.signals['Short_MA'] = self.data['Close'].rolling(window=short_window, min_periods=1).mean()
        self.signals['Long_MA'] = self.data['Close'].rolling(window=long_window, min_periods=1).mean()
        
        # Generate signals
        self.signals['Signal'] = 0
        self.signals['Signal'][short_window:] = np.where(
            self.signals['Short_MA'][short_window:] > self.signals['Long_MA'][short_window:], 1, 0
        )
        self.signals['Position'] = self.signals['Signal'].diff()

    def rsi_strategy(self, period=14, overbought=70, oversold=30):
        """
        Implement the RSI (Relative Strength Index) strategy.

        :param period: The period for calculating RSI.
        :param overbought: The overbought threshold.
        :param oversold: The oversold threshold.
        """
        logging.info("Calculating RSI.")
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        self.signals['RSI'] = 100 - (100 / (1 + rs))

        # Generate signals
        self.signals['Signal'] = 0
        self.signals['Signal'] = np.where(self.signals['RSI'] > overbought, -1, self.signals['Signal'])
        self.signals['Signal'] = np.where(self.signals['RSI'] < oversold, 1, self.signals['Signal'])
        self.signals['Position'] = self.signals['Signal'].diff()

    def plot_signals(self):
        """
        Plot the trading signals along with the price data.
        """
        logging.info("Plotting trading signals.")
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.signals['Short_MA'], label='Short Moving Average', alpha=0.75)
        plt.plot(self.signals['Long_MA'], label='Long Moving Average', alpha=0.75)

        # Plot buy signals
        plt.plot(self.signals[self.signals['Position'] == 1].index,
                 self.data['Close'][self.signals['Position'] == 1],
                 '^', markersize=10, color='g', lw=0, label='Buy Signal')

        # Plot sell signals
        plt.plot(self.signals[self.signals['Position'] == -1].index,
                 self.data['Close'][self.signals['Position'] == -1],
                 'v', markersize=10, color='r', lw=0, label='Sell Signal')

        plt.title('Trading Strategy Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    # Load historical price data
    try:
        data = pd.read_csv('historical_price_data.csv', parse_dates=['Date'], index_col='Date')
        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return

    # Initialize trading strategy
    strategy = TradingStrategy(data)

    # Apply trading strategies
    strategy.moving_average_crossover()
    strategy.rsi_strategy()

    # Plot the results
    strategy.plot_signals()

if __name__ == "__main__":
    main()
```
