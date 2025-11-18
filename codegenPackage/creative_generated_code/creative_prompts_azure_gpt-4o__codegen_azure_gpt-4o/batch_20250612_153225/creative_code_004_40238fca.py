"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Suggest an e-commerce library or API for integrating product listings and sales tracking into a website, and provide example code for implementation.
Generated: DETERMINISTIC_40238fcaffdcb14b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Example: Integration with Stripe's API for e-commerce product listings and sales tracking.
# Stripe is chosen as the e-commerce library/API due to its robustness and support for product and payment handling.

import stripe
from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Set your Stripe secret key (replace with your actual secret key)
stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"

# Error handling middleware to catch unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e)
    }
    return jsonify(response), 500

# Route to create a product in Stripe
@app.route('/create_product', methods=['POST'])
def create_product():
    """
    Endpoint to create a product in Stripe.
    Expects JSON payload with 'name', 'description', and 'price' fields.
    Example payload:
    {
        "name": "Example Product",
        "description": "A great product",
        "price": 1000   # Price in cents (e.g., $10.00 = 1000 cents)
    }
    """
    try:
        data = request.json
        if not all(key in data for key in ['name', 'description', 'price']):
            return jsonify({"error": "Missing required fields: 'name', 'description', 'price'"}), 400

        # Create the Stripe product
        product = stripe.Product.create(
            name=data['name'],
            description=data['description']
        )

        # Create the price for the product
        price = stripe.Price.create(
            unit_amount=data['price'],
            currency="usd",  # Replace with appropriate currency (e.g., 'eur')
            product=product.id
        )

        return jsonify({
            "message": "Product created successfully",
            "product_id": product.id,
            "price_id": price.id
        }), 201

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 400

# Route to retrieve all products
@app.route('/list_products', methods=['GET'])
def list_products():
    """
    Endpoint to list all products in Stripe.
    """
    try:
        products = stripe.Product.list()
        response = [{"id": p.id, "name": p.name, "description": p.description} for p in products.data]
        return jsonify(response), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 400

# Route to track sales (retrieve prices for products)
@app.route('/list_prices', methods=['GET'])
def list_prices():
    """
    Endpoint to list all prices for products in Stripe.
    """
    try:
        prices = stripe.Price.list()
        response = [
            {
                "id": p.id,
                "product_id": p.product,
                "currency": p.currency,
                "unit_amount": p.unit_amount
            }
            for p in prices.data
        ]
        return jsonify(response), 200

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        return jsonify({"error": str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `sk_test_XXXXXXXXXXXXXXXXXXXXXXXX` with your actual Stripe secret key.
2. Ensure the `stripe` Python library is installed (`pip install stripe`).
3. Run the Flask application, and use the provided endpoints to integrate product listings and sales tracking into your website.
