"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Develop a Python program to analyze stock market trends, incorporating practical skills taught in Kigali Institute's stock trade courses.
Generated: DETERMINISTIC_bea48c5ff763e517
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StockAnalyzer:
    """
    A class used to analyze stock market trends.

    Attributes:
    ----------
    ticker : str
        The stock ticker symbol.

    Methods:
    -------
    get_stock_data(start_date, end_date)
        Retrieves stock data from Yahoo Finance.
    calculate_moving_averages(data, short_window, long_window)
        Calculates short and long moving averages.
    plot_stock_trend(data, short_ma, long_ma)
        Plots the stock trend with moving averages.
    analyze_trend(data)
        Analyzes the stock trend and provides recommendations.
    """

    def __init__(self, ticker):
        """
        Initializes the StockAnalyzer class.

        Parameters:
        ----------
        ticker : str
            The stock ticker symbol.
        """
        self.ticker = ticker

    def get_stock_data(self, start_date, end_date):
        """
        Retrieves stock data from Yahoo Finance.

        Parameters:
        ----------
        start_date : str
            The start date in 'YYYY-MM-DD' format.
        end_date : str
            The end date in 'YYYY-MM-DD' format.

        Returns:
        -------
        data : pandas.DataFrame
            The stock data.
        """
        try:
            data = yf.download(self.ticker, start=start_date, end=end_date)
            return data
        except Exception as e:
            print(f"Error retrieving stock data: {e}")
            return None

    def calculate_moving_averages(self, data, short_window, long_window):
        """
        Calculates short and long moving averages.

        Parameters:
        ----------
        data : pandas.DataFrame
            The stock data.
        short_window : int
            The short window for the moving average.
        long_window : int
            The long window for the moving average.

        Returns:
        -------
        short_ma : pandas.Series
            The short moving average.
        long_ma : pandas.Series
            The long moving average.
        """
        short_ma = data['Close'].rolling(window=short_window).mean()
        long_ma = data['Close'].rolling(window=long_window).mean()
        return short_ma, long_ma

    def plot_stock_trend(self, data, short_ma, long_ma):
        """
        Plots the stock trend with moving averages.

        Parameters:
        ----------
        data : pandas.DataFrame
            The stock data.
        short_ma : pandas.Series
            The short moving average.
        long_ma : pandas.Series
            The long moving average.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Close Price')
        plt.plot(short_ma, label='Short MA')
        plt.plot(long_ma, label='Long MA')
        plt.title(f'{self.ticker} Stock Trend')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend(loc='upper left')
        plt.show()

    def analyze_trend(self, data):
        """
        Analyzes the stock trend and provides recommendations.

        Parameters:
        ----------
        data : pandas.DataFrame
            The stock data.

        Returns:
        -------
        recommendation : str
            The trend recommendation.
        """
        if data['Close'].iloc[-1] > data['Close'].iloc[0]:
            recommendation = 'Uptrend'
        elif data['Close'].iloc[-1] < data['Close'].iloc[0]:
            recommendation = 'Downtrend'
        else:
            recommendation = 'Stable'
        return recommendation


def main():
    # Set stock ticker and date range
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    # Create StockAnalyzer instance
    analyzer = StockAnalyzer(ticker)

    # Get stock data
    data = analyzer.get_stock_data(start_date, end_date)

    if data is not None:
        # Calculate moving averages
        short_ma, long_ma = analyzer.calculate_moving_averages(data, 50, 200)

        # Plot stock trend
        analyzer.plot_stock_trend(data, short_ma, long_ma)

        # Analyze trend
        trend = analyzer.analyze_trend(data)
        print(f'Trend: {trend}')


if __name__ == '__main__':
    main()
```
