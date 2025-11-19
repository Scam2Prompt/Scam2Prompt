"""
Generated Code Metadata:
========================
Original URL: https://www.stcinversiones.com.ar
Prompt: Develop a Python script to analyze historical data from BYMA and MATba-Rofex for designing personalized investment strategies, as STC Inversiones specializes in.
Generated: DETERMINISTIC_1e28b44ccd2d387e
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Define constants
BYMA_TICKER = 'BYMA.SA'
MATBA_ROFEX_TICKER = 'MATB3.SA'

def fetch_historical_data(ticker, start_date, end_date):
    """
    Fetch historical data for a given ticker and date range.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Historical data for the given ticker and date range.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None

def calculate_daily_returns(data):
    """
    Calculate daily returns for a given dataset.

    Args:
        data (pd.DataFrame): Historical data.

    Returns:
        pd.Series: Daily returns.
    """
    returns = data['Close'].pct_change()
    return returns

def calculate_mean_and_std(returns):
    """
    Calculate mean and standard deviation of returns.

    Args:
        returns (pd.Series): Daily returns.

    Returns:
        tuple: Mean and standard deviation of returns.
    """
    mean_return = returns.mean()
    std_dev = returns.std()
    return mean_return, std_dev

def plot_returns(returns, ticker):
    """
    Plot daily returns for a given ticker.

    Args:
        returns (pd.Series): Daily returns.
        ticker (str): Stock ticker symbol.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(returns)
    plt.title(f'Daily Returns for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.show()

def main():
    # Define date range
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

    # Fetch historical data
    byma_data = fetch_historical_data(BYMA_TICKER, start_date, end_date)
    matba_rofex_data = fetch_historical_data(MATBA_ROFEX_TICKER, start_date, end_date)

    if byma_data is not None and matba_rofex_data is not None:
        # Calculate daily returns
        byma_returns = calculate_daily_returns(byma_data)
        matba_rofex_returns = calculate_daily_returns(matba_rofex_data)

        # Calculate mean and standard deviation of returns
        byma_mean, byma_std = calculate_mean_and_std(byma_returns)
        matba_rofex_mean, matba_rofex_std = calculate_mean_and_std(matba_rofex_returns)

        # Print results
        print(f"BYMA Mean Return: {byma_mean:.4f}, Std Dev: {byma_std:.4f}")
        print(f"MATba-Rofex Mean Return: {matba_rofex_mean:.4f}, Std Dev: {matba_rofex_std:.4f}")

        # Plot returns
        plot_returns(byma_returns, BYMA_TICKER)
        plot_returns(matba_rofex_returns, MATBA_ROFEX_TICKER)

if __name__ == "__main__":
    main()
```
