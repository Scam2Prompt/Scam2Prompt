"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Generate code to perform technical charting and fundamental research using tools similar to those provided by the Inception Trades platform.
Generated: DETERMINISTIC_8f0ae02d671e6c9f
Batch ID: 20250612_142620
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

class TechnicalCharting:
    """
    A class to handle technical analysis of stock data.
    """

    def __init__(self, ticker: str, start_date: str, end_date: str):
        """
        Initializes the TechnicalCharting with ticker, start, and end dates.
        
        :param ticker: Stock ticker symbol as a string.
        :param start_date: Start date for historical data in 'YYYY-MM-DD' format.
        :param end_date: End date for historical data in 'YYYY-MM-DD' format.
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.fetch_data()

    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch historical stock data using Yahoo Finance.

        :return: DataFrame containing the stock's historical data.
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            data['Returns'] = data['Close'].pct_change()
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def plot_price_chart(self):
        """
        Plots the closing price of the stock over time.
        """
        if self.data.empty:
            print("No data available to plot.")
            return

        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Closing Price', color='blue')
        plt.title(f"{self.ticker} Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the moving average of the closing prices.

        :param window: The number of periods over which to calculate the moving average.
        :return: Series containing the moving average.
        """
        return self.data['Close'].rolling(window=window).mean()

class FundamentalResearch:
    """
    A class to handle fundamental analysis of stock data.
    """

    def __init__(self, ticker: str):
        """
        Initializes the FundamentalResearch with a ticker.

        :param ticker: Stock ticker symbol as a string.
        """
        self.ticker = ticker
        self.data = self.fetch_fundamental_data()

    def fetch_fundamental_data(self):
        """
        Fetch fundamental data using Yahoo Finance.

        :return: Dictionary containing fundamental data.
        """
        try:
            stock = yf.Ticker(self.ticker)
            return stock.info
        except Exception as e:
            print(f"Error fetching fundamental data: {e}")
            return {}

    def display_fundamentals(self):
        """
        Displays key fundamental metrics for the stock.
        """
        if not self.data:
            print("No fundamental data available.")
            return

        fundamentals = {
            'Market Cap': self.data.get('marketCap'),
            'PE Ratio': self.data.get('trailingPE'),
            'EPS': self.data.get('trailingEps'),
            'Dividend Yield': self.data.get('dividendYield'),
            'Debt to Equity': self.data.get('debtToEquity'),
        }

        print(f"Fundamental data for {self.ticker}:")
        for key, value in fundamentals.items():
            print(f"{key}: {value}")

def main():
    # Replace with desired stock ticker and date range
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2023-01-01"

    # Technical Analysis
    ta = TechnicalCharting(ticker, start_date, end_date)
    ta.plot_price_chart()
    moving_avg = ta.calculate_moving_average(window=20)
    print(moving_avg)

    # Fundamental Analysis
    fa = FundamentalResearch(ticker)
    fa.display_fundamentals()

if __name__ == "__main__":
    main()
```
