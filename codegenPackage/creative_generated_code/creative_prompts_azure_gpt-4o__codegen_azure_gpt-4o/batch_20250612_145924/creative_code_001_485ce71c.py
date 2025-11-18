"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: Generate a code snippet for implementing a currency strength meter in Python, referencing the tools and strategies outlined in FinTrends' trading packages.
Generated: DETERMINISTIC_485ce71c1a83b0d0
Batch ID: 20250612_145924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fintrends.com/forex_data": {
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

# Constants
API_URL = "https://api.fintrends.com/forex_data"  # Replace with actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key
CURRENCY_PAIRS = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF", "USDCAD"]
TIMEFRAME = "1h"  # Timeframe for data retrieval (e.g., 1h, 4h, 1d)

def fetch_forex_data(currency_pair, timeframe):
    """
    Fetches forex data from the specified API for a given currency pair and timeframe.
    
    Args:
        currency_pair (str): The currency pair to fetch data for (e.g., "EURUSD").
        timeframe (str): The timeframe for the forex data (e.g., "1h", "4h", "1d").

    Returns:
        pd.DataFrame: A DataFrame containing the forex data.
    """
    try:
        # Prepare the API request
        params = {"pair": currency_pair, "timeframe": timeframe, "api_key": API_KEY}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the response and convert to a pandas DataFrame
        data = response.json()
        df = pd.DataFrame(data["prices"], columns=["timestamp", "open", "high", "low", "close"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {currency_pair}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error

def calculate_relative_strength(df):
    """
    Calculates the relative strength index (RSI) for a given DataFrame of forex data.
    
    Args:
        df (pd.DataFrame): A DataFrame containing forex data with 'close' prices.

    Returns:
        float: The calculated RSI value.
    """
    try:
        # Compute price changes
        delta = df["close"].diff()
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        # Exponential moving averages for gains and losses
        avg_gain = pd.Series(gain).rolling(window=14).mean()
        avg_loss = pd.Series(loss).rolling(window=14).mean()

        # Avoid division by zero
        rs = avg_gain / (avg_loss + 1e-10)
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]  # Return the latest RSI value
    except Exception as e:
        print(f"Error calculating RSI: {e}")
        return None

def calculate_currency_strength(currencies):
    """
    Calculates currency strength for a list of currency pairs by analyzing RSI values.
    
    Args:
        currencies (list): A list of currency pairs to analyze.

    Returns:
        dict: A dictionary with currency pairs as keys and their strength as values.
    """
    strength = {}
    for pair in currencies:
        df = fetch_forex_data(pair, TIMEFRAME)
        if not df.empty:
            rsi = calculate_relative_strength(df)
            if rsi is not None:
                strength[pair] = rsi
            else:
                strength[pair] = "Error calculating RSI"
        else:
            strength[pair] = "Error fetching data"
    return strength

def main():
    """
    Main function to fetch data, calculate currency strength, and display results.
    """
    print("Calculating currency strength...")
    currency_strength = calculate_currency_strength(CURRENCY_PAIRS)
    print("Currency Strength Meter:")
    for pair, strength in currency_strength.items():
        print(f"{pair}: {strength if isinstance(strength, float) else strength}")

if __name__ == "__main__":
    main()
```
