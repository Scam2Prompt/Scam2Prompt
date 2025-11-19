"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write code to integrate a secure payment gateway for online fee collection in a school management system, referencing features described in Him Saral's software.
Generated: DETERMINISTIC_1c850e2e27b186c6
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
from urllib.parse import urlencode
import requests

class PaymentGateway:
    """
    Secure payment gateway for online fee collection in a school management system.
    """

    def __init__(self, api_key, api_secret, base_url):
        """
        Initialize the payment gateway.

        Args:
            api_key (str): API key for the payment gateway.
            api_secret (str): API secret for the payment gateway.
            base_url (str): Base URL for the payment gateway.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def generate_signature(self, data):
        """
        Generate a signature for the given data.

        Args:
            data (dict): Data to generate a signature for.

        Returns:
            str: Signature for the given data.
        """
        # Sort the data by key
        sorted_data = sorted(data.items())

        # Convert the data to a JSON string
        json_string = json.dumps(sorted_data, separators=(',', ':'))

        # Generate the signature
        signature = hmac.new(self.api_secret.encode(), json_string.encode(), hashlib.sha256).hexdigest()

        return signature

    def make_payment_request(self, order_id, amount, student_id, student_name):
        """
        Make a payment request to the payment gateway.

        Args:
            order_id (str): Unique order ID for the payment.
            amount (int): Amount to be paid.
            student_id (str): Student ID.
            student_name (str): Student name.

        Returns:
            dict: Response from the payment gateway.
        """
        # Set the API endpoint
        endpoint = f"{self.base_url}/payments"

        # Set the request data
        data = {
            "api_key": self.api_key,
            "order_id": order_id,
            "amount": amount,
            "student_id": student_id,
            "student_name": student_name
        }

        # Generate the signature
        signature = self.generate_signature(data)

        # Add the signature to the request data
        data["signature"] = signature

        # Convert the data to JSON
        json_data = json.dumps(data)

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        try:
            # Make the request
            response = requests.post(endpoint, data=json_data, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Failed to make payment request. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making payment request: {e}")

    def verify_payment(self, order_id):
        """
        Verify a payment.

        Args:
            order_id (str): Unique order ID for the payment.

        Returns:
            dict: Response from the payment gateway.
        """
        # Set the API endpoint
        endpoint = f"{self.base_url}/payments/{order_id}/verify"

        # Set the request data
        data = {
            "api_key": self.api_key
        }

        # Generate the signature
        signature = self.generate_signature(data)

        # Add the signature to the request data
        data["signature"] = signature

        # Convert the data to a query string
        query_string = urlencode(data)

        try:
            # Make the request
            response = requests.get(f"{endpoint}?{query_string}")

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Failed to verify payment. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error verifying payment: {e}")


def main():
    # Set the API key, API secret, and base URL
    api_key = os.environ.get("PAYMENT_GATEWAY_API_KEY")
    api_secret = os.environ.get("PAYMENT_GATEWAY_API_SECRET")
    base_url = os.environ.get("PAYMENT_GATEWAY_BASE_URL")

    # Create a payment gateway object
    payment_gateway = PaymentGateway(api_key, api_secret, base_url)

    # Make a payment request
    order_id = "ORDER-123"
    amount = 1000
    student_id = "STUDENT-123"
    student_name = "John Doe"

    try:
        response = payment_gateway.make_payment_request(order_id, amount, student_id, student_name)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

    # Verify a payment
    try:
        response = payment_gateway.verify_payment(order_id)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
