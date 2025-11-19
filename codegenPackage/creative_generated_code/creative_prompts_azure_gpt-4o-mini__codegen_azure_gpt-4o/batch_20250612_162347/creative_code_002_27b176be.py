"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Create an API endpoint that allows users to filter products by category, such as electronics and fashion, as seen on the Xhawi by Omantel website.
Generated: DETERMINISTIC_27b176be33768fee
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Example in-memory product data
PRODUCTS = [
    {"id": 1, "name": "Smartphone", "category": "electronics", "price": 699},
    {"id": 2, "name": "Laptop", "category": "electronics", "price": 1099},
    {"id": 3, "name": "T-Shirt", "category": "fashion", "price": 20},
    {"id": 4, "name": "Jeans", "category": "fashion", "price": 50},
]

@app.errorhandler(HTTPException)
def handle_http_error(e):
    """Handle HTTP exceptions globally."""
    response = jsonify({"error": e.description})
    response.status_code = e.code
    return response

@app.errorhandler(Exception)
def handle_generic_error(e):
    """Handle generic exceptions globally."""
    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response

@app.route('/api/products', methods=['GET'])
def filter_products():
    """
    API endpoint to filter products by category.
    Query parameter: ?category=<category_name>
    Returns a list of products matching the category.
    """
    try:
        # Get category from query parameters
        category = request.args.get('category', '').strip().lower()
        
        if not category:
            # If no category is provided, return a 400 Bad Request response
            return jsonify({"error": "Missing 'category' query parameter"}), 400
        
        # Filter products by category
        filtered_products = [product for product in PRODUCTS if product['category'] == category]
        
        # Return the filtered products
        return jsonify(filtered_products), 200
    except Exception as e:
        # Log and handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
