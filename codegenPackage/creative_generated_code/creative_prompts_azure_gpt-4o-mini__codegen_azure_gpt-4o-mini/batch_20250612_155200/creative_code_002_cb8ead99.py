"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-azuki.com
Prompt: Provide an example of how to implement a shopping cart API that includes the CHIKARA cooling shirt and its specifications.
Generated: DETERMINISTIC_cb8ead9999f0f0ed
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample product data for the CHIKARA cooling shirt
products = {
    "CHIKARA_Cooling_Shirt": {
        "id": 1,
        "name": "CHIKARA Cooling Shirt",
        "description": "A high-performance cooling shirt designed for athletes.",
        "price": 49.99,
        "specifications": {
            "material": "Polyester",
            "color": "Blue",
            "sizes_available": ["S", "M", "L", "XL"],
            "moisture_wicking": True,
            "machine_washable": True
        }
    }
}

# In-memory shopping cart
cart = []

@app.route('/api/cart', methods=['GET'])
def get_cart():
    """Retrieve the current shopping cart contents."""
    return jsonify(cart), 200

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    """Add a product to the shopping cart."""
    product_id = request.json.get('product_id')

    # Validate input
    if product_id not in products:
        abort(404, description="Product not found.")

    # Add product to cart
    product = products[product_id]
    cart.append(product)
    return jsonify({"message": "Product added to cart.", "cart": cart}), 201

@app.route('/api/cart/clear', methods=['DELETE'])
def clear_cart():
    """Clear the shopping cart."""
    cart.clear()
    return jsonify({"message": "Shopping cart cleared."}), 200

@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart():
    """Remove a product from the shopping cart."""
    product_id = request.json.get('product_id')

    # Validate input
    if product_id not in products:
        abort(404, description="Product not found in the cart.")

    # Remove product from cart if it exists
    global cart
    cart = [item for item in cart if item['id'] != products[product_id]['id']]
    return jsonify({"message": "Product removed from cart.", "cart": cart}), 200

@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Return a custom 500 error message."""
    return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
