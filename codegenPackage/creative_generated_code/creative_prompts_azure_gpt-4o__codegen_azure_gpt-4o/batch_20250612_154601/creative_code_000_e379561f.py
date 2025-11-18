"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Write Python code using a trading API to analyze CFD price movements for stocks, indices, and cryptocurrencies, incorporating advanced analytical tools similar to those described on Emarlado's platform.
Generated: DETERMINISTIC_e379561fc3520fea
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-trading-api.com": {
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
import numpy as np
from datetime import datetime, timedelta

# Constants for API access
API_URL = "https://example-trading-api.com"
API_KEY = "your-api-key-here"

# Symbols to analyze (stocks, indices, cryptocurrencies)
SYMBOLS = ["AAPL", "SPX500", "BTCUSD"]

# Timeframe for historical data
TIMEFRAME = "1h"  # Options: '1h', '4h', '1d', etc.
DATA_PERIOD = 100  # Number of data points to retrieve

# Advanced analytical tools configuration
MOVING_AVERAGES = [10, 50]  # Short-term and long-term moving averages
RSI_PERIOD = 14  # Relative Strength Index (RSI) period

# Error handling for API requests
def fetch_price_data(symbol, timeframe, data_period):
    """
    Fetch historical price data for a given symbol, timeframe, and period.

    Parameters:
        symbol (str): Trading symbol (e.g., AAPL, SPX500, BTCUSD).
        timeframe (str): Timeframe for historical data (e.g., '1h', '1d').
        data_period (int): Number of data points to retrieve.

    Returns:
        pd.DataFrame: DataFrame containing historical price data.
    """
    try:
        url = f"{API_URL}/prices"
        params = {
            "symbol": symbol,
            "timeframe": timeframe,
            "count": data_period,
            "apikey": API_KEY
        }
        response = requests.get(url, params=params)

        # Raise an exception if the request fails
        response.raise_for_status()

        # Convert the JSON response to a DataFrame
        data = response.json()
        return pd.DataFrame(data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

def calculate_moving_average(data, periods):
    """
    Calculate moving averages for the given periods.

    Parameters:
        data (pd.DataFrame): Historical price data with a 'close' column.
        periods (list): List of periods for moving averages.

    Returns:
        pd.DataFrame: DataFrame with moving average columns added.
    """
    for period in periods:
        data[f"MA_{period}"] = data['close'].rolling(window=period).mean()
    return data

def calculate_rsi(data, period):
    """
    Calculate Relative Strength Index (RSI) for the given period.

    Parameters:
        data (pd.DataFrame): Historical price data with a 'close' column.
        period (int): Period for RSI calculation.

    Returns:
        pd.Series: Series containing RSI values.
    """
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    # Avoid division by zero
    loss.replace(0, np.nan, inplace=True)

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def analyze_prices(symbol):
    """
    Perform price analysis for a given trading symbol.

    Parameters:
        symbol (str): Trading symbol (e.g., AAPL, SPX500, BTCUSD).

    Returns:
        pd.DataFrame: DataFrame with analytical data added.
    """
    # Fetch historical price data
    data = fetch_price_data(symbol, TIMEFRAME, DATA_PERIOD)

    if data.empty:
        print(f"No data available for {symbol}. Skipping analysis.")
        return data

    # Ensure data is sorted by time
    data['time'] = pd.to_datetime(data['time'])
    data.sort_values('time', inplace=True)

    # Add moving averages
    data = calculate_moving_average(data, MOVING_AVERAGES)

    # Add RSI
    data['RSI'] = calculate_rsi(data, RSI_PERIOD)

    # Add column for simple trend direction
    data['Trend'] = np.where(data['MA_10'] > data['MA_50'], 'Uptrend', 'Downtrend')

    return data

def main():
    """
    Main function to execute price analysis for all symbols.
    """
    print("Starting price analysis...")
    for symbol in SYMBOLS:
        print(f"Analyzing {symbol}...")
        analyzed_data = analyze_prices(symbol)

        if not analyzed_data.empty:
            print(f"Analysis for {symbol} complete.")
            print(analyzed_data.tail())  # Display last few rows of data

        print("-" * 40)

if __name__ == "__main__":
    main()
```
