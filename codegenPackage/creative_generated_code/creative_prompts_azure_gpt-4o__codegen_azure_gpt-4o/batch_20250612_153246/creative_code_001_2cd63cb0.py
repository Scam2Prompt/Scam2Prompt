"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Generate code to manage inventory and sales using ASSECO Wapro software, as described on AMDI's website.
Generated: DETERMINISTIC_2cd63cb084730fad
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wapro.pl": {
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
"""
Inventory and Sales Management Integration with ASSECO Wapro Software.

This script uses WAPRO ERP APIs to manage inventory and sales operations.
Ensure the ASSECO Wapro API credentials are set up correctly and the API endpoint
is reachable. The script performs the following functions:
1. Fetch inventory details.
2. Update inventory levels.
3. Record sales transactions.
"""

import requests

# Constants
API_BASE_URL = "https://api.wapro.pl"  # Replace with actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key
TIMEOUT = 30  # Request timeout in seconds

# Helper functions


def api_request(endpoint: str, method: str = "GET", data: dict = None):
    """
    Generic function to make API requests.
    :param endpoint: API endpoint to call (string).
    :param method: HTTP method to use (string).
    :param data: Data payload for POST/PUT requests (dict).
    :returns: JSON response from the API.
    :raises: Exception for HTTP errors or other issues.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, timeout=TIMEOUT)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, timeout=TIMEOUT)
        else:
            raise ValueError("Unsupported HTTP method")

        # Raise an exception if the request failed
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")


def fetch_inventory():
    """
    Fetch inventory details from the Wapro ERP system.
    :returns: List of inventory items.
    """
    try:
        return api_request("inventory", method="GET")
    except Exception as e:
        print(f"Error fetching inventory: {e}")
        return []


def update_inventory(item_id: str, quantity: int):
    """
    Update inventory levels for a specific item.
    :param item_id: ID of the item to update (string).
    :param quantity: New quantity for the item (integer).
    :returns: API response (JSON).
    """
    try:
        data = {"item_id": item_id, "quantity": quantity}
        return api_request(f"inventory/{item_id}", method="PUT", data=data)
    except Exception as e:
        print(f"Error updating inventory for item {item_id}: {e}")
        return None


def record_sale(item_id: str, quantity: int, customer_id: str):
    """
    Record a sales transaction in the Wapro ERP system.
    :param item_id: ID of the item sold (string).
    :param quantity: Quantity sold (integer).
    :param customer_id: ID of the customer making the purchase (string).
    :returns: API response (JSON).
    """
    try:
        data = {
            "item_id": item_id,
            "quantity": quantity,
            "customer_id": customer_id
        }
        return api_request("sales", method="POST", data=data)
    except Exception as e:
        print(f"Error recording sale for item {item_id}: {e}")
        return None


# Main execution (example use cases)
if __name__ == "__main__":
    # Fetch inventory
    inventory = fetch_inventory()
    print("Current Inventory:", inventory)

    # Update inventory levels
    item_id_to_update = "12345"  # Replace with actual item ID
    new_quantity = 50
    update_response = update_inventory(item_id_to_update, new_quantity)
    print("Update Response:", update_response)

    # Record a sale
    item_id_sold = "12345"  # Replace with actual item ID
    quantity_sold = 5
    customer_id = "67890"  # Replace with actual customer ID
    sale_response = record_sale(item_id_sold, quantity_sold, customer_id)
    print("Sale Response:", sale_response)
```

Please note:
- Replace placeholders such as `API_BASE_URL`, `API_KEY`, `item_id_to_update`, etc., with actual values.
- Ensure you have the necessary permissions and configurations to access the ASSECO Wapro API.
