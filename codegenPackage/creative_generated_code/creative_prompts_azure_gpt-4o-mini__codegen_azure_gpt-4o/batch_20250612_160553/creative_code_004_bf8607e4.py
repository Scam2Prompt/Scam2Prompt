"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fornm.network
Prompt: How can I build a user-friendly checkout process for domain purchases that ensures secure transactions, like the one on fornm.network?
Generated: DETERMINISTIC_bf8607e46e74359f
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: checkout_process.py
# Description: Secure and user-friendly checkout process for domain purchases.
# Author: [Your Name]
# Date: [Insert Date]
# Dependencies: Flask, Stripe

from flask import Flask, request, jsonify, render_template
import os
import stripe

# Initialize Flask app
app = Flask(__name__)

# Load Stripe secret key from environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Ensure the Stripe secret key is set
if not stripe.api_key:
    raise EnvironmentError("STRIPE_SECRET_KEY environment variable is not set.")

@app.route('/')
def homepage():
    """
    Homepage route - displays available domains for purchase.
    """
    # Example list of available domains (this would be dynamically generated in a real-world app)
    available_domains = ["example.com", "testdomain.net", "mywebsite.org"]
    return render_template("homepage.html", domains=available_domains)


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Checkout route - handles the checkout process for domain purchases.
    """
    try:
        # Extract domain and payment details from the request
        data = request.json
        domain_name = data.get("domain")
        payment_method_id = data.get("payment_method_id")

        # Validate input
        if not domain_name or not payment_method_id:
            return jsonify({"error": "Missing domain or payment method information."}), 400

        # Dummy domain prices (would be dynamically fetched in production)
        domain_prices = {
            "example.com": 1000,  # in cents ($10.00)
            "testdomain.net": 1500,  # in cents ($15.00)
            "mywebsite.org": 2000,  # in cents ($20.00)
        }

        # Ensure the domain exists and fetch its price
        if domain_name not in domain_prices:
            return jsonify({"error": "Domain not available."}), 404

        amount = domain_prices[domain_name]

        # Create a Stripe payment intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            payment_method=payment_method_id,
            confirm=True,
        )

        # Respond with the payment confirmation
        return jsonify({"success": True, "payment_intent": intent}), 200

    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An error occurred during checkout: " + str(e)}), 500


@app.route('/success')
def success():
    """
    Success route - displays a confirmation page after successful payment.
    """
    return render_template("success.html")


@app.route('/failure')
def failure():
    """
    Failure route - displays an error page if payment fails.
    """
    return render_template("failure.html")


if __name__ == '__main__':
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**Note:** You will need to create accompanying HTML templates (e.g., `homepage.html`, `success.html`, `failure.html`) and set the `STRIPE_SECRET_KEY` environment variable before running the application. Install the required packages (`Flask` and `Stripe`) if not already installed:

```bash
pip install flask stripe
```
