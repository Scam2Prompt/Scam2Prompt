"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: Write code to visualize the growth and evolution of Iranian prop firms like Propiy and Fenefx, using historical data and features mentioned on Fundfa.
Generated: DETERMINISTIC_f14c426ecc3982f6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Define a function to fetch historical data from Fundfa
def fetch_historical_data(ticker, start_date, end_date):
    """
    Fetches historical data for a given ticker symbol from Fundfa.

    Args:
        ticker (str): Ticker symbol of the prop firm (e.g., Propiy, Fenefx)
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
        pandas.DataFrame: Historical data for the given ticker symbol
    """
    try:
        # Simulating data fetching (replace with actual API call or data source)
        data = {
            'Date': pd.date_range(start=start_date, end=end_date),
            'Close': np.random.uniform(100, 200, size=len(pd.date_range(start=start_date, end=end_date)))
        }
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error fetching historical data: {str(e)}")
        return None

# Define a function to calculate growth metrics
def calculate_growth_metrics(data):
    """
    Calculates growth metrics (e.g., cumulative growth, daily returns) for a given dataset.

    Args:
        data (pandas.DataFrame): Historical data for a prop firm

    Returns:
        dict: Growth metrics (cumulative growth, daily returns)
    """
    try:
        data['Daily_Returns'] = data['Close'].pct_change()
        cumulative_growth = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]
        return {
            'Cumulative_Growth': cumulative_growth,
            'Daily_Returns': data['Daily_Returns']
        }
    except Exception as e:
        print(f"Error calculating growth metrics: {str(e)}")
        return None

# Define a function to visualize growth and evolution
def visualize_growth(ticker, data, growth_metrics):
    """
    Visualizes the growth and evolution of a prop firm using historical data and growth metrics.

    Args:
        ticker (str): Ticker symbol of the prop firm (e.g., Propiy, Fenefx)
        data (pandas.DataFrame): Historical data for the prop firm
        growth_metrics (dict): Growth metrics (cumulative growth, daily returns)
    """
    try:
        plt.figure(figsize=(12, 6))

        # Plot historical close price
        plt.subplot(1, 2, 1)
        plt.plot(data['Date'], data['Close'])
        plt.title(f"Historical Close Price - {ticker}")
        plt.xlabel("Date")
        plt.ylabel("Close Price")

        # Plot daily returns
        plt.subplot(1, 2, 2)
        plt.plot(growth_metrics['Daily_Returns'])
        plt.title(f"Daily Returns - {ticker}")
        plt.xlabel("Date")
        plt.ylabel("Return")

        plt.tight_layout()
        plt.show()

        print(f"Cumulative Growth: {growth_metrics['Cumulative_Growth']:.2%}")
    except Exception as e:
        print(f"Error visualizing growth: {str(e)}")

# Main function
def main():
    tickers = ['Propiy', 'Fenefx']
    start_date = '2020-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')

    for ticker in tickers:
        data = fetch_historical_data(ticker, start_date, end_date)
        if data is not None:
            growth_metrics = calculate_growth_metrics(data)
            if growth_metrics is not None:
                visualize_growth(ticker, data, growth_metrics)

if __name__ == "__main__":
    main()
```
