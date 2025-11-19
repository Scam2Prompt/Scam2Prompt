"""
Generated Code Metadata:
========================
Original URL: https://issowork.com
Prompt: "Create a RESTful API for managing clothing inventory, including endpoints for adding, updating, and deleting products, inspired by ISSO's product offerings."
Generated: DETERMINISTIC_37c0f795ecd163c6
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for clothing inventory
inventory = {}

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

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Adds a new product to the inventory.
    Expects JSON payload with 'id', 'name', 'category', 'price', and 'quantity'.
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'category' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    product_id = data['id']
    if product_id in inventory:
        return jsonify({"error": "Conflict", "message": "Product with this ID already exists"}), 409

    inventory[product_id] = {
        "name": data['name'],
        "category": data['category'],
        "price": data['price'],
        "quantity": data['quantity']
    }
    return jsonify({"message": "Product added successfully", "product": inventory[product_id]}), 201

# Endpoint to update an existing product
@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Updates an existing product in the inventory.
    Expects JSON payload with 'name', 'category', 'price', and/or 'quantity'.
    """
    if product_id not in inventory:
        return jsonify({"error": "Not Found", "message": "Product not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Missing request body"}), 400

    product = inventory[product_id]
    product.update({key: value for key, value in data.items() if key in product})
    return jsonify({"message": "Product updated successfully", "product": product}), 200

# Endpoint to delete a product
@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Deletes a product from the inventory.
    """
    if product_id not in inventory:
        return jsonify({"error": "Not Found", "message": "Product not found"}), 404

    del inventory[product_id]
    return jsonify({"message": "Product deleted successfully"}), 200

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    """
    Lists all products in the inventory.
    """
    return jsonify({"products": inventory}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
