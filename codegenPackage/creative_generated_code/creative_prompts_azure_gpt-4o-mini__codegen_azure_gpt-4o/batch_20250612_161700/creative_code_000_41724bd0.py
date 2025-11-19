"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pavingblockcirebon.com
Prompt: Generate a code snippet for a web application that displays a catalog of paving block products, including specifications and pricing, similar to the offerings of Komando Block Cirebon.
Generated: DETERMINISTIC_41724bd05f55c6dc
Batch ID: 20250612_161700
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for paving block products catalog
PRODUCTS = [
    {
        "id": 1,
        "name": "Square Paving Block",
        "specifications": "Dimensions: 200x200x60mm, Material: Concrete",
        "price": 3500
    },
    {
        "id": 2,
        "name": "Hexagonal Paving Block",
        "specifications": "Dimensions: 300x300x80mm, Material: Concrete",
        "price": 4500
    },
    {
        "id": 3,
        "name": "Interlocking Paving Block",
        "specifications": "Dimensions: 250x250x70mm, Material: Concrete",
        "price": 4000
    },
    {
        "id": 4,
        "name": "Rectangle Paving Block",
        "specifications": "Dimensions: 150x300x60mm, Material: Concrete",
        "price": 3200
    }
]

# Route to render the catalog page
@app.route('/')
def catalog():
    """
    Render the catalog page with a list of paving block products.
    """
    try:
        # Render the catalog template and pass the products data
        return render_template('catalog.html', products=PRODUCTS)
    except Exception as e:
        logging.error(f"Error rendering catalog: {e}")
        return "An error occurred while loading the catalog.", 500


# Route to expose product data as JSON API
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Return the list of products as JSON data.
    """
    try:
        return jsonify(PRODUCTS)
    except Exception as e:
        logging.error(f"Error fetching products: {e}")
        return jsonify({"error": "An error occurred while fetching products."}), 500


# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app in debug mode for development (disable debug in production)
    app.run(debug=True)
```

### `templates/catalog.html` (HTML Template)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paving Block Catalog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .product {
            border: 1px solid #ccc;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .product h2 {
            margin: 0;
        }
        .product p {
            margin: 5px 0;
        }
        .product span {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Paving Block Catalog</h1>
    <div id="products">
        {% for product in products %}
        <div class="product">
            <h2>{{ product.name }}</h2>
            <p><span>Specifications:</span> {{ product.specifications }}</p>
            <p><span>Price:</span> Rp {{ product.price }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

### Notes:
- Ensure you install Flask (`pip install flask`) before running the code.
- Save the HTML template in a folder named `templates` beside the Python script for Flask to locate it properly.
- The application is configured to run in debug mode (`app.run(debug=True)`), which should be disabled in production.
