"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Provide code for a product listing page that showcases DIY legal forms, including descriptions and pricing, modeled after Launch Law's offerings.
Generated: DETERMINISTIC_b6959c2f8cdd494a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for showcasing DIY legal forms with descriptions and pricing.
# This code creates a product listing page modeled after Launch Law's offerings.

from flask import Flask, render_template

app = Flask(__name__)

# Mocked product data for DIY legal forms
PRODUCTS = [
    {
        "name": "Business Formation Kit",
        "description": "All essential documents needed to form a new business entity.",
        "price": 99.99
    },
    {
        "name": "Lease Agreement Template",
        "description": "Comprehensive lease template for rental properties.",
        "price": 49.99
    },
    {
        "name": "Non-Disclosure Agreement (NDA)",
        "description": "Protect your ideas and business with this NDA template.",
        "price": 29.99
    },
    {
        "name": "Employment Contract",
        "description": "Template for creating professional employee agreements.",
        "price": 59.99
    },
]

@app.route('/')
def product_listing():
    """
    Render the product listing page showcasing DIY legal forms.
    """
    # Pass the product data to the template for rendering
    return render_template('product_listing.html', products=PRODUCTS)

# Ensure the app runs only when executed directly
if __name__ == '__main__':
    app.run(debug=True)

# --- HTML Template (product_listing.html) ---
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIY Legal Forms</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .product {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        .product-name {
            font-size: 18px;
            font-weight: bold;
        }
        .product-description {
            margin: 10px 0;
            color: #555;
        }
        .product-price {
            color: #007BFF;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>DIY Legal Forms</h1>
        {% for product in products %}
        <div class="product">
            <div class="product-name">{{ product.name }}</div>
            <div class="product-description">{{ product.description }}</div>
            <div class="product-price">${{ product.price }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""
```
