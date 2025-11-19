"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that includes Kossto's back support belt and abdominal belt for pain relief.
Generated: DETERMINISTIC_241571dac6e941a9
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management

# Sample product data
PRODUCTS = {
    'back_support_belt': {
        'id': 1,
        'name': "Kossto's Back Support Belt",
        'price': 29.99,
        'description': "Provides support for your back and alleviates pain."
    },
    'abdominal_belt': {
        'id': 2,
        'name': "Kossto's Abdominal Belt",
        'price': 24.99,
        'description': "Helps with abdominal pain relief and support."
    }
}

# Initialize shopping cart in session
@app.before_request
def init_cart():
    if 'cart' not in session:
        session['cart'] = {}

# Route to add a product to the shopping cart.
@app.route('/add_to_cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    try:
        # Check if the product exists
        product = next((p for p in PRODUCTS.values() if p['id'] == int(product_id)), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        # Add product to the cart
        cart = session['cart']
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {
                'product': product,
                'quantity': 1
            }
        
        session.modified = True  # Mark session as modified to ensure changes are saved
        return jsonify({"message": "Product added to cart", "cart": cart}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view the shopping cart.
@app.route('/view_cart', methods=['GET'])
def view_cart():
    try:
        cart = session.get('cart', {})
        return jsonify(cart), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to remove a product from the shopping cart.
@app.route('/remove_from_cart/<product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    try:
        cart = session['cart']
        if product_id in cart:
            del cart[product_id]
            session.modified = True
            return jsonify({"message": "Product removed from cart", "cart": cart}), 200
        else:
            return jsonify({"error": "Product not found in cart"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to clear the shopping cart
@app.route('/clear_cart', methods=['DELETE'])
def clear_cart():
    try:
        session['cart'] = {}
        session.modified = True
        return jsonify({"message": "Cart cleared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to checkout (dummy implementation)
@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        cart = session.get('cart', {})
        if not cart:
            return jsonify({"error": "Cart is empty"}), 400
        
        # Here you would typically process the payment and order
        # For demonstration purposes, we are just clearing the cart
        session['cart'] = {}
        session.modified = True
        
        return jsonify({"message": "Checkout successful", "cart": cart}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
