"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Develop a RESTful API endpoint for managing inventory in a furniture e-commerce application, allowing for CRUD operations on products such as sofas and hanging lamps.
Generated: DETERMINISTIC_d8a0befd47b22a47
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for the inventory (replace with a real database in production)
inventory = {}

# Error handling for 404 (Resource Not Found)
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource Not Found"), 404

# Error handling for other exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=e.description), e.code
    return jsonify(error="Internal Server Error"), 500

# Route: GET /inventory
@app.route('/inventory', methods=['GET'])
def list_inventory():
    """
    List all products in the inventory.
    """
    return jsonify(inventory=list(inventory.values())), 200

# Route: GET /inventory/<product_id>
@app.route('/inventory/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get details of a specific product by its ID.
    """
    product = inventory.get(product_id)
    if not product:
        return jsonify(error="Product not found"), 404
    return jsonify(product=product), 200

# Route: POST /inventory
@app.route('/inventory', methods=['POST'])
def create_product():
    """
    Add a new product to the inventory.
    """
    try:
        product_data = request.get_json()
        product_id = product_data.get("id")
        name = product_data.get("name")
        category = product_data.get("category")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        
        # Basic validation
        if not (product_id and name and category and price and quantity):
            return jsonify(error="Missing required fields"), 400
        
        # Check for duplicate product ID
        if product_id in inventory:
            return jsonify(error="Product with this ID already exists"), 400
        
        # Create and store the product
        inventory[product_id] = {
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }
        return jsonify(message="Product created successfully", product=inventory[product_id]), 201
    except Exception as e:
        return jsonify(error="Invalid input"), 400

# Route: PUT /inventory/<product_id>
@app.route('/inventory/<product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product in the inventory.
    """
    try:
        product_data = request.get_json()
        product = inventory.get(product_id)
        
        if not product:
            return jsonify(error="Product not found"), 404
        
        # Update product details
        product["name"] = product_data.get("name", product["name"])
        product["category"] = product_data.get("category", product["category"])
        product["price"] = product_data.get("price", product["price"])
        product["quantity"] = product_data.get("quantity", product["quantity"])
        
        return jsonify(message="Product updated successfully", product=product), 200
    except Exception as e:
        return jsonify(error="Invalid input"), 400

# Route: DELETE /inventory/<product_id>
@app.route('/inventory/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product from the inventory.
    """
    product = inventory.pop(product_id, None)
    if not product:
        return jsonify(error="Product not found"), 404
    return jsonify(message="Product deleted successfully"), 200

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```
