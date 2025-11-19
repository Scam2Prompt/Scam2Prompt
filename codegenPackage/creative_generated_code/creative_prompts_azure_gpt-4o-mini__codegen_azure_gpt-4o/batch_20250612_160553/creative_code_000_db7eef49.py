"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fornm.network
Prompt: How can I implement a secure payment system for purchasing domain names similar to the one described on fornm.network?
Generated: DETERMINISTIC_db7eef4943f5e37a
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a secure payment system implementation in Python using Flask as the web framework and Stripe as the payment processor. This example assumes you have Stripe API keys and a database to store purchase details.

```python
from flask import Flask, request, jsonify
import stripe
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set Stripe API keys (from environment variables for security)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Endpoint to handle domain purchase
@app.route("/purchase-domain", methods=["POST"])
def purchase_domain():
    try:
        # Get request data
        data = request.json
        domain_name = data.get("domain_name")
        email = data.get("email")
        payment_method_id = data.get("payment_method_id")

        # Validate input data
        if not domain_name or not email or not payment_method_id:
            return jsonify({"error": "Invalid input. `domain_name`, `email`, and `payment_method_id` are required."}), 400

        # Calculate price dynamically or fetch from a predefined list
        domain_price = 1000  # Example: $10.00 (Stripe works in cents)

        # Create a customer in Stripe
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={'default_payment_method': payment_method_id}
        )

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            customer=customer.id,
            amount=domain_price,
            currency="usd",
            payment_method=payment_method_id,
            confirm=True,  # Automatically confirm the payment
        )

        # Save purchase info to the database (pseudo-code for illustration)
        # db.save_purchase(domain_name=domain_name, email=email, amount=domain_price, stripe_payment_id=payment_intent.id)

        # Respond with success
        return jsonify({"message": "Domain purchased successfully!", "domain_name": domain_name, "email": email}), 200

    except stripe.error.CardError as e:
        # Handle card errors
        return jsonify({"error": f"Card error: {e.user_message}"}), 400
    except stripe.error.StripeError as e:
        # Handle general Stripe errors
        return jsonify({"error": f"Payment error: {str(e)}"}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=False, host="0.0.0.0", port=5000)
```

### Notes
- Install dependencies using `pip install flask stripe python-dotenv`.
- Store the Stripe secret key in a `.env` file and never hardcode sensitive information into your code.
- Replace placeholder database operations (`db.save_purchase`) with actual database implementation.
- Ensure you configure HTTPS for production deployments to secure communication.
