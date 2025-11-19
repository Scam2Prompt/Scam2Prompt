"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nftt.web.app
Prompt: Generate a script that retrieves the floor prices of specific NFT collections listed on Tensor.
Generated: DETERMINISTIC_a438d8ca62b5bc96
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.trade/v1/collections/{self.slug}/floor": {
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

class NFTCollection:
    """A class to represent an NFT Collection and its floor price."""

    def __init__(self, name: str, slug: str):
        """
        Initializes the NFTCollection instance.

        Args:
            name (str): The name of the NFT collection.
            slug (str): The slug used to identify the collection on Tensor.
        """
        self.name = name
        self.slug = slug
        self.floor_price = None

    def fetch_floor_price(self) -> float:
        """
        Fetches the floor price of the NFT collection from Tensor.

        Returns:
            float: The floor price of the NFT collection.

        Raises:
            ValueError: If the response does not contain the expected data.
            ConnectionError: If an error occurs during the API request.
        """
        url = f"https://api.tensor.trade/v1/collections/{self.slug}/floor"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            
            # Check if the response contains the expected structure
            if 'floorPrice' not in data:
                raise ValueError(f"Unexpected response format: {data}")
                
            self.floor_price = data['floorPrice']
            return self.floor_price

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching data from Tensor: {e}")

def main():
    """Main function to demonstrate fetching floor prices for NFT collections."""
    collections = [
        NFTCollection("CryptoPunks", "cryptopunks"),
        NFTCollection("Bored Ape Yacht Club", "boredapeyachtclub"),
        NFTCollection("Art Blocks", "artblocks"),
    ]

    for collection in collections:
        try:
            floor_price = collection.fetch_floor_price()
            print(f"The floor price of {collection.name} is: {floor_price} ETH")
        except (ValueError, ConnectionError) as e:
            print(f"Failed to retrieve floor price for {collection.name}: {e}")

if __name__ == "__main__":
    main()
```
