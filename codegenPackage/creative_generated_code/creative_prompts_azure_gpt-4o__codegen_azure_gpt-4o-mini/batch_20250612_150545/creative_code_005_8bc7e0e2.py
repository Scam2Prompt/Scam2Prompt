"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-soles.web.app
Prompt: Implement a feature to display the price difference between the floor price and sell price for NFTs on Tensor, using collections such as "Zero Monke Biz" and "Degenerate Ape Academy" as examples.
Generated: DETERMINISTIC_8bc7e0e2b874631b
Batch ID: 20250612_150545
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.trade/v1/nfts": {
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

class NFTPriceChecker:
    """A class to fetch and compare floor prices and sell prices for NFTs."""
    
    def __init__(self, collection_name):
        """
        Initializes the NFTPriceChecker with the specified collection name.
        
        Args:
            collection_name (str): The name of the NFT collection to check.
        """
        self.collection_name = collection_name
        self.api_url = "https://api.tensor.trade/v1/nfts"  # Example API endpoint

    def fetch_floor_price(self):
        """Fetches the current floor price for the specified NFT collection."""
        try:
            response = requests.get(self.api_url, params={"collection": self.collection_name})
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data.get('floor_price', 0)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching floor price for {self.collection_name}: {e}")
            return None

    def fetch_sell_price(self, nft_id):
        """Fetches the sell price for a specific NFT based on its ID.
        
        Args:
            nft_id (str): The unique identifier for the NFT.

        Returns:
            float: The sell price of the NFT, or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_url}/{nft_id}")
            response.raise_for_status()
            data = response.json()
            return data.get('sell_price', 0)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching sell price for NFT ID {nft_id}: {e}")
            return None

    def calculate_price_difference(self, floor_price, sell_price):
        """Calculates the price difference between the floor price and the sell price.
        
        Args:
            floor_price (float): The floor price for the NFT collection.
            sell_price (float): The sell price for the NFT.

        Returns:
            float: The price difference, or None if either price is invalid.
        """
        if floor_price is None or sell_price is None:
            print("Invalid price, cannot calculate difference.")
            return None
        return sell_price - floor_price

    def display_price_difference(self, nft_id):
        """Fetches prices and displays the difference between floor and sell prices.
        
        Args:
            nft_id (str): The unique identifier for the NFT.
        """
        floor_price = self.fetch_floor_price()
        sell_price = self.fetch_sell_price(nft_id)

        if floor_price is not None and sell_price is not None:
            price_difference = self.calculate_price_difference(floor_price, sell_price)
            print(f"Collection: {self.collection_name}")
            print(f"Floor Price: {floor_price}")
            print(f"Sell Price: {sell_price}")
            print(f"Price Difference: {price_difference}")
        else:
            print("Could not retrieve all necessary prices.")

# Example usage
if __name__ == "__main__":
    collection_name = "Zero Monke Biz"  # Change to desired collection
    nft_id = "example_nft_id"  # Replace with actual NFT ID to check sell price

    checker = NFTPriceChecker(collection_name)
    checker.display_price_difference(nft_id)
```
