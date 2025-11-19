"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Generate a code snippet for setting up an e-commerce website using the tools and methods discussed on FinishDrop, focusing on product integration and optimized site design.
Generated: DETERMINISTIC_f50d8576f52a89f2
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python code snippet using the Flask framework for setting up an e-commerce website. It focuses on product integration and optimized site design.

```python
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Initialize Flask app
app = Flask(__name__)

# In-memory database for products (For production, use a real database like PostgreSQL/MySQL)
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "description": "High-performance laptop", "image_url": "/static/images/laptop.jpg"},
    {"id": 2, "name": "Phone", "price": 499.99, "description": "Latest smartphone", "image_url": "/static/images/phone.jpg"},
]

# Home Page: Display Available Products
@app.route('/')
def home():
    """
    Route to display the home page with product listings.
    """
    return render_template('home.html', products=products)

# Product Details Page
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Route to display details for a specific product.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return "Product not found", 404
    return render_template('product_details.html', product=product)

# Add New Product (Admin Route)
@app.route('/add-product', methods=['POST'])
def add_product():
    """
    Route to add a new product (accessible via POST request).
    """
    try:
        # Extract product data from the request
        new_product = {
            "id": len(products) + 1,
            "name": request.form['name'],
            "price": float(request.form['price']),
            "description": request.form['description'],
            "image_url": request.form['image_url']
        }
        products.append(new_product)
        # Redirect to the home page after adding the product
        return redirect(url_for('home'))
    except Exception as e:
        # Handle errors gracefully
        return f"Error adding product: {str(e)}", 500

# API to List All Products (JSON Response)
@app.route('/api/products', methods=['GET'])
def api_get_products():
    """
    Route to retrieve all products in JSON format.
    """
    return jsonify(products)

# Error Handling: Custom 404 Page
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error page for 404 Not Found errors.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Use debug=True for development; for production, set debug=False
    app.run(debug=True)
```

### Directory Structure:
```
/static/
    images/
        laptop.jpg
        phone.jpg
/templates/
    home.html
    product_details.html
    404.html
app.py  (The above Python script)
```

### Sample `home.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Site</title>
</head>
<body>
    <h1>Welcome to Our E-Commerce Site!</h1>
    <ul>
        {% for product in products %}
        <li>
            <a href="{{ url_for('product_details', product_id=product.id) }}">
                <img src="{{ product.image_url }}" alt="{{ product.name }}" style="width:100px;height:100px;">
                <h2>{{ product.name }}</h2>
                <p>${{ product.price }}</p>
            </a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Sample `product_details.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <img src="{{ product.image_url }}" alt="{{ product.name }}" style="width:200px;height:200px;">
    <p>Description: {{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Sample `404.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```
