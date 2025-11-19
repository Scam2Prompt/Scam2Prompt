"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Illustrate how to implement a market analysis tool that combines technical and fundamental analysis to provide comprehensive insights, as described by AIvest Securities Limited.
Generated: DETERMINISTIC_a774e458d51ace7a
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a market analysis tool that combines technical and fundamental analysis. 

```python
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.linear_model import LinearRegression
from datetime import datetime

class MarketAnalysisTool:
    """
    A market analysis tool that combines technical and fundamental analysis
    to provide comprehensive insights into stock performance.
    """

    def __init__(self, ticker):
        """
        Initializes the tool with a stock ticker.

        :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple)
        """
        self.ticker = ticker
        self.data = None
        self.fundamentals = None

    def fetch_data(self, start_date, end_date):
        """
        Fetches historical stock data from Yahoo Finance.

        :param start_date: Start date for the data (YYYY-MM-DD)
        :param end_date: End date for the data (YYYY-MM-DD)
        """
        try:
            self.data = yf.download(self.ticker, start=start_date, end=end_date)
        except Exception as e:
            raise RuntimeError(f"Error fetching data for {self.ticker}: {str(e)}")

    def calculate_technical_indicators(self):
        """
        Calculates basic technical indicators like moving averages and RSI.
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")

        # Moving Averages
        self.data['MA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data['MA_200'] = self.data['Close'].rolling(window=200).mean()

        # Relative Strength Index (RSI)
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def fetch_fundamental_data(self):
        """
        Fetches basic fundamental data using the Yahoo Finance library.
        """
        try:
            stock = yf.Ticker(self.ticker)
            self.fundamentals = stock.info
        except Exception as e:
            raise RuntimeError(f"Error fetching fundamental data for {self.ticker}: {str(e)}")

    def perform_regression_analysis(self):
        """
        Performs linear regression analysis on stock closing prices.

        :return: Regression coefficient and intercept
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")

        X = np.arange(len(self.data)).reshape(-1, 1)  # Days since start
        y = self.data['Close'].values.reshape(-1, 1)

        model = LinearRegression()
        model.fit(X, y)

        return model.coef_[0][0], model.intercept_[0]

    def generate_report(self):
        """
        Generates a comprehensive report combining technical and fundamental analysis.

        :return: Dictionary containing insights
        """
        if self.data is None or self.fundamentals is None:
            raise ValueError("Ensure both technical and fundamental data are available.")

        report = {
            "Technical Analysis": {
                "Latest RSI": self.data['RSI'].iloc[-1],
                "50-Day Moving Average": self.data['MA_50'].iloc[-1],
                "200-Day Moving Average": self.data['MA_200'].iloc[-1]
            },
            "Fundamental Analysis": {
                "Market Cap": self.fundamentals.get('marketCap', 'N/A'),
                "PE Ratio": self.fundamentals.get('trailingPE', 'N/A'),
                "Dividend Yield": self.fundamentals.get('dividendYield', 'N/A')
            }
        }

        # Regression analysis
        slope, intercept = self.perform_regression_analysis()
        report["Trend Analysis"] = {
            "Regression Slope": slope,
            "Regression Intercept": intercept
        }

        return report


if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')

    tool = MarketAnalysisTool(ticker)

    try:
        tool.fetch_data(start_date, end_date)
        tool.calculate_technical_indicators()
        tool.fetch_fundamental_data()
        report = tool.generate_report()

        print("Market Analysis Report:")
        for category, details in report.items():
            print(f"\n{category}:")
            for key, value in details.items():
                print(f"  {key}: {value}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

This script fetches stock data from Yahoo Finance, calculates some basic technical indicators (MA, RSI), retrieves fundamental information, performs regression analysis on the closing prices, and generates a report combining these insights.
