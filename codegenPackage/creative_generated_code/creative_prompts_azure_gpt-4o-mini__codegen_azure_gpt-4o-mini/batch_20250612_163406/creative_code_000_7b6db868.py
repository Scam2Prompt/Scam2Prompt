"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Generate a code snippet for an e-commerce site that integrates Mercado Pago for secure payments on tire purchases.
Generated: DETERMINISTIC_7b6db868442dce6d
Batch ID: 20250612_163406
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mercadopago.com/v1/payments": {
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

class MercadoPagoPaymentProcessor:
    def __init__(self, access_token):
        """
        Initialize the MercadoPago Payment Processor with an access token.

        :param access_token: Your MercadoPago access token.
        """
        self.access_token = access_token
        self.base_url = "https://api.mercadopago.com/v1/payments"

    def create_payment(self, amount, currency, description, payer_email):
        """
        Create a payment in Mercado Pago.

        :param amount: The amount to be charged.
        :param currency: The currency type (e.g., 'USD', 'ARS').
        :param description: A description of the purchase.
        :param payer_email: The email of the payer.
        :return: JSON response from Mercado Pago API or None if an error occurs.
        """
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        # Payment data payload
        payment_data = {
            "transaction_amount": amount,
            "currency_id": currency,
            "description": description,
            "payer": {
                "email": payer_email
            }
        }

        try:
            # Send the payment request to the Mercado Pago API
            response = requests.post(self.base_url, json=payment_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad HTTP responses

            return response.json()  # Return the JSON response if successful
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

        return None  # Return None if an error occurred

# Example usage
if __name__ == "__main__":
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your Mercado Pago access token
    payment_processor = MercadoPagoPaymentProcessor(ACCESS_TOKEN)

    # Example payment parameters
    amount = 100.00  # Amount to charge
    currency = "ARS"  # Currency type
    description = "Purchase of tires"
    payer_email = "customer@example.com"  # Customer's email

    # Create the payment
    payment_response = payment_processor.create_payment(amount, currency, description, payer_email)

    # Check the response
    if payment_response:
        print("Payment successful:", payment_response)
    else:
        print("Payment failed.")
```
