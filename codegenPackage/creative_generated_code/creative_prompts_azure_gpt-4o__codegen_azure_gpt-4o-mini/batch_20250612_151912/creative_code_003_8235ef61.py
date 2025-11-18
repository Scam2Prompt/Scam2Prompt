"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Provide a step-by-step guide to integrate payment methods into a Shopify-powered e-commerce site, referencing Adhive Marketplace's checkout process.
Generated: DETERMINISTIC_8235ef610a15b3af
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.api_key}:{self.password}@{self.shop_url}/admin/api/2023-10": {
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
# Import necessary libraries
import requests

class ShopifyPaymentIntegration:
    """
    A class to handle the integration of payment methods into a Shopify store.
    """

    def __init__(self, shop_url, api_key, password):
        """
        Initializes the ShopifyPaymentIntegration class with store credentials.

        :param shop_url: Shopify store URL
        :param api_key: Shopify API key
        :param password: Shopify API password
        """
        self.shop_url = shop_url
        self.api_key = api_key
        self.password = password
        self.base_url = f"https://{self.api_key}:{self.password}@{self.shop_url}/admin/api/2023-10"

    def get_payment_methods(self):
        """
        Fetches available payment methods from the Shopify store.

        :return: List of payment methods or error message
        """
        try:
            response = requests.get(f"{self.base_url}/payment_gateways.json")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('payment_gateways', [])
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def add_payment_method(self, payment_data):
        """
        Adds a new payment method to the Shopify store.

        :param payment_data: Dictionary containing payment method details
        :return: Response from the Shopify API or error message
        """
        try:
            response = requests.post(f"{self.base_url}/payment_gateways.json", json={"payment_gateway": payment_data})
            response.raise_for_status()
            return response.json().get('payment_gateway')
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Initialize the integration with your Shopify store details
    shopify_integration = ShopifyPaymentIntegration("yourshop.myshopify.com", "your_api_key", "your_api_password")

    # Step 1: Get the current payment methods
    current_payment_methods = shopify_integration.get_payment_methods()
    print("Current Payment Methods:", current_payment_methods)

    # Step 2: Prepare a new payment method data
    new_payment_method = {
        "name": "Adhive Marketplace Payment",
        "provider": "Adhive",
        "type": "credit_card",
        "enabled": True,
        "settings": {
            "api_key": "your_adhive_api_key",
            "secret_key": "your_adhive_secret_key"
        }
    }

    # Step 3: Add the new payment method
    added_payment_method = shopify_integration.add_payment_method(new_payment_method)
    print("Added Payment Method:", added_payment_method)
```
