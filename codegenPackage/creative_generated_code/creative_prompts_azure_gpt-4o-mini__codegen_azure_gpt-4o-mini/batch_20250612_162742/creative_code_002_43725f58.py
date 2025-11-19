"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script that can track orders from an online electronics store, similar to the features on the provided webpage.
Generated: DETERMINISTIC_43725f58d2300607
Batch ID: 20250612_162742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.onlinestore.com": {
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
import json
import requests
from datetime import datetime

class OrderTracker:
    """
    A class to track orders from an online electronics store.
    """

    def __init__(self, api_base_url):
        """
        Initializes the OrderTracker with the API base URL.

        :param api_base_url: The base URL for the order tracking API.
        """
        self.api_base_url = api_base_url

    def get_order_status(self, order_id):
        """
        Retrieves the status of a specific order.

        :param order_id: The ID of the order to track.
        :return: A dictionary containing the order status information.
        :raises ValueError: If the order ID is invalid.
        :raises Exception: If there is an error fetching the order status.
        """
        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID must be a non-empty string.")

        url = f"{self.api_base_url}/orders/{order_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching order status: {e}")

    def display_order_status(self, order_id):
        """
        Displays the status of the given order in a user-friendly format.

        :param order_id: The ID of the order to display the status for.
        """
        try:
            order_status = self.get_order_status(order_id)
            print(f"Order ID: {order_status['id']}")
            print(f"Status: {order_status['status']}")
            print(f"Placed on: {datetime.fromisoformat(order_status['placed_at']).strftime('%Y-%m-%d %H:%M:%S')}")
            if 'tracking_info' in order_status:
                print(f"Tracking Info: {order_status['tracking_info']}")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(e)

def main():
    """
    Main function to execute the order tracking script.
    """
    api_base_url = "https://api.onlinestore.com"  # Replace with the actual API base URL
    order_tracker = OrderTracker(api_base_url)

    order_id = input("Enter the Order ID to track: ")
    order_tracker.display_order_status(order_id)

if __name__ == "__main__":
    main()
```
