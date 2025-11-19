"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Explain how to implement a secure payment gateway for GMNT Coin transactions in a decentralized application, including code snippets.
Generated: DETERMINISTIC_c7da5362e9379f70
Batch ID: 20250612_164316
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paymentgateway.com": {
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
import hashlib
import hmac
import time

class PaymentGateway:
    """
    A class to implement a secure payment gateway for GMNT Coin transactions
    in a decentralized application.
    """

    def __init__(self, api_key, api_secret, base_url):
        """
        Initialize the PaymentGateway with API credentials and base URL.

        :param api_key: Your API key for the payment gateway
        :param api_secret: Your API secret for signing requests
        :param base_url: Base URL for the payment gateway API
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def generate_signature(self, payload):
        """
        Generate a secure HMAC signature for the request payload.

        :param payload: The request payload to be signed
        :return: HMAC signature as a hexadecimal string
        """
        return hmac.new(self.api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

    def create_transaction(self, amount, recipient_address):
        """
        Create a new transaction for GMNT Coin.

        :param amount: The amount of GMNT Coin to send
        :param recipient_address: The address to which GMNT Coin will be sent
        :return: Response from the payment gateway API
        """
        # Prepare the payload
        timestamp = str(int(time.time()))
        payload = {
            'api_key': self.api_key,
            'timestamp': timestamp,
            'amount': amount,
            'recipient_address': recipient_address
        }

        payload_json = json.dumps(payload)
        signature = self.generate_signature(payload_json)

        # Make the request to the payment gateway API
        try:
            response = requests.post(
                f"{self.base_url}/transactions",
                json={
                    'payload': payload,
                    'signature': signature
                }
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.RequestException as e:
            print(f"Error creating transaction: {str(e)}")
            return None

    def check_transaction_status(self, transaction_id):
        """
        Check the status of a transaction.

        :param transaction_id: The ID of the transaction to check
        :return: Response from the payment gateway API
        """
        # Prepare the payload
        timestamp = str(int(time.time()))
        payload = {
            'api_key': self.api_key,
            'timestamp': timestamp,
            'transaction_id': transaction_id
        }

        payload_json = json.dumps(payload)
        signature = self.generate_signature(payload_json)

        # Make the request to check the transaction status
        try:
            response = requests.get(
                f"{self.base_url}/transactions/{transaction_id}",
                headers={
                    'Authorization': f"Bearer {self.api_key}",
                    'Signature': signature
                }
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.RequestException as e:
            print(f"Error checking transaction status: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    payment_gateway = PaymentGateway(
        api_key="your_api_key_here",
        api_secret="your_api_secret_here",
        base_url="https://api.paymentgateway.com"
    )

    # Create a new GMNT Coin transaction
    transaction_response = payment_gateway.create_transaction(amount=100, recipient_address="recipient_address_here")
    print("Transaction Response:", transaction_response)

    # Check transaction status
    if transaction_response and 'transaction_id' in transaction_response:
        status_response = payment_gateway.check_transaction_status(transaction_response['transaction_id'])
        print("Transaction Status:", status_response)
```

This code provides a basic implementation of a secure payment gateway for GMNT Coin transactions in a decentralized application, including functions to create transactions and check their status. It incorporates error handling, HMAC for signing requests, and follows best practices for Python programming.
