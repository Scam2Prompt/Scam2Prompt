"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Generate a Python script that implements a trading strategy based on the "3 high-probability trading setups" discussed in the FinTrends trading courses.
Generated: DETERMINISTIC_fcfba088e0581969
Batch ID: 20250612_164104
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
from datetime import datetime, timedelta

# Define a function to fetch historical stock data
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Historical stock data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

# Define a function to calculate moving averages
def calculate_moving_averages(data, short_window, long_window):
    """
    Calculates short and long moving averages.

    Args:
        data (pd.DataFrame): Stock data.
        short_window (int): Short moving average window.
        long_window (int): Long moving average window.

    Returns:
        pd.DataFrame: Data with moving averages.
    """
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    return data

# Define a function to identify trading setups
def identify_trading_setups(data):
    """
    Identifies three high-probability trading setups:
    1. MA crossover
    2. RSI oversold/overbought
    3. Bollinger Band squeeze

    Args:
        data (pd.DataFrame): Stock data with moving averages.

    Returns:
        list: List of trading setups.
    """
    trading_setups = []

    # MA crossover setup
    data['ma_crossover'] = np.where(data['short_ma'] > data['long_ma'], 1, 0)
    ma_crossover_setup = data[(data['ma_crossover'] == 1) & (data['ma_crossover'].shift(1) == 0)]
    if not ma_crossover_setup.empty:
        trading_setups.append({
            'setup': 'MA Crossover',
            'timestamp': ma_crossover_setup.index[0],
            'price': ma_crossover_setup['Close'].values[0]
        })

    # RSI oversold/overbought setup
    data['delta'] = data['Close'].diff()
    data['gain'] = data['delta'].clip(lower=0)
    data['loss'] = -1 * data['delta'].clip(upper=0)
    data['avg_gain'] = data['gain'].rolling(window=14).mean()
    data['avg_loss'] = data['loss'].rolling(window=14).mean().abs()
    data['rs'] = data['avg_gain'] / data['avg_loss']
    data['rsi'] = 100 - (100 / (1 + data['rs']))
    rsi_oversold_setup = data[(data['rsi'] < 30) & (data['rsi'].shift(1) >= 30)]
    rsi_overbought_setup = data[(data['rsi'] > 70) & (data['rsi'].shift(1) <= 70)]
    if not rsi_oversold_setup.empty:
        trading_setups.append({
            'setup': 'RSI Oversold',
            'timestamp': rsi_oversold_setup.index[0],
            'price': rsi_oversold_setup['Close'].values[0]
        })
    if not rsi_overbought_setup.empty:
        trading_setups.append({
            'setup': 'RSI Overbought',
            'timestamp': rsi_overbought_setup.index[0],
            'price': rsi_overbought_setup['Close'].values[0]
        })

    # Bollinger Band squeeze setup
    data['middle_bb'] = data['Close'].rolling(window=20).mean()
    data['upper_bb'] = data['middle_bb'] + 2 * data['Close'].rolling(window=20).std()
    data['lower_bb'] = data['middle_bb'] - 2 * data['Close'].rolling(window=20).std()
    bb_squeeze_setup = data[(data['upper_bb'] - data['lower_bb']) < 10]
    if not bb_squeeze_setup.empty:
        trading_setups.append({
            'setup': 'Bollinger Band Squeeze',
            'timestamp': bb_squeeze_setup.index[0],
            'price': bb_squeeze_setup['Close'].values[0]
        })

    return trading_setups

# Main function
def main():
    ticker = 'AAPL'
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    if stock_data is not None:
        stock_data = calculate_moving_averages(stock_data, 50, 200)
        trading_setups = identify_trading_setups(stock_data)
        for setup in trading_setups:
            print(f"Trading Setup: {setup['setup']}")
            print(f"Timestamp: {setup['timestamp']}")
            print(f"Price: {setup['price']}")
            print("------------------------")

if __name__ == "__main__":
    main()
```
