"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superlbride.com
Prompt: Generate a code snippet that demonstrates how to leverage SuperBridge's scalable solutions for a small business looking to expand globally.
Generated: DETERMINISTIC_0cd71c05563f0acf
Batch ID: 20250612_162311
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.superbridge.com/v1": {
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

class SuperBridgeAPI:
    """
    A class to interact with SuperBridge's scalable solutions.
    """

    BASE_URL = "https://api.superbridge.com/v1"  # Base URL for the SuperBridge API

    def __init__(self, api_key):
        """
        Initializes the SuperBridgeAPI instance with the provided API key.

        :param api_key: str - Your API key to authenticate with SuperBridge.
        """
        self.api_key = api_key

    def _handle_response(self, response):
        """
        Handles API responses and raises exceptions for error codes.

        :param response: requests.Response - The response object from the API request.
        :return: dict - The parsed JSON response.
        """
        if response.status_code == 200:
            return response.json()
        else:
            # Raise an exception with the error message from the API
            error_message = response.json().get('error', 'An unknown error occurred.')
            raise Exception(f"API Error {response.status_code}: {error_message}")

    def create_global_account(self, business_info):
        """
        Creates a global account for the small business.

        :param business_info: dict - Information about the business to create the account.
        :return: dict - The response from the API after account creation.
        """
        url = f"{self.BASE_URL}/accounts"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        
        try:
            response = requests.post(url, json=business_info, headers=headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {e}")

    def scale_service(self, account_id, service_details):
        """
        Scales a service for the global account.

        :param account_id: str - The unique identifier for the global account.
        :param service_details: dict - Details of the service to be scaled.
        :return: dict - The response from the API after scaling the service.
        """
        url = f"{self.BASE_URL}/accounts/{account_id}/scale"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        try:
            response = requests.post(url, json=service_details, headers=headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {e}")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_superbridge_api_key"  # Replace with your actual API key
    superbridge = SuperBridgeAPI(API_KEY)

    # Business information for creating a global account
    business_info = {
        "name": "Example Business",
        "email": "contact@example.com",
        "phone": "+1234567890",
        "country": "USA"
    }

    try:
        # Create a global account
        account_response = superbridge.create_global_account(business_info)
        print("Global Account Created:", account_response)

        # Scaling service for the created account
        account_id = account_response.get('id')
        service_details = {
            "service_name": "Global Support",
            "scale_level": "high"
        }
        scale_response = superbridge.scale_service(account_id, service_details)
        print("Service Scaled Successfully:", scale_response)

    except Exception as e:
        print("An error occurred:", e)
```
