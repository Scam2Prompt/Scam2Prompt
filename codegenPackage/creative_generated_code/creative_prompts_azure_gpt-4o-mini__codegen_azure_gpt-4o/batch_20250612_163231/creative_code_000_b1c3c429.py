"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caldrera.xyz
Prompt: Generate a code snippet for a secure payment integration for domain purchases, referencing features like "fast transfers" and "hassle-free payments."
Generated: DETERMINISTIC_b1c3c429e63b3273
Batch ID: 20250612_163231
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

# Initialize the Flask app
app = Flask(__name__)

# Stripe API keys (store securely in environment variables)
STRIPE_SECRET_KEY = "sk_test_your_secret_key"
STRIPE_PUBLIC_KEY = "pk_test_your_public_key"
stripe.api_key = STRIPE_SECRET_KEY

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    """
    Endpoint to create a PaymentIntent for domain purchases.
    Implements secure and hassle-free payment processing using Stripe.
    """
    try:
        # Extract purchase details from request
        data = request.json
        domain_name = data.get("domain_name", "example.com")
        purchase_price = data.get("purchase_price", 100.00)  # Default price in USD

        if not domain_name or purchase_price <= 0:
            return jsonify({"error": "Invalid domain name or purchase price."}), 400

        # Create a PaymentIntent on Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(purchase_price * 100),  # Stripe uses smallest currency unit (cents)
            currency='usd',
            description=f"Purchase of domain: {domain_name}",
            payment_method_types=["card"]  # Only accept card payments
        )

        # Return the client secret for the PaymentIntent to the frontend
        return jsonify({
            "clientSecret": payment_intent.client_secret,
            "domainName": domain_name,
            "message": "Payment initiated successfully."
        })

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/success', methods=['GET'])
def payment_success():
    """
    Endpoint to confirm the success of a domain transfer.
    This could be used as a webhook endpoint or post-payment confirmation.
    """
    try:
        # Simulate fast and hassle-free domain transfer
        return jsonify({
            "status": "success",
            "message": "Domain transfer successful. Thank you for your purchase!"
        })

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An error occurred during domain transfer."}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use production-grade server settings in a real deployment (e.g., gunicorn or uwsgi)
    app.run(debug=True)
```
