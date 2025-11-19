"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantera-etf.com
Prompt: What are some libraries for financial data analysis that could be useful for working with ETFs, as seen on pantera-etf.com?
Generated: DETERMINISTIC_f2be6ac3e5647fc2
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for financial data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm

# Function to fetch ETF data from Yahoo Finance
def fetch_etf_data(etf_symbol, start_date, end_date):
    """
    Fetch historical price data for the given ETF symbol.
    
    Parameters:
        etf_symbol (str): The ticker symbol of the ETF.
        start_date (str): Start date for fetching data in 'YYYY-MM-DD' format.
        end_date (str): End date for fetching data in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame containing historical price data.
    """
    try:
        etf_data = yf.download(etf_symbol, start=start_date, end=end_date)
        return etf_data
    except Exception as e:
        print(f"Error fetching data for {etf_symbol}: {e}")
        return None

# Function to calculate daily returns
def calculate_daily_returns(etf_data):
    """
    Calculate daily returns from the price data.
    
    Parameters:
        etf_data (pd.DataFrame): DataFrame containing historical price data.

    Returns:
        pd.Series: Series containing daily returns.
    """
    if etf_data is None or 'Adj Close' not in etf_data:
        print("Invalid ETF data provided for daily return calculation.")
        return None
    
    daily_returns = etf_data['Adj Close'].pct_change().dropna()
    return daily_returns

# Function to plot ETF performance
def plot_etf_performance(etf_data, etf_symbol):
    """
    Plot the adjusted close price of the ETF over time.
    
    Parameters:
        etf_data (pd.DataFrame): DataFrame containing historical price data.
        etf_symbol (str): The ticker symbol of the ETF.
    """
    if etf_data is None:
        print("No data to plot.")
        return
    
    plt.figure(figsize=(14, 7))
    plt.plot(etf_data.index, etf_data['Adj Close'], label=f'{etf_symbol} Adjusted Close Price')
    plt.title(f'{etf_symbol} Performance Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define the ETF symbol and date range
    etf_symbol = "SPY"  # Example: SPDR S&P 500 ETF Trust
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    
    # Fetch ETF data
    etf_data = fetch_etf_data(etf_symbol, start_date, end_date)
    
    # Calculate daily returns
    daily_returns = calculate_daily_returns(etf_data)
    
    # Print daily returns summary
    if daily_returns is not None:
        print(daily_returns.describe())
    
    # Plot ETF performance
    plot_etf_performance(etf_data, etf_symbol)
```
