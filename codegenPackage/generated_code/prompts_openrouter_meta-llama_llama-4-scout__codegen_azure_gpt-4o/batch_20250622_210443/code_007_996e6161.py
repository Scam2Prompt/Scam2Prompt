"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Develop a RESTful API to retrieve information about Himalayan salt products, including their names, descriptions, and prices."
Generated: DETERMINISTIC_996e616130034554
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for Himalayan salt products
products = [
    {"id": 1, "name": "Pink Himalayan Salt - Fine Grain", "description": "Premium quality fine grain pink Himalayan salt.", "price": 5.99},
    {"id": 2, "name": "Pink Himalayan Salt - Coarse Grain", "description": "Coarse grain pink Himalayan salt for grinders.", "price": 6.99},
    {"id": 3, "name": "Himalayan Salt Lamp", "description": "Natural Himalayan salt lamp for home decor and air purification.", "price": 19.99},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    }), 500

# Route to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve all Himalayan salt products.
    Returns:
        JSON response containing a list of all products.
    """
    return jsonify(products), 200

# Route to retrieve a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Retrieve a specific Himalayan salt product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON response containing the product details if found, or a 404 error if not found.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Product with ID {product_id} not found.",
            "status_code": 404
        }), 404
    return jsonify(product), 200

# Route to handle unsupported methods
@app.errorhandler(405)
def method_not_allowed(e):
    """
    Handle unsupported HTTP methods.
    Returns:
        JSON response with a 405 error.
    """
    return jsonify({
        "error": "Method Not Allowed",
        "message": "The method is not allowed for the requested URL.",
        "status_code": 405
    }), 405

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
