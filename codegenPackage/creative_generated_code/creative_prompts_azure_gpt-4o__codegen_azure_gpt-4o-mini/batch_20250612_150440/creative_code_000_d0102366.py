"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledqinlv.com
Prompt: Write Python code to interact with OpenSea's API for retrieving the top 10 trending NFT collections based on floor price changes in the past 7 days.
Generated: DETERMINISTIC_d0102366bee9e86d
Batch ID: 20250612_150440
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
    BASE_URL = "https://api.opensea.io/api/v1"

    def __init__(self):
        """Initialize OpenSea API client."""
        pass

    def get_trending_collections(self, limit=10):
        """
        Retrieve the top trending NFT collections based on floor price changes
        in the past 7 days.

        Args:
            limit (int): The number of trending collections to retrieve.
        
        Returns:
            list: A list of trending NFT collections.
        
        Raises:
            ValueError: If the response from the API is not valid.
            Exception: If there is a connection error or any other issue.
        """
        try:
            # Prepare the endpoint URL
            endpoint = f"{self.BASE_URL}/collections/trending"
            params = {
                "limit": limit,
                "order_direction": "desc",
                "offset": 0,
                "days": 7
            }

            # Make the API request
            response = requests.get(endpoint, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Extract data from the response
            data = response.json()
            collections = data.get('collections', [])

            if not collections:
                raise ValueError("No collections found in the response.")

            return collections

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while connecting to OpenSea API: {e}")
            raise  # Re-raise the exception for further handling
        except ValueError as ve:
            print(f"Value error: {ve}")
            raise  # Re-raise the exception for further handling

if __name__ == "__main__":
    api = OpenSeaAPI()
    try:
        trending_collections = api.get_trending_collections()
        print("Top 10 Trending NFT Collections:")
        for collection in trending_collections:
            print(f"- {collection['name']} (Floor Price Change: {collection['floor_price_change']})")
    except Exception as e:
        print(f"Failed to retrieve trending collections: {e}")
```
