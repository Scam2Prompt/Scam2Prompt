"""
Generated Code Metadata:
========================
Original URL: https://immediate-byte.com
Prompt: Generate a Python script to perform technical analysis on historical market data, using tools and techniques like chart patterns, trends, and support and resistance levels.
Generated: DETERMINISTIC_b4e461378ae6497c
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
import talib

class TechnicalAnalysis:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        """
        Initialize the TechnicalAnalysis class with stock ticker and date range.

        :param ticker: Stock ticker symbol (e.g., 'AAPL')
        :param start_date: Start date for historical data (format: 'YYYY-MM-DD')
        :param end_date: End date for historical data (format: 'YYYY-MM-DD')
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.fetch_data()

    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch historical market data from Yahoo Finance.

        :return: DataFrame containing historical market data
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError("No data fetched. Please check the ticker symbol and date range.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculate the moving average for the given window.

        :param window: The number of periods to calculate the moving average
        :return: Series containing the moving average
        """
        return self.data['Close'].rolling(window=window).mean()

    def identify_support_resistance(self) -> tuple:
        """
        Identify support and resistance levels based on historical data.

        :return: Tuple containing support and resistance levels
        """
        support = self.data['Close'].min()
        resistance = self.data['Close'].max()
        return support, resistance

    def plot_data(self):
        """
        Plot historical closing prices along with moving averages and support/resistance levels.
        """
        try:
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Close'], label='Close Price', color='blue', alpha=0.5)
            ma20 = self.calculate_moving_average(20)
            ma50 = self.calculate_moving_average(50)
            plt.plot(ma20, label='20-Day MA', color='orange', linestyle='--')
            plt.plot(ma50, label='50-Day MA', color='red', linestyle='--')

            support, resistance = self.identify_support_resistance()
            plt.axhline(y=support, color='green', linestyle='--', label='Support Level')
            plt.axhline(y=resistance, color='red', linestyle='--', label='Resistance Level')

            plt.title(f'Technical Analysis of {self.ticker}')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error plotting data: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        ticker_symbol = 'AAPL'  # Change to desired stock ticker
        start = '2020-01-01'
        end = '2023-01-01'
        
        ta = TechnicalAnalysis(ticker=ticker_symbol, start_date=start, end_date=end)
        ta.plot_data()
    except Exception as e:
        print(f"An error occurred: {e}")
```
