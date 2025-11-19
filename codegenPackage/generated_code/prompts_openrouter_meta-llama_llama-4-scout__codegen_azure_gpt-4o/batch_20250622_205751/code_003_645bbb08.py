"""
Generated Code Metadata:
========================
Original URL: https://notion817.tistory.com
Prompt: Recommend APIs or libraries for creating a subscription-based model for a blog, similar to "구독하기" (Subscribe), and provide a code example.
Generated: DETERMINISTIC_645bbb08d88231c4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from stripe import Stripe, error

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
STRIPE_API_KEY = "your_stripe_secret_key"
STRIPE_PUBLIC_KEY = "your_stripe_public_key"

# Initialize Stripe
Stripe.api_key = STRIPE_API_KEY

# Route to create a subscription
@app.route('/create-subscription', methods=['POST'])
def create_subscription():
    """
    Endpoint to create a subscription for a user.
    Expects a JSON payload with 'email' and 'payment_method_id'.
    """
    try:
        # Parse request data
        data = request.json
        email = data.get('email')
        payment_method_id = data.get('payment_method_id')

        if not email or not payment_method_id:
            return jsonify({"error": "Email and payment method ID are required"}), 400

        # Create a customer in Stripe
        customer = Stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )

        # Create a subscription for the customer
        subscription = Stripe.Subscription.create(
            customer=customer.id,
            items=[
                {"price": "your_price_id"}  # Replace with your actual price ID
            ]
        )

        # Return subscription details
        return jsonify({
            "subscription_id": subscription.id,
            "status": subscription.status
        }), 200

    except error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to cancel a subscription
@app.route('/cancel-subscription', methods=['POST'])
def cancel_subscription():
    """
    Endpoint to cancel a subscription for a user.
    Expects a JSON payload with 'subscription_id'.
    """
    try:
        # Parse request data
        data = request.json
        subscription_id = data.get('subscription_id')

        if not subscription_id:
            return jsonify({"error": "Subscription ID is required"}), 400

        # Cancel the subscription in Stripe
        subscription = Stripe.Subscription.retrieve(subscription_id)
        subscription.delete()

        # Return confirmation
        return jsonify({"message": "Subscription canceled successfully"}), 200

    except error.StripeError as e:
        # Handle Stripe errors
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle other errors
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `your_stripe_secret_key`, `your_stripe_public_key`, and `your_price_id` with actual values from your Stripe account.
- Install required libraries using `pip install flask stripe`.
- Ensure proper security measures for handling sensitive data in production.
