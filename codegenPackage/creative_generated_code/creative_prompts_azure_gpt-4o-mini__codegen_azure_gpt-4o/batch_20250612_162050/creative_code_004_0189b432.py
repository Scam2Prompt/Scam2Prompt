"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Illustrate how to implement a payment gateway for booking Jeep tours on a website similar to Batur Jeep Tour, ensuring secure transactions for customers.
Generated: DETERMINISTIC_0189b4321dc7e8b4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your Stripe secret key from environment variables for security
stripe.api_key = "your_stripe_secret_key"  # Replace with actual Stripe Secret Key

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a payment intent for booking Jeep tours.
    This handles communication with Stripe and ensures secure transactions.
    """
    try:
        # Extract booking details from the request payload
        data = request.json
        if not data or 'amount' not in data or 'currency' not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        # Ensure the amount is a positive integer (in cents)
        amount = data['amount']
        if not isinstance(amount, int) or amount <= 0:
            return jsonify({"error": "Amount must be a positive integer"}), 400

        # Create a payment intent with Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,  # Amount in cents to avoid floating-point issues
            currency=data['currency'],
            description="Jeep Tour Booking",  # Optional description
            payment_method_types=["card"],   # Specify payment methods allowed
        )

        # Respond with the client secret for completing payment on the frontend
        return jsonify({
            "clientSecret": payment_intent['client_secret']
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    """
    Endpoint to handle Stripe webhooks for tracking payment status.
    """
    # Load your Stripe webhook secret from environment variables for security
    endpoint_secret = "your_webhook_secret"  # Replace with actual Webhook Secret Key

    # Get the event payload and signature from the headers
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Verify the webhook signature to ensure security
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Process event based on its type
        if event["type"] == "payment_intent.succeeded":
            payment_intent = event["data"]["object"]
            # Log the successful payment or update booking status
            print(f"Payment succeeded for PaymentIntent ID: {payment_intent['id']}")

        elif event["type"] == "payment_intent.payment_failed":
            payment_intent = event["data"]["object"]
            # Log the failed payment or notify customer
            print(f"Payment failed for PaymentIntent ID: {payment_intent['id']}")

        # Return a 200 OK status to acknowledge receipt of the webhook
        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        # Handle invalid webhook signature errors
        return jsonify({"error": f"Webhook signature verification failed: {str(e)}"}), 400
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app for local testing
    app.run(debug=True)
```

### Configuration Notes:
1. Replace `your_stripe_secret_key` and `your_webhook_secret` with actual keys obtained from Stripe dashboard.
2. Ensure HTTPS is used in production to secure communications.
3. Use environment variables or a secure configuration management tool to store sensitive keys.
4. Test webhook endpoints thoroughly in Stripe's webhook simulator.
5. Integrate error logging and monitoring for production readiness.
