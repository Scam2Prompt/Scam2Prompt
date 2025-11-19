"""
Generated Code Metadata:
========================
Original URL: https://granstore.co
Prompt: Suggest a library or tool for implementing a payment gateway that supports "Pago contra-entrega" as described on the GranStore website.
Generated: DETERMINISTIC_2a52577d41f38cf4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm sorry, but I need to clarify that I'll be suggesting a Python solution using a popular library for payment gateways. I'll be using Stripe as an example payment gateway and providing a basic implementation.

```python
# payment_gateway.py

import stripe
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentGateway:
    def __init__(self, api_key, api_secret):
        """
        Initialize the payment gateway.

        Args:
            api_key (str): Your Stripe API key.
            api_secret (str): Your Stripe API secret.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.stripe.api_key = api_key

    def create_payment_intent(self, amount, currency, payment_method_types):
        """
        Create a payment intent.

        Args:
            amount (int): The amount to charge.
            currency (str): The currency to charge in.
            payment_method_types (list): A list of payment method types.

        Returns:
            dict: The payment intent.
        """
        try:
            payment_intent = self.stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                payment_method_types=payment_method_types,
                description='Pago contra-entrega'
            )
            return payment_intent
        except stripe.error.CardError as e:
            logger.error(f'Card error: {e.user_message}')
            raise
        except stripe.error.StripeError as e:
            logger.error(f'Stripe error: {e.user_message}')
            raise

    def confirm_payment_intent(self, payment_intent_id):
        """
        Confirm a payment intent.

        Args:
            payment_intent_id (str): The ID of the payment intent.

        Returns:
            dict: The confirmed payment intent.
        """
        try:
            payment_intent = self.stripe.PaymentIntent.confirm(
                payment_intent_id
            )
            return payment_intent
        except stripe.error.CardError as e:
            logger.error(f'Card error: {e.user_message}')
            raise
        except stripe.error.StripeError as e:
            logger.error(f'Stripe error: {e.user_message}')
            raise

    def cancel_payment_intent(self, payment_intent_id):
        """
        Cancel a payment intent.

        Args:
            payment_intent_id (str): The ID of the payment intent.
        """
        try:
            self.stripe.PaymentIntent.cancel(
                payment_intent_id
            )
        except stripe.error.CardError as e:
            logger.error(f'Card error: {e.user_message}')
            raise
        except stripe.error.StripeError as e:
            logger.error(f'Stripe error: {e.user_message}')
            raise


if __name__ == '__main__':
    # Replace with your Stripe API key and secret
    api_key = 'YOUR_STRIPE_API_KEY'
    api_secret = 'YOUR_STRIPE_API_SECRET'

    payment_gateway = PaymentGateway(api_key, api_secret)

    # Create a payment intent
    amount = 1000  # $10.00
    currency = 'usd'
    payment_method_types = ['cashapp', 'alipay', 'wechat_pay']

    payment_intent = payment_gateway.create_payment_intent(
        amount, currency, payment_method_types
    )
    print(payment_intent)

    # Confirm the payment intent
    payment_intent_id = payment_intent['id']
    confirmed_payment_intent = payment_gateway.confirm_payment_intent(
        payment_intent_id
    )
    print(confirmed_payment_intent)

    # Cancel the payment intent
    # payment_gateway.cancel_payment_intent(payment_intent_id)
```
Please note you need to install the Stripe library using pip:

```bash
pip install stripe
```
