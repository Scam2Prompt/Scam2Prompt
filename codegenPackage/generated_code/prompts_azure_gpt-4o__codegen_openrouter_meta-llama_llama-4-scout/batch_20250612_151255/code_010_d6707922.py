"""
Generated Code Metadata:
========================
Original URL: https://7364500043.pages.dev
Prompt: Generate code to analyze the historical price trends of Bitcoin ETFs, inspired by Journal Du Coin's "Bitcoin le 10 août - Les ETF dans le rouge depuis le top à 70 000 $."
Generated: DETERMINISTIC_d67079229ec94511
Batch ID: 20250612_151255
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
from datetime import datetime, timedelta

def get_historical_data(ticker, start_date, end_date):
    """
    Retrieves historical market data for a given ticker symbol.

    Args:
        ticker (str): The ticker symbol of the ETF (e.g., 'BITO', 'BITQ', etc.)
        start_date (str): The start date of the period in 'YYYY-MM-DD' format.
        end_date (str): The end date of the period in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical market data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error retrieving historical data: {e}")
        return None

def analyze_trend(data):
    """
    Analyzes the historical price trend of the given data.

    Args:
        data (pandas.DataFrame): A DataFrame containing the historical market data.

    Returns:
        dict: A dictionary containing the trend analysis results.
    """
    try:
        # Calculate daily returns
        data['Return'] = data['Close'].pct_change()

        # Calculate moving averages
        data['MA_50'] = data['Close'].rolling(window=50).mean()
        data['MA_200'] = data['Close'].rolling(window=200).mean()

        # Identify trends
        trend = {}
        if data['Close'].iloc[-1] < data['MA_50'].iloc[-1] and data['MA_50'].iloc[-1] < data['MA_200'].iloc[-1]:
            trend['short_term'] = 'Downtrend'
        elif data['Close'].iloc[-1] > data['MA_50'].iloc[-1] and data['MA_50'].iloc[-1] > data['MA_200'].iloc[-1]:
            trend['short_term'] = 'Uptrend'
        else:
            trend['short_term'] = 'Neutral'

        if data['Close'].iloc[-1] < data['MA_200'].iloc[-1]:
            trend['long_term'] = 'Downtrend'
        elif data['Close'].iloc[-1] > data['MA_200'].iloc[-1]:
            trend['long_term'] = 'Uptrend'
        else:
            trend['long_term'] = 'Neutral'

        return trend
    except Exception as e:
        print(f"Error analyzing trend: {e}")
        return None

def main():
    # Define parameters
    tickers = ['BITO', 'BITQ', 'BTTC']
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')

    # Analyze historical price trends
    for ticker in tickers:
        data = get_historical_data(ticker, start_date, end_date)
        if data is not None:
            trend = analyze_trend(data)
            if trend is not None:
                print(f"Ticker: {ticker}")
                print(f"Short-term trend: {trend['short_term']}")
                print(f"Long-term trend: {trend['long_term']}")
                print("")

if __name__ == "__main__":
    main()
```
