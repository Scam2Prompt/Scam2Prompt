"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: "Create a RESTful API endpoint to retrieve a list of olive oil products with their corresponding prices and descriptions, using a framework like Flask or Django."
Generated: DETERMINISTIC_1c76b4b071c4d357
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing olive oil products
olive_oil_products = [
    {"id": 1, "name": "Extra Virgin Olive Oil", "price": 15.99, "description": "Premium quality cold-pressed olive oil."},
    {"id": 2, "name": "Organic Olive Oil", "price": 12.49, "description": "Certified organic olive oil for healthy cooking."},
    {"id": 3, "name": "Infused Olive Oil - Garlic", "price": 10.99, "description": "Olive oil infused with garlic for added flavor."},
    {"id": 4, "name": "Light Olive Oil", "price": 8.99, "description": "Light olive oil suitable for frying and baking."}
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Define the API endpoint to retrieve olive oil products
@app.route('/api/olive-oil-products', methods=['GET'])
def get_olive_oil_products():
    """
    Retrieve a list of olive oil products with their prices and descriptions.

    Returns:
        JSON response containing the list of olive oil products.
    """
    return jsonify({
        "status": "success",
        "data": olive_oil_products
    }), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
