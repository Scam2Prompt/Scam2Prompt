"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bijenwasdoek.nl
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site selling beeswax wraps, highlighting the zero-waste lifestyle aspect.
Generated: DETERMINISTIC_0bd893d9320f76a2
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for our product catalog
PRODUCTS = {
    1: {"name": "Beeswax Wraps - Small", "price": 10.0, "stock": 50},
    2: {"name": "Beeswax Wraps - Medium", "price": 15.0, "stock": 30},
    3: {"name": "Beeswax Wraps - Large", "price": 20.0, "stock": 20},
}

# In-memory shopping cart for the session
cart = {}

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """Add a product to the shopping cart.

    Request JSON should include:
    - product_id: ID of the product to add
    - quantity: Number of items to add
    """
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Validate input
    if not isinstance(product_id, int) or not isinstance(quantity, int) or quantity <= 0:
        return jsonify({"error": "Invalid product ID or quantity."}), 400
    
    product = PRODUCTS.get(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404

    # Update cart
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {"name": product['name'], "price": product['price'], "quantity": quantity}

    return jsonify({"message": "Product added to cart.", "cart": cart}), 200

@app.route('/view_cart', methods=['GET'])
def view_cart():
    """View current contents of the shopping cart."""
    return jsonify(cart), 200

@app.route('/checkout', methods=['POST'])
def checkout():
    """Checkout the shopping cart and provide a summary."""
    if not cart:
        return jsonify({"error": "Cart is empty."}), 400

    total_cost = sum(item['price'] * item['quantity'] for item in cart.values())
    
    # Clear the cart after checkout
    cart.clear()
    
    return jsonify({"message": "Checkout successful!", "total_cost": total_cost}), 200

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    """Remove a product from the shopping cart.

    Request JSON should include:
    - product_id: ID of the product to remove
    - quantity: Number of items to remove
    """
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Validate input
    if not isinstance(product_id, int) or not isinstance(quantity, int) or quantity <= 0:
        return jsonify({"error": "Invalid product ID or quantity."}), 400

    if product_id not in cart:
        return jsonify({"error": "Product not in cart."}), 404

    # Update cart
    if cart[product_id]['quantity'] <= quantity:
        del cart[product_id]  # Remove item if quantity is zero or less
    else:
        cart[product_id]['quantity'] -= quantity

    return jsonify({"message": "Product removed from cart.", "cart": cart}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
