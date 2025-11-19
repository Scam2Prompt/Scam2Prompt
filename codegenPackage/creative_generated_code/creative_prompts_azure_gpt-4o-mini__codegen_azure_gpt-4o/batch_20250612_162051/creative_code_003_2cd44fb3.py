"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wouo.com.br
Prompt: Develop a RESTful API endpoint for managing product listings, including inhalers and syringes, inspired by the product catalog on Wouo.com.br.
Generated: DETERMINISTIC_2cd44fb3b679bc52
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# In-memory database for product listings
# In production, this would be replaced by a persistent database (e.g., PostgreSQL, MongoDB, etc.)
products = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    })
    response.status_code = e.code
    return response

# Error handler for uncaught exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    response = jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    })
    response.status_code = 500
    return response

# Helper function to validate product input
def validate_product_data(data):
    required_fields = ['name', 'category', 'price', 'stock']
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return "Invalid price. Must be a positive number."
    if not isinstance(data['stock'], int) or data['stock'] < 0:
        return "Invalid stock. Must be a non-negative integer."
    return None

# Route: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve all products.
    Returns:
        List of all products in the catalog.
    """
    return jsonify(products), 200

# Route: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the catalog.
    Request JSON:
        {
            "name": "Product name",
            "category": "Product category",
            "price": 100.0,
            "stock": 10
        }
    Returns:
        Newly created product or validation error.
    """
    data = request.get_json()
    validation_error = validate_product_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "category": data['category'],
        "price": data['price'],
        "stock": data['stock']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Route: Update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product by ID.
    Request JSON:
        {
            "name": "Updated name",
            "category": "Updated category",
            "price": 150.0,
            "stock": 20
        }
    Returns:
        Updated product or error message if not found.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    validation_error = validate_product_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    product.update({
        "name": data['name'],
        "category": data['category'],
        "price": data['price'],
        "stock": data['stock']
    })
    return jsonify(product), 200

# Route: Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by ID.
    Returns:
        Success message or error if product not found.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```
