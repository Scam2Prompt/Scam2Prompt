"""
Generated Code Metadata:
========================
Original URL: https://www.houseofolsha.com
Prompt: Develop a RESTful API for managing Baju Kurung products, including endpoints for retrieving product information, updating inventory, and processing orders.
Generated: DETERMINISTIC_bb41f65e559562d9
Batch ID: 20250622_210703
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

# In-memory database for Baju Kurung products
products = {
    1: {"name": "Baju Kurung Modern", "price": 120.00, "inventory": 50},
    2: {"name": "Baju Kurung Traditional", "price": 100.00, "inventory": 30},
    3: {"name": "Baju Kurung Lace", "price": 150.00, "inventory": 20},
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Endpoint to retrieve a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Endpoint to update inventory for a specific product
@app.route('/products/<int:product_id>/inventory', methods=['PUT'])
def update_inventory(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data or 'inventory' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    try:
        new_inventory = int(data['inventory'])
        if new_inventory < 0:
            return jsonify({"error": "Inventory cannot be negative"}), 400
        product['inventory'] = new_inventory
        return jsonify({"message": "Inventory updated successfully", "product": product}), 200
    except ValueError:
        return jsonify({"error": "Inventory must be a valid integer"}), 400

# Endpoint to process an order for a specific product
@app.route('/products/<int:product_id>/order', methods=['POST'])
def process_order(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data or 'quantity' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    try:
        quantity = int(data['quantity'])
        if quantity <= 0:
            return jsonify({"error": "Order quantity must be greater than zero"}), 400
        if quantity > product['inventory']:
            return jsonify({"error": "Insufficient inventory"}), 400

        product['inventory'] -= quantity
        return jsonify({"message": "Order processed successfully", "product": product}), 200
    except ValueError:
        return jsonify({"error": "Quantity must be a valid integer"}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
