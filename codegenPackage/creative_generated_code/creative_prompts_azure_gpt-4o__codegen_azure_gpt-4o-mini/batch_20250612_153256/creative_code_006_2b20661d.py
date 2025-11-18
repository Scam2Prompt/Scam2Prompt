"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstmemes.com
Prompt: Create a Python script to track and visualize the performance of meme coins mentioned on Wall Street Memes, such as $WSM.
Generated: DETERMINISTIC_2b20661da3e98b5e
Batch ID: 20250612_153256
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range": {
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
from datetime import datetime, timedelta

# Constants
API_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = ["wsm"]  # List of meme coins (in lowercase format for CoinGecko)
CURRENCY = "usd"  # Currency for price tracking
DAYS = 30  # Number of days for historical data

# Function to fetch current price of meme coins
def fetch_current_prices(coins, currency):
    try:
        response = requests.get(API_URL, params={"ids": ','.join(coins), "vs_currencies": currency})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current prices: {e}")
        return None

# Function to fetch historical price data of meme coins
def fetch_historical_prices(coin, days, currency):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range",
                                params={"vs_currency": currency,
                                        "from": start_date.timestamp(),
                                        "to": end_date.timestamp()})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical prices for {coin}: {e}")
        return None

# Function to visualize price data
def visualize_prices(coin, historical_data):
    # Extracting prices and timestamps
    prices = historical_data['prices']
    timestamps = [datetime.fromtimestamp(price[0] / 1000) for price in prices]
    values = [price[1] for price in prices]

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, values, label=f"{coin.upper()} Price", color='blue')
    plt.title(f"{coin.upper()} Price Over the Last {DAYS} Days")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function to run the script
def main():
    # Fetch current prices
    current_prices = fetch_current_prices(COINS, CURRENCY)
    if current_prices:
        print(f"Current Prices: {current_prices}")

    # Fetch historical prices for each coin
    for coin in COINS:
        historical_data = fetch_historical_prices(coin, DAYS, CURRENCY)
        if historical_data:
            visualize_prices(coin, historical_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
