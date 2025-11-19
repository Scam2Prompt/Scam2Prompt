"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Write a Python script that integrates with an API to manage orders for digital printing services, focusing on quick turnaround times as highlighted by Detalj Reklam.
Generated: DETERMINISTIC_a619de4555d3df3b
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.detaljreklam.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalPrintingAPI:
    """
    A class to interact with the Digital Printing API for managing orders.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client with the base URL and API key.

        :param base_url: The base URL of the API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request (for POST).
        :return: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                logging.error("Unsupported HTTP method: %s", method)
                return None

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")

        return None

    def create_order(self, order_data):
        """
        Creates a new order in the digital printing service.

        :param order_data: A dictionary containing order details.
        :return: The response from the API or None if an error occurred.
        """
        logging.info("Creating a new order with data: %s", order_data)
        return self._make_request('orders', method='POST', data=order_data)

    def get_order_status(self, order_id):
        """
        Retrieves the status of an existing order.

        :param order_id: The ID of the order to check.
        :return: The order status or None if an error occurred.
        """
        logging.info("Fetching status for order ID: %s", order_id)
        return self._make_request(f'orders/{order_id}', method='GET')

def main():
    # Configuration for the API
    BASE_URL = "https://api.detaljreklam.com/v1"  # Example base URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Initialize the API client
    api_client = DigitalPrintingAPI(BASE_URL, API_KEY)

    # Example order data
    order_data = {
        "customer_name": "John Doe",
        "product": "Business Cards",
        "quantity": 100,
        "turnaround_time": "24 hours"
    }

    # Create a new order
    order_response = api_client.create_order(order_data)
    if order_response:
        logging.info("Order created successfully: %s", order_response)

        # Check the status of the created order
        order_id = order_response.get('id')
        status_response = api_client.get_order_status(order_id)
        if status_response:
            logging.info("Order status: %s", status_response)

if __name__ == "__main__":
    main()
```
