"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://michelledoylegoldsmith.com
Prompt: Develop a shopping cart feature for a website specializing in custom jewelry, ensuring it includes options for ethically sourced gemstones and recycled gold.
Generated: DETERMINISTIC_56e395f94d47cc05
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Sample product data (normally stored in a database)
PRODUCTS = {
    1: {"name": "Custom Ring", "price": 200, "ethically_sourced": True, "recycled_gold": False},
    2: {"name": "Ethical Sapphire Necklace", "price": 500, "ethically_sourced": True, "recycled_gold": True},
    3: {"name": "Recycled Gold Bracelet", "price": 150, "ethically_sourced": False, "recycled_gold": True},
}

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def cart():
    """Manage the shopping cart."""
    if 'cart' not in session:
        session['cart'] = {}

    if request.method == 'POST':
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity', 1)

        if product_id not in PRODUCTS:
            return jsonify({"error": "Product not found"}), 404

        # Add product to the cart
        if product_id in session['cart']:
            session['cart'][product_id] += quantity
        else:
            session['cart'][product_id] = quantity
        return jsonify({"message": "Product added to cart", "cart": session['cart']}), 200

    elif request.method == 'GET':
        # Return the current shopping cart
        return jsonify({"cart": session['cart']}), 200

    elif request.method == 'DELETE':
        product_id = request.json.get('product_id')

        if product_id in session['cart']:
            del session['cart'][product_id]
            return jsonify({"message": "Product removed from cart", "cart": session['cart']}), 200
        else:
            return jsonify({"error": "Product not found in cart"}), 404

    return jsonify({"error": "Invalid request method"}), 405

@app.route('/products', methods=['GET'])
def list_products():
    """List all available products."""
    return jsonify(PRODUCTS), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask using `pip install Flask` and replace `'your_secret_key'` with a secure key before running the application.
