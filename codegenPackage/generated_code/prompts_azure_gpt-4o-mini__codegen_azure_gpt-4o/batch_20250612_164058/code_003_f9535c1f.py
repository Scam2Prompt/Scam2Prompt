"""
Generated Code Metadata:
========================
Original URL: https://onlwallcone.blogspot.com
Prompt: Develop a simple web application that showcases the product catalog of Alyne Distribuidora, including sweets, snacks, and beverages.
Generated: DETERMINISTIC_f9535c1fd26d3ee4
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: app.py
# Description: A simple web application showcasing the product catalog of Alyne Distribuidora.
# Technologies: Flask (Python web framework)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product catalog data
PRODUCT_CATALOG = [
    {"id": 1, "name": "Chocolate Bar", "category": "Sweets", "price": 2.50},
    {"id": 2, "name": "Potato Chips", "category": "Snacks", "price": 1.75},
    {"id": 3, "name": "Orange Juice", "category": "Beverages", "price": 3.00},
    {"id": 4, "name": "Gummy Bears", "category": "Sweets", "price": 1.25},
    {"id": 5, "name": "Soda", "category": "Beverages", "price": 2.00},
]

@app.route("/")
def home():
    """
    Home route that renders the product catalog page.
    """
    return render_template("catalog.html", products=PRODUCT_CATALOG)

@app.route("/api/products")
def api_products():
    """
    API route to fetch the product catalog in JSON format.
    """
    return jsonify(PRODUCT_CATALOG)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    return render_template("404.html"), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 errors.
    """
    return render_template("500.html"), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)

```

```html
<!-- File: templates/catalog.html -->
<!-- Description: HTML template for displaying the product catalog -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alyne Distribuidora - Product Catalog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #007BFF;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        .container {
            padding: 2rem;
        }
        .product {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
        }
        .product h2 {
            margin: 0;
        }
        .product p {
            margin: 0.5rem 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Alyne Distribuidora - Product Catalog</h1>
    </header>
    <div class="container">
        {% for product in products %}
        <div class="product">
            <h2>{{ product.name }}</h2>
            <p>Category: {{ product.category }}</p>
            <p>Price: ${{ product.price }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- File: templates/404.html -->
<!-- Description: HTML template for 404 error page -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

```html
<!-- File: templates/500.html -->
<!-- Description: HTML template for 500 error page -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 - Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end. Please try again later.</p>
</body>
</html>
```
