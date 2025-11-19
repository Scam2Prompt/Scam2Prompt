"""
Generated Code Metadata:
========================
Original URL: https://bit-gpt-urex.com
Prompt: Write Python code to simulate cryptocurrency market analysis using historical price trends and technical indicators, as described in the Bit GPT Urex platform.
Generated: DETERMINISTIC_370f043e0b956b2f
Batch ID: 20250612_150843
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
from datetime import datetime, timedelta

class CryptoMarketAnalyzer:
    """
    A class to analyze cryptocurrency market trends using historical price data
    and technical indicators.
    """

    def __init__(self, symbol: str, start_date: str, end_date: str):
        """
        Initializes the CryptoMarketAnalyzer with the given cryptocurrency symbol
        and date range.

        :param symbol: The ticker symbol of the cryptocurrency (e.g., 'BTC-USD').
        :param start_date: The start date for historical data in 'YYYY-MM-DD' format.
        :param end_date: The end date for historical data in 'YYYY-MM-DD' format.
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        """
        Fetch historical price data for the specified cryptocurrency from Yahoo Finance.
        """
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("No data fetched. Please check the symbol and date range.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_indicators(self):
        """
        Calculate technical indicators: Moving Averages and RSI.
        """
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")

        # Calculate Moving Averages
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()

        # Calculate RSI
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def plot_data(self):
        """
        Plot the historical price data along with the calculated indicators.
        """
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")

        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', color='blue')
        plt.plot(self.data['SMA_20'], label='20-Day SMA', color='orange')
        plt.plot(self.data['SMA_50'], label='50-Day SMA', color='green')
        plt.title(f'{self.symbol} Price and Technical Indicators')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

        # Plot RSI
        plt.figure(figsize=(14, 5))
        plt.plot(self.data['RSI'], label='RSI', color='purple')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.title(f'{self.symbol} RSI')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the cryptocurrency market analysis.
    """
    # Define parameters
    symbol = 'BTC-USD'
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Create an instance of the analyzer
    analyzer = CryptoMarketAnalyzer(symbol, start_date, end_date)

    # Fetch data, calculate indicators, and plot results
    try:
        analyzer.fetch_data()
        analyzer.calculate_indicators()
        analyzer.plot_data()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
