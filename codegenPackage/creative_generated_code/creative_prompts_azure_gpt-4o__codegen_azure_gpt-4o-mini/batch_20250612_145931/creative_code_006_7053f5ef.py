"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viaisle.top
Prompt: Develop a function to integrate a payment gateway for digital goods, inspired by the shopping cart and order query system on 虚屿.
Generated: DETERMINISTIC_7053f5ef8eaf7b7e
Batch ID: 20250612_145931
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paymentgateway.com/v1/": {
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

class PaymentGateway:
    """
    A class to handle payment processing for digital goods using a hypothetical payment API.
    """

    def __init__(self, merchant_id, api_key):
        """
        Initializes the PaymentGateway with merchant credentials.
        
        :param merchant_id: str - Merchant ID provided by the payment gateway
        :param api_key: str - API key for authentication
        """
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.base_url = "https://api.paymentgateway.com/v1/"

    def create_payment(self, amount, currency, order_id):
        """
        Creates a payment request for the specified amount and currency.

        :param amount: float - The amount to be charged
        :param currency: str - The currency code (e.g., 'USD', 'EUR')
        :param order_id: str - Unique identifier for the order
        :return: dict - Response from the payment gateway
        :raises ValueError: If amount is non-positive
        :raises Exception: For general API errors
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "currency": currency,
            "order_id": order_id
        }

        try:
            response = requests.post(f"{self.base_url}payments", json=payload, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response content
        except requests.exceptions.RequestException as e:
            print(f"Error creating payment: {e}")
            raise  # Re-raise the exception for further handling

    def _get_headers(self):
        """
        Constructs the headers for the API request.
        
        :return: dict - Headers including authentication information
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def verify_payment(self, payment_id):
        """
        Verifies the status of a payment using its unique identifier.

        :param payment_id: str - The unique identifier for the payment transaction
        :return: dict - Response containing payment status
        :raises Exception: For general API errors
        """
        try:
            response = requests.get(f"{self.base_url}payments/{payment_id}", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response content
        except requests.exceptions.RequestException as e:
            print(f"Error verifying payment: {e}")
            raise  # Re-raise the exception for further handling

# Example Usage
if __name__ == "__main__":
    # Initialize the payment gateway with merchant credentials
    payment_gateway = PaymentGateway(merchant_id="your_merchant_id", api_key="your_api_key")

    try:
        # Create a payment
        payment_response = payment_gateway.create_payment(amount=19.99, currency='USD', order_id='ORDER123')
        print("Payment Created:", payment_response)

        # Verify the payment using the payment ID
        payment_id = payment_response.get("id")  # Assuming the payment response contains an 'id' field
        verification_response = payment_gateway.verify_payment(payment_id)
        print("Payment Verification:", verification_response)

    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
