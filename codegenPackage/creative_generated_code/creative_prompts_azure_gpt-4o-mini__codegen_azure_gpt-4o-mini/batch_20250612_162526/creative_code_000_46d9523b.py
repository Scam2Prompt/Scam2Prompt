"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Generate a code snippet for integrating One World Supply's plumbing tools and fixtures into a construction management software API.
Generated: DETERMINISTIC_46d9523b0cf43c48
Batch ID: 20250612_162526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.oneworldsupply.com/v1/": {
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

class OneWorldSupplyAPI:
    """
    A class to interact with One World Supply's plumbing tools and fixtures API.
    """

    BASE_URL = "https://api.oneworldsupply.com/v1/"
    
    def __init__(self, api_key):
        """
        Initializes the API client with the provided API key.

        Args:
            api_key (str): Your API key for authenticating requests.
        """
        self.api_key = api_key

    def get_plumbing_tools(self):
        """
        Fetches the list of plumbing tools from the API.

        Returns:
            list: A list of plumbing tools.
        """
        endpoint = f"{self.BASE_URL}tools"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching plumbing tools: {e}")
            return []

    def get_fixture_details(self, fixture_id):
        """
        Fetches details for a specific plumbing fixture by its ID.

        Args:
            fixture_id (str): The ID of the fixture to retrieve.

        Returns:
            dict: A dictionary containing fixture details.
        """
        endpoint = f"{self.BASE_URL}fixtures/{fixture_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching fixture details for ID {fixture_id}: {e}")
            return None

    def create_order(self, order_data):
        """
        Creates a new order for plumbing tools and fixtures.

        Args:
            order_data (dict): A dictionary containing order details.

        Returns:
            dict: The response from the API after creating the order.
        """
        endpoint = f"{self.BASE_URL}orders"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(order_data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating order: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    api_client = OneWorldSupplyAPI(API_KEY)
    
    # Fetch plumbing tools
    tools = api_client.get_plumbing_tools()
    print("Plumbing Tools:", tools)
    
    # Fetch details for a specific fixture
    fixture_id = "12345"  # Replace with a valid fixture ID
    fixture_details = api_client.get_fixture_details(fixture_id)
    print("Fixture Details:", fixture_details)
    
    # Create a new order
    order_data = {
        "items": [
            {"tool_id": "tool_123", "quantity": 2},
            {"fixture_id": "fixture_456", "quantity": 1}
        ],
        "customer_id": "customer_789"
    }
    order_response = api_client.create_order(order_data)
    print("Order Response:", order_response)
```
