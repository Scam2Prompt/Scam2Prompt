"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: "Design a simple API to manage wishlist and cart functionality for an e-commerce website like Gvika."
Generated: DETERMINISTIC_0b34d27dec2ea141
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for wishlist and cart
wishlist = {}
cart = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to add an item to the wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    try:
        data = request.json
        item_id = generate_id()
        item = {
            "id": item_id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": data.get("quantity", 1)
        }
        if not item["name"] or not item["price"]:
            return error_response("Item name and price are required.")
        wishlist[item_id] = item
        return jsonify({"message": "Item added to wishlist.", "item": item}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to view all items in the wishlist
@app.route('/wishlist', methods=['GET'])
def view_wishlist():
    return jsonify({"wishlist": list(wishlist.values())}), 200

# Route to remove an item from the wishlist
@app.route('/wishlist/<item_id>', methods=['DELETE'])
def remove_from_wishlist(item_id):
    if item_id in wishlist:
        removed_item = wishlist.pop(item_id)
        return jsonify({"message": "Item removed from wishlist.", "item": removed_item}), 200
    return error_response("Item not found in wishlist.", 404)

# Route to add an item to the cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.json
        item_id = generate_id()
        item = {
            "id": item_id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": data.get("quantity", 1)
        }
        if not item["name"] or not item["price"]:
            return error_response("Item name and price are required.")
        cart[item_id] = item
        return jsonify({"message": "Item added to cart.", "item": item}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to view all items in the cart
@app.route('/cart', methods=['GET'])
def view_cart():
    return jsonify({"cart": list(cart.values())}), 200

# Route to remove an item from the cart
@app.route('/cart/<item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    if item_id in cart:
        removed_item = cart.pop(item_id)
        return jsonify({"message": "Item removed from cart.", "item": removed_item}), 200
    return error_response("Item not found in cart.", 404)

# Route to move an item from wishlist to cart
@app.route('/wishlist-to-cart/<item_id>', methods=['POST'])
def move_wishlist_to_cart(item_id):
    if item_id in wishlist:
        item = wishlist.pop(item_id)
        cart[item_id] = item
        return jsonify({"message": "Item moved from wishlist to cart.", "item": item}), 200
    return error_response("Item not found in wishlist.", 404)

# Route to clear the wishlist
@app.route('/wishlist/clear', methods=['DELETE'])
def clear_wishlist():
    wishlist.clear()
    return jsonify({"message": "Wishlist cleared."}), 200

# Route to clear the cart
@app.route('/cart/clear', methods=['DELETE'])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cart cleared."}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
