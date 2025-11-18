"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Recommend a framework to create a responsive e-commerce website for a tech store like Akash Infotech, focusing on showcasing computer products and accessories.
Generated: DETERMINISTIC_dfdb133bb14c8063
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the Flask framework as a backend to create a responsive e-commerce website
for showcasing computer products and accessories. Flask provides simplicity and flexibility,
while integrating well with modern front-end frameworks like React/Vue.js for responsive design.
"""

from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Example product data (in a production app, use a database)
PRODUCTS = [
    {
        "id": 1,
        "name": "Gaming Laptop",
        "price": 1200.00,
        "category": "Computers",
        "description": "High-performance laptop for gaming and productivity.",
        "image_url": "/static/images/gaming_laptop.jpg"
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "price": 25.00,
        "category": "Accessories",
        "description": "Ergonomic wireless mouse with adjustable DPI settings.",
        "image_url": "/static/images/wireless_mouse.jpg"
    },
    # Add more products as necessary...
]

@app.route("/")
def home():
    """
    Home route to render the main page of the e-commerce site.
    The main page displays a list of products.
    """
    return render_template("index.html", products=PRODUCTS)

@app.route("/product/<int:product_id>")
def product_details(product_id):
    """
    Route to display the details of a specific product.
    :param product_id: ID of the product to display.
    """
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return render_template("product_details.html", product=product)

@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error handler to display a user-friendly error page.
    """
    return render_template("404.html"), 404

# Run the application
if __name__ == "__main__":
    # Use debug mode for development; disable in production for security.
    app.run(debug=True)
```

### Front-End Code (HTML templates)
Below are the basic templates for the application. Save these files in the `templates` folder.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akash Infotech - Home</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Welcome to Akash Infotech</h1>
    <div class="product-list">
        {% for product in products %}
        <div class="product">
            <h2>{{ product.name }}</h2>
            <img src="{{ product.image_url }}" alt="{{ product.name }}" width="150">
            <p>{{ product.description }}</p>
            <p>Price: ${{ product.price }}</p>
            <a href="/product/{{ product.id }}">View Details</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

#### `product_details.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} - Akash Infotech</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>{{ product.name }}</h1>
    <img src="{{ product.image_url }}" alt="{{ product.name }}" width="300">
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```

### Notes
1. Place the `static` folder alongside the `templates` folder, and include necessary CSS and images.
2. Use a database (e.g., SQLite, PostgreSQL) to store product data in a production environment.
3. Integrate with a modern front-end framework (like React or Vue.js) to enhance responsiveness and interactivity.
