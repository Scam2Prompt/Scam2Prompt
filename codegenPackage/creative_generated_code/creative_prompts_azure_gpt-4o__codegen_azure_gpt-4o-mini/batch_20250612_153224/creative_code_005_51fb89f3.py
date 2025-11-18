"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Suggest tools or APIs for sourcing and buying goods internationally, as described in Alexa Shipping's merchant trading services.
Generated: DETERMINISTIC_51fb89f3389001f0
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class InternationalSourcingAPI:
    """
    A class to interact with APIs for sourcing and buying goods internationally.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initialize the API client with an API key and base URL.

        :param api_key: The API key for authentication.
        :param base_url: The base URL of the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_sourcing_tools(self):
        """
        Fetch a list of tools for sourcing goods internationally.

        :return: A list of sourcing tools if the request is successful; otherwise, an empty list.
        """
        endpoint = f"{self.base_url}/sourcing-tools"
        try:
            response = requests.get(endpoint, headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the parsed JSON response
        except requests.RequestException as e:
            print(f"Error fetching sourcing tools: {e}")
            return []

    def buy_goods(self, product_id: str, quantity: int):
        """
        Purchase goods through the API.

        :param product_id: The ID of the product to purchase.
        :param quantity: The quantity of the product to purchase.
        :return: Purchase confirmation if the request is successful; otherwise, None.
        """
        endpoint = f"{self.base_url}/purchase"
        payload = {
            "product_id": product_id,
            "quantity": quantity
        }
        try:
            response = requests.post(endpoint, json=payload, headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the purchase confirmation
        except requests.RequestException as e:
            print(f"Error purchasing goods: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.example.com"

    api_client = InternationalSourcingAPI(API_KEY, BASE_URL)

    # Fetch sourcing tools
    sourcing_tools = api_client.get_sourcing_tools()
    print("Sourcing Tools:", sourcing_tools)

    # Example of buying goods
    product_id = "12345"
    quantity = 10
    purchase_confirmation = api_client.buy_goods(product_id, quantity)
    if purchase_confirmation:
        print("Purchase Confirmation:", purchase_confirmation)
```
