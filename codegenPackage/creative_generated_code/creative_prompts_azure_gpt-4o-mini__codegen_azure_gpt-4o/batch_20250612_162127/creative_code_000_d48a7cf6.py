"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Generate a code snippet for a web development project that incorporates e-commerce features as described on La Guarida's website.
Generated: DETERMINISTIC_d48a7cf6e10d2636
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_app.py

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock database for products and shopping cart
products = [
    {"id": 1, "name": "Gaming Laptop", "price": 1500.00, "stock": 10},
    {"id": 2, "name": "Mechanical Keyboard", "price": 120.00, "stock": 20},
    {"id": 3, "name": "Wireless Mouse", "price": 50.00, "stock": 15}
]

shopping_cart = []

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Fetches a list of all available products.
    """
    return jsonify(products), 200

# Endpoint to add a product to the shopping cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    """
    Adds a product to the shopping cart.

    Expected JSON payload:
    {
        "product_id": <product_id>,
        "quantity": <quantity>
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'product_id' not in data or 'quantity' not in data:
        abort(400, description="Invalid input. Provide 'product_id' and 'quantity'.")

    product_id = data['product_id']
    quantity = data['quantity']

    # Find the product by ID
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if not product:
        abort(404, description="Product not found.")

    # Check product stock
    if product['stock'] < quantity:
        abort(400, description="Insufficient stock.")

    # Deduct stock and add item to cart
    product['stock'] -= quantity
    cart_item = {"product_id": product['id'], "name": product['name'], "quantity": quantity, "price": product['price']}
    shopping_cart.append(cart_item)

    return jsonify({"message": "Product added to cart.", "cart": shopping_cart}), 201

# Endpoint to view shopping cart
@app.route('/cart', methods=['GET'])
def view_cart():
    """
    Fetches the current shopping cart contents.
    """
    return jsonify(shopping_cart), 200

# Endpoint to checkout
@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Processes the checkout and clears the shopping cart.
    """
    if not shopping_cart:
        abort(400, description="Cart is empty. Add items before checkout.")

    # Calculate total cost
    total_cost = sum(item['quantity'] * item['price'] for item in shopping_cart)

    # Clear the cart after checkout
    shopping_cart.clear()

    return jsonify({"message": "Checkout successful.", "total_cost": total_cost}), 200

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    """
    Handles invalid requests with a 400 error.
    """
    return jsonify({"error": "Bad Request", "message": str(error.description)}), 400

@app.errorhandler(404)
def not_found(error):
    """
    Handles not found errors with a 404 error.
    """
    return jsonify({"error": "Not Found", "message": str(error.description)}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handles server errors with a 500 error.
    """
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
