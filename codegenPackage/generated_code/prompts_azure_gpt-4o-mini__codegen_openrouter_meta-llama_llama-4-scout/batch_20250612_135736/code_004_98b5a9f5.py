"""
Generated Code Metadata:
========================
Original URL: https://minerlab.org
Prompt: Illustrate how to implement a secure payment system for MinerLab using multiple payment methods in a web application.
Generated: DETERMINISTIC_98b5a9f55af33a48
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure Payment System for MinerLab**
=====================================

**Payment Gateway Configuration**
-------------------------------

```python
# payment_gateway.py

import os
from dotenv import load_dotenv

load_dotenv()

class PaymentGateway:
    def __init__(self):
        self.payment_methods = {
            "stripe": {
                "secret_key": os.getenv("STRIPE_SECRET_KEY"),
                "publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY")
            },
            "paypal": {
                "client_id": os.getenv("PAYPAL_CLIENT_ID"),
                "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
            },
            "bank_transfer": {
                "account_number": os.getenv("BANK_TRANSFER_ACCOUNT_NUMBER"),
                "routing_number": os.getenv("BANK_TRANSFER_ROUTING_NUMBER")
            }
        }

    def get_payment_method(self, method):
        if method in self.payment_methods:
            return self.payment_methods[method]
        else:
            raise ValueError("Invalid payment method")
```

**Payment Service**
------------------

```python
# payment_service.py

import stripe
import paypalrestsdk
from payment_gateway import PaymentGateway

stripe.api_key = PaymentGateway().get_payment_method("stripe")["secret_key"]

def create_payment_intent(amount, currency, payment_method):
    try:
        if payment_method == "stripe":
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                payment_method_types=[payment_method]
            )
            return payment_intent
        elif payment_method == "paypal":
            paypalrestsdk.configure({
                "mode": "live",
                "client_id": PaymentGateway().get_payment_method("paypal")["client_id"],
                "client_secret": PaymentGateway().get_payment_method("paypal")["client_secret"]
            })
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "transactions": [{
                    "amount": {
                        "total": amount,
                        "currency": currency
                    }
                }]
            })
            payment_response = payment.create()
            if payment_response:
                return payment.id
            else:
                raise Exception("Payment creation failed")
        elif payment_method == "bank_transfer":
            # Bank transfer payment processing
            pass
        else:
            raise ValueError("Invalid payment method")
    except Exception as e:
        raise Exception(f"Payment creation failed: {str(e)}")

def process_payment(payment_intent_id, payment_method):
    try:
        if payment_method == "stripe":
            payment_intent = stripe.PaymentIntent.confirm(payment_intent_id)
            return payment_intent
        elif payment_method == "paypal":
            paypalrestsdk.configure({
                "mode": "live",
                "client_id": PaymentGateway().get_payment_method("paypal")["client_id"],
                "client_secret": PaymentGateway().get_payment_method("paypal")["client_secret"]
            })
            payment = paypalrestsdk.Payment.find(payment_intent_id)
            if payment:
                payment_response = payment.execute({"payer_id": payment.payer.payer_id})
                if payment_response:
                    return payment_response
                else:
                    raise Exception("Payment execution failed")
            else:
                raise Exception("Payment not found")
        elif payment_method == "bank_transfer":
            # Bank transfer payment processing
            pass
        else:
            raise ValueError("Invalid payment method")
    except Exception as e:
        raise Exception(f"Payment processing failed: {str(e)}")
```

**Web Application Integration**
---------------------------

```python
# app.py

from flask import Flask, request, jsonify
from payment_service import create_payment_intent, process_payment

app = Flask(__name__)

@app.route("/payment", methods=["POST"])
def create_payment():
    try:
        amount = request.json["amount"]
        currency = request.json["currency"]
        payment_method = request.json["payment_method"]
        payment_intent = create_payment_intent(amount, currency, payment_method)
        return jsonify({"payment_intent_id": payment_intent})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/payment/process", methods=["POST"])
def process_payment_request():
    try:
        payment_intent_id = request.json["payment_intent_id"]
        payment_method = request.json["payment_method"]
        payment_response = process_payment(payment_intent_id, payment_method)
        return jsonify({"payment_response": payment_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

**.env File**
-------------

```makefile
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret
BANK_TRANSFER_ACCOUNT_NUMBER=your_bank_transfer_account_number
BANK_TRANSFER_ROUTING_NUMBER=your_bank_transfer_routing_number
```

**Requirements**
---------------

```makefile
Flask==2.0.2
stripe==4.5.0
paypalrestsdk==1.4.0
python-dotenv==0.19.2
```
