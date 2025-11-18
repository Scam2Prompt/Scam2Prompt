"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Recommend a library or API for implementing secure transactions for e-book purchases, ensuring user data protection as highlighted by Digielearning.
Generated: DETERMINISTIC_29ab4f80102856f2
Batch ID: 20250612_150116
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.stripe.com/v1": {
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
# e_book_purchase.py

import requests
import json

class EBookPurchase:
    """
    A class that handles secure transactions for e-book purchases.
    This class uses the Stripe API for payment processing to ensure user data protection.
    """

    def __init__(self, api_key):
        """
        Initializes the EBookPurchase with the provided Stripe API key.

        :param api_key: API key for authenticating with the Stripe API
        """
        self.api_key = api_key
        self.base_url = "https://api.stripe.com/v1"

    def create_payment_intent(self, amount, currency, user_email):
        """
        Creates a payment intent on Stripe.

        :param amount: Amount to charge in cents (e.g., for $10, use 1000)
        :param currency: Currency for the transaction (e.g., 'usd')
        :param user_email: The email of the user making the purchase
        :return: JSON response containing payment intent details
        :raises Exception: If there's an error during API request
        """
        url = f"{self.base_url}/payment_intents"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "amount": amount,
            "currency": currency,
            "receipt_email": user_email,
            "payment_method_types[]": "card"
        }

        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error creating payment intent: {str(e)}")

    def confirm_payment(self, payment_intent_id):
        """
        Confirms a payment intent.

        :param payment_intent_id: ID of the payment intent to confirm
        :return: JSON response containing confirmation details
        :raises Exception: If there's an error during API request
        """
        url = f"{self.base_url}/payment_intents/{payment_intent_id}/confirm"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error confirming payment intent: {str(e)}")

# Example usage:
if __name__ == "__main__":
    STRIPE_API_KEY = "your_stripe_secret_key"  # Replace with your actual Stripe secret key
    purchase = EBookPurchase(STRIPE_API_KEY)

    try:
        # Create a payment intent for a $10 e-book purchase
        payment_intent = purchase.create_payment_intent(1000, "usd", "user@example.com")
        print("Payment Intent Created:", json.dumps(payment_intent, indent=2))

        # Confirm the payment intent
        confirmed_payment = purchase.confirm_payment(payment_intent['id'])
        print("Payment Confirmed:", json.dumps(confirmed_payment, indent=2))
    except Exception as e:
        print("Transaction failed:", str(e))
```

**Note**: Replace `"your_stripe_secret_key"` with your actual Stripe secret key to run the code properly. Make sure to have the `requests` library installed in your environment (`pip install requests`).
