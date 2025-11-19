"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Generate a code snippet for an e-commerce website that displays a collection of MDF art products, including categories like "Name and Monogram Wall Plate" and "Tea Coaster."
Generated: DETERMINISTIC_399618aac011844b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for MDF art products
products = [
    {
        "id": 1,
        "name": "Name and Monogram Wall Plate",
        "category": "Wall Decor",
        "price": 25.99,
        "description": "Personalized wall plate made of high-quality MDF material.",
        "image_url": "/static/images/monogram_wall_plate.jpg",
    },
    {
        "id": 2,
        "name": "Tea Coaster Set",
        "category": "Dining Decor",
        "price": 15.99,
        "description": "Crafted MDF tea coaster set with artistic designs.",
        "image_url": "/static/images/tea_coaster_set.jpg",
    },
]

@app.route('/')
def index():
    """
    Render the home page with the list of MDF art products.
    """
    return render_template('index.html', products=products)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    API endpoint to retrieve the list of products in JSON format.
    """
    try:
        # Return JSON representation of the products
        return jsonify(products), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": "An error occurred while fetching products", "details": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)

# Below is a sample template for `index.html` located in the `templates` folder:
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDF Art Products</title>
</head>
<body>
    <h1>Welcome to Our MDF Art Collection</h1>
    <div>
        {% for product in products %}
        <div style="margin-bottom: 20px; border: 1px solid #ddd; padding: 10px;">
            <h2>{{ product.name }}</h2>
            <p>Category: {{ product.category }}</p>
            <p>Description: {{ product.description }}</p>
            <p>Price: ${{ product.price }}</p>
            <img src="{{ product.image_url }}" alt="{{ product.name }}" style="width: 200px; height: auto;">
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""
```
