"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Generate a high-probability trading setup using Trend Analysis and technical indicators, and provide a code example in Python for backtesting the strategy.
Generated: DETERMINISTIC_1ff9c089877759bc
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
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short and long moving averages.

    Parameters:
    data (pandas.Series): Closing prices
    short_window (int): Short window for MA
    long_window (int): Long window for MA

    Returns:
    short_ma (pandas.Series): Short moving average
    long_ma (pandas.Series): Long moving average
    """
    short_ma = data.rolling(window=short_window).mean()
    long_ma = data.rolling(window=long_window).mean()
    return short_ma, long_ma

# Define a function to calculate RSI
def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI).

    Parameters:
    data (pandas.Series): Closing prices
    window (int): Window for RSI calculation

    Returns:
    rsi (pandas.Series): RSI values
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
    data (pandas.DataFrame): Historical data with 'Close' column
    short_window (int): Short window for MA
    long_window (int): Long window for MA

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
    signals['signal'] = np.where((short_ma > long_ma) & (rsi < 70), 1, 0)
    # Generate sell signal
    signals['signal'] = np.where((short_ma < long_ma) & (rsi > 30), -1, signals['signal'])

    return signals

# Define a function to backtest the strategy
def backtest_strategy(ticker, short_window, long_window):
    """
    Backtest the trading strategy.

    Parameters:
    ticker (str): Stock ticker symbol
    short_window (int): Short window for MA
    long_window (int): Long window for MA

    Returns:
    results (pandas.DataFrame): Backtesting results
    """
    data = yf.download(ticker, period='1y')
    signals = generate_signals(data, short_window, long_window)

    # Initialize portfolio
    portfolio = pd.DataFrame(index=data.index)
    portfolio['positions'] = signals['signal']

    # Calculate portfolio value
    portfolio['positions_diff'] = portfolio['positions'].diff()
    portfolio['positions_diff'] = np.where(portfolio['positions_diff'].isnull(), 0, portfolio['positions_diff'])
    portfolio['positions_cum'] = portfolio['positions_diff'].cumsum()

    # Calculate returns
    portfolio['returns'] = data['Close'].pct_change() * portfolio['positions_cum'].shift(1)

    # Calculate cumulative returns
    portfolio['cumulative_returns'] = (1 + portfolio['returns']).cumprod()

    results = pd.DataFrame({
        'cumulative_returns': portfolio['cumulative_returns'],
        'benchmark': (1 + data['Close'].pct_change()).cumprod()
    })

    return results

# Example usage
if __name__ == '__main__':
    ticker = 'AAPL'
    short_window = 20
    long_window = 50

    try:
        results = backtest_strategy(ticker, short_window, long_window)
        plt.figure(figsize=(10,6))
        plt.plot(results['cumulative_returns'], label='Strategy')
        plt.plot(results['benchmark'], label='Benchmark')
        plt.title('Backtesting Results')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
```
