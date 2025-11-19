"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvercstore.com
Prompt: Describe the process of ordering promotional items through the NVIDIA Partner Promotional Portal and how to ensure compliance with return policies.
Generated: DETERMINISTIC_e20fa1f9b694ab0e
Batch ID: 20250612_163546
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nvidia.com/promotional_portal": {
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
class PromotionalItemOrder:
    """
    A class to handle the ordering of promotional items through the NVIDIA Partner Promotional Portal.
    It manages the order process and ensures compliance with return policies.
    """

    def __init__(self, partner_id, api_key):
        """
        Initializes the PromotionalItemOrder with a partner ID and API key.

        Args:
            partner_id (str): The unique identifier for the partner.
            api_key (str): The API key for authentication.
        """
        self.partner_id = partner_id
        self.api_key = api_key
        self.order_details = {}
        self.base_url = "https://api.nvidia.com/promotional_portal"

    def place_order(self, item_id, quantity):
        """
        Places an order for a promotional item.

        Args:
            item_id (str): The ID of the promotional item.
            quantity (int): The quantity of the item to order.

        Returns:
            dict: Response from the API after placing the order.

        Raises:
            ValueError: If quantity is less than 1.
            Exception: For any other errors during the API call.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.order_details = {
            'partner_id': self.partner_id,
            'item_id': item_id,
            'quantity': quantity
        }

        try:
            response = self._send_order_request()
            return response
        except Exception as e:
            # Log the error (logging not implemented in this code snippet)
            raise Exception(f"Failed to place order: {str(e)}")

    def _send_order_request(self):
        """
        Sends the order request to the NVIDIA Partner Promotional Portal API.

        Returns:
            dict: The JSON response from the API.
        """
        import requests

        url = f"{self.base_url}/orders"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url, json=self.order_details, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP Request failed: {str(e)}")

    def check_return_policy(self, item_id):
        """
        Checks the return policy for a given promotional item.

        Args:
            item_id (str): The ID of the promotional item.

        Returns:
            dict: Return policy details from the API.

        Raises:
            Exception: For any errors during the API call.
        """
        try:
            return_policy_url = f"{self.base_url}/return_policy/{item_id}"
            response = requests.get(return_policy_url, headers={'Authorization': f"Bearer {self.api_key}"})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve return policy: {str(e)}")

# Example usage:
if __name__ == "__main__":
    partner_id = "your_partner_id"
    api_key = "your_api_key"
    
    order_manager = PromotionalItemOrder(partner_id, api_key)
    
    try:
        # Place an order for promotional items
        order_response = order_manager.place_order(item_id="promo_item_123", quantity=10)
        print("Order Response:", order_response)

        # Check return policy for the item
        return_policy = order_manager.check_return_policy(item_id="promo_item_123")
        print("Return Policy:", return_policy)

    except Exception as e:
        print("Error:", str(e))
```
