"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Provide an API recommendation for managing inventory and tracking international exports for facade products like "KUA-03 اتصالات آندرکات," as described by Karen Fixing.
Generated: DETERMINISTIC_3b97f88fb257f4c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database for products and exports
inventory = {}
exports = []

# Utility function for generating unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route: Add a new product to the inventory
@app.route('/inventory', methods=['POST'])
def add_product():
    """
    Adds a new product to the inventory.
    Request Body:
    {
        "name": "Product Name",
        "category": "Category",
        "quantity": Integer
    }
    """
    data = request.json
    name = data.get("name")
    category = data.get("category")
    quantity = data.get("quantity")

    if not name or not category or quantity is None:
        return error_response("Missing required fields: name, category, quantity")

    if not isinstance(quantity, int) or quantity < 0:
        return error_response("Quantity must be a non-negative integer")

    product_id = generate_id()
    inventory[product_id] = {
        "id": product_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    return jsonify({"message": "Product added successfully", "product": inventory[product_id]}), 201

# Route: Get all products in the inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Retrieves all products in the inventory.
    """
    return jsonify(list(inventory.values())), 200

# Route: Update inventory quantity for a product
@app.route('/inventory/<product_id>', methods=['PUT'])
def update_product_quantity(product_id):
    """
    Updates the quantity of a product in the inventory.
    Request Body:
    {
        "quantity": Integer
    }
    """
    data = request.json
    quantity = data.get("quantity")

    if product_id not in inventory:
        return error_response("Product not found", 404)

    if not isinstance(quantity, int) or quantity < 0:
        return error_response("Quantity must be a non-negative integer")

    inventory[product_id]['quantity'] = quantity

    return jsonify({"message": "Product quantity updated", "product": inventory[product_id]}), 200

# Route: Record an export of a product
@app.route('/exports', methods=['POST'])
def record_export():
    """
    Records an export of a product.
    Request Body:
    {
        "product_id": "Product ID",
        "destination": "Export Destination",
        "quantity": Integer
    }
    """
    data = request.json
    product_id = data.get("product_id")
    destination = data.get("destination")
    export_quantity = data.get("quantity")

    if not product_id or not destination or export_quantity is None:
        return error_response("Missing required fields: product_id, destination, quantity")

    if product_id not in inventory:
        return error_response("Product not found", 404)

    if not isinstance(export_quantity, int) or export_quantity <= 0:
        return error_response("Export quantity must be a positive integer")

    if inventory[product_id]['quantity'] < export_quantity:
        return error_response("Insufficient inventory for export")

    inventory[product_id]['quantity'] -= export_quantity
    export_id = generate_id()
    export_record = {
        "id": export_id,
        "product_id": product_id,
        "destination": destination,
        "quantity": export_quantity
    }
    exports.append(export_record)

    return jsonify({"message": "Export recorded successfully", "export": export_record}), 201

# Route: Get all export records
@app.route('/exports', methods=['GET'])
def get_exports():
    """
    Retrieves all export records.
    """
    return jsonify(exports), 200

# Route: Get a specific product by ID
@app.route('/inventory/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieves a specific product from the inventory by ID.
    """
    if product_id not in inventory:
        return error_response("Product not found", 404)

    return jsonify(inventory[product_id]), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
