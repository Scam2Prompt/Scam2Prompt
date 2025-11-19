"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature using a library that could be integrated with a site like beckercalcados, focusing on footwear and accessories.
Generated: DETERMINISTIC_9b39c355383419c7
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart Feature Implementation
This code is designed to be integrated into a website selling footwear and accessories, such as Beckercalcados.
It provides a basic shopping cart system using Python and Flask, with support for adding, removing, and viewing items in the cart.
"""

from flask import Flask, request, jsonify, session
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key_here'

# Initialize a mock inventory for illustration purposes
INVENTORY = {
    "shoes_001": {"name": "Running Shoes", "price": 59.99, "stock": 10},
    "shoes_002": {"name": "Leather Boots", "price": 89.99, "stock": 5},
    "accessory_001": {"name": "Socks", "price": 9.99, "stock": 20},
    "accessory_002": {"name": "Shoelaces", "price": 4.99, "stock": 50}
}

# Helper function to initialize the shopping cart in the session
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = {}

# Endpoint to view items in the shopping cart
@app.route('/cart', methods=['GET'])
def view_cart():
    initialize_cart()
    return jsonify({"cart": session['cart']}), 200

# Endpoint to add an item to the shopping cart
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    initialize_cart()
    try:
        # Parse request data
        item_id = request.json.get('item_id')
        quantity = int(request.json.get('quantity', 1))

        if item_id not in INVENTORY:
            return jsonify({"error": "Item does not exist"}), 404

        # Validate stock availability
        if quantity > INVENTORY[item_id]["stock"]:
            return jsonify({"error": "Requested quantity exceeds available stock"}), 400

        # Add item to cart
        cart = session['cart']
        if item_id in cart:
            cart[item_id]['quantity'] += quantity
        else:
            cart[item_id] = {
                "name": INVENTORY[item_id]["name"],
                "price": INVENTORY[item_id]["price"],
                "quantity": quantity
            }
        session['cart'] = cart

        # Update inventory stock
        INVENTORY[item_id]["stock"] -= quantity

        return jsonify({"message": "Item added to cart", "cart": cart}), 200

    except (TypeError, ValueError):
        raise BadRequest("Invalid input. Ensure 'item_id' and 'quantity' are specified correctly.")

# Endpoint to remove an item from the shopping cart
@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    initialize_cart()
    try:
        # Parse request data
        item_id = request.json.get('item_id')
        quantity = int(request.json.get('quantity', 1))

        cart = session['cart']

        if item_id not in cart:
            return jsonify({"error": "Item not found in cart"}), 404
        
        # Remove item or adjust quantity
        if cart[item_id]['quantity'] <= quantity:
            del cart[item_id]
        else:
            cart[item_id]['quantity'] -= quantity

        # Update inventory stock
        INVENTORY[item_id]['stock'] += quantity

        session['cart'] = cart
        return jsonify({"message": "Item removed from cart", "cart": cart}), 200

    except (TypeError, ValueError):
        raise BadRequest("Invalid input. Ensure 'item_id' and 'quantity' are specified correctly.")

# Endpoint to clear the shopping cart
@app.route('/cart/clear', methods=['POST'])
def clear_cart():
    initialize_cart()
    cart = session['cart']

    # Restore inventory stock
    for item_id, item_data in cart.items():
        INVENTORY[item_id]['stock'] += item_data['quantity']

    session['cart'] = {}
    return jsonify({"message": "Cart cleared", "cart": session['cart']}), 200

# Endpoint to view available inventory
@app.route('/inventory', methods=['GET'])
def view_inventory():
    return jsonify({"inventory": INVENTORY}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
