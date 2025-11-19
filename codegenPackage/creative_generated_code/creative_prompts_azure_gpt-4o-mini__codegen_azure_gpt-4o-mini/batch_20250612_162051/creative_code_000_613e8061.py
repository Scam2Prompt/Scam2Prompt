"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Generate a code snippet for an e-commerce website that implements a shopping cart feature, similar to the one found on Simplymente Airsoft, allowing users to add tactical clothing items like sweatshirts and t-shirts.
Generated: DETERMINISTIC_613e8061b55954e8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, session, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Sample item database
ITEMS = {
    1: {'name': 'Tactical Sweatshirt', 'price': 49.99},
    2: {'name': 'Tactical T-Shirt', 'price': 29.99},
}

@app.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    """Add an item to the shopping cart."""
    item = ITEMS.get(item_id)
    
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    # Initialize cart in session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = {}
    
    # Add or update the item in the cart
    if item_id in session['cart']:
        session['cart'][item_id]['quantity'] += 1
    else:
        session['cart'][item_id] = {'name': item['name'], 'price': item['price'], 'quantity': 1}

    return jsonify({'message': 'Item added to cart', 'cart': session['cart']}), 200

@app.route('/view_cart', methods=['GET'])
def view_cart():
    """View the items in the shopping cart."""
    cart = session.get('cart', {})
    return jsonify(cart), 200

@app.route('/remove_from_cart/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    """Remove an item from the shopping cart."""
    if 'cart' not in session or item_id not in session['cart']:
        return jsonify({'error': 'Item not in cart'}), 404
        
    # Reduce quantity or remove item from cart
    if session['cart'][item_id]['quantity'] > 1:
        session['cart'][item_id]['quantity'] -= 1
    else:
        del session['cart'][item_id]
    
    return jsonify({'message': 'Item removed from cart', 'cart': session['cart']}), 200

@app.route('/checkout', methods=['POST'])
def checkout():
    """Process the checkout of items in the cart."""
    cart = session.get('cart', {})
    
    if not cart:
        return jsonify({'error': 'Cart is empty'}), 400

    # Here, integrate payment processing (not implemented in this example)
    
    # Clear the cart after successful checkout
    session.pop('cart', None)
    
    return jsonify({'message': 'Checkout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
