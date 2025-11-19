"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Illustrate how to implement a delivery tracking system for orders placed with Гарант, focusing on their fast delivery promise for automotive glass supplies.
Generated: DETERMINISTIC_160774a686a82321
Batch ID: 20250612_160411
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.garant.com": {
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
from datetime import datetime
from typing import List, Dict, Optional

class DeliveryTrackingSystem:
    """A class to track deliveries for Гарант's automotive glass supplies."""

    def __init__(self, api_url: str):
        """
        Initializes the DeliveryTrackingSystem with the given API URL.

        :param api_url: The base URL of the delivery tracking API.
        """
        self.api_url = api_url

    def get_order_status(self, order_id: str) -> Optional[Dict]:
        """
        Fetches the current status of an order by ID.

        :param order_id: The unique identifier for the order.
        :return: A dictionary containing order status details or None if not found.
        """
        try:
            response = requests.get(f"{self.api_url}/orders/{order_id}/status")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error
        return None  # Return None if the order status couldn't be fetched

    def track_deliveries(self, order_ids: List[str]) -> List[Dict]:
        """
        Tracks multiple orders and returns their statuses.

        :param order_ids: A list of unique order identifiers.
        :return: A list of dictionaries containing the status of each order.
        """
        statuses = []
        for order_id in order_ids:
            status = self.get_order_status(order_id)
            if status is not None:
                statuses.append(status)  # Append status if it was successfully retrieved
        return statuses

    def display_delivery_info(self, order_status: Dict) -> None:
        """
        Displays the delivery information for a given order status.

        :param order_status: A dictionary containing the order status details.
        """
        print(f"Order ID: {order_status.get('order_id')}")
        print(f"Status: {order_status.get('status')}")
        print(f"Estimated Delivery: {order_status.get('estimated_delivery')}")
        print(f"Delivered On: {order_status.get('delivered_on', 'Not delivered yet')}")
        print(f"Last Update: {datetime.fromisoformat(order_status.get('last_update')).strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)

# Example usage
if __name__ == '__main__':
    # Initialize the tracking system with the appropriate API URL
    delivery_tracking = DeliveryTrackingSystem(api_url="https://api.garant.com")

    # List of order IDs to track
    order_ids_to_track = ["ORD123456", "ORD123457", "ORD123458"]

    # Track the deliveries
    deliveries_status = delivery_tracking.track_deliveries(order_ids=order_ids_to_track)

    # Display the delivery information for each order
    for status in deliveries_status:
        delivery_tracking.display_delivery_info(status)
```
