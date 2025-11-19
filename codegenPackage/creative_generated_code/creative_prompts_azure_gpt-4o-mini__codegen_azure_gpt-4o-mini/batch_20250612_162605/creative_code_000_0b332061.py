"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-dashboard.vercel.app
Prompt: How can I use the OpenSea Dashboard API to retrieve item price and rarity data for my NFT collection?
Generated: DETERMINISTIC_0b332061310c427f
Batch ID: 20250612_162605
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1": {
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

class OpenSeaAPI:
    """
    A class to interact with the OpenSea API to retrieve NFT collection
    prices and rarity data.
    """

    BASE_URL = "https://api.opensea.io/api/v1"

    def __init__(self):
        """
        Initializes the OpenSeaAPI class.
        """
        pass

    def get_collection_data(self, collection_slug):
        """
        Retrieves the collection data for a given collection slug.

        Args:
            collection_slug (str): The slug of the NFT collection.

        Returns:
            dict: Collection data including price and rarity information.

        Raises:
            Exception: If the API request fails.
        """
        endpoint = f"{self.BASE_URL}/assets"
        params = {
            "order_direction": "desc",
            "offset": "0",
            "limit": "20",
            "collection": collection_slug,
            "order_by": "price"
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

    def extract_price_and_rarity(self, collection_data):
        """
        Extracts price and rarity information from the collection data.

        Args:
            collection_data (dict): The JSON response data from OpenSea API.

        Returns:
            list: A list of dictionaries containing item price and rarity.
        """
        item_info = []

        for asset in collection_data.get('assets', []):
            item = {
                "name": asset.get("name"),
                "price": asset.get("sell_orders", [{}])[0].get("current_price", "N/A"),
                "rarity": asset.get("traits", [])
            }
            item_info.append(item)

        return item_info

def main():
    """
    Main function to retrieve and display NFT collection data.
    """
    opensea_api = OpenSeaAPI()
    collection_slug = "your-collection-slug-here"  # Replace with your collection slug

    try:
        collection_data = opensea_api.get_collection_data(collection_slug)
        item_info = opensea_api.extract_price_and_rarity(collection_data)

        # Display the item information
        for item in item_info:
            print(f"Item Name: {item['name']}, Price: {item['price']}, Rarity: {item['rarity']}")
    except Exception as e:
        print(f"Failed to retrieve collection data: {e}")

if __name__ == "__main__":
    main()
```
