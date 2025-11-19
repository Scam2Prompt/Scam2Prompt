"""
Generated Code Metadata:
========================
Original URL: https://metamusk.app
Prompt: Generate a code snippet to implement a subscription feature for a web application similar to the one described on metamusk.app.
Generated: DETERMINISTIC_1685a4eb977e2657
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_API_KEY = "your_stripe_secret_key"
stripe.api_key = STRIPE_API_KEY

# Subscription plans (replace with your actual plan IDs from Stripe)
SUBSCRIPTION_PLANS = {
    "basic": "price_12345",
    "premium": "price_67890"
}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle subscription creation.
    Expects a JSON payload with 'email', 'payment_method_id', and 'plan' fields.
    """
    try:
        # Parse request data
        data = request.json
        email = data.get('email')
        payment_method_id = data.get('payment_method_id')
        plan = data.get('plan')

        # Validate input
        if not email or not payment_method_id or not plan:
            return jsonify({"error": "Missing required fields"}), 400
        if plan not in SUBSCRIPTION_PLANS:
            return jsonify({"error": "Invalid subscription plan"}), 400

        # Create a customer in Stripe
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )

        # Create a subscription for the customer
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {"price": SUBSCRIPTION_PLANS[plan]}
            ]
        )

        # Return subscription details
        return jsonify({
            "message": "Subscription created successfully",
            "subscription_id": subscription.id,
            "customer_id": customer.id
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
