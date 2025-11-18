"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techbinance.com
Prompt: Generate a script to analyze historical Bitcoin price data using a library like Pandas, incorporating ideas from Tech Binance's coverage of Bitcoin's global impact.
Generated: DETERMINISTIC_e73331f64bc43c38
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coindesk.com/v1/bpi/historical/close.json": {
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
import matplotlib.pyplot as plt
from datetime import datetime
import requests

# Constants for API endpoint and the Bitcoin historical price data
API_URL = "https://api.coindesk.com/v1/bpi/historical/close.json"
CURRENCY = "USD"

def fetch_bitcoin_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch historical Bitcoin price data from the Coindesk API.

    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: DataFrame containing Bitcoin prices
    """
    try:
        response = requests.get(API_URL, params={"start": start_date, "end": end_date, "currency": CURRENCY})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return pd.DataFrame(list(data['bpi'].items()), columns=['Date', 'Price'])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def analyze_bitcoin_data(df: pd.DataFrame) -> None:
    """
    Analyze Bitcoin price data and plot the results.

    :param df: DataFrame containing Bitcoin prices
    """
    if df.empty:
        print("No data to analyze.")
        return

    # Convert 'Date' to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Calculate rolling mean (30-day window)
    df['Rolling Mean'] = df['Price'].rolling(window=30).mean()

    # Plotting Bitcoin price and its rolling mean
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['Price'], label='Bitcoin Price', color='blue')
    plt.plot(df.index, df['Rolling Mean'], label='30-Day Rolling Mean', color='orange')
    plt.title("Historical Bitcoin Prices")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to execute the Bitcoin analysis.
    """
    # Define date range for the analysis
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # Fetch and analyze Bitcoin data
    bitcoin_data = fetch_bitcoin_data(start_date, end_date)
    analyze_bitcoin_data(bitcoin_data)

if __name__ == "__main__":
    main()
```
