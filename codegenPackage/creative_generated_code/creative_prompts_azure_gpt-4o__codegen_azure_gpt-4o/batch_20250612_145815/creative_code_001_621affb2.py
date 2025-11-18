"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Recommend libraries or APIs for implementing a subscription-based payment system inspired by platforms like Rentsy, with multi-language support for Polish, English, Ukrainian, and Russian.
Generated: DETERMINISTIC_621affb29bae3573
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code that outlines a subscription-based payment system using `Stripe` for payment processing and `Flask-Babel` for multi-language support. 

```python
# Import necessary libraries
import stripe  # For payment processing
from flask import Flask, request, jsonify
from flask_babel import Babel, gettext

# Initialize Flask application
app = Flask(__name__)

# Configure Stripe API credentials (replace placeholders with actual keys)
stripe.api_key = "your_stripe_secret_key"

# Babel configuration for multi-language support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'pl', 'uk', 'ru']  # Supported languages
babel = Babel(app)

# Function to determine user's preferred language based on request
@babel.localeselector
def get_locale():
    # Check for 'lang' parameter in query string or default to 'en'
    return request.args.get('lang', 'en')


# Endpoint to create a subscription
@app.route('/create-subscription', methods=['POST'])
def create_subscription():
    """
    Creates a new subscription for a user using Stripe API.
    Expects JSON payload with keys: 'customer_email', 'payment_method_id', 'price_id'.
    """
    try:
        # Parse JSON payload
        data = request.json
        customer_email = data.get("customer_email")
        payment_method_id = data.get("payment_method_id")
        price_id = data.get("price_id")

        # Validate required inputs
        if not all([customer_email, payment_method_id, price_id]):
            return jsonify({"error": gettext("Missing required inputs.")}), 400

        # Create customer in Stripe
        customer = stripe.Customer.create(
            email=customer_email,
            payment_method=payment_method_id,
            invoice_settings={"default_payment_method": payment_method_id}
        )

        # Create subscription for the customer
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": price_id}],
            expand=["latest_invoice.payment_intent"]
        )

        return jsonify({
            "message": gettext("Subscription created successfully."),
            "subscription_id": subscription.id,
            "customer_id": customer.id
        }), 201

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": gettext("Stripe error: ") + str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": gettext("An error occurred: ") + str(e)}), 500


# Endpoint to cancel a subscription
@app.route('/cancel-subscription', methods=['POST'])
def cancel_subscription():
    """
    Cancels an existing subscription using Stripe API.
    Expects JSON payload with key: 'subscription_id'.
    """
    try:
        # Parse JSON payload
        data = request.json
        subscription_id = data.get("subscription_id")

        # Validate required input
        if not subscription_id:
            return jsonify({"error": gettext("Missing subscription ID.")}), 400

        # Cancel subscription
        subscription = stripe.Subscription.delete(subscription_id)

        return jsonify({
            "message": gettext("Subscription cancelled successfully."),
            "subscription_id": subscription_id
        }), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": gettext("Stripe error: ") + str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": gettext("An error occurred: ") + str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Notes:
- Replace `your_stripe_secret_key` with your actual Stripe secret key.
- Multi-language support is enabled via Flask-Babel, and translations can be handled using `.po` files in the appropriate locales directory.
- Install dependencies using `pip install stripe flask flask-babel`.
- Ensure proper environment variables management for sensitive keys in production.
