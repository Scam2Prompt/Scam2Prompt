"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Write a Python script that integrates with an API to manage orders for digital printing services, focusing on quick turnaround times as highlighted by Detalj Reklam.
Generated: DETERMINISTIC_a619de4555d3df3b
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.digitalprintingservices.com/v1": {
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

class DigitalPrintingAPI:
    """
    A class to interact with the Digital Printing Services API for managing orders.
    """

    BASE_URL = "https://api.digitalprintingservices.com/v1"  # Replace with the actual API endpoint
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_TOKEN"  # Replace with your API token
    }

    def __init__(self):
        """Initializes the DigitalPrintingAPI instance."""
        pass

    def create_order(self, order_data):
        """
        Creates a new order for digital printing.

        Args:
            order_data (dict): A dictionary containing order details.

        Returns:
            dict: The created order response from the API.

        Raises:
            Exception: If an error occurs during the API request.
        """
        try:
            response = requests.post(f"{self.BASE_URL}/orders", headers=self.HEADERS, data=json.dumps(order_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error creating order: {e}") from e

    def get_order(self, order_id):
        """
        Retrieves the details of a specific order.

        Args:
            order_id (str): The ID of the order to retrieve.

        Returns:
            dict: The order details retrieved from the API.

        Raises:
            Exception: If an error occurs during the API request.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/orders/{order_id}", headers=self.HEADERS)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error retrieving order {order_id}: {e}") from e

    def list_orders(self):
        """
        Lists all orders placed.

        Returns:
            list: A list of all orders retrieved from the API.

        Raises:
            Exception: If an error occurs during the API request.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/orders", headers=self.HEADERS)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error retrieving orders: {e}") from e

    def update_order(self, order_id, update_data):
        """
        Updates an existing order.

        Args:
            order_id (str): The ID of the order to update.
            update_data (dict): A dictionary containing the updated order details.

        Returns:
            dict: The updated order response from the API.

        Raises:
            Exception: If an error occurs during the API request.
        """
        try:
            response = requests.put(f"{self.BASE_URL}/orders/{order_id}", headers=self.HEADERS, data=json.dumps(update_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error updating order {order_id}: {e}") from e

    def delete_order(self, order_id):
        """
        Deletes a specified order.

        Args:
            order_id (str): The ID of the order to delete.

        Returns:
            dict: The response from the API confirming deletion.

        Raises:
            Exception: If an error occurs during the API request.
        """
        try:
            response = requests.delete(f"{self.BASE_URL}/orders/{order_id}", headers=self.HEADERS)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error deleting order {order_id}: {e}") from e

# Example usage (commented out for production readiness)
# if __name__ == "__main__":
#     api = DigitalPrintingAPI()
#     try:
#         new_order = {
#             "customer_name": "John Doe",
#             "product": "Business Cards",
#             "quantity": 100,
#             "turnaround_time": "48 hours"
#         }
#         order_response = api.create_order(new_order)
#         print("Order created successfully:", order_response)
#     except Exception as e:
#         print(e)
```
