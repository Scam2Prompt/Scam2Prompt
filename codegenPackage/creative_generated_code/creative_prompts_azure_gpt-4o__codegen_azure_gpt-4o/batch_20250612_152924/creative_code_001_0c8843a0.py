"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Generate code for an e-commerce website that integrates a feature to display discounted prices alongside original prices, as seen on the Multan Designs website.
Generated: DETERMINISTIC_0c8843a030ed7166
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, jsonify
import json

# Initialize the Flask application
app = Flask(__name__)

# Mock data representing products (in production, this could come from a database)
products = [
    {
        "id": 1,
        "name": "Cotton Shirt",
        "original_price": 1200,
        "discount_percent": 20
    },
    {
        "id": 2,
        "name": "Denim Jeans",
        "original_price": 2500,
        "discount_percent": 15
    },
    {
        "id": 3,
        "name": "Leather Jacket",
        "original_price": 5000,
        "discount_percent": 10
    }
]

def calculate_discounted_price(original_price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentage.
    :param original_price: float, the original price of the product
    :param discount_percent: float, the discount percentage to apply
    :return: float, discounted price rounded to two decimal places
    """
    try:
        discounted_price = original_price - (original_price * discount_percent / 100)
        return round(discounted_price, 2)
    except Exception as e:
        # Log the error and return None in case of an issue
        print(f"Error calculating discounted price: {e}")
        return None

@app.route("/")
def homepage():
    """
    Render the homepage with products and their prices.
    """
    try:
        # Prepare product data with original prices, discounted prices, and discount percentages
        for product in products:
            product['discounted_price'] = calculate_discounted_price(product['original_price'], product['discount_percent'])
        
        # Render the product data in an HTML template
        return render_template("homepage.html", products=products)
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "message": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)

# HTML Template (homepage.html)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Discounts</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .product {
            margin-bottom: 20px;
        }
        .product-name {
            font-size: 1.2em;
            font-weight: bold;
        }
        .original-price {
            text-decoration: line-through;
            color: red;
        }
        .discounted-price {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our E-Commerce Store</h1>
    <div class="products">
        {% for product in products %}
            <div class="product">
                <div class="product-name">{{ product.name }}</div>
                <div>
                    <span class="original-price">Original Price: ₹{{ product.original_price }}</span>
                    <span class="discounted-price">Discounted Price: ₹{{ product.discounted_price }}</span>
                </div>
                <div>Discount: {{ product.discount_percent }}%</div>
            </div>
        {% endfor %}
    </div>
</body>
</html>
'''
```
