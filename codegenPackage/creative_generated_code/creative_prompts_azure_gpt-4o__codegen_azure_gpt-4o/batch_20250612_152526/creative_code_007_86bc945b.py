"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Using Flask, create an API endpoint that allows users to search for products by category (e.g., "Watches," "Bags") and filters results based on discount percentage.
Generated: DETERMINISTIC_86bc945b9421297d
Batch ID: 20250612_152526
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

# Mock product data
PRODUCTS = [
    {"id": 1, "name": "Luxury Watch", "category": "Watches", "price": 500, "discount_percentage": 20},
    {"id": 2, "name": "Casual Watch", "category": "Watches", "price": 150, "discount_percentage": 10},
    {"id": 3, "name": "Leather Bag", "category": "Bags", "price": 300, "discount_percentage": 25},
    {"id": 4, "name": "Travel Backpack", "category": "Bags", "price": 120, "discount_percentage": 15},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    API endpoint to search for products by category and filter by discount percentage.
    Query parameters:
    - category: The category of products to search for (required).
    - min_discount: Minimum discount percentage to filter products (optional).
    """
    try:
        # Extract query parameters
        category = request.args.get('category')
        min_discount = request.args.get('min_discount', type=int)

        if not category:
            raise BadRequest("The 'category' parameter is required.")

        # Filter products based on category
        filtered_products = [product for product in PRODUCTS if product['category'].lower() == category.lower()]

        # Further filter by discount percentage, if provided
        if min_discount is not None:
            filtered_products = [product for product in filtered_products if product['discount_percentage'] >= min_discount]

        return jsonify({
            "status": "success",
            "data": filtered_products
        })

    except BadRequest as e:
        # Handle bad requests
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred."
        }), 500

if __name__ == '__main__':
    # Start Flask application
    app.run(debug=True)
```
