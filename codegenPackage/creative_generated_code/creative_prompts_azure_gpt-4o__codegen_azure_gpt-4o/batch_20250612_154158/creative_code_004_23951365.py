"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rworld.pro
Prompt: Suggest APIs for integrating payment processing into a ride-sharing app similar to RideBNB, and provide example code for implementation.
Generated: DETERMINISTIC_23951365d64e7b88
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuring the Stripe API key (replace 'your_secret_key' with actual secret key)
stripe.api_key = "your_secret_key"

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a Stripe Payment Intent.
    This is used to initiate payment for a ride in the ride-sharing app.
    """
    try:
        # Extract payment details from the request
        data = request.json
        amount = data.get('amount')  # Amount in cents (e.g., 15.00 USD -> 1500 cents)
        currency = data.get('currency', 'usd')  # Default to USD if no currency provided
        
        if not amount or amount <= 0:
            return jsonify({"error": "Invalid amount"}), 400
        
        # Create a PaymentIntent with the provided details
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods={
                'enabled': True,
            },
        )
        
        # Return the client secret to the frontend
        return jsonify({
            "clientSecret": payment_intent['client_secret']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An error occurred: " + str(e)}), 500


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint to handle Stripe webhooks.
    This listens for payment events such as 'payment_intent.succeeded'.
    """
    # Replace 'your_webhook_secret' with the actual webhook secret from Stripe
    webhook_secret = "your_webhook_secret"
    
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    
    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
        
        # Handle different event types
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            # Perform post-payment actions, e.g., marking ride as paid
            print(f"Payment for {payment_intent['amount']} succeeded.")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            print(f"Payment for {payment_intent['amount']} failed.")
        
        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        # Handle webhook signature verification failures
        return jsonify({"error": "Invalid webhook signature"}), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An error occurred: " + str(e)}), 500


if __name__ == '__main__':
    # Start the Flask server
    app.run(port=5000)
```

### Notes:
- Replace `your_secret_key` and `your_webhook_secret` with the appropriate keys obtained from Stripe.
- This code assumes you're using Flask for the backend and Stripe as the payment provider.
- For production, make sure the server is secured (e.g., HTTPS), and environment variables are used to store sensitive keys.
