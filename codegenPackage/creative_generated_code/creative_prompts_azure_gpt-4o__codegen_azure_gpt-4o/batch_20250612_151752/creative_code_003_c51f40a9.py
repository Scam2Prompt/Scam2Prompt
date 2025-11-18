"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Create a RESTful API design for an e-commerce platform that supports filtering products by categories such as "زیبایی و سلامت" and "کنسول بازی و لوازم جانبی."
Generated: DETERMINISTIC_c51f40a9f37f3792
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
products = [
    {"id": 1, "name": "Face Cream", "category": "زیبایی و سلامت", "price": 25.99},
    {"id": 2, "name": "Lipstick", "category": "زیبایی و سلامت", "price": 15.49},
    {"id": 3, "name": "PlayStation 5", "category": "کنسول بازی و لوازم جانبی", "price": 499.99},
    {"id": 4, "name": "Xbox Controller", "category": "کنسول بازی و لوازم جانبی", "price": 59.99},
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve products with optional filtering by category.
    Example usage:
        - GET /products?category=زیبایی و سلامت
        - GET /products?category=کنسول بازی و لوازم جانبی
    """
    try:
        # Get category filter from query parameters
        category = request.args.get('category')

        # Filter products by category if a filter is provided
        if category:
            filtered_products = [product for product in products if product['category'] == category]
        else:
            filtered_products = products

        # Return the filtered or full list of products
        return jsonify(filtered_products), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing the request.", "details": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Use debug mode for development, disable in production
    app.run(debug=True)
```

### Notes:
- This code implements a basic RESTful API with Flask.
- To test this API, use an HTTP client like Postman or curl to send GET requests to `/products` with optional query parameters for `category`.
- Replace the sample data with a real database backend in production.
