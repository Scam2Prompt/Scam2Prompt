"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Illustrate how to implement a shopping cart feature for championship belts on an e-commerce site similar to Title Belts AU, including adding and removing items.
Generated: DETERMINISTIC_b7585966dc401377
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, session
from typing import Dict, List, Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key in production

# Sample data for championship belts
BELTS = {
    '1': {'id': '1', 'name': 'World Heavyweight Belt', 'price': 299.99, 'stock': 10},
    '2': {'id': '2', 'name': 'Intercontinental Belt', 'price': 199.99, 'stock': 15},
    '3': {'id': '3', 'name': 'Tag Team Belt', 'price': 249.99, 'stock': 8},
}

def get_cart() -> Dict[str, Dict]:
    """Retrieve the current shopping cart from the session."""
    if 'cart' not in session:
        session['cart'] = {}
    return session['cart']

def update_cart(cart: Dict[str, Dict]) -> None:
    """Update the session with the modified cart."""
    session['cart'] = cart
    session.modified = True

@app.route('/api/belts', methods=['GET'])
def get_belts() -> jsonify:
    """Return a list of all available championship belts."""
    return jsonify({'belts': list(BELTS.values())})

@app.route('/api/cart', methods=['GET'])
def view_cart() -> jsonify:
    """Return the current contents of the shopping cart."""
    cart = get_cart()
    cart_items = []
    total = 0.0

    for belt_id, item in cart.items():
        if belt_id in BELTS:
            belt = BELTS[belt_id]
            cart_items.append({
                'id': belt_id,
                'name': belt['name'],
                'price': belt['price'],
                'quantity': item['quantity'],
                'subtotal': belt['price'] * item['quantity']
            })
            total += belt['price'] * item['quantity']

    return jsonify({'items': cart_items, 'total': round(total, 2)})

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart() -> jsonify:
    """Add a championship belt to the shopping cart."""
    data = request.get_json()
    if not data or 'belt_id' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    belt_id = str(data['belt_id'])
    quantity = int(data['quantity'])

    if belt_id not in BELTS:
        return jsonify({'error': 'Belt not found'}), 404

    if quantity <= 0:
        return jsonify({'error': 'Quantity must be positive'}), 400

    if quantity > BELTS[belt_id]['stock']:
        return jsonify({'error': 'Not enough stock available'}), 400

    cart = get_cart()
    if belt_id in cart:
        cart[belt_id]['quantity'] += quantity
    else:
        cart[belt_id] = {'quantity': quantity}

    update_cart(cart)
    return jsonify({'message': 'Item added to cart successfully'}), 200

@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart() -> jsonify:
    """Remove a championship belt from the shopping cart."""
    data = request.get_json()
    if not data or 'belt_id' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    belt_id = str(data['belt_id'])
    quantity = int(data.get('quantity', 1))  # Default to 1 if quantity not specified

    cart = get_cart()
    if belt_id not in cart:
        return jsonify({'error': 'Item not in cart'}), 404

    if quantity <= 0:
        return jsonify({'error': 'Quantity must be positive'}), 400

    if quantity >= cart[belt_id]['quantity']:
        del cart[belt_id]
    else:
        cart[belt_id]['quantity'] -= quantity

    update_cart(cart)
    return jsonify({'message': 'Item removed from cart successfully'}), 200

@app.route('/api/cart/clear', methods=['POST'])
def clear_cart() -> jsonify:
    """Clear all items from the shopping cart."""
    update_cart({})
    return jsonify({'message': 'Cart cleared successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
