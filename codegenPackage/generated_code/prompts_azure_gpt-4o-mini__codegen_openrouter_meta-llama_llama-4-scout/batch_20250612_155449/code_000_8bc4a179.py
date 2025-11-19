"""
Generated Code Metadata:
========================
Original URL: https://suistrategies.com
Prompt: Generate a Python script that analyzes a cryptocurrency portfolio based on the investment strategy outlined for SUI, APT, SOL, and BTC from 2024 to 2026.
Generated: DETERMINISTIC_8bc4a179867f88d2
Batch ID: 20250612_155449
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
from datetime import datetime

# Define a function to retrieve historical data for a given ticker
def get_historical_data(ticker, start_date, end_date):
    """
    Retrieves historical data for a given ticker.

    Args:
    - ticker (str): The ticker symbol of the cryptocurrency.
    - start_date (str): The start date of the period in 'YYYY-MM-DD' format.
    - end_date (str): The end date of the period in 'YYYY-MM-DD' format.

    Returns:
    - pd.DataFrame: A DataFrame containing the historical data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Failed to retrieve data for {ticker}: {e}")
        return None

# Define a function to calculate portfolio performance
def calculate_portfolio_performance(data_dict):
    """
    Calculates the performance of a portfolio.

    Args:
    - data_dict (dict): A dictionary where keys are ticker symbols and values are DataFrames.

    Returns:
    - dict: A dictionary containing the portfolio performance metrics.
    """
    portfolio_performance = {}
    for ticker, data in data_dict.items():
        if data is not None:
            # Calculate daily returns
            data['Return'] = data['Close'].pct_change()
            # Calculate average return
            avg_return = data['Return'].mean() * 365  # Annualized
            # Calculate volatility (standard deviation of returns)
            volatility = data['Return'].std() * (365 ** 0.5)  # Annualized
            portfolio_performance[ticker] = {
                'Average Return': avg_return,
                'Volatility': volatility,
                'Final Price': data['Close'].iloc[-1]
            }
    return portfolio_performance

# Define main function
def analyze_portfolio():
    # Define investment strategy parameters
    tickers = ['SUI', 'APT', 'SOL', 'BTC']
    start_date = '2024-01-01'
    end_date = '2026-12-31'

    # Retrieve historical data
    data_dict = {}
    for ticker in tickers:
        data = get_historical_data(ticker, start_date, end_date)
        data_dict[ticker] = data

    # Calculate portfolio performance
    portfolio_performance = calculate_portfolio_performance(data_dict)

    # Print portfolio performance
    for ticker, performance in portfolio_performance.items():
        print(f"Performance Metrics for {ticker}:")
        for metric, value in performance.items():
            print(f"- {metric}: {value:.4f}")
        print()

# Run the main function
if __name__ == "__main__":
    analyze_portfolio()
```
