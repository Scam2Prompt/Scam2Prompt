"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Generate a code snippet for an e-commerce website that showcases handmade leather and faux leather products, similar to the offerings on Rope-Bunny.de.
Generated: DETERMINISTIC_a93ac9c41bd7a3a7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Sample product data for handmade leather and faux leather products
# In production, this data would typically come from a database
PRODUCTS = [
    {
        "id": 1,
        "name": "Handmade Leather Wallet",
        "description": "Premium leather wallet crafted with care.",
        "price": 49.99,
        "image_url": "/static/images/leather_wallet.jpg",
        "category": "leather"
    },
    {
        "id": 2,
        "name": "Faux Leather Backpack",
        "description": "Stylish faux leather backpack for everyday use.",
        "price": 65.99,
        "image_url": "/static/images/faux_backpack.jpg",
        "category": "faux_leather"
    },
    {
        "id": 3,
        "name": "Handmade Leather Belt",
        "description": "Elegant leather belt with classic design.",
        "price": 39.99,
        "image_url": "/static/images/leather_belt.jpg",
        "category": "leather"
    },
]

# Route for homepage
@app.route('/')
def homepage():
    """
    Render the homepage displaying handmade leather and faux leather products.
    """
    return render_template('index.html', products=PRODUCTS)

# Route for product details
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Render the product details page for a specific product.
    """
    # Search for the product by ID
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    
    # Handle case where product is not found
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return render_template('product_details.html', product=product)

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

# Run the Flask app
if __name__ == "__main__":
    # Ensure the app runs only when executed directly
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Files required to make this code functional:**

1. `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce - Handmade Products</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Handmade Leather & Faux Leather Products</h1>
    <div class="products">
        {% for product in products %}
        <div class="product">
            <img src="{{ product.image_url }}" alt="{{ product.name }}">
            <h2><a href="/product/{{ product.id }}">{{ product.name }}</a></h2>
            <p>{{ product.description }}</p>
            <p><strong>Price:</strong> ${{ product.price }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

2. `templates/product_details.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>{{ product.name }}</h1>
    <img src="{{ product.image_url }}" alt="{{ product.name }}">
    <p>{{ product.description }}</p>
    <p><strong>Price:</strong> ${{ product.price }}</p>
    <a href="/">Back to Products</a>
</body>
</html>
```

3. `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Back to Homepage</a>
</body>
</html>
```

4. Static assets folder (`static`) should contain images (e.g., `leather_wallet.jpg`, `faux_backpack.jpg`, etc.) and CSS (`style.css`) for styling.
