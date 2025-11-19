"""
Generated Code Metadata:
========================
Original URL: https://diamondtradingfx.com
Prompt: Develop a simple trading strategy using technical indicators for predicting the direction of financial market movements, specifically for beginners.
Generated: DETERMINISTIC_a971b49473541e44
Batch ID: 20250622_205459
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
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short and long moving averages.

    Parameters:
    data (pandas.Series): Closing prices of a stock
    short_window (int): Short window for moving average
    long_window (int): Long window for moving average

    Returns:
    short_ma (pandas.Series): Short moving average
    long_ma (pandas.Series): Long moving average
    """
    short_ma = data.rolling(window=short_window).mean()
    long_ma = data.rolling(window=long_window).mean()
    return short_ma, long_ma

# Define a function to calculate Relative Strength Index (RSI)
def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).

    Parameters:
    data (pandas.Series): Closing prices of a stock
    window (int): Window for RSI calculation

    Returns:
    rsi (pandas.Series): Relative Strength Index
    """
    delta = data.diff().dropna()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(window).mean()
    roll_down = down.rolling(window).mean().abs()
    RS = roll_up / roll_down
    RSI = 100.0 - (100.0 / (1.0 + RS))
    return RSI

# Define a function to generate trading signals
def generate_signals(data, short_window, long_window):
    """
    Generate trading signals based on moving averages and RSI.

    Parameters:
    data (pandas.DataFrame): Stock data with 'Close' column
    short_window (int): Short window for moving average
    long_window (int): Long window for moving average

    Returns:
    signals (pandas.DataFrame): Trading signals
    """
    close_prices = data['Close']
    short_ma, long_ma = calculate_moving_averages(close_prices, short_window, long_window)
    rsi = calculate_rsi(close_prices)

    signals = pd.DataFrame(index=data.index)
    signals['short_ma'] = short_ma
    signals['long_ma'] = long_ma
    signals['rsi'] = rsi

    # Generate buy signal
    signals['signal'] = 0.0
    signals.loc[(short_ma > long_ma) & (rsi < 70), 'signal'] = 1.0

    # Generate sell signal
    signals.loc[(short_ma < long_ma) & (rsi > 30), 'signal'] = -1.0

    return signals

# Define a function to backtest the trading strategy
def backtest_strategy(ticker, short_window, long_window):
    """
    Backtest the trading strategy.

    Parameters:
    ticker (str): Stock ticker symbol
    short_window (int): Short window for moving average
    long_window (int): Long window for moving average

    Returns:
    performance (pandas.DataFrame): Strategy performance
    """
    try:
        data = yf.download(ticker, period='1y')
        signals = generate_signals(data, short_window, long_window)

        # Calculate strategy performance
        data['position'] = signals['signal'].shift(1)
        data['strategy'] = data['Close'] * data['position']
        data['pnl'] = data['strategy'].diff()

        performance = data[['Close', 'position', 'strategy', 'pnl']]

        return performance

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    ticker = 'AAPL'
    short_window = 20
    long_window = 50

    performance = backtest_strategy(ticker, short_window, long_window)

    if performance is not None:
        print(performance)

        # Plot the strategy performance
        plt.figure(figsize=(12,6))
        plt.plot(performance['Close'], label='Close Price')
        plt.plot(performance['strategy'], label='Strategy')
        plt.legend(loc='upper left')
        plt.show()
```
