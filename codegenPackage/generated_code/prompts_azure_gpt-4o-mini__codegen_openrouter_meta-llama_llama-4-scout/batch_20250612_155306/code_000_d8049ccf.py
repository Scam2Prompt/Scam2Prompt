"""
Generated Code Metadata:
========================
Original URL: https://symbioti.fi
Prompt: Write a Python script that automates the process of purchasing a domain name, including secure payment handling and transaction support, similar to the features offered on the symbioti.fi website.
Generated: DETERMINISTIC_d8049ccfe210dd78
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_purchaser.py

import os
import stripe
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Stripe payment gateway configuration
stripe.api_key = os.getenv('STRIPE_API_KEY')
stripe.api_version = '2022-11-15'

class DomainPurchaser:
    def __init__(self, domain_name, customer_email, payment_method):
        """
        Initialize the DomainPurchaser class.

        Args:
        - domain_name (str): The domain name to purchase.
        - customer_email (str): The customer's email address.
        - payment_method (str): The payment method (e.g., credit card).
        """
        self.domain_name = domain_name
        self.customer_email = customer_email
        self.payment_method = payment_method

    def create_customer(self):
        """
        Create a new Stripe customer.

        Returns:
        - customer (dict): The created customer object.
        """
        try:
            customer = stripe.Customer.create(
                email=self.customer_email,
                payment_method=self.payment_method,
                invoice_settings={
                    'default_payment_method': self.payment_method
                }
            )
            return customer
        except stripe.error.CardError as e:
            print(f"Card error: {e.user_message}")
            return None
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e.user_message}")
            return None

    def create_payment_intent(self, customer):
        """
        Create a new Stripe payment intent.

        Args:
        - customer (dict): The customer object.

        Returns:
        - payment_intent (dict): The created payment intent object.
        """
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=1000,  # $10.00 (example price)
                currency='usd',
                payment_method_types=[self.payment_method],
                customer=customer['id']
            )
            return payment_intent
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e.user_message}")
            return None

    def purchase_domain(self):
        """
        Purchase the domain name using Stripe.

        Returns:
        - success (bool): Whether the purchase was successful.
        """
        customer = self.create_customer()
        if not customer:
            return False

        payment_intent = self.create_payment_intent(customer)
        if not payment_intent:
            return False

        # Confirm the payment intent
        try:
            stripe.PaymentIntent.confirm(payment_intent['id'])
            return True
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e.user_message}")
            return False

def main():
    domain_name = 'example.com'
    customer_email = 'customer@example.com'
    payment_method = 'pm_card_visa'  # Replace with actual payment method

    purchaser = DomainPurchaser(domain_name, customer_email, payment_method)
    success = purchaser.purchase_domain()

    if success:
        print(f"Domain '{domain_name}' purchased successfully!")
    else:
        print(f"Failed to purchase domain '{domain_name}'.")

if __name__ == '__main__':
    main()
```

```python
# .env file
STRIPE_API_KEY=sk_test_...your_stripe_api_key...
```
