"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Develop a RESTful API endpoint that allows users to search for "لوازم منزل" and "مبلمان باغی" by price range and product type.
Generated: DETERMINISTIC_03eb1bc02afd837a
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for products (in real-world applications, this would come from a database)
PRODUCTS = [
    {"id": 1, "name": "لوازم منزل", "type": "home_accessory", "price": 100},
    {"id": 2, "name": "مبلمان باغی", "type": "garden_furniture", "price": 300},
    {"id": 3, "name": "لوازم منزل", "type": "home_accessory", "price": 200},
    {"id": 4, "name": "مبلمان باغی", "type": "garden_furniture", "price": 400},
]

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """
    RESTful API endpoint to search for products based on price range and product type.
    ---
    Parameters:
    - `min_price` (query string): Minimum price for filtering results (required).
    - `max_price` (query string): Maximum price for filtering results (required).
    - `type` (query string): Product type to filter results (optional, e.g., "home_accessory" or "garden_furniture").

    Returns:
    - JSON object containing the filtered list of products.
    """
    try:
        # Retrieve query parameters
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        product_type = request.args.get('type', type=str)

        # Validate required parameters
        if min_price is None or max_price is None:
            raise BadRequest("Both min_price and max_price parameters are required.")

        # Filter products based on price range and optional product type
        filtered_products = [
            product for product in PRODUCTS
            if min_price <= product['price'] <= max_price and
               (product_type is None or product['type'] == product_type)
        ]

        return jsonify({"success": True, "products": filtered_products}), 200

    except BadRequest as e:
        # Handle missing query parameters or other request issues
        return jsonify({"success": False, "error": str(e)}), 400

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"success": False, "error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
