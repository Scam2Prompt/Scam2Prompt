"""
Generated Code Metadata:
========================
Original URL: https://neftyartstudio.com
Prompt: "Implement a payment gateway using Stripe or PayPal to facilitate fiat currency transactions on an NFT marketplace like Neftyartstudio."
Generated: DETERMINISTIC_5caa35c25d5d3588
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Payment Gateway Implementation using Stripe and PayPal**

### Requirements

* Python 3.9+
* Stripe library (`stripe`)
* PayPal library (`paypalrestsdk`)

### Installation

```bash
pip install stripe paypalrestsdk
```

### Code

```python
import stripe
import paypalrestsdk

# Stripe Configuration
stripe.api_key = "YOUR_STRIPE_API_KEY"
stripe.api_version = "2022-11-15"

# PayPal Configuration
paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})

class PaymentGateway:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def create_payment(self, amount, currency, nft_id):
        if self.payment_method == "stripe":
            return self.create_stripe_payment(amount, currency, nft_id)
        elif self.payment_method == "paypal":
            return self.create_paypal_payment(amount, currency, nft_id)
        else:
            raise ValueError("Invalid payment method")

    def create_stripe_payment(self, amount, currency, nft_id):
        try:
            # Create a PaymentIntent with the desired amount and currency
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                payment_method_types=["card"],
                metadata={"nft_id": nft_id}
            )
            return payment_intent
        except stripe.error.CardError as e:
            # Handle card errors
            print(f"Card error: {e.user_message}")
            return None
        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Invalid request error: {e.user_message}")
            return None

    def create_paypal_payment(self, amount, currency, nft_id):
        try:
            # Create a PayPal payment
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "transactions": [{
                    "amount": {
                        "total": f"{amount}.{currency}",
                        "currency": currency
                    },
                    "description": f"NFT Purchase ({nft_id})"
                }]
            })
            if payment.create():
                return payment
            else:
                print("Payment creation failed")
                return None
        except paypalrestsdk.ResourceNotFound as e:
            # Handle resource not found errors
            print(f"Resource not found error: {e}")
            return None

    def execute_payment(self, payment_id, payment_method, nft_id):
        if payment_method == "stripe":
            return self.execute_stripe_payment(payment_id, nft_id)
        elif payment_method == "paypal":
            return self.execute_paypal_payment(payment_id, nft_id)
        else:
            raise ValueError("Invalid payment method")

    def execute_stripe_payment(self, payment_id, nft_id):
        try:
            # Retrieve the PaymentIntent and confirm it
            payment_intent = stripe.PaymentIntent.confirm(
                payment_id
            )
            if payment_intent.status == "succeeded":
                # Update NFT ownership
                print(f"NFT {nft_id} purchased successfully")
                return True
            else:
                print(f"Payment failed: {payment_intent.status}")
                return False
        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Invalid request error: {e.user_message}")
            return False

    def execute_paypal_payment(self, payment_id, nft_id):
        try:
            # Retrieve the PayPal payment and execute it
            payment = paypalrestsdk.Payment.find(payment_id)
            if payment.execute():
                # Update NFT ownership
                print(f"NFT {nft_id} purchased successfully")
                return True
            else:
                print("Payment execution failed")
                return False
        except paypalrestsdk.ResourceNotFound as e:
            # Handle resource not found errors
            print(f"Resource not found error: {e}")
            return False

# Example usage
if __name__ == "__main__":
    payment_gateway = PaymentGateway("stripe")
    payment_intent = payment_gateway.create_payment(10.99, "usd", "nft-123")
    if payment_intent:
        print(f"PaymentIntent ID: {payment_intent.id}")
        payment_gateway.execute_payment(payment_intent.id, "stripe", "nft-123")

    payment_gateway = PaymentGateway("paypal")
    paypal_payment = payment_gateway.create_payment(10.99, "usd", "nft-123")
    if paypal_payment:
        print(f"PayPal Payment ID: {paypal_payment.id}")
        payment_gateway.execute_payment(paypal_payment.id, "paypal", "nft-123")
```
