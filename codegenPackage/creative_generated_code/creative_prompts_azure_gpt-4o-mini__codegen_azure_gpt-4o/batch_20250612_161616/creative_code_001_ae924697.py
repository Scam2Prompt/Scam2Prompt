"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lunaroz.ro
Prompt: How can I implement a shopping cart feature that allows users to add personalized textile products, as seen on lunaroz.ro?
Generated: DETERMINISTIC_ae92469758818228
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation using Python and Flask for a shopping cart feature that allows users to add personalized textile products.

```python
from flask import Flask, request, jsonify, session
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Initialize shopping cart in session
@app.before_request
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

# Helper function to validate product input
def validate_product_input(data):
    required_fields = ['product_id', 'name', 'price', 'customization']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return False, "Invalid price value"
    return True, ""

# Route to add product to shopping cart
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    try:
        product_data = request.json
        # Validate input
        is_valid, error_message = validate_product_input(product_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate unique item ID for cart entry
        cart_item = {
            "item_id": str(uuid4()),  # Unique ID for the cart entry
            "product_id": product_data['product_id'],  # Product ID
            "name": product_data['name'],  # Product name
            "price": product_data['price'],  # Product price
            "customization": product_data['customization'],  # Customization details
            "quantity": product_data.get('quantity', 1)  # Default quantity is 1
        }

        # Add product to cart stored in session
        session['cart'].append(cart_item)
        session.modified = True  # Ensure session updates are saved
        return jsonify({"message": "Product added to cart", "cart_item": cart_item}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to view shopping cart
@app.route('/cart', methods=['GET'])
def view_cart():
    cart = session.get('cart', [])
    return jsonify({"cart": cart}), 200

# Route to remove a product from the cart
@app.route('/cart/remove/<item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    try:
        cart = session.get('cart', [])
        # Find the item in the cart
        updated_cart = [item for item in cart if item['item_id'] != item_id]
        if len(cart) == len(updated_cart):
            return jsonify({"error": "Item not found in cart"}), 404

        # Update session cart
        session['cart'] = updated_cart
        session.modified = True
        return jsonify({"message": "Item removed successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to clear the entire shopping cart
@app.route('/cart/clear', methods=['POST'])
def clear_cart():
    try:
        session['cart'] = []
        session.modified = True
        return jsonify({"message": "Cart cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features of the Code:
1. **Add Product:** Allows users to add personalized products with customization details.
2. **View Cart:** Retrieves all items currently in the shopping cart.
3. **Remove Product:** Removes a specific product from the cart using a unique item ID.
4. **Clear Cart:** Clears the entire shopping cart.
