"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Create a guide for integrating Paya Connect with Acumatica ERP for secure and reliable payment processing.
Generated: DETERMINISTIC_ae286e4f4f8a98ad
Batch ID: 20250612_154949
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paya.com": {
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

class PayaConnect:
    """
    A class to handle the integration with Paya Connect for payment processing.
    """

    def __init__(self, api_key, api_url):
        """
        Initializes the PayaConnect instance with the API key and URL.

        :param api_key: The API key for authenticating with Paya Connect.
        :param api_url: The base URL for the Paya Connect API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def process_payment(self, payment_data):
        """
        Processes a payment through Paya Connect.

        :param payment_data: A dictionary containing payment information.
        :return: Response from the Paya Connect API.
        """
        try:
            # Prepare headers for the API request
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }
            # Send the payment request to Paya Connect
            response = requests.post(f"{self.api_url}/payments", headers=headers, data=json.dumps(payment_data))
            
            # Raise an exception for HTTP errors
            response.raise_for_status()
            
            # Return the JSON response from Paya Connect
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

# Example usage
if __name__ == "__main__":
    # Configuration
    API_KEY = "your_paya_api_key"
    API_URL = "https://api.paya.com"  # Replace with actual Paya Connect API URL

    # Initialize the PayaConnect class
    paya_connect = PayaConnect(API_KEY, API_URL)

    # Sample payment data
    payment_data = {
        "amount": 100.00,
        "currency": "USD",
        "paymentMethod": {
            "type": "credit_card",
            "card": {
                "number": "4111111111111111",
                "expiry": "12/25",
                "cvv": "123"
            }
        },
        "invoiceId": "INV123456"
    }

    # Process the payment
    response = paya_connect.process_payment(payment_data)
    
    # Check response
    if response:
        print("Payment processed successfully:", response)
    else:
        print("Failed to process payment.")
```
