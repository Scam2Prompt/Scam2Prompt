"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Write code to integrate a swag fulfillment system with an existing ERP platform, ensuring scalable distribution and real-time inventory visibility, as outlined by Avail Labs.
Generated: DETERMINISTIC_6a66245036663b4c
Batch ID: 20250612_154147
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.erpplatform.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.swagfulfillment.com": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class SwagFulfillmentSystem:
    def __init__(self, swag_api_url, erp_api_url, api_key):
        """
        Initialize the Swag Fulfillment System with API URLs and API key.

        :param swag_api_url: URL for the swag fulfillment API
        :param erp_api_url: URL for the ERP platform API
        :param api_key: API key for authentication
        """
        self.swag_api_url = swag_api_url
        self.erp_api_url = erp_api_url
        self.api_key = api_key

    def get_inventory(self):
        """
        Fetch the current inventory from the swag fulfillment system.

        :return: Inventory data as a JSON object or raises an error
        """
        try:
            response = requests.get(f"{self.swag_api_url}/inventory", headers=self._get_headers())
            response.raise_for_status()
            logging.info("Successfully fetched inventory data.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching inventory: {e}")
            raise

    def fulfill_order(self, order_data):
        """
        Fulfill an order by sending the order details to the swag fulfillment system.

        :param order_data: Data containing the order information
        :return: Response from the fulfillment system or raises an error
        """
        try:
            response = requests.post(f"{self.swag_api_url}/fulfill", headers=self._get_headers(), json=order_data)
            response.raise_for_status()
            logging.info("Order fulfilled successfully.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fulfilling order: {e}")
            raise

    def update_inventory(self, inventory_data):
        """
        Update inventory levels in the ERP system based on the swag fulfillment system data.

        :param inventory_data: Data containing the updated inventory information
        :return: Response from the ERP system or raises an error
        """
        try:
            response = requests.post(f"{self.erp_api_url}/inventory/update", headers=self._get_headers(), json=inventory_data)
            response.raise_for_status()
            logging.info("Inventory updated successfully in ERP system.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error updating inventory: {e}")
            raise

    def _get_headers(self):
        """
        Generate headers for API requests.

        :return: Dictionary of headers
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

# Example usage:
if __name__ == "__main__":
    # Initialize with appropriate URLs and API key
    swag_fulfillment = SwagFulfillmentSystem(
        swag_api_url="https://api.swagfulfillment.com",
        erp_api_url="https://api.erpplatform.com",
        api_key="your_api_key_here"
    )

    try:
        # Example: Fetch inventory
        inventory_data = swag_fulfillment.get_inventory()

        # Example: Update ERP with fetched inventory
        swag_fulfillment.update_inventory(inventory_data)

        # Example: Fulfill an order
        order_data = {
            "order_id": "12345",
            "items": [
                {"sku": "SWAG001", "quantity": 2},
                {"sku": "SWAG002", "quantity": 1}
            ]
        }
        swag_fulfillment.fulfill_order(order_data)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
