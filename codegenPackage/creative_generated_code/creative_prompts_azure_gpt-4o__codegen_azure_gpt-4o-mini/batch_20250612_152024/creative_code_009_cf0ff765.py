"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quotrio.xyz
Prompt: Write a Python script to calculate and visualize cryptocurrency market trends across 50+ markets, as mentioned in QuotRio's platform details.
Generated: DETERMINISTIC_cf0ff765e7cb4ce8
Batch ID: 20250612_152024
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
import matplotlib.pyplot as plt
import numpy as np

# Constants for the API endpoint and parameters
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
CURRENCY = "usd"
MARKET_COUNT = 50

def fetch_market_data():
    """
    Fetches cryptocurrency market data from the CoinGecko API.

    Returns:
        list: A list of dictionaries containing market data for cryptocurrencies.
    """
    try:
        params = {
            'vs_currency': CURRENCY,
            'order': 'market_cap_desc',
            'per_page': MARKET_COUNT,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h',
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return []

def process_market_data(data):
    """
    Processes the raw market data into a DataFrame.

    Args:
        data (list): Raw market data.

    Returns:
        pd.DataFrame: A DataFrame containing processed market data.
    """
    if not data:
        return pd.DataFrame()  # Return an empty DataFrame if no data

    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Select relevant columns
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h']]
    
    return df

def visualize_market_trends(df):
    """
    Visualizes the market trends of cryptocurrencies.

    Args:
        df (pd.DataFrame): DataFrame containing market data to visualize.
    """
    if df.empty:
        print("No data available for visualization.")
        return

    # Sort data by market cap
    df_sorted = df.sort_values(by='market_cap', ascending=False)

    # Create a plot for the top 10 cryptocurrencies by market cap
    plt.figure(figsize=(12, 6))
    plt.barh(df_sorted['name'].head(10), df_sorted['market_cap'].head(10), color='skyblue')
    plt.xlabel('Market Cap (in USD)')
    plt.title('Top 10 Cryptocurrencies by Market Cap')
    plt.gca().invert_yaxis()  # Invert y-axis for better readability
    plt.show()

def main():
    """
    Main function to execute the cryptocurrency market trend analysis.
    """
    # Fetch market data
    raw_data = fetch_market_data()
    
    # Process market data
    market_data = process_market_data(raw_data)
    
    # Visualize market trends
    visualize_market_trends(market_data)

if __name__ == "__main__":
    main()
```
