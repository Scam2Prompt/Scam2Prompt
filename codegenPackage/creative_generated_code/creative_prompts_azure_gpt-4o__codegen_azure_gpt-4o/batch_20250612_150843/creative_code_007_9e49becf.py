"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bittorrentcode.com
Prompt: Write a Python script to evaluate cryptocurrency market volatility and identify potentially profitable trading opportunities, inspired by the BitTorrent Code app's approach.
Generated: DETERMINISTIC_9e49becfa1d8492d
Batch ID: 20250612_150843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/markets": {
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
API_URL = 'https://api.coingecko.com/api/v3/coins/markets'
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,  # Number of cryptocurrencies to fetch
    'page': 1,
    'sparkline': True  # Include 7-day historical data
}

# Function to fetch data from CoinGecko API
def fetch_market_data():
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching market data: {e}")
        return None

# Function to calculate volatility (standard deviation of price changes)
def calculate_volatility(prices):
    try:
        if not prices or len(prices) < 2:
            raise ValueError("Insufficient price data to calculate volatility.")
        returns = np.diff(prices) / prices[:-1]  # Calculate daily returns
        return np.std(returns)  # Standard deviation of returns
    except Exception as e:
        print(f"Error calculating volatility: {e}")
        return None

# Function to identify trading opportunities based on volatility
def identify_opportunities(data):
    opportunities = []
    for coin in data:
        try:
            sparkline_prices = coin.get('sparkline_in_7d', {}).get('price', [])
            if not sparkline_prices:
                continue
            volatility = calculate_volatility(sparkline_prices)
            if volatility is not None and volatility > 0.05:  # Threshold for high volatility
                opportunities.append({
                    'name': coin['name'],
                    'symbol': coin['symbol'],
                    'volatility': volatility,
                    'current_price': coin['current_price']
                })
        except KeyError as e:
            print(f"Missing data for coin: {e}")
    return opportunities

# Main function
def main():
    print("Fetching cryptocurrency market data...")
    market_data = fetch_market_data()
    if market_data is None:
        print("Unable to retrieve market data. Exiting.")
        return

    print("Analyzing market volatility...")
    opportunities = identify_opportunities(market_data)

    if opportunities:
        print(f"Found {len(opportunities)} opportunities:")
        df = pd.DataFrame(opportunities)
        print(df.sort_values(by='volatility', ascending=False))
    else:
        print("No profitable trading opportunities identified.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
