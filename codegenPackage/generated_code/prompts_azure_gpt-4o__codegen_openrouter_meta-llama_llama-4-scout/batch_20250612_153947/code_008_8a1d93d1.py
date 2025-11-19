"""
Generated Code Metadata:
========================
Original URL: https://crypstocks.co
Prompt: Create a Python script to analyze the effectiveness of past crypto investment strategies, inspired by Crypstocks' historical performance tracking.
Generated: DETERMINISTIC_8a1d93d104422f28
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_strategy_analyzer.py

import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime

def fetch_historical_data(ticker, start_date, end_date):
    """
    Fetch historical market data for a given ticker symbol.

    Args:
        ticker (str): Ticker symbol (e.g., BTC-USD)
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
        pd.DataFrame: Historical market data
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

def calculate_strategy_performance(data, strategy):
    """
    Calculate performance metrics for a given strategy.

    Args:
        data (pd.DataFrame): Historical market data
        strategy (dict): Strategy parameters (e.g., {'type': 'moving_average', 'short_window': 20, 'long_window': 50})

    Returns:
        dict: Performance metrics (e.g., {'returns': 0.1, 'sharpe_ratio': 1.2})
    """
    try:
        if strategy['type'] == 'moving_average':
            data['short_ma'] = data['Close'].rolling(window=strategy['short_window']).mean()
            data['long_ma'] = data['Close'].rolling(window=strategy['long_window']).mean()
            data['signal'] = np.where(data['short_ma'] > data['long_ma'], 1, 0)
            data['position'] = data['signal'].diff()
            data['returns'] = data['Close'].pct_change() * data['position']
            performance = {
                'returns': data['returns'].sum(),
                'sharpe_ratio': data['returns'].mean() / data['returns'].std() * np.sqrt(252)
            }
            return performance
        else:
            raise ValueError("Unsupported strategy type")
    except Exception as e:
        print(f"Error calculating strategy performance: {e}")
        return None

def analyze_strategy(ticker, start_date, end_date, strategy):
    """
    Analyze the effectiveness of a crypto investment strategy.

    Args:
        ticker (str): Ticker symbol (e.g., BTC-USD)
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        strategy (dict): Strategy parameters (e.g., {'type': 'moving_average', 'short_window': 20, 'long_window': 50})

    Returns:
        dict: Performance metrics (e.g., {'returns': 0.1, 'sharpe_ratio': 1.2})
    """
    data = fetch_historical_data(ticker, start_date, end_date)
    if data is not None:
        performance = calculate_strategy_performance(data, strategy)
        return performance
    else:
        return None

def main():
    ticker = 'BTC-USD'
    start_date = '2020-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')
    strategy = {
        'type': 'moving_average',
        'short_window': 20,
        'long_window': 50
    }
    performance = analyze_strategy(ticker, start_date, end_date, strategy)
    if performance is not None:
        print("Strategy Performance:")
        print(f"Returns: {performance['returns']:.2f}")
        print(f"Sharpe Ratio: {performance['sharpe_ratio']:.2f}")
    else:
        print("Failed to analyze strategy")

if __name__ == "__main__":
    main()
```
