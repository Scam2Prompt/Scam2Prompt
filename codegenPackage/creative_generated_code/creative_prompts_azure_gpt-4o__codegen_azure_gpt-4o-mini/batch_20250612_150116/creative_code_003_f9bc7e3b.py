"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcore-profit.com
Prompt: Develop a script to analyze historical cryptocurrency prices and technical indicators, mimicking the functionality of the Bitcore Profit app.
Generated: DETERMINISTIC_f9bc7e3b08f86a8c
Batch ID: 20250612_150116
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
import yfinance as yf
import matplotlib.pyplot as plt

class CryptoAnalyzer:
    """
    A class to analyze historical cryptocurrency prices and calculate technical indicators.
    """

    def __init__(self, symbol: str, start: str, end: str):
        """
        Initialize the CryptoAnalyzer with the cryptocurrency symbol and date range.

        :param symbol: The symbol of the cryptocurrency (e.g., 'BTC-USD').
        :param start: Start date for historical data (format: 'YYYY-MM-DD').
        :param end: End date for historical data (format: 'YYYY-MM-DD').
        """
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = None
        self.indicators = {}

    def fetch_data(self):
        """
        Fetch historical price data for the specified cryptocurrency.
        """
        try:
            self.data = yf.download(self.symbol, start=self.start, end=self.end)
            if self.data.empty:
                raise ValueError("No data fetched, please check the cryptocurrency symbol and date range.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculate the moving average for the closing prices.

        :param window: The window size for the moving average.
        :return: Pandas Series with the moving average values.
        """
        if self.data is None:
            raise ValueError("Data not fetched. Call fetch_data() before calculating moving average.")
        return self.data['Close'].rolling(window=window).mean()

    def calculate_rsi(self, period: int) -> pd.Series:
        """
        Calculate the Relative Strength Index (RSI).

        :param period: The period over which to calculate RSI.
        :return: Pandas Series with RSI values.
        """
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def plot_data(self):
        """
        Plot the historical closing prices and moving averages.
        """
        if self.data is None:
            raise ValueError("Data not fetched. Call fetch_data() before plotting.")

        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', color='blue')
        
        for window in [20, 50]:
            ma = self.calculate_moving_average(window)
            plt.plot(ma, label=f'MA {window}', alpha=0.7)

        plt.title(f'{self.symbol} Price and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the crypto analysis.
    """
    # User inputs
    symbol = 'BTC-USD'  # Change this to any other cryptocurrency symbol as needed
    start_date = '2022-01-01'
    end_date = '2023-10-01'

    # Create an instance of the CryptoAnalyzer
    analyzer = CryptoAnalyzer(symbol, start_date, end_date)

    # Fetch data
    analyzer.fetch_data()

    # Calculate and display RSI
    rsi = analyzer.calculate_rsi(period=14)
    print(rsi)

    # Plot the data
    analyzer.plot_data()

if __name__ == "__main__":
    main()
```
