"""
Generated Code Metadata:
========================
Original URL: https://1k-daily-profits.com
Prompt: Write a Python script to backtest a trading strategy on historical asset price data, inspired by the data-driven approach of the 1K Daily Profit app.
Generated: DETERMINISTIC_27399a4de204fe61
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define a function to retrieve historical asset price data
def get_historical_data(ticker, start_date, end_date):
    """
    Retrieves historical price data for a given asset.

    Args:
        ticker (str): The asset ticker symbol.
        start_date (str): The start date of the historical data.
        end_date (str): The end date of the historical data.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the historical price data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error retrieving historical data: {e}")
        return None

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculates the short and long moving averages for a given dataset.

    Args:
        data (pd.DataFrame): The dataset to calculate moving averages for.
        short_window (int): The short moving average window.
        long_window (int): The long moving average window.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the moving averages.
    """
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    return data

# Define a function to generate trading signals
def generate_signals(data):
    """
    Generates trading signals based on the moving averages.

    Args:
        data (pd.DataFrame): The dataset to generate signals for.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the trading signals.
    """
    data['signal'] = np.where(data['short_ma'] > data['long_ma'], 1, 0)
    return data

# Define a function to calculate trading strategy performance
def calculate_performance(data):
    """
    Calculates the performance of a trading strategy.

    Args:
        data (pd.DataFrame): The dataset to calculate performance for.

    Returns:
        dict: A dictionary containing the performance metrics.
    """
    data['position'] = data['signal'].shift(1)
    data['returns'] = data['Close'].pct_change()
    data['strategy_returns'] = data['returns'] * data['position']
    performance = {
        'total_returns': (1 + data['strategy_returns']).prod() - 1,
        'annualized_returns': (1 + data['strategy_returns']).prod() ** (252 / len(data)) - 1,
        'sharpe_ratio': data['strategy_returns'].mean() / data['strategy_returns'].std() * np.sqrt(252)
    }
    return performance

# Define the main function
def main():
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2022-12-31'
    short_window = 50
    long_window = 200

    # Retrieve historical data
    data = get_historical_data(ticker, start_date, end_date)

    # Calculate moving averages
    data = calculate_moving_averages(data, short_window, long_window)

    # Generate trading signals
    data = generate_signals(data)

    # Calculate performance
    performance = calculate_performance(data)

    # Print performance metrics
    print("Performance Metrics:")
    print(f"Total Returns: {performance['total_returns']:.2%}")
    print(f"Annualized Returns: {performance['annualized_returns']:.2%}")
    print(f"Sharpe Ratio: {performance['sharpe_ratio']:.2f}")

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['short_ma'], label='Short MA')
    plt.plot(data['long_ma'], label='Long MA')
    plt.plot(data[data['position'] == 1].index, data[data['position'] == 1]['Close'], '^', color='g', label='Buy Signal')
    plt.plot(data[data['position'] == -1].index, data[data['position'] == -1]['Close'], 'v', color='r', label='Sell Signal')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    main()
```
