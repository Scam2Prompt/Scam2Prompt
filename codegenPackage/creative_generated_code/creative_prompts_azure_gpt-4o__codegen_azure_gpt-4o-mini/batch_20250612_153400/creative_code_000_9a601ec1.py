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
  "https://api.highlight.com/v1/": {
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
    A class to interact with the Highlight platform API to fetch details of trending
    generative art collections on the Base blockchain.
    """

    BASE_URL = "https://api.highlight.com/v1/"
    
    def __init__(self, api_key: str):
        """
        Initializes the HighlightAPI with the provided API key.
        
        :param api_key: str: Your API key for authentication.
        """
        self.api_key = api_key

    def fetch_trending_collections(self, price_filter: float = None, artist_name: str = None):
        """
        Fetches trending generative art collections from the Highlight API.
        
        :param price_filter: float: Optional price filter to limit results by price.
        :param artist_name: str: Optional artist name filter to limit results by artist.
        :return: dict: A dictionary containing trending collections or an error message.
        """
        endpoint = f"{self.BASE_URL}trending-art-collections"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        params = {}
        
        if price_filter is not None:
            params['price'] = price_filter
        if artist_name is not None:
            params['artist'] = artist_name

        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with a valid API key
    api_key = 'your_api_key'
    highlight_api = HighlightAPI(api_key)

    # Fetch trending collections with optional filters
    trending_collections = highlight_api.fetch_trending_collections(price_filter=100.0, artist_name="John Doe")

    # Print the fetched collections
    print(trending_collections)
```

Make sure to replace `'your_api_key'` with your actual API key for the Highlight platform before running the code.
