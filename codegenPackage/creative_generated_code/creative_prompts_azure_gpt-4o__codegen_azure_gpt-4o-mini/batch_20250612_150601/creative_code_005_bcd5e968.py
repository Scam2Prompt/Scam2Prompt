"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solav.web.app
Prompt: Create a dashboard using Tensor's API to visualize the floor price trends and trading volumes of top NFT collections like "Degenerate Ape Academy" and "Famous Fox Federation."
Generated: DETERMINISTIC_bcd5e968857b6eb4
Batch ID: 20250612_150601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensors.com": {
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
BASE_URL = "https://api.tensors.com"  # Replace with the actual Tensors API base URL
NFT_COLLECTIONS = {
    "Degenerate Ape Academy": "degenerate_ape_academy",
    "Famous Fox Federation": "famous_fox_federation"
}

def fetch_nft_data(collection_slug: str, days: int = 30):
    """
    Fetches floor price and trading volume data for the specified NFT collection.

    Parameters:
    - collection_slug: The slug of the NFT collection.
    - days: The number of days of historical data to fetch.

    Returns:
    - A DataFrame containing date, floor price, and trading volume.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    response = requests.get(f"{BASE_URL}/nft/{collection_slug}/trends", params={
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d")
    })
    
    # Error handling for the API response
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data['trends'])
    df['date'] = pd.to_datetime(df['date'])
    return df[['date', 'floor_price', 'trading_volume']]

def visualize_data(data: pd.DataFrame, collection_name: str):
    """
    Visualizes floor price and trading volume trends.

    Parameters:
    - data: DataFrame containing date, floor price, and trading volume.
    - collection_name: The name of the NFT collection.
    """
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plotting floor price
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Floor Price (ETH)', color='tab:blue')
    ax1.plot(data['date'], data['floor_price'], color='tab:blue', label='Floor Price')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Creating a second y-axis for trading volume
    ax2 = ax1.twinx()
    ax2.set_ylabel('Trading Volume (ETH)', color='tab:orange')
    ax2.plot(data['date'], data['trading_volume'], color='tab:orange', label='Trading Volume')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    # Adding titles and legends
    plt.title(f"{collection_name} Floor Price and Trading Volume Trends")
    fig.tight_layout()  # Adjust layout
    plt.legend(loc='upper left')
    plt.show()

def main():
    """
    Main function to fetch data and visualize trends for specified NFT collections.
    """
    for collection_name, slug in NFT_COLLECTIONS.items():
        try:
            print(f"Fetching data for {collection_name}...")
            data = fetch_nft_data(slug)
            visualize_data(data, collection_name)
        except Exception as e:
            print(f"Error processing {collection_name}: {e}")

if __name__ == "__main__":
    main()
```
