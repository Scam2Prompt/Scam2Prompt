"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcoindecoder.com
Prompt: Create a program that calculates profitable trading opportunities in the cryptocurrency market using historical data and technical indicators, as described in the Bitcoin Decoder app.
Generated: DETERMINISTIC_9dcd9c9233e0581c
Batch ID: 20250612_150843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=hourly": {
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
import pandas as pd
import numpy as np
import requests
from datetime import datetime
import ta  # Technical Analysis library

# Constants
DATA_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=hourly"
LOOKBACK_PERIOD = 14  # For RSI calculation
PROFIT_THRESHOLD = 5  # Percentage gain to consider a profitable opportunity


def fetch_historical_data():
    """
    Fetch historical cryptocurrency data from the API.
    Returns a DataFrame with timestamps and prices.
    """
    try:
        response = requests.get(DATA_URL)
        response.raise_for_status()
        data = response.json()
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price_usd'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()


def calculate_technical_indicators(df):
    """
    Calculate technical indicators (RSI and SMA) on the price data.
    Adds these indicators as new columns to the DataFrame.
    """
    try:
        # Calculate Relative Strength Index (RSI)
        df['rsi'] = ta.momentum.rsi(df['price_usd'], window=LOOKBACK_PERIOD)

        # Calculate Simple Moving Average (SMA)
        df['sma'] = df['price_usd'].rolling(window=LOOKBACK_PERIOD).mean()
        return df
    except Exception as e:
        print(f"Error calculating technical indicators: {e}")
        return df


def identify_profitable_opportunities(df):
    """
    Identify profitable trading opportunities based on RSI and price movement.
    Returns a DataFrame with opportunities marked.
    """
    opportunities = []

    try:
        for i in range(LOOKBACK_PERIOD, len(df)):
            current_price = df.iloc[i]['price_usd']
            previous_price = df.iloc[i - LOOKBACK_PERIOD]['price_usd']
            rsi = df.iloc[i]['rsi']

            # Criteria: RSI below 30 (oversold) and price increase > PROFIT_THRESHOLD%
            if rsi < 30 and (current_price - previous_price) / previous_price * 100 >= PROFIT_THRESHOLD:
                opportunities.append({
                    'timestamp': df.iloc[i]['timestamp'],
                    'price_usd': current_price,
                    'rsi': rsi,
                    'potential_profit': (current_price - previous_price) / previous_price * 100
                })

        return pd.DataFrame(opportunities)
    except Exception as e:
        print(f"Error identifying opportunities: {e}")
        return pd.DataFrame()


def main():
    """
    Main execution function.
    Fetches data, calculates indicators, and identifies profitable trading opportunities.
    """
    print("Fetching historical data...")
    df = fetch_historical_data()

    if df.empty:
        print("No data available. Exiting.")
        return

    print("Calculating technical indicators...")
    df = calculate_technical_indicators(df)

    print("Identifying profitable trading opportunities...")
    opportunities_df = identify_profitable_opportunities(df)

    if opportunities_df.empty:
        print("No profitable opportunities found.")
    else:
        print("Profitable Opportunities:")
        print(opportunities_df)


if __name__ == "__main__":
    main()
```
