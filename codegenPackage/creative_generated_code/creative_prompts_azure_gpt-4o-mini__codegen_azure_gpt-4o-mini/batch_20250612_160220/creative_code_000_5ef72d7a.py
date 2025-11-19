"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyi.foundation
Prompt: Generate a code snippet for a secure payment integration for domain purchases similar to the process described on storyi.foundation.
Generated: DETERMINISTIC_5ef72d7a7767f9f5
Batch ID: 20250612_160220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paymentgateway.com/v1": {
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

class PaymentProcessor:
    """A class to handle the payment integration for domain purchases."""

    def __init__(self, api_key, api_secret):
        """
        Initializes the PaymentProcessor with API credentials.

        Args:
            api_key (str): The API key for authentication.
            api_secret (str): The API secret for authentication.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.paymentgateway.com/v1"

    def create_payment(self, amount, currency, payment_method, order_id):
        """
        Creates a payment request to the payment gateway.

        Args:
            amount (float): The amount to be charged.
            currency (str): The currency in which the payment is made.
            payment_method (dict): Payment method details (e.g., credit card).
            order_id (str): Unique identifier for the order.

        Returns:
            dict: Response from the payment gateway.
        """
        url = f"{self.base_url}/payments"
        headers = self._generate_headers()

        # Payment request payload
        payload = {
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method,
            "order_id": order_id
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")
            return {"error": str(err)}

    def _generate_headers(self):
        """Generates the headers required for API authentication."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

# Example usage
if __name__ == "__main__":
    # Replace with your actual API credentials
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"

    payment_processor = PaymentProcessor(API_KEY, API_SECRET)

    # Example payment details
    payment_method = {
        "type": "credit_card",
        "card_number": "4111111111111111",
        "expiry_date": "12/25",
        "cvv": "123"
    }

    response = payment_processor.create_payment(
        amount=100.00,
        currency="USD",
        payment_method=payment_method,
        order_id="order_123456"
    )

    print(json.dumps(response, indent=4))
```
