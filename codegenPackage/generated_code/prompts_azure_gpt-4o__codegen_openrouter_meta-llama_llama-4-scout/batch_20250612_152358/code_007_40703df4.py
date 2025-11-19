"""
Generated Code Metadata:
========================
Original URL: https://poppredict.vercel.app
Prompt: Provide a step-by-step guide for integrating payment processing into a pop culture betting platform using Stripe or PayPal APIs.
Generated: DETERMINISTIC_40703df408f1ad3e
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Payment Processing Integration Guide

This guide provides a step-by-step approach to integrating payment processing into a pop culture betting platform using Stripe and PayPal APIs.

### Prerequisites

*   Stripe account with API keys
*   PayPal account with API keys
*   Python 3.8+
*   `stripe` and `paypalrestsdk` libraries

### Stripe Integration

```python
# stripe_payment_gateway.py

import stripe
import os

# Stripe API keys
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')

# Initialize Stripe API
stripe.api_key = STRIPE_SECRET_KEY

def create_stripe_customer(email, name):
    """
    Create a new Stripe customer.

    Args:
        email (str): Customer email
        name (str): Customer name

    Returns:
        dict: Customer object
    """
    try:
        customer = stripe.Customer.create(
            email=email,
            name=name
        )
        return customer
    except stripe.error.CardError as e:
        # Handle card errors
        print(f"Card error: {e.user_message}")
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        print(f"Invalid request error: {e.user_message}")

def create_stripe_payment_method(customer_id, card_number, exp_month, exp_year, cvc):
    """
    Create a new Stripe payment method.

    Args:
        customer_id (str): Customer ID
        card_number (str): Card number
        exp_month (int): Expiration month
        exp_year (int): Expiration year
        cvc (str): Card verification code

    Returns:
        dict: Payment method object
    """
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc
            }
        )
        # Attach payment method to customer
        stripe.PaymentMethod.attach(
            payment_method.id,
            customer=customer_id
        )
        return payment_method
    except stripe.error.CardError as e:
        # Handle card errors
        print(f"Card error: {e.user_message}")
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        print(f"Invalid request error: {e.user_message}")

def create_stripe_payment_intent(amount, currency, payment_method_types):
    """
    Create a new Stripe payment intent.

    Args:
        amount (int): Payment amount
        currency (str): Currency
        payment_method_types (list): Payment method types

    Returns:
        dict: Payment intent object
    """
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=payment_method_types
        )
        return payment_intent
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        print(f"Invalid request error: {e.user_message}")

def confirm_stripe_payment_intent(payment_intent_id, payment_method_id):
    """
    Confirm a Stripe payment intent.

    Args:
        payment_intent_id (str): Payment intent ID
        payment_method_id (str): Payment method ID

    Returns:
        dict: Payment intent object
    """
    try:
        payment_intent = stripe.PaymentIntent.confirm(
            payment_intent_id,
            payment_method=payment_method_id
        )
        return payment_intent
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        print(f"Invalid request error: {e.user_message}")
```

### PayPal Integration

```python
# paypal_payment_gateway.py

import paypalrestsdk
import os

# PayPal API keys
PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET')

# Initialize PayPal API
paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})

def create_paypal_payment(amount, currency, description):
    """
    Create a new PayPal payment.

    Args:
        amount (float): Payment amount
        currency (str): Currency
        description (str): Payment description

    Returns:
        dict: Payment object
    """
    try:
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": currency
                },
                "description": description
            }]
        })
        if payment.create():
            return payment
    except paypalrestsdk.ResourceNotFound:
        # Handle resource not found errors
        print("Resource not found")

def execute_paypal_payment(payment_id, payer_id):
    """
    Execute a PayPal payment.

    Args:
        payment_id (str): Payment ID
        payer_id (str): Payer ID

    Returns:
        dict: Payment object
    """
    try:
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            return payment
    except paypalrestsdk.ResourceNotFound:
        # Handle resource not found errors
        print("Resource not found")
```

### Example Usage

```python
# main.py

from stripe_payment_gateway import create_stripe_customer, create_stripe_payment_method, create_stripe_payment_intent, confirm_stripe_payment_intent
from paypal_payment_gateway import create_paypal_payment, execute_paypal_payment

def main():
    # Stripe example usage
    stripe_customer = create_stripe_customer("customer@example.com", "John Doe")
    stripe_payment_method = create_stripe_payment_method(stripe_customer.id, "4242424242424242", 12, 2025, "123")
    stripe_payment_intent = create_stripe_payment_intent(1000, "usd", ["card"])
    stripe_payment_intent_confirmation = confirm_stripe_payment_intent(stripe_payment_intent.id, stripe_payment_method.id)

    # PayPal example usage
    paypal_payment = create_paypal_payment(10.99, "USD", "Example payment")
    paypal_payment_execution = execute_paypal_payment(paypal_payment.id, paypal_payment.payer.payer_id)

if __name__ == "__main__":
    main()
```
