"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Create a RESTful API endpoint for managing product inventory at a sweet shop like Govind Sweets, covering items such as Mini Samosa and Chocolate Cake.
Generated: DETERMINISTIC_189b49699b128108
Batch ID: 20250612_162050
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

# In-memory product inventory
inventory = {
    "Mini Samosa": {"price": 10, "quantity": 50},
    "Chocolate Cake": {"price": 200, "quantity": 10}
}

# Error handler for JSON response on unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500


# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Get the list of all products in the inventory.
    """
    return jsonify(inventory), 200


# Route to get a specific product
@app.route('/api/products/<product_name>', methods=['GET'])
def get_product(product_name):
    """
    Get details of a specific product by its name.
    """
    product = inventory.get(product_name)
    if not product:
        return jsonify({"error": f"Product '{product_name}' not found"}), 404
    return jsonify({product_name: product}), 200


# Route to add or update a product
@app.route('/api/products', methods=['POST'])
def add_or_update_product():
    """
    Add a new product or update an existing product's details.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ["name", "price", "quantity"]):
        return jsonify({"error": "Invalid input. Required fields: name, price, quantity"}), 400
    
    product_name = data["name"]
    inventory[product_name] = {
        "price": data["price"],
        "quantity": data["quantity"]
    }
    return jsonify({"message": f"Product '{product_name}' added/updated successfully"}), 201


# Route to delete a product
@app.route('/api/products/<product_name>', methods=['DELETE'])
def delete_product(product_name):
    """
    Delete a product from the inventory.
    """
    if product_name not in inventory:
        return jsonify({"error": f"Product '{product_name}' not found"}), 404
    
    del inventory[product_name]
    return jsonify({"message": f"Product '{product_name}' deleted successfully"}), 200


# Main entry point for running the Flask application
if __name__ == '__main__':
    # Run the app on localhost
    app.run(debug=True)
```
