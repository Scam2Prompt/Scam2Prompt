"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiquest.pages.dev
Prompt: Develop a tool to search for specific addresses and tokens using the De.Fi API's advanced search functionality.
Generated: DETERMINISTIC_9c0e15af3d6be10e
Batch ID: 20250612_151931
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.de.fi/v1/advanced_search": {
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

class DeFiAdvancedSearch:
    """
    A tool to search for specific addresses and tokens using the De.Fi API's advanced search functionality.
    """

    def __init__(self, api_key: str):
        """
        Initialize the search tool with the provided API key.
        
        Args:
            api_key (str): Your De.Fi API key.
        """
        self.base_url = "https://api.de.fi/v1/advanced_search"
        self.api_key = api_key

    def search(self, query: str, search_type: str = "address"):
        """
        Perform an advanced search using the De.Fi API.

        Args:
            query (str): The search query (address or token name).
            search_type (str): The type of search ("address" or "token"). Defaults to "address".

        Returns:
            dict: Parsed JSON response from the API.

        Raises:
            ValueError: If an invalid `search_type` is provided.
            Exception: If the API request fails.
        """
        # Validate search type
        if search_type not in ["address", "token"]:
            raise ValueError("Invalid search_type. Must be 'address' or 'token'.")

        # Define request parameters
        params = {
            "query": query,
            "type": search_type
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            # Make API request
            response = requests.get(self.base_url, params=params, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP codes >= 400

            # Parse JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle request errors
            raise Exception(f"API request failed: {e}")

if __name__ == "__main__":
    # Example usage of the tool

    # Replace with your actual De.Fi API key
    API_KEY = "your_api_key_here"

    # Initialize the search tool
    search_tool = DeFiAdvancedSearch(API_KEY)

    try:
        # Perform a search for an address
        address_query = "0x1234567890abcdef1234567890abcdef12345678"
        address_results = search_tool.search(query=address_query, search_type="address")
        print("Address Search Results:")
        print(address_results)

        # Perform a search for a token
        token_query = "ETH"
        token_results = search_tool.search(query=token_query, search_type="token")
        print("\nToken Search Results:")
        print(token_results)

    except Exception as e:
        # Handle any errors
        print(f"Error: {e}")
```
