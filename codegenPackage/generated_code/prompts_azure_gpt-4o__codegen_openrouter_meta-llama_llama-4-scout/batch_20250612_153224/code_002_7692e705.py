"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: Generate code to backtest price action trading strategies based on the MG Mentorship 2023 course listed on LearningAtCheap.com.
Generated: DETERMINISTIC_7692e705c5542572
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for backtesting price action trading strategies. However, I need to clarify that I don't have direct access to the MG Mentorship 2023 course materials. I'll provide a general implementation based on common price action trading strategies. 

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculate short and long moving averages.

    Args:
        data (pandas.DataFrame): Historical price data.
        short_window (int): Short moving average window.
        long_window (int): Long moving average window.

    Returns:
        pandas.DataFrame: Data with moving averages added.
    """
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    return data

# Define a function to generate trading signals
def generate_signals(data):
    """
    Generate trading signals based on price action.

    Args:
        data (pandas.DataFrame): Historical price data with moving averages.

    Returns:
        pandas.DataFrame: Data with trading signals added.
    """
    data['signal'] = np.where(data['short_ma'] > data['long_ma'], 1, 0)
    data['position'] = data['signal'].diff()
    return data

# Define a function to calculate trading performance
def calculate_performance(data):
    """
    Calculate trading performance metrics.

    Args:
        data (pandas.DataFrame): Historical price data with trading signals.

    Returns:
        dict: Trading performance metrics.
    """
    data['p/l'] = data['Close'].pct_change() * data['position'].shift(1)
    data['p/l_cum'] = (1 + data['p/l']).cumprod()
    performance = {
        'total_return': data['p/l_cum'].iloc[-1] - 1,
        'max_drawdown': data['p/l_cum'].cummax() - data['p/l_cum'].rolling(window=(data.shape[0])).apply(lambda x: (x.max() - x) / x.max(), raw=False).max(),
        'sharpe_ratio': data['p/l'].mean() / data['p/l'].std() * np.sqrt(252)
    }
    return performance

# Define a function to backtest a trading strategy
def backtest_strategy(ticker, short_window, long_window):
    """
    Backtest a price action trading strategy.

    Args:
        ticker (str): Stock ticker symbol.
        short_window (int): Short moving average window.
        long_window (int): Long moving average window.

    Returns:
        pandas.DataFrame: Historical price data with trading signals and performance metrics.
    """
    try:
        # Download historical price data
        data = yf.download(ticker, period='1y')

        # Calculate moving averages
        data = calculate_moving_averages(data, short_window, long_window)

        # Generate trading signals
        data = generate_signals(data)

        # Calculate trading performance
        performance = calculate_performance(data)

        # Plot trading performance
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Close Price')
        plt.plot(data['short_ma'], label='Short MA')
        plt.plot(data['long_ma'], label='Long MA')
        plt.plot(data[data['position'] == 1].index, data[data['position'] == 1]['Close'], '^', color='g', label='Buy Signal')
        plt.plot(data[data['position'] == -1].index, data[data['position'] == -1]['Close'], 'v', color='r', label='Sell Signal')
        plt.legend(loc='upper left')
        plt.show()

        return data, performance

    except Exception as e:
        print(f"Error backtesting strategy: {e}")
        return None, None

# Example usage
ticker = 'AAPL'
short_window = 50
long_window = 200
data, performance = backtest_strategy(ticker, short_window, long_window)
print(performance)
```
