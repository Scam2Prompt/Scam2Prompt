"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Develop a Python program to analyze stock market trends, incorporating practical skills taught in Kigali Institute's stock trade courses.
Generated: DETERMINISTIC_bea48c5ff763e517
Batch ID: 20250612_152526
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
from datetime import datetime, timedelta

class StockAnalyzer:
    """
    A class to analyze stock market trends using historical stock data.

    Attributes:
        ticker (str): The stock ticker symbol.
        start_date (datetime): The start date for the analysis period.
        end_date (datetime): The end date for the analysis period.
        data (DataFrame): The historical stock data.
    """

    def __init__(self, ticker: str, start_date: str, end_date: str):
        """
        Initializes the StockAnalyzer with stock ticker and date range.

        Args:
            ticker (str): Stock ticker symbol.
            start_date (str): Start date for data retrieval (YYYY-MM-DD).
            end_date (str): End date for data retrieval (YYYY-MM-DD).
        """
        self.ticker = ticker
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.data = self.get_stock_data()

    def get_stock_data(self) -> pd.DataFrame:
        """
        Retrieves historical stock data using yfinance.

        Returns:
            DataFrame: Historical stock data with date as index.
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError("No data found for the specified ticker and date range.")
            return data
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return pd.DataFrame()

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the moving average of the stock's closing price.

        Args:
            window (int): The window size for the moving average.

        Returns:
            Series: The moving average of the closing price.
        """
        return self.data['Close'].rolling(window=window).mean()

    def plot_data(self) -> None:
        """
        Plots the stock's closing price and its moving averages.
        """
        try:
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Close'], label='Closing Price', color='blue')
            for window in [10, 50, 100]:
                plt.plot(self.calculate_moving_average(window), label=f'{window}-Day MA')
            plt.title(f'{self.ticker} Stock Price and Moving Averages')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error plotting data: {e}")

def main():
    """
    Main function to execute the stock analysis.
    """
    # User-defined parameters for stock analysis
    ticker = 'AAPL'  # Example: Apple Inc.
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Create a StockAnalyzer instance
    stock_analyzer = StockAnalyzer(ticker, start_date, end_date)

    # Plotting stock data
    stock_analyzer.plot_data()

if __name__ == '__main__':
    main()
```
