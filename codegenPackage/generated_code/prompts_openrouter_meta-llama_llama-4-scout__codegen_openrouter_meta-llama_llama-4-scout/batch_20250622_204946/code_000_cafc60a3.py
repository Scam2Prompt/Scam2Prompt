"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Write a Python script to implement a simple Forex trading strategy using technical indicators, such as moving averages and RSI, for a beginner trader.
Generated: DETERMINISTIC_cafc60a3d17bb641
Batch ID: 20250622_204946
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

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short and long moving averages.

    Parameters:
    data (pandas.DataFrame): Historical price data
    short_window (int): Short moving average window
    long_window (int): Long moving average window

    Returns:
    pandas.DataFrame: Data with moving averages added
    """
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    return data

# Define a function to calculate RSI
def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).

    Parameters:
    data (pandas.DataFrame): Historical price data
    window (int): RSI window

    Returns:
    pandas.DataFrame: Data with RSI added
    """
    delta = data['Close'].diff().dropna()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(window).mean()
    roll_down = down.rolling(window).mean().abs()
    RS = roll_up / roll_down
    RSI = 100.0 - (100.0 / (1.0 + RS))
    data['RSI'] = RSI
    return data

# Define a function to generate trading signals
def generate_signals(data):
    """
    Generate trading signals based on moving averages and RSI.

    Parameters:
    data (pandas.DataFrame): Historical price data with indicators

    Returns:
    pandas.DataFrame: Data with trading signals added
    """
    data['signal'] = np.where((data['short_ma'] > data['long_ma']) & (data['RSI'] < 70), 1, 0)
    data['signal'] = np.where((data['short_ma'] < data['long_ma']) & (data['RSI'] > 30), -1, data['signal'])
    return data

# Define a function to backtest the strategy
def backtest_strategy(ticker, short_window, long_window):
    """
    Backtest the Forex trading strategy.

    Parameters:
    ticker (str): Currency pair ticker
    short_window (int): Short moving average window
    long_window (int): Long moving average window

    Returns:
    pandas.DataFrame: Backtested strategy performance
    """
    try:
        # Download historical data
        data = yf.download(ticker, period='1y')

        # Calculate moving averages and RSI
        data = calculate_moving_averages(data, short_window, long_window)
        data = calculate_rsi(data)

        # Generate trading signals
        data = generate_signals(data)

        # Calculate strategy performance
        data['position'] = data['signal'].diff()
        data['strategy_returns'] = data['position'].shift(1) * data['Close'].pct_change()
        data['cumulative_returns'] = (1 + data['strategy_returns']).cumprod()

        return data

    except Exception as e:
        print(f"Error backtesting strategy: {e}")
        return None

# Main function
def main():
    ticker = 'EURUSD=X'  # Currency pair ticker
    short_window = 50
    long_window = 200

    performance = backtest_strategy(ticker, short_window, long_window)
    if performance is not None:
        print(performance)

if __name__ == "__main__":
    main()
```
