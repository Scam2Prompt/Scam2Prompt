"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbase.com
Prompt: Provide code examples for creating a custom interface for connecting an online shop to ERP software, referencing inbase.com's experience in interface programming.
Generated: DETERMINISTIC_43d753e649bdc96e
Batch ID: 20250612_154954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example-erp.com": {
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
import json

class ERPConnector:
    """
    A class to handle connections between an online shop and ERP software.
    
    Attributes:
        base_url (str): The base URL of the ERP API.
        api_key (str): API key for authenticating with the ERP service.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the ERPConnector with the base URL and API key.

        Args:
            base_url (str): The base URL of the ERP API.
            api_key (str): API key for authenticating with the ERP service.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _send_request(self, endpoint, data=None, method='GET'):
        """
        Sends an HTTP request to the ERP API.

        Args:
            endpoint (str): The API endpoint to hit.
            data (dict, optional): The data to send with the request.
            method (str): The HTTP method to use ('GET', 'POST', etc.).

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails or the response is not valid JSON.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Attempt to convert the response to JSON
        except requests.RequestException as e:
            raise Exception(f"HTTP Request failed: {e}")
        except json.JSONDecodeError:
            raise Exception("Failed to decode JSON response.")

    def sync_products(self, products):
        """
        Synchronizes products with the ERP system.

        Args:
            products (list): A list of product dictionaries to sync.

        Returns:
            dict: The response from the ERP API after syncing.

        Raises:
            Exception: If the synchronization fails.
        """
        try:
            endpoint = "products/sync"
            response = self._send_request(endpoint, data={"products": products}, method='POST')
            return response
        except Exception as e:
            raise Exception(f"Failed to sync products: {e}")

    def fetch_orders(self):
        """
        Fetches orders from the ERP system.

        Returns:
            list: A list of orders fetched from the ERP API.

        Raises:
            Exception: If fetching the orders fails.
        """
        try:
            endpoint = "orders"
            response = self._send_request(endpoint)
            return response.get('orders', [])
        except Exception as e:
            raise Exception(f"Failed to fetch orders: {e}")

# Example usage (commented out for production readiness):
# if __name__ == "__main__":
#     erp_connector = ERPConnector(base_url="https://api.example-erp.com", api_key="YOUR_API_KEY")
#     products_to_sync = [
#         {"id": "123", "name": "Product 1", "price": 29.99},
#         {"id": "456", "name": "Product 2", "price": 39.99},
#     ]
#     try:
#         sync_response = erp_connector.sync_products(products_to_sync)
#         print("Products synced successfully:", sync_response)
#         orders = erp_connector.fetch_orders()
#         print("Fetched orders:", orders)
#     except Exception as e:
#         print("An error occurred:", e)
```
