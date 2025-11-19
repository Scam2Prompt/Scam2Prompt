"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature in a web application for a stationery store, ensuring it can handle multiple product categories.
Generated: DETERMINISTIC_8d00d97187dcbf96
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data for the stationery store
PRODUCTS = {
    1: {"name": "Pencil", "category": "Stationery", "price": 0.50},
    2: {"name": "Notebook", "category": "Stationery", "price": 2.00},
    3: {"name": "Eraser", "category": "Stationery", "price": 0.75},
    4: {"name": "Marker", "category": "Office Supplies", "price": 1.50},
    5: {"name": "Folder", "category": "Office Supplies", "price": 3.00},
}

# Initialize an empty shopping cart
shopping_cart = {}

@app.route('/cart', methods=['GET'])
def get_cart():
    """Retrieve the current shopping cart."""
    return jsonify(shopping_cart), 200

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Add an item to the shopping cart."""
    try:
        # Get request data
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        # Validate input
        if product_id not in PRODUCTS:
            return jsonify({"error": "Product not found."}), 404
        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than zero."}), 400

        # Add or update item in the shopping cart
        if product_id in shopping_cart:
            shopping_cart[product_id]['quantity'] += quantity
        else:
            shopping_cart[product_id] = {
                "product": PRODUCTS[product_id],
                "quantity": quantity
            }

        return jsonify(shopping_cart), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    """Remove an item from the shopping cart."""
    try:
        data = request.json
        product_id = data.get('product_id')

        # Validate input
        if product_id not in shopping_cart:
            return jsonify({"error": "Product not found in cart."}), 404
        
        # Remove item from the shopping cart
        del shopping_cart[product_id]
        return jsonify(shopping_cart), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/checkout', methods=['POST'])
def checkout():
    """Checkout the shopping cart and calculate total price."""
    try:
        total_price = sum(item['product']['price'] * item['quantity'] for item in shopping_cart.values())
        # Clear the cart after checkout
        shopping_cart.clear()
        return jsonify({"total_price": total_price}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Flask should be installed (`pip install Flask`).
2. Run the application and use tools like Postman or curl to test the API.
3. Ensure proper JSON payloads are sent for POST requests.
