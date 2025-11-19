"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Write a Python function that retrieves the unique items and their prices from the Heart Full of Love JamCards collection on Ethereum.
Generated: DETERMINISTIC_8f4449957e8ac1dd
Batch ID: 20250612_160133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets": {
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
from typing import List, Dict, Any, Tuple

def fetch_ethereum_nft_data(collection_name: str) -> List[Dict[str, Any]]:
    """
    Fetches NFT data from the OpenSea API for a given collection on Ethereum.

    Args:
        collection_name (str): The name of the NFT collection to retrieve data from.

    Returns:
        List[Dict[str, Any]]: A list of unique items with their details including price.

    Raises:
        ValueError: If the API response is unsuccessful or the collection is not found.
    """
    url = f"https://api.opensea.io/api/v1/assets"
    params = {
        "order_direction": "asc",
        "offset": "0",
        "limit": "50",
        "collection": collection_name
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        if 'assets' not in data:
            raise ValueError(f"No assets found for the collection '{collection_name}'.")

        return data['assets']
    
    except requests.RequestException as e:
        raise ValueError(f"Error fetching data from OpenSea API: {e}")

def get_unique_items_and_prices(collection_name: str) -> List[Tuple[str, float]]:
    """
    Retrieves unique items and their prices from a specified NFT collection on Ethereum.

    Args:
        collection_name (str): The name of the NFT collection.

    Returns:
        List[Tuple[str, float]]: A list of tuples containing unique item names and their prices.
    """
    items = fetch_ethereum_nft_data(collection_name)
    unique_items = {}

    # Iterate over the fetched items to collect unique names and their prices
    for item in items:
        name = item.get('name')
        # The price is usually listed under 'sell_orders' in the asset details
        price = None

        if 'sell_orders' in item and item['sell_orders']:
            price = float(item['sell_orders'][0]['current_price']) / (10 ** 18)  # Price is in Wei

        if name and price is not None:
            unique_items[name] = price

    return list(unique_items.items())

# Example usage of the function
if __name__ == "__main__":
    collection_name = "heart-full-of-love-jamcards"
    try:
        unique_items_and_prices = get_unique_items_and_prices(collection_name)
        for item, price in unique_items_and_prices:
            print(f"Item: {item}, Price: {price} ETH")
    except ValueError as e:
        print(e)
```
