"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qiananjs.com
Prompt: Generate code to calculate and visualize pivot points for forex pairs like GBP/USD and USD/CNY using FXCG's trading data and integrate it with the MT4 platform.
Generated: DETERMINISTIC_2cac45433cca68d8
Batch ID: 20250612_154651
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
from datetime import datetime
import MetaTrader5 as mt5

# Initialize MetaTrader 5 connection
if not mt5.initialize():
    print("Initialize failed, error code =", mt5.last_error())
    quit()

def fetch_fx_data(symbol, timeframe, num_bars):
    """
    Fetch historical trading data for a specific forex pair.

    :param symbol: Forex pair symbol (e.g., 'GBPUSD', 'USDCNY')
    :param timeframe: Timeframe for historical data (e.g., mt5.TIMEFRAME_H1)
    :param num_bars: Number of bars to fetch
    :return: DataFrame containing the open, high, low, close prices
    """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    if rates is None:
        print(f"Failed to fetch data for {symbol}, error code =", mt5.last_error())
        return None
    return pd.DataFrame(rates)

def calculate_pivot_points(df):
    """
    Calculate pivot points, support, and resistance levels.

    :param df: DataFrame containing 'open', 'high', 'low', 'close' columns
    :return: DataFrame with pivot points and levels added
    """
    pivot_point = (df['high'] + df['low'] + df['close']) / 3
    support1 = (2 * pivot_point) - df['high']
    support2 = pivot_point - (df['high'] - df['low'])
    resistance1 = (2 * pivot_point) - df['low']
    resistance2 = pivot_point + (df['high'] - df['low'])

    df['Pivot'] = pivot_point
    df['Support1'] = support1
    df['Support2'] = support2
    df['Resistance1'] = resistance1
    df['Resistance2'] = resistance2
    
    return df

def visualize_pivot_points(df, symbol):
    """
    Visualize pivot points along with historical prices.

    :param df: DataFrame containing pivot points and price data
    :param symbol: Forex pair symbol
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df['time'], df['close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(df['time'], df['Pivot'], label='Pivot Point', color='yellow', linestyle='--')
    plt.plot(df['time'], df['Support1'], label='Support 1', color='red', linestyle='--')
    plt.plot(df['time'], df['Support2'], label='Support 2', color='darkred', linestyle='--')
    plt.plot(df['time'], df['Resistance1'], label='Resistance 1', color='green', linestyle='--')
    plt.plot(df['time'], df['Resistance2'], label='Resistance 2', color='darkgreen', linestyle='--')

    plt.title(f'Pivot Points for {symbol}')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Parameters
    symbol = 'GBPUSD'  # Change to desired forex pair
    timeframe = mt5.TIMEFRAME_H1  # 1-hour timeframe
    num_bars = 500  # Number of bars to fetch

    # Fetch data
    df = fetch_fx_data(symbol, timeframe, num_bars)
    if df is None:
        return

    # Convert time to datetime format and set as index
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)

    # Calculate pivot points
    df = calculate_pivot_points(df)

    # Visualize pivot points
    visualize_pivot_points(df, symbol)

    # Shutdown MT5 connection
    mt5.shutdown()

if __name__ == "__main__":
    main()
```
