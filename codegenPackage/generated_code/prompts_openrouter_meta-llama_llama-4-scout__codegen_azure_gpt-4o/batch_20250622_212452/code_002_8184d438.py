"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate a RESTful API endpoint to retrieve a list of products, sorted by price, from a collection of tableware items similar to those on this webpage.
Generated: DETERMINISTIC_8184d438db741ef3
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing tableware items
tableware_items = [
    {"id": 1, "name": "Plate", "price": 12.99},
    {"id": 2, "name": "Cup", "price": 5.49},
    {"id": 3, "name": "Bowl", "price": 8.99},
    {"id": 4, "name": "Spoon", "price": 2.99},
    {"id": 5, "name": "Fork", "price": 3.49},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    RESTful API endpoint to retrieve a list of tableware products sorted by price.
    Query Parameters:
        - order: 'asc' for ascending order, 'desc' for descending order (default: 'asc')
    Returns:
        - JSON response containing the sorted list of products.
    """
    try:
        # Get the 'order' query parameter (default to 'asc' if not provided)
        order = request.args.get('order', 'asc').lower()
        
        # Validate the 'order' parameter
        if order not in ['asc', 'desc']:
            raise BadRequest("Invalid 'order' parameter. Use 'asc' or 'desc'.")
        
        # Sort the products by price based on the 'order' parameter
        sorted_items = sorted(tableware_items, key=lambda x: x['price'], reverse=(order == 'desc'))
        
        # Return the sorted list of products as a JSON response
        return jsonify(sorted_items), 200
    except BadRequest as e:
        # Handle invalid query parameters
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
