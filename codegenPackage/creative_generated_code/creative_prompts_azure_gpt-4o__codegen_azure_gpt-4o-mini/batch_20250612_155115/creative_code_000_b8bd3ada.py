"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Write Python code to analyze and visualize the performance history of stocks and bonds for portfolio diversification, incorporating strategies mentioned on Investolazlo.
Generated: DETERMINISTIC_b8bd3ada79f51203
Batch ID: 20250612_155115
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
import seaborn as sns
import yfinance as yf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def fetch_data(tickers, start_date, end_date):
    """
    Fetch historical stock and bond data from Yahoo Finance.

    :param tickers: List of ticker symbols.
    :param start_date: Start date for the data retrieval.
    :param end_date: End date for the data retrieval.
    :return: DataFrame containing historical prices.
    """
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        logging.info("Data fetched successfully for tickers: %s", tickers)
        return data
    except Exception as e:
        logging.error("Error fetching data: %s", e)
        raise


def calculate_returns(data):
    """
    Calculate daily returns from price data.

    :param data: DataFrame of price data.
    :return: DataFrame of daily returns.
    """
    returns = data.pct_change().dropna()
    logging.info("Daily returns calculated.")
    return returns


def visualize_returns(returns):
    """
    Visualize returns using a heatmap and line plot.

    :param returns: DataFrame of daily returns.
    """
    plt.figure(figsize=(12, 6))
    
    # Heatmap of correlation
    plt.subplot(1, 2, 1)
    sns.heatmap(returns.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Returns Correlation Heatmap')

    # Line plot of cumulative returns
    cumulative_returns = (1 + returns).cumprod() - 1
    plt.subplot(1, 2, 2)
    cumulative_returns.plot(title='Cumulative Returns', fontsize=12)
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    
    plt.tight_layout()
    plt.show()
    logging.info("Visualization completed.")


def main():
    # Define tickers for analysis (example: S&P 500 ETF and a bond ETF)
    tickers = ['SPY', 'BND']
    start_date = '2020-01-01'
    end_date = '2023-10-01'

    # Fetch data
    try:
        price_data = fetch_data(tickers, start_date, end_date)

        # Calculate returns
        returns = calculate_returns(price_data)

        # Visualize returns
        visualize_returns(returns)

    except Exception as e:
        logging.error("An error occurred in the main execution: %s", e)


if __name__ == "__main__":
    main()
```
