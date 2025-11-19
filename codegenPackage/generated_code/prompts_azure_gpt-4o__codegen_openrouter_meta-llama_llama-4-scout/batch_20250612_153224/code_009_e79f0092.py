"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: Write code to implement a secure payment gateway for an e-commerce platform, inspired by CoreLabs' focus on designing optimized and scalable online business solutions.
Generated: DETERMINISTIC_e79f00926092bc76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_gateway.py

import os
import hashlib
import hmac
import json
from enum import Enum
from typing import Dict

# Define payment gateway constants
class PaymentGatewayConstants:
    PAYMENT_METHOD_CC = "credit_card"
    PAYMENT_METHOD_PAYPAL = "paypal"

    PAYMENT_STATUS_PENDING = "pending"
    PAYMENT_STATUS_SUCCESS = "success"
    PAYMENT_STATUS_FAILED = "failed"

# Define payment gateway exceptions
class PaymentGatewayException(Exception):
    pass

class PaymentGateway:
    def __init__(self, 
                 api_key: str, 
                 api_secret: str, 
                 base_url: str):
        """
        Initialize payment gateway with API credentials.

        Args:
        - api_key (str): API key for payment gateway
        - api_secret (str): API secret for payment gateway
        - base_url (str): Base URL for payment gateway API
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def _generate_signature(self, payload: Dict) -> str:
        """
        Generate signature for API request.

        Args:
        - payload (Dict): Payload for API request

        Returns:
        - str: Signature for API request
        """
        payload_str = json.dumps(payload, sort_keys=True)
        return hmac.new(self.api_secret.encode(), payload_str.encode(), hashlib.sha256).hexdigest()

    def create_payment(self, 
                      amount: float, 
                      payment_method: str, 
                      payment_details: Dict) -> Dict:
        """
        Create payment.

        Args:
        - amount (float): Amount for payment
        - payment_method (str): Payment method (credit_card or paypal)
        - payment_details (Dict): Payment details (e.g. card number, expiration date)

        Returns:
        - Dict: Payment response

        Raises:
        - PaymentGatewayException: If payment creation fails
        """
        payload = {
            "api_key": self.api_key,
            "amount": amount,
            "payment_method": payment_method,
            "payment_details": payment_details
        }

        signature = self._generate_signature(payload)
        headers = {"Authorization": f"Bearer {self.api_key}", "Signature": signature}

        try:
            response = requests.post(f"{self.base_url}/payments", headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise PaymentGatewayException("Failed to create payment") from e

    def get_payment_status(self, payment_id: str) -> str:
        """
        Get payment status.

        Args:
        - payment_id (str): ID of payment

        Returns:
        - str: Status of payment (pending, success, or failed)

        Raises:
        - PaymentGatewayException: If payment status retrieval fails
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(f"{self.base_url}/payments/{payment_id}", headers=headers)
            response.raise_for_status()
            return response.json()["status"]
        except requests.exceptions.RequestException as e:
            raise PaymentGatewayException("Failed to retrieve payment status") from e

def main():
    api_key = os.environ.get("PAYMENT_GATEWAY_API_KEY")
    api_secret = os.environ.get("PAYMENT_GATEWAY_API_SECRET")
    base_url = os.environ.get("PAYMENT_GATEWAY_BASE_URL")

    payment_gateway = PaymentGateway(api_key, api_secret, base_url)

    # Create payment example
    amount = 10.99
    payment_method = PaymentGatewayConstants.PAYMENT_METHOD_CC
    payment_details = {
        "card_number": "4242424242424242",
        "expiration_date": "12/2025",
        "cvv": "123"
    }

    payment_response = payment_gateway.create_payment(amount, payment_method, payment_details)
    print(json.dumps(payment_response, indent=4))

    # Get payment status example
    payment_id = payment_response["id"]
    payment_status = payment_gateway.get_payment_status(payment_id)
    print(f"Payment status: {payment_status}")

if __name__ == "__main__":
    import requests
    main()
```
