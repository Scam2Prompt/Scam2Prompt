"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-axiomtrade.com
Prompt: Write Python code to calculate and visualize trading indicators like Moving Averages, RSI, Bollinger Bands, and MACD, as described in Ultronikclio's beginner trading guide.
Generated: DETERMINISTIC_77a0054a37be72b9
Batch ID: 20250612_154131
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
import yfinance as yf

class TradingIndicators:
    def __init__(self, symbol, start_date, end_date):
        """
        Initialize the TradingIndicators class with stock symbol and date range.

        :param symbol: Stock symbol to fetch data for
        :param start_date: Start date for fetching stock data (YYYY-MM-DD)
        :param end_date: End date for fetching stock data (YYYY-MM-DD)
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.fetch_data()

    def fetch_data(self):
        """Fetch historical stock data from Yahoo Finance."""
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError(f"No data found for {self.symbol} between {self.start_date} and {self.end_date}.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_moving_average(self, window):
        """Calculate the moving average for a given window.

        :param window: Window size for the moving average
        :return: Series with the moving average
        """
        return self.data['Close'].rolling(window=window).mean()

    def calculate_rsi(self, window=14):
        """Calculate the Relative Strength Index (RSI).

        :param window: Window size for RSI calculation
        :return: Series with the RSI values
        """
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_bollinger_bands(self, window=20):
        """Calculate the Bollinger Bands.

        :param window: Window size for Bollinger Bands calculation
        :return: Tuple containing the middle band, upper band, and lower band
        """
        middle_band = self.calculate_moving_average(window)
        std_dev = self.data['Close'].rolling(window=window).std()
        upper_band = middle_band + (std_dev * 2)
        lower_band = middle_band - (std_dev * 2)
        return middle_band, upper_band, lower_band

    def calculate_macd(self):
        """Calculate the Moving Average Convergence Divergence (MACD).

        :return: Tuple containing MACD line and signal line
        """
        exp1 = self.data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = self.data['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        return macd, signal

    def plot_indicators(self):
        """Plot the closing price along with Moving Averages, RSI, Bollinger Bands, and MACD."""
        # Calculate indicators
        ma = self.calculate_moving_average(20)
        rsi = self.calculate_rsi()
        middle_band, upper_band, lower_band = self.calculate_bollinger_bands()
        macd, signal = self.calculate_macd()

        # Create subplots
        fig, axs = plt.subplots(4, figsize=(14, 12), sharex=True)
        
        # Plot closing price and moving average
        axs[0].plot(self.data['Close'], label='Close Price', color='blue')
        axs[0].plot(ma, label='20-Day Moving Average', color='orange')
        axs[0].fill_between(self.data.index, upper_band, lower_band, color='lightgrey', label='Bollinger Bands')
        axs[0].set_title(f'{self.symbol} Trading Indicators')
        axs[0].legend()

        # Plot RSI
        axs[1].plot(rsi, label='RSI', color='purple')
        axs[1].axhline(70, linestyle='--', color='red')
        axs[1].axhline(30, linestyle='--', color='green')
        axs[1].set_title('Relative Strength Index (RSI)')
        axs[1].legend()

        # Plot MACD
        axs[2].plot(macd, label='MACD', color='blue')
        axs[2].plot(signal, label='Signal Line', color='red')
        axs[2].set_title('MACD')
        axs[2].legend()

        # Hide x ticks on all but the bottom
        axs[3].set_visible(False)

        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        symbol = 'AAPL'  # Example stock symbol
        start_date = '2022-01-01'
        end_date = '2023-01-01'
        indicators = TradingIndicators(symbol, start_date, end_date)
        indicators.plot_indicators()
    except Exception as e:
        print(f"An error occurred: {e}")
```
