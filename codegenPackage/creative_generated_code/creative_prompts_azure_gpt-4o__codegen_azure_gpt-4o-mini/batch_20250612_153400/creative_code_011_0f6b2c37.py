"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Generate code to interact with MultiversX's blockchain for on-chain leveraged trading, referencing the AshPerp project mentioned on the website.
Generated: DETERMINISTIC_0f6b2c375f3448ed
Batch ID: 20250612_153400
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multiversx.com": {
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
from requests.exceptions import HTTPError

class MultiversXClient:
    """Client to interact with the MultiversX blockchain for on-chain leveraged trading."""
    
    BASE_URL = "https://api.multiversx.com"
    
    def __init__(self, api_key):
        """Initializes the client with the provided API key."""
        self.api_key = api_key
    
    def _get_headers(self):
        """Returns the headers required for API requests."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_market_data(self, market_id):
        """
        Fetches the market data for the specified market.

        :param market_id: The ID of the market to query.
        :return: A dictionary containing market data.
        :raises HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/markets/{market_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def create_order(self, market_id, order_type, amount, price):
        """
        Creates a new order in the specified market.

        :param market_id: The ID of the market where the order will be placed.
        :param order_type: Type of order ('buy' or 'sell').
        :param amount: The amount of the asset to trade.
        :param price: The price at which to place the order.
        :return: A dictionary containing order confirmation data.
        :raises HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/orders"
        order_data = {
            "marketId": market_id,
            "type": order_type,
            "amount": amount,
            "price": price
        }
        try:
            response = requests.post(url, json=order_data, headers=self._get_headers())
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred while creating order: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred while creating order: {err}")
            raise

    def get_order_status(self, order_id):
        """
        Fetches the status of a specific order.

        :param order_id: The ID of the order to query.
        :return: A dictionary containing the status of the order.
        :raises HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/orders/{order_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred while fetching order status: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred while fetching order status: {err}")
            raise

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    client = MultiversXClient(api_key)

    try:
        market_data = client.get_market_data("market_id_here")  # Replace with an actual market ID
        print("Market Data:", market_data)

        order_response = client.create_order("market_id_here", "buy", 10, 100)  # Example order
        print("Order Response:", order_response)

        order_status = client.get_order_status(order_response['id'])
        print("Order Status:", order_status)

    except Exception as e:
        print(f"An error occurred during the operation: {e}")
```
