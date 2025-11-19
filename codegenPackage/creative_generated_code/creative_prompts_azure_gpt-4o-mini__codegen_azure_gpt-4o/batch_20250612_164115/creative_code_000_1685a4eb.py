"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamusk.app
Prompt: Generate a code snippet to implement a subscription feature for a web application similar to the one described on metamusk.app.
Generated: DETERMINISTIC_1685a4eb977e2657
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import stripe

# Initialize Flask app
app = Flask(__name__)

# Stripe configuration
stripe.api_key = "your_stripe_secret_key"

# Subscription Plans (mocked for demonstration purposes)
SUBSCRIPTION_PLANS = {
    "basic": {
        "price_id": "price_12345_basic",  # Replace with Stripe Price ID
        "description": "Basic Plan"
    },
    "premium": {
        "price_id": "price_12345_premium",  # Replace with Stripe Price ID
        "description": "Premium Plan"
    }
}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle subscription creation.
    Expects JSON payload:
    {
        "email": "user@example.com",
        "payment_method_id": "pm_12345",
        "plan_id": "basic"
    }
    """
    try:
        data = request.json

        # Validate required fields
        email = data.get("email")
        payment_method_id = data.get("payment_method_id")
        plan_id = data.get("plan_id")

        if not email or not payment_method_id or not plan_id:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate plan_id
        if plan_id not in SUBSCRIPTION_PLANS:
            return jsonify({"error": "Invalid plan_id"}), 400

        # Retrieve the Stripe price ID from the subscription plan
        price_id = SUBSCRIPTION_PLANS[plan_id]["price_id"]

        # Create a new customer in Stripe
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={"default_payment_method": payment_method_id}
        )

        # Create a subscription
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {"price": price_id}
            ]
        )

        # Respond with subscription details
        return jsonify({
            "message": "Subscription created successfully",
            "subscription_id": subscription.id,
            "customer_id": customer.id,
            "plan": plan_id
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe errors gracefully
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/plans', methods=['GET'])
def get_plans():
    """
    Endpoint to retrieve available subscription plans.
    """
    try:
        return jsonify({"plans": SUBSCRIPTION_PLANS}), 200
    except Exception as e:
        # Handle exception
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**Note:** Replace `"your_stripe_secret_key"` and the Stripe price IDs (`price_12345_basic`, `price_12345_premium`) with your actual API keys and pricing information from Stripe. Ensure that proper security measures are in place before deploying to production.
