"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.nl
Prompt: Write a Python code snippet that demonstrates a basic investment strategy using technical indicators, and provide an explanation of the code in the context of Immediate Peak's investment education.
Generated: DETERMINISTIC_fbda8c408055bdaf
Batch ID: 20250622_211310
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

class InvestmentStrategy:
    """
    A class to implement a basic investment strategy using technical indicators.
    """

    def __init__(self, ticker: str, start_date: str, end_date: str):
        """
        Initializes the InvestmentStrategy with a stock ticker and date range.

        :param ticker: Stock ticker symbol (e.g., 'AAPL').
        :param start_date: Start date for historical data (format: 'YYYY-MM-DD').
        :param end_date: End date for historical data (format: 'YYYY-MM-DD').
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.fetch_data()

    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch historical stock data from Yahoo Finance.

        :return: DataFrame containing historical stock prices.
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError("No data fetched. Please check the ticker symbol and date range.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def calculate_indicators(self) -> None:
        """
        Calculate technical indicators: Moving Averages and RSI.
        """
        # Calculate the 50-day and 200-day moving averages
        self.data['MA50'] = self.data['Close'].rolling(window=50).mean()
        self.data['MA200'] = self.data['Close'].rolling(window=200).mean()

        # Calculate the Relative Strength Index (RSI)
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def generate_signals(self) -> None:
        """
        Generate buy/sell signals based on moving averages and RSI.
        """
        self.data['Signal'] = 0
        self.data['Signal'][50:] = np.where(
            (self.data['MA50'][50:] > self.data['MA200'][50:]) & (self.data['RSI'][50:] < 30), 1, 0
        )  # Buy signal
        self.data['Signal'][50:] = np.where(
            (self.data['MA50'][50:] < self.data['MA200'][50:]) & (self.data['RSI'][50:] > 70), -1, self.data['Signal'][50:]
        )  # Sell signal

    def plot_signals(self) -> None:
        """
        Plot the stock price along with buy/sell signals and moving averages.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['MA50'], label='50-Day MA', alpha=0.75)
        plt.plot(self.data['MA200'], label='200-Day MA', alpha=0.75)

        # Plot buy signals
        buy_signals = self.data[self.data['Signal'] == 1]
        plt.scatter(buy_signals.index, buy_signals['Close'][buy_signals['Signal'] == 1], marker='^', color='g', label='Buy Signal', alpha=1)

        # Plot sell signals
        sell_signals = self.data[self.data['Signal'] == -1]
        plt.scatter(sell_signals.index, sell_signals['Close'][sell_signals['Signal'] == -1], marker='v', color='r', label='Sell Signal', alpha=1)

        plt.title(f'{self.ticker} Price and Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Example usage of the InvestmentStrategy class
    strategy = InvestmentStrategy(ticker='AAPL', start_date='2020-01-01', end_date='2023-01-01')
    strategy.calculate_indicators()
    strategy.generate_signals()
    strategy.plot_signals()
```
