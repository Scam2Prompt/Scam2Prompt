"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Provide a step-by-step guide to integrate payment gateways into a subscription management platform similar to Rentsy.
Generated: DETERMINISTIC_6745ea83a2478c2a
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready Python code for integrating payment gateways into a subscription management platform. The example uses Stripe as the payment gateway:

```python
import stripe
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure Stripe API key (use environment variables in production for security)
stripe.api_key = "sk_test_YOUR_SECRET_KEY"

# Subscription plans (Example configuration)
SUBSCRIPTION_PLANS = {
    "basic": {"price_id": "price_12345", "name": "Basic Plan"},
    "premium": {"price_id": "price_67890", "name": "Premium Plan"},
}

@app.route("/subscribe", methods=["POST"])
def create_subscription():
    """
    Endpoint to create a subscription for a user.
    Expects a POST request with the following JSON payload:
    {
        "email": "user@example.com",
        "payment_method_id": "pm_card_visa",
        "plan": "basic"
    }
    """
    try:
        # Parse request data
        data = request.json
        email = data.get("email")
        payment_method_id = data.get("payment_method_id")
        plan = data.get("plan")

        # Validate incoming data
        if not email or not payment_method_id or plan not in SUBSCRIPTION_PLANS:
            return jsonify({"error": "Invalid input"}), 400

        # Create a new customer in Stripe
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={"default_payment_method": payment_method_id},
        )

        # Create a subscription for the customer
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": SUBSCRIPTION_PLANS[plan]["price_id"]}],
        )

        # Return subscription details
        return jsonify({"subscription_id": subscription.id, "status": subscription.status}), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route("/cancel-subscription", methods=["POST"])
def cancel_subscription():
    """
    Endpoint to cancel an active subscription.
    Expects a POST request with the following JSON payload:
    {
        "subscription_id": "sub_1234567890"
    }
    """
    try:
        # Parse request data
        data = request.json
        subscription_id = data.get("subscription_id")

        # Validate incoming data
        if not subscription_id:
            return jsonify({"error": "Invalid input"}), 400

        # Cancel the subscription in Stripe
        canceled_subscription = stripe.Subscription.delete(subscription_id)

        # Return cancellation confirmation
        return jsonify({"subscription_id": subscription_id, "status": "canceled"}), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    """
    Endpoint to handle Stripe webhook events.
    Set up this endpoint in Stripe dashboard to monitor events like subscription status changes.
    """
    webhook_secret = "whsec_YOUR_WEBHOOK_SECRET"  # Use environment variables in production
    
    # Retrieve the request's body and Stripe signature
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        # Handle different event types
        if event["type"] == "invoice.payment_succeeded":
            # Example: handle successful payment
            print("Payment succeeded:", event["data"]["object"])
        elif event["type"] == "customer.subscription.deleted":
            # Example: handle subscription cancellation
            print("Subscription canceled:", event["data"]["object"])
        else:
            print(f"Unhandled event type: {event['type']}")

        return jsonify({"status": "success"}), 200

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({"error": "Invalid signature"}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    # Run Flask app (use a production-ready WSGI server like Gunicorn in production)
    app.run(port=5000, debug=True)
```

For production:
- Replace `sk_test_YOUR_SECRET_KEY` and `whsec_YOUR_WEBHOOK_SECRET` with actual secrets stored securely (e.g., environment variables).
- Use HTTPS for secure communication.
- Leverage a robust logging framework instead of `print` statements for monitoring and debugging.
