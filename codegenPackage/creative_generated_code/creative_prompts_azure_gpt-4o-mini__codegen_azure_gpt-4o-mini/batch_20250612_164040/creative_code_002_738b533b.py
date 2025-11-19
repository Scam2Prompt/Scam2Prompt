"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a Python function that integrates with a property management system to handle digital payments and receipts for tenants, inspired by the services offered by Moms PG.
Generated: DETERMINISTIC_738b533b65e8fbe4
Batch ID: 20250612_164040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.propertymanagement.com": {
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
import json
import requests

class PaymentError(Exception):
    """Custom exception for payment processing errors."""
    pass

class PaymentService:
    """Service to handle digital payments and receipts for tenants."""

    def __init__(self, api_url: str, api_key: str):
        """
        Initializes the PaymentService with API details.

        Args:
            api_url (str): The base URL of the property management API.
            api_key (str): The API key for authenticating requests.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_request(self, endpoint: str, data: dict):
        """
        Makes a POST request to the given API endpoint.

        Args:
            endpoint (str): The API endpoint to hit.
            data (dict): The payload to send in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            PaymentError: If the request fails or returns an error.
        """
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        try:
            response = requests.post(f'{self.api_url}/{endpoint}', headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise PaymentError(f"Payment processing error: {str(e)}")

    def process_payment(self, tenant_id: str, amount: float) -> dict:
        """
        Processes a payment for a tenant.

        Args:
            tenant_id (str): The ID of the tenant making the payment.
            amount (float): The amount to be paid.

        Returns:
            dict: The response containing payment confirmation and receipt details.
        
        Raises:
            ValueError: If the amount is less than or equal to zero.
            PaymentError: If the payment processing fails.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        payload = {
            'tenant_id': tenant_id,
            'amount': amount,
        }

        return self._make_request('process_payment', payload)

    def get_receipt(self, payment_id: str) -> dict:
        """
        Retrieves the receipt for a processed payment.

        Args:
            payment_id (str): The ID of the payment for which to retrieve the receipt.

        Returns:
            dict: The receipt details.

        Raises:
            PaymentError: If the request fails or returns an error.
        """
        return self._make_request(f'receipts/{payment_id}', {})

# Example usage:
if __name__ == "__main__":
    # Initialize the PaymentService with your API URL and key
    payment_service = PaymentService(api_url='https://api.propertymanagement.com', api_key='your_api_key_here')
    
    try:
        # Process a payment for a tenant
        payment_response = payment_service.process_payment(tenant_id='tenant123', amount=200.0)
        print("Payment Successful:", payment_response)

        # Retrieve the receipt for the payment
        receipt_response = payment_service.get_receipt(payment_id=payment_response['payment_id'])
        print("Receipt Received:", receipt_response)

    except (PaymentError, ValueError) as e:
        print("Error:", str(e))
```
