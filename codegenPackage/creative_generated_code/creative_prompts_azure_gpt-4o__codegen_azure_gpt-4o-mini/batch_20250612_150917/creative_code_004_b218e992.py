"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdaily.info
Prompt: Write a script to analyze on-chain data for Ethereum, focusing on whale accumulation and its correlation with ETH price trends during the 2025 bull market.
Generated: DETERMINISTIC_b218e992dd5d455b
Batch ID: 20250612_150917
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.coingecko.com/api/v3/coins/ethereum/market_chart": {
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

# Constants for API endpoints
ETH_PRICE_API = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
ETHERSCAN_API = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API key

def fetch_eth_price(days=365):
    """Fetch historical Ethereum price data."""
    try:
        response = requests.get(ETH_PRICE_API, params={'vs_currency': 'usd', 'days': days})
        response.raise_for_status()  # Raise an error for bad responses
        price_data = response.json()
        return pd.DataFrame(price_data['prices'], columns=['timestamp', 'price']).assign(timestamp=lambda df: pd.to_datetime(df['timestamp'], unit='ms'))
    except Exception as e:
        print(f"Error fetching Ethereum price data: {e}")
        return pd.DataFrame()

def fetch_whale_data(addresses, start_block, end_block):
    """Fetch transaction data for specified whale addresses."""
    whale_data = []
    for address in addresses:
        try:
            response = requests.get(ETHERSCAN_API, params={
                'module': 'account',
                'action': 'txlist',
                'address': address,
                'startblock': start_block,
                'endblock': end_block,
                'sort': 'asc',
                'apikey': ETHERSCAN_API_KEY
            })
            response.raise_for_status()
            whale_data.extend(response.json().get('result', []))
        except Exception as e:
            print(f"Error fetching data for address {address}: {e}")
    return pd.DataFrame(whale_data)

def analyze_data(price_data, whale_data):
    """Analyze whale accumulation and its correlation with ETH price trends."""
    # Convert timestamps to datetime
    whale_data['timeStamp'] = pd.to_datetime(whale_data['timeStamp'], unit='s')
    
    # Grouping whale transactions by date
    whale_daily = whale_data.groupby(whale_data['timeStamp'].dt.date).agg({'value': 'sum'}).reset_index()
    whale_daily.columns = ['date', 'whale_accumulation']
    
    # Merge price and whale data on date
    combined_data = pd.merge(price_data, whale_daily, left_on='timestamp', right_on='date', how='inner')
    return combined_data

def plot_data(combined_data):
    """Plot ETH price and whale accumulation data."""
    plt.figure(figsize=(14, 7))
    plt.subplot(2, 1, 1)
    plt.plot(combined_data['timestamp'], combined_data['price'], label='ETH Price', color='blue')
    plt.title('Ethereum Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.bar(combined_data['timestamp'], combined_data['whale_accumulation'], label='Whale Accumulation', color='orange')
    plt.title('Whale Accumulation Trend')
    plt.xlabel('Date')
    plt.ylabel('Accumulation')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the analysis."""
    # Define parameters for analysis
    whale_addresses = ['0xAddress1', '0xAddress2']  # Replace with actual whale addresses
    start_block = 0
    end_block = 99999999  # Use a high number to include all blocks

    # Fetch data
    price_data = fetch_eth_price(days=730)  # Last 2 years of data
    whale_data = fetch_whale_data(whale_addresses, start_block, end_block)

    # Analyze and plot data if available
    if not price_data.empty and not whale_data.empty:
        combined_data = analyze_data(price_data, whale_data)
        plot_data(combined_data)
    else:
        print("No data available for analysis.")

if __name__ == "__main__":
    main()
```
