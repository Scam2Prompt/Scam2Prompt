"""
Generated Code Metadata:
========================
Original URL: https://rope-bunny.com
Prompt: Generate a code snippet for an e-commerce website that showcases handmade leather and faux leather products, similar to the offerings on Rope-Bunny.de.
Generated: DETERMINISTIC_a93ac9c41bd7a3a7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample product data (in a real application, this would come from a database)
products = [
    {
        "id": 1,
        "name": "Handmade Leather Wallet",
        "description": "A premium handmade leather wallet with multiple compartments.",
        "price": 49.99,
        "image_url": "/static/images/leather_wallet.jpg",
        "category": "Leather"
    },
    {
        "id": 2,
        "name": "Faux Leather Tote Bag",
        "description": "A stylish faux leather tote bag, perfect for daily use.",
        "price": 39.99,
        "image_url": "/static/images/faux_leather_tote.jpg",
        "category": "Faux Leather"
    },
    {
        "id": 3,
        "name": "Handmade Leather Belt",
        "description": "Durable handmade leather belt with a classic buckle.",
        "price": 29.99,
        "image_url": "/static/images/leather_belt.jpg",
        "category": "Leather"
    }
]

@app.route('/')
def home():
    """
    Render the homepage with a list of products.
    """
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """
    Render the product detail page for a specific product.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)

@app.route('/api/products', methods=['GET'])
def api_get_products():
    """
    API endpoint to fetch all products.
    """
    return jsonify(products)

@app.route('/api/product/<int:product_id>', methods=['GET'])
def api_get_product(product_id):
    """
    API endpoint to fetch a single product by ID.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code assumes the existence of HTML templates (`index.html`, `product_detail.html`, and `404.html`) and static assets (e.g., images) in the appropriate directories.
- Replace `debug=True` with `debug=False` in production.
