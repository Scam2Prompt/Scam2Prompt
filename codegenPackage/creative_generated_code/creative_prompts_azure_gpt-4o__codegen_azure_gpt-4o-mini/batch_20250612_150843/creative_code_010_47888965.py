"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-proair-500.com
Prompt: Write a script to calculate and display comprehensive insights on cryptocurrency market trends, leveraging AI and algorithms for real-time analysis, inspired by the Trade Pro Air 500 app.
Generated: DETERMINISTIC_478889650f03229d
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Constants for API and time window
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
CURRENCY = "usd"
LIMIT = 100  # Number of coins to fetch
TIME_WINDOW_DAYS = 30  # Look back period for trends

def fetch_market_data():
    """Fetches cryptocurrency market data from the CoinGecko API."""
    try:
        response = requests.get(API_URL, params={'vs_currency': CURRENCY, 'order': 'market_cap_desc', 'per_page': LIMIT, 'page': 1, 'sparkline': 'false'})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return []

def calculate_trends(market_data):
    """Calculates market trends based on fetched data.
    
    Args:
        market_data (list): List of cryptocurrency market data.
        
    Returns:
        pd.DataFrame: DataFrame containing trend insights.
    """
    trends = []
    
    for coin in market_data:
        price_change_percentage_24h = coin.get('price_change_percentage_24h', 0)
        market_cap_change_percentage_24h = coin.get('market_cap_change_percentage_24h', 0)
        trends.append({
            "name": coin['name'],
            "symbol": coin['symbol'],
            "current_price": coin['current_price'],
            "price_change_percentage_24h": price_change_percentage_24h,
            "market_cap_change_percentage_24h": market_cap_change_percentage_24h
        })
    
    return pd.DataFrame(trends)

def plot_trends(trends_df):
    """Plots market trends for selected cryptocurrencies.
    
    Args:
        trends_df (pd.DataFrame): DataFrame containing trend insights.
    """
    plt.figure(figsize=(12, 6))
    plt.bar(trends_df['name'], trends_df['price_change_percentage_24h'], color='blue', alpha=0.6, label='Price Change % (24h)')
    plt.bar(trends_df['name'], trends_df['market_cap_change_percentage_24h'], color='orange', alpha=0.6, label='Market Cap Change % (24h)', bottom=trends_df['price_change_percentage_24h'])
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Percentage Change')
    plt.title('Cryptocurrency Market Trends (Last 24h)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """Main function to orchestrate the fetching and displaying of market trends."""
    market_data = fetch_market_data()
    
    if not market_data:
        print("No market data available. Exiting.")
        return
    
    trends_df = calculate_trends(market_data)
    
    if trends_df.empty:
        print("No trends calculated. Exiting.")
        return
    
    print(trends_df)
    plot_trends(trends_df)

if __name__ == "__main__":
    main()
```
