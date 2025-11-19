"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Write a Python script to implement a simple Forex trading strategy using technical indicators, such as moving averages and RSI, for a beginner trader.
Generated: DETERMINISTIC_cafc60a3d17bb641
Batch ID: 20250622_204946
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

class ForexTradingStrategy:
    def __init__(self, symbol, start_date, end_date):
        """
        Initialize the ForexTradingStrategy with the given parameters.

        :param symbol: The currency pair symbol (e.g., 'EURUSD=X').
        :param start_date: The start date for fetching historical data.
        :param end_date: The end date for fetching historical data.
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.fetch_data()

    def fetch_data(self):
        """
        Fetch historical Forex data from Yahoo Finance.

        :return: A DataFrame containing the historical data.
        """
        try:
            data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError("No data fetched. Please check the symbol and date range.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def calculate_indicators(self):
        """
        Calculate technical indicators: Moving Averages and RSI.

        :return: DataFrame with added indicators.
        """
        # Calculate Moving Averages
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()

        # Calculate RSI
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

        return self.data

    def generate_signals(self):
        """
        Generate buy/sell signals based on the indicators.

        :return: DataFrame with buy/sell signals.
        """
        self.data['Signal'] = 0
        self.data['Signal'] = np.where(
            (self.data['SMA_20'] > self.data['SMA_50']) & (self.data['RSI'] < 30), 1, 0)  # Buy signal
        self.data['Signal'] = np.where(
            (self.data['SMA_20'] < self.data['SMA_50']) & (self.data['RSI'] > 70), -1, self.data['Signal'])  # Sell signal
        return self.data

    def plot_signals(self):
        """
        Plot the closing price along with the buy/sell signals and indicators.

        :return: None
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['SMA_20'], label='20-Day SMA', alpha=0.75)
        plt.plot(self.data['SMA_50'], label='50-Day SMA', alpha=0.75)

        # Plot buy signals
        buy_signals = self.data[self.data['Signal'] == 1]
        plt.scatter(buy_signals.index, buy_signals['Close'][buy_signals['Signal'] == 1], 
                    label='Buy Signal', marker='^', color='g', s=100)

        # Plot sell signals
        sell_signals = self.data[self.data['Signal'] == -1]
        plt.scatter(sell_signals.index, sell_signals['Close'][sell_signals['Signal'] == -1], 
                    label='Sell Signal', marker='v', color='r', s=100)

        plt.title(f'{self.symbol} Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Define parameters for the trading strategy
    forex_symbol = 'EURUSD=X'  # Example currency pair
    start = '2020-01-01'  # Start date for historical data
    end = '2023-01-01'  # End date for historical data

    # Create an instance of the ForexTradingStrategy
    strategy = ForexTradingStrategy(forex_symbol, start, end)

    # Calculate indicators
    strategy.calculate_indicators()

    # Generate trading signals
    strategy.generate_signals()

    # Plot the results
    strategy.plot_signals()
```
