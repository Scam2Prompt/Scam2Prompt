"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexscreener-web3.github.io
Prompt: Create a Python script that utilizes Dexscreener data to perform technical analysis on a trading pair, overlaying moving averages and volume indicators on a price chart.
Generated: DETERMINISTIC_ab5d67b03ba4bd0b
Batch ID: 20250612_153758
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dexscreener.com/latest/dex/pairs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
DEXSCREENER_API_URL = "https://api.dexscreener.com/latest/dex/pairs"
TRADING_PAIR = "ethereum/usdt"  # Example trading pair
MOVING_AVERAGE_SHORT = 20  # Short moving average period
MOVING_AVERAGE_LONG = 50   # Long moving average period

def fetch_price_data(pair: str):
    """
    Fetch price data for the given trading pair from Dexscreener API.
    
    Args:
        pair (str): The trading pair to fetch data for.
        
    Returns:
        pd.DataFrame: DataFrame containing price data.
    """
    try:
        response = requests.get(f"{DEXSCREENER_API_URL}/{pair}")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract relevant price data
        prices = data['pair']['priceHistory']
        df = pd.DataFrame(prices)
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        
        return df[['price', 'volume']]
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def calculate_moving_averages(df: pd.DataFrame, short_window: int, long_window: int):
    """
    Calculate short and long moving averages.
    
    Args:
        df (pd.DataFrame): DataFrame containing price data.
        short_window (int): Short moving average period.
        long_window (int): Long moving average period.
    
    Returns:
        pd.DataFrame: DataFrame with moving averages added.
    """
    df['MA_Short'] = df['price'].rolling(window=short_window).mean()
    df['MA_Long'] = df['price'].rolling(window=long_window).mean()
    return df

def plot_data(df: pd.DataFrame):
    """
    Plot price data along with moving averages and volume.
    
    Args:
        df (pd.DataFrame): DataFrame containing price data and moving averages.
    """
    if df.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(14, 7))

    # Plot price
    plt.subplot(2, 1, 1)
    plt.plot(df.index, df['price'], label='Price', color='blue', alpha=0.5)
    plt.plot(df.index, df['MA_Short'], label=f'MA {MOVING_AVERAGE_SHORT}', color='red', linestyle='--')
    plt.plot(df.index, df['MA_Long'], label=f'MA {MOVING_AVERAGE_LONG}', color='green', linestyle='--')
    plt.title(f'{TRADING_PAIR} Price Chart with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()

    # Plot volume
    plt.subplot(2, 1, 2)
    plt.bar(df.index, df['volume'], color='gray', alpha=0.5)
    plt.title('Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid()

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the script.
    """
    price_data = fetch_price_data(TRADING_PAIR)
    price_data = calculate_moving_averages(price_data, MOVING_AVERAGE_SHORT, MOVING_AVERAGE_LONG)
    plot_data(price_data)

if __name__ == "__main__":
    main()
```
