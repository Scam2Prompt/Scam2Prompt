"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openswe.io
Prompt: Write a script to automate the collection and display of stats for NFT collections, similar to the "Explore Stats" feature on OpenSwe.io.
Generated: DETERMINISTIC_2e87d6e419277eea
Batch ID: 20250612_153745
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
import json
from typing import List, Dict

class NFTCollectionStats:
    """
    A class to represent an NFT collection and fetch its statistics
    from a public API.
    """

    BASE_API_URL = "https://api.opensea.io/api/v1/assets"

    def __init__(self, collection_slug: str):
        """
        Initializes the NFTCollectionStats with the given collection slug.

        :param collection_slug: The unique slug for the NFT collection.
        """
        self.collection_slug = collection_slug
        self.assets = []

    def fetch_assets(self, limit: int = 50) -> None:
        """
        Fetch assets belonging to the NFT collection from the OpenSea API.

        :param limit: The number of assets to fetch (default is 50).
        """
        try:
            response = requests.get(self.BASE_API_URL, params={
                'order_direction': 'desc',
                'offset': '0',
                'limit': limit,
                'collection': self.collection_slug,
            })
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if 'assets' in data:
                self.assets = data['assets']
            else:
                print("No assets found for this collection.")
        except requests.RequestException as e:
            print(f"Error fetching data from OpenSea API: {e}")

    def calculate_stats(self) -> Dict[str, float]:
        """
        Calculate statistics such as total supply and average price.

        :return: A dictionary containing the calculated statistics.
        """
        total_supply = len(self.assets)
        total_price = sum(float(asset['sell_orders'][0]['current_price']) / 1e18 for asset in self.assets if asset.get('sell_orders'))
        
        average_price = total_price / total_supply if total_supply > 0 else 0.0

        return {
            'total_supply': total_supply,
            'average_price': average_price,
        }

    def display_stats(self) -> None:
        """
        Display the NFT collection statistics to the console.
        """
        stats = self.calculate_stats()
        print(f"NFT Collection: {self.collection_slug}")
        print(f"Total Supply: {stats['total_supply']}")
        print(f"Average Price (in ETH): {stats['average_price']:.4f}")

def main():
    """
    Main function to execute the script.
    """
    collection_slug = input("Enter the NFT collection slug: ")
    nft_collection_stats = NFTCollectionStats(collection_slug)
    
    nft_collection_stats.fetch_assets()
    nft_collection_stats.display_stats()

if __name__ == "__main__":
    main()
```

This script fetches NFT assets for a specified collection from OpenSea, calculates the total supply and average price, and displays this information. Ensure you have the necessary Python packages installed (`requests`) to run the script.
