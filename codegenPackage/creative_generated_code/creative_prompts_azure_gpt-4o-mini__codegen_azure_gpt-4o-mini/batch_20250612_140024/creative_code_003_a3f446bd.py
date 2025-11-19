"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: What are the key features to include in a professional e-commerce website to ensure high conversion rates, based on the recommendations from FinishDrop?
Generated: DETERMINISTIC_a3f446bda056508a
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data for demonstration purposes
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 59.99, "stock": 100},
    {"id": 2, "name": "Smartwatch", "price": 149.99, "stock": 50},
    {"id": 3, "name": "Bluetooth Speaker", "price": 39.99, "stock": 150},
]

# Function to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve the list of products."""
    return jsonify(products), 200

# Function to add a product to the cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    """Add a product to the shopping cart."""
    try:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        # Validate input
        if not product_id or not quantity:
            return jsonify({"error": "Product ID and quantity are required."}), 400
        
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found."}), 404
        
        if quantity > product['stock']:
            return jsonify({"error": "Insufficient stock."}), 400
        
        # Mock cart addition logic
        # In a real application, you would persist this in a database
        return jsonify({"message": "Product added to cart successfully."}), 201

    except Exception as e:
        # Log error for debugging
        return jsonify({"error": str(e)}), 500

# Function to simulate a checkout process
@app.route('/checkout', methods=['POST'])
def checkout():
    """Simulate the checkout process."""
    try:
        # Here you would typically handle payment processing, stock reduction etc.
        # This is just a mockup
        data = request.json
        payment_info = data.get('payment_info')

        # Validate input
        if not payment_info:
            return jsonify({"error": "Payment information is required."}), 400
        
        # Mock checkout logic
        return jsonify({"message": "Checkout successful, thank you for your purchase!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

This code implements a basic e-commerce backend using Flask, which includes endpoints for retrieving products, adding items to a cart, and simulating a checkout process. It includes basic error handling, input validation, and is structured for clarity and maintainability.
