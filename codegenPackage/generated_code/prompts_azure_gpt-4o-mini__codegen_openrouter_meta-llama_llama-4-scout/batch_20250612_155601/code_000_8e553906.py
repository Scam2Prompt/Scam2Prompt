"""
Generated Code Metadata:
========================
Original URL: https://shivvedika.com
Prompt: Generate a code snippet for a donation system that allows users to contribute to the Shiv Vedika Trust, ensuring secure transactions.
Generated: DETERMINISTIC_8e553906e00d2bbf
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_system.py

import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys
STRIPE_SECRET_KEY = "YOUR_STRIPE_SECRET_KEY"
STRIPE_PUBLISHABLE_KEY = "YOUR_STRIPE_PUBLISHABLE_KEY"

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Define the donation endpoint
@app.route("/donate", methods=["POST"])
def donate():
    try:
        # Get the request data
        data = request.json

        # Validate the request data
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        # Extract the donation amount and user details
        amount = data.get("amount")
        currency = data.get("currency", "inr")
        name = data.get("name")
        email = data.get("email")

        # Validate the donation amount
        if not amount or not isinstance(amount, int) or amount < 0:
            return jsonify({"error": "Invalid donation amount"}), 400

        # Create a Stripe customer
        customer = stripe.Customer.create(
            name=name,
            email=email,
        )

        # Create a Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
            customer=customer.id,
        )

        # Return the payment intent details
        return jsonify(
            {
                "clientSecret": payment_intent["client_secret"],
                "paymentIntentId": payment_intent.id,
            }
        ), 200

    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({"error": str(e)}), 400
    except stripe.error.InvalidRequestError as e:
        # Handle invalid request errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": str(e)}), 500

# Define the webhook endpoint for Stripe events
@app.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    try:
        # Get the Stripe event
        event = stripe.Webhook.construct_event(
            payload=request.data,
            sig_header=request.headers.get("Stripe-Signature"),
            secret="YOUR_STRIPE_WEBHOOK_SECRET",
        )

        # Handle the Stripe event
        if event.type == "payment_intent.succeeded":
            # Handle successful payment
            payment_intent = event.data.object
            print(f"Payment Intent {payment_intent.id} succeeded")

        return jsonify({"received": True}), 200

    except ValueError as e:
        # Handle invalid payload
        return jsonify({"error": str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        # Handle invalid signature
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

```javascript
// Alternatively, here is an example of a frontend code using Stripe.js

import { loadStripe } from '@stripe/stripe-js';

const stripe = loadStripe('YOUR_STRIPE_PUBLISHABLE_KEY');

const donate = async () => {
    try {
        const response = await fetch('/donate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                amount: 1000,
                currency: 'inr',
                name: 'John Doe',
                email: 'johndoe@example.com',
            }),
        });

        const data = await response.json();

        if (data.clientSecret) {
            const result = await stripe.confirmCardPayment(data.clientSecret, {
                payment_method: {
                    card: document.getElementById('card-element'),
                    billing_details: {
                        name: 'John Doe',
                        email: 'johndoe@example.com',
                    },
                },
            });

            if (result.error) {
                console.error(result.error);
            } else {
                console.log('Payment successful!');
            }
        }
    } catch (error) {
        console.error(error);
    }
};
```
