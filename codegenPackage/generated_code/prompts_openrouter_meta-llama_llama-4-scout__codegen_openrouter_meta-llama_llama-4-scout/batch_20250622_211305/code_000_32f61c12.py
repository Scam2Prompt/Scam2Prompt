"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoinboom.com
Prompt: Write a Python script that implements a basic trading algorithm using historical price data and technical indicators, similar to the Bitcoin Boom app's analysis features.
Generated: DETERMINISTIC_32f61c12c1747e49
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import yfinance as yf
import numpy as np

# Define a function to calculate the moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short and long moving averages.

    Parameters:
    data (pandas.DataFrame): Historical price data.
    short_window (int): Short window for moving average.
    long_window (int): Long window for moving average.

    Returns:
    pandas.DataFrame: Data with moving averages added.
    """
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    return data

# Define a function to calculate the Relative Strength Index (RSI)
def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).

    Parameters:
    data (pandas.DataFrame): Historical price data.
    window (int): Window for RSI calculation.

    Returns:
    pandas.DataFrame: Data with RSI added.
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
    data (pandas.DataFrame): Historical price data with indicators.

    Returns:
    pandas.DataFrame: Data with trading signals added.
    """
    data['signal'] = np.where((data['short_ma'] > data['long_ma']) & (data['RSI'] < 70), 1, 0)
    data['signal'] = np.where((data['short_ma'] < data['long_ma']) & (data['RSI'] > 30), -1, data['signal'])
    return data

# Define a function to backtest the trading strategy
def backtest_strategy(data):
    """
    Backtest the trading strategy.

    Parameters:
    data (pandas.DataFrame): Historical price data with trading signals.

    Returns:
    float: Total return of the strategy.
    """
    data['position'] = data['signal'].diff()
    data['position'] = data['position'].fillna(0)
    data['strategy_returns'] = data['position'].shift(1) * data['Close'].pct_change()
    data['strategy_returns'] = data['strategy_returns'].fillna(0)
    total_return = (1 + data['strategy_returns']).cumprod().iloc[-1]
    return total_return

# Main function
def main():
    try:
        # Download historical price data
        ticker = yf.Ticker("BTC-USD")
        data = ticker.history(period="1y")

        # Calculate moving averages
        data = calculate_moving_averages(data, short_window=20, long_window=50)

        # Calculate RSI
        data = calculate_rsi(data)

        # Generate trading signals
        data = generate_signals(data)

        # Backtest the strategy
        total_return = backtest_strategy(data)

        print(f"Total return of the strategy: {total_return:.2%}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
