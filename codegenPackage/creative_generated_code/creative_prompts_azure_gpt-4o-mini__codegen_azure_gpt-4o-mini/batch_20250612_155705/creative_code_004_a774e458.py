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

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from typing import List, Dict

class MarketAnalysisTool:
    """
    A class to perform market analysis using both technical and fundamental analysis.
    """

    def __init__(self, ticker: str):
        """
        Initializes the MarketAnalysisTool with a stock ticker.

        Args:
            ticker (str): The stock symbol for the market analysis.
        """
        self.ticker = ticker
        self.data = None

    def fetch_historical_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetches historical stock data from Yahoo Finance.

        Args:
            start_date (str): The start date for historical data in 'YYYY-MM-DD' format.
            end_date (str): The end date for historical data in 'YYYY-MM-DD' format.

        Returns:
            pd.DataFrame: Historical stock data.
        """
        try:
            self.data = yf.download(self.ticker, start=start_date, end=end_date)
            if self.data.empty:
                raise ValueError("No data fetched. Check the ticker symbol or date range.")
            return self.data
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return pd.DataFrame()

    def calculate_technical_indicators(self) -> Dict[str, pd.Series]:
        """
        Calculate technical indicators such as Moving Averages and RSI.

        Returns:
            Dict[str, pd.Series]: A dictionary containing calculated technical indicators.
        """
        if self.data is None:
            print("No historical data available. Please fetch data first.")
            return {}

        indicators = {}
        
        # Calculate Moving Averages
        indicators['SMA_20'] = self.data['Close'].rolling(window=20).mean()  # 20-day Simple Moving Average
        indicators['SMA_50'] = self.data['Close'].rolling(window=50).mean()  # 50-day Simple Moving Average
        
        # Calculate RSI (Relative Strength Index)
        delta = self.data['Close'].diff(1)
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        indicators['RSI'] = 100 - (100 / (1 + rs))
        
        return indicators

    def fetch_fundamental_data(self) -> Dict[str, float]:
        """
        Fetches fundamental data such as P/E Ratio and Market Cap from Yahoo Finance.

        Returns:
            Dict[str, float]: A dictionary containing fundamental metrics.
        """
        try:
            stock_info = yf.Ticker(self.ticker).info
            fundamental_data = {
                "P/E Ratio": stock_info.get('forwardPE', None),
                "Market Cap": stock_info.get('marketCap', None),
                "Dividend Yield": stock_info.get('dividendYield', None)
            }
            return fundamental_data
        except Exception as e:
            print(f"Error fetching fundamental data: {e}")
            return {}

    def plot_data(self):
        """
        Plot the closing price and technical indicators.
        """
        if self.data is None:
            print("No historical data available. Please fetch data first.")
            return
        
        indicators = self.calculate_technical_indicators()
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Close'], label='Close Price', color='blue')
        plt.plot(indicators['SMA_20'], label='20-day SMA', color='orange')
        plt.plot(indicators['SMA_50'], label='50-day SMA', color='green')
        plt.title(f'{self.ticker} Price and Technical Indicators')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    ticker_symbol = 'AAPL'  # Example ticker symbol
    market_analysis_tool = MarketAnalysisTool(ticker_symbol)
    historical_data = market_analysis_tool.fetch_historical_data('2022-01-01', '2023-01-01')
    
    technical_indicators = market_analysis_tool.calculate_technical_indicators()
    fundamental_data = market_analysis_tool.fetch_fundamental_data()
    
    print("Technical Indicators:")
    print(technical_indicators)
    
    print("\nFundamental Data:")
    print(fundamental_data)
    
    market_analysis_tool.plot_data()
```
