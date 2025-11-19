"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Write a code snippet that integrates a payment system for ordering железобетонные изделия, considering flexible payment options mentioned on the Paradigma website.
Generated: DETERMINISTIC_f962ac0f8358f015
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code snippet that integrates a payment system for ordering железобетонные изделия (reinforced concrete products). It uses Flask as a web framework and simulates flexible payment options:

```python
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Stripe API configuration (replace with your actual keys)
stripe.api_key = "sk_test_your_secret_key"

# Product catalog (can be replaced with a database)
PRODUCTS = {
    "block": {"name": "Concrete Block", "price": 1000},  # Price in cents
    "slab": {"name": "Concrete Slab", "price": 8000},    # Price in cents
    "column": {"name": "Concrete Column", "price": 12000} # Price in cents
}

@app.route("/order", methods=["POST"])
def create_order():
    """
    Endpoint to handle product ordering and payment.
    Expects JSON payload with 'product_id' and 'payment_method'.
    """
    try:
        # Parse request JSON
        data = request.json
        product_id = data.get("product_id")
        payment_method = data.get("payment_method")  # e.g., "card", "bank_transfer"

        if not product_id or product_id not in PRODUCTS:
            return jsonify({"error": "Invalid product ID"}), 400

        # Fetch product details
        product = PRODUCTS[product_id]

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=product["price"],  # Amount in cents
            currency="usd",
            payment_method_types=["card", "bank_transfer"],  # Flexible payment options
            description=f"Order of {product['name']}"
        )

        return jsonify({
            "message": "Order created successfully.",
            "client_secret": payment_intent.client_secret,  # Used for client-side Stripe integration
            "product": product
        }), 200
    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

Replace `"sk_test_your_secret_key"` with your actual Stripe API secret key before deploying this code to production. Ensure that error handling and environment-specific configurations meet your requirements.
