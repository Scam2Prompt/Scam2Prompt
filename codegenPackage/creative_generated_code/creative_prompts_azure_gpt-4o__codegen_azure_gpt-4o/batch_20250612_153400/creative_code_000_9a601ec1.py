"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degen-4g1.pages.dev
Prompt: Write code to interact with the Highlight platform API to fetch details of trending generative art collections on the Base blockchain. Include parameters for filtering by price and artist name.
Generated: DETERMINISTIC_9a601ec1f3b96f21
Batch ID: 20250612_153400
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.highlight.xyz": {
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

class HighlightAPI:
    """
    A class to interact with the Highlight platform API to fetch details
    of trending generative art collections on the Base blockchain.
    """

    BASE_URL = "https://api.highlight.xyz"  # Replace with actual base URL of Highlight API

    def __init__(self, api_key):
        """
        Initialize the HighlightAPI client with an API key.

        :param api_key: Your API key for accessing the Highlight platform API.
        """
        self.api_key = api_key

    def fetch_trending_art_collections(self, min_price=None, max_price=None, artist_name=None):
        """
        Fetch details of trending generative art collections, with optional filtering.

        :param min_price: Minimum price filter (optional).
        :param max_price: Maximum price filter (optional).
        :param artist_name: Artist name filter (optional).
        :return: A list of trending art collections matching the filters.
        """
        try:
            # Endpoint for fetching trending art collections
            endpoint = f"{self.BASE_URL}/collections/trending"

            # Prepare query parameters
            params = {
                "blockchain": "Base",  # Filter by Base blockchain
            }

            # Add price filters if specified
            if min_price:
                params["min_price"] = min_price
            if max_price:
                params["max_price"] = max_price

            # Add artist name filter if specified
            if artist_name:
                params["artist_name"] = artist_name

            # Headers for the API request
            headers = {
                "Authorization": f"Bearer {self.api_key}",  # API key for authentication
                "Content-Type": "application/json",         # Expect JSON responses
            }

            # Make the GET request
            response = requests.get(endpoint, params=params, headers=headers)

            # Raise an HTTPError if the response contains a client/server error
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            print(f"An error occurred while fetching trending art collections: {e}")
            return None


# Example usage of the HighlightAPI class
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    api_key = "your_api_key_here"
    api_client = HighlightAPI(api_key)

    # Fetch collections with optional filters
    trending_collections = api_client.fetch_trending_art_collections(
        min_price=0.5,  # Minimum price filter
        max_price=10,   # Maximum price filter
        artist_name="John Doe"  # Filter by artist name
    )

    if trending_collections:
        print("Trending Generative Art Collections:")
        for collection in trending_collections:
            print(collection)
    else:
        print("No collections found or an error occurred.")
```
