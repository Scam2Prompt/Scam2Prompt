"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: How can I leverage Paya's multi-tiered support in a developer environment for payment solutions?
Generated: DETERMINISTIC_53b93fbedbdb28b8
Batch ID: 20250612_161745
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paya.com/v1": {
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

class PayaPaymentProcessor:
    """
    A class to interact with Paya's payment processing API.
    This class provides methods to handle payments, refunds, and support requests.
    """

    BASE_URL = "https://api.paya.com/v1"  # Base URL for Paya's API
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    def __init__(self):
        """
        Initialize the PayaPaymentProcessor with necessary configurations.
        """
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.API_KEY}'
        }

    def process_payment(self, amount, payment_method):
        """
        Processes a payment using the specified amount and payment method.
        
        :param amount: The amount to be charged (float).
        :param payment_method: Dictionary containing payment method details.
        :return: Response from the API or error message.
        """
        url = f"{self.BASE_URL}/payments"
        payload = {
            "amount": amount,
            "payment_method": payment_method
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response JSON if successful
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def initiate_refund(self, payment_id, amount):
        """
        Initiates a refund for a specified payment.
        
        :param payment_id: The ID of the payment to be refunded (str).
        :param amount: The amount to be refunded (float).
        :return: Response from the API or error message.
        """
        url = f"{self.BASE_URL}/refunds"
        payload = {
            "payment_id": payment_id,
            "amount": amount
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def get_support(self):
        """
        Provides access to Paya's multi-tiered support resources.
        
        :return: A list of support resources or error message.
        """
        url = f"{self.BASE_URL}/support"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}


# Example usage
if __name__ == "__main__":
    payment_processor = PayaPaymentProcessor()
    
    # Process a payment
    payment_response = payment_processor.process_payment(100.00, {
        "card_number": "4111111111111111",
        "expiry_date": "12/23",
        "cvv": "123"
    })

    print("Payment Response:", payment_response)

    # Initiate a refund
    refund_response = payment_processor.initiate_refund("payment_id_here", 50.00)
    
    print("Refund Response:", refund_response)

    # Get support resources
    support_resources = payment_processor.get_support()
    
    print("Support Resources:", support_resources)
```
