"""
Generated Code Metadata:
========================
Original URL: https://shopmetlife.pk
Prompt: Write a Python code snippet to create a product catalog page for an e-commerce website selling hair care products, including product names, prices, and descriptions, similar to the ones listed on ShopMetlife.
Generated: DETERMINISTIC_24930e26508ea686
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product data for the catalog
PRODUCTS = [
    {
        "id": 1,
        "name": "Hydrating Shampoo",
        "price": 15.99,
        "description": "A gentle shampoo that hydrates and nourishes your hair."
    },
    {
        "id": 2,
        "name": "Volumizing Conditioner",
        "price": 12.99,
        "description": "Adds volume and shine to your hair without weighing it down."
    },
    {
        "id": 3,
        "name": "Argan Oil Hair Serum",
        "price": 19.99,
        "description": "Smooths frizz and adds a healthy shine to your hair."
    },
    {
        "id": 4,
        "name": "Deep Repair Hair Mask",
        "price": 24.99,
        "description": "Repairs damaged hair and restores its natural strength."
    }
]

@app.route('/')
def product_catalog():
    """
    Renders the product catalog page with a list of hair care products.
    """
    try:
        # Render the catalog page with product data
        return render_template('catalog.html', products=PRODUCTS)
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({"error": "An error occurred while loading the catalog.", "details": str(e)}), 500

# HTML template for the product catalog (to be saved as 'templates/catalog.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hair Care Product Catalog</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .product { border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; border-radius: 5px; }
        .product h2 { margin: 0; font-size: 1.5em; }
        .product p { margin: 5px 0; }
        .product .price { font-weight: bold; color: #2a9d8f; }
    </style>
</head>
<body>
    <h1>Hair Care Product Catalog</h1>
    {% for product in products %}
    <div class="product">
        <h2>{{ product.name }}</h2>
        <p class="price">${{ product.price }}</p>
        <p>{{ product.description }}</p>
    </div>
    {% endfor %}
</body>
</html>
"""

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
```
