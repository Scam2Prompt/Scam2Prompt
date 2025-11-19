"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a shopping cart with items, similar to the "Carrinho de Compras" feature on aquarelaesmalte.
Generated: DETERMINISTIC_117939f9d393ed84
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, render_template, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

# Sample items for demonstration purposes
ITEMS = {
    1: {'name': 'Nail Polish A', 'price': 10.00},
    2: {'name': 'Nail Polish B', 'price': 15.00},
    3: {'name': 'Nail Polish C', 'price': 20.00},
}

# Initialize shopping cart
@app.route('/cart')
def cart():
    """Display the shopping cart with items."""
    cart_items = session.get('cart', {})
    total_price = sum(ITEMS[item_id]['price'] * quantity for item_id, quantity in cart_items.items())
    
    return render_template('cart.html', cart=cart_items, total_price=total_price)

@app.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    """Add an item to the shopping cart."""
    if item_id not in ITEMS:
        flash('Item not found!', 'error')
        return redirect(url_for('cart'))

    cart = session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    session['cart'] = cart
    flash('Item added to cart!', 'success')
    
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    """Remove an item from the shopping cart."""
    cart = session.get('cart', {})
    
    if item_id in cart:
        del cart[item_id]
        session['cart'] = cart
        flash('Item removed from cart!', 'success')
    else:
        flash('Item not in cart!', 'error')
        
    return redirect(url_for('cart'))

if __name__ == '__main__':
    # Runs the Flask application
    app.run(debug=True)
```

```html
<!-- templates/cart.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    {% if cart %}
        <ul>
            {% for item_id, quantity in cart.items() %}
                <li>
                    {{ ITEMS[item_id]['name'] }} - Quantity: {{ quantity }} - Price: ${{ ITEMS[item_id]['price'] * quantity }}
                    <form action="{{ url_for('remove_from_cart', item_id=item_id) }}" method="post">
                        <button type="submit">Remove</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
        <h2>Total Price: ${{ total_price }}</h2>
    {% else %}
        <p>Your cart is empty.</p>
    {% endif %}
    <a href="/">Continue Shopping</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask installed in your environment to run the above code.
- Replace `'your_secret_key'` with a secure random key for session management.
- The HTML template should be placed in a folder named `templates` in the same directory as your script.
- Adjust the item names and prices in the `ITEMS` dictionary as needed.
