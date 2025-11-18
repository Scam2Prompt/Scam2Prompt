"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orderly-network.pages.dev
Prompt: How can I use the Orderly API to fetch real-time trading data for a decentralized exchange built on NEAR or EVM?
Generated: DETERMINISTIC_7f8d1b26aefe7e88
Batch ID: 20250612_151038
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.orderly.network": {
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

class OrderlyAPI:
    """
    A class to interact with the Orderly API for fetching real-time trading data.

    Attributes:
        base_url (str): The base URL for the Orderly API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key):
        """
        Initializes the OrderlyAPI with the provided API key.

        Args:
            api_key (str): The API key for authentication.
        """
        self.base_url = "https://api.orderly.network"
        self.api_key = api_key

    def get_market_data(self, market_id):
        """
        Fetches real-time trading data for a specified market.

        Args:
            market_id (str): The ID of the market to fetch data for.

        Returns:
            dict: The trading data for the specified market.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/markets/{market_id}/data"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Return the response data as JSON
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # HTTP error
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Other errors

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual API key for Orderly API
    api_key = "your_api_key"
    market_id = "your_market_id"  # Replace with the actual market ID

    orderly_api = OrderlyAPI(api_key)

    try:
        market_data = orderly_api.get_market_data(market_id)
        print("Market Data:", market_data)  # Output the fetched market data
    except Exception as e:
        print("Error fetching market data:", e)  # Handle the error gracefully
```
