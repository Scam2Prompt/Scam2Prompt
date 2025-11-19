"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Design a RESTful API for managing hot tub and spa inventory, including endpoints for retrieving product information and pricing, inspired by the Country Leisure Mfg product offerings.
Generated: DETERMINISTIC_33759ec7c457d0a3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing hot tub and spa inventory
inventory = [
    {
        "id": 1,
        "name": "Deluxe Hot Tub",
        "description": "A luxurious hot tub with 6 seats and LED lighting.",
        "price": 7999.99,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Compact Spa",
        "description": "A compact spa perfect for small spaces.",
        "price": 4999.99,
        "stock": 10
    },
    {
        "id": 3,
        "name": "Family Spa",
        "description": "A spacious spa designed for family use.",
        "price": 8999.99,
        "stock": 3
    }
]

# Error response helper function
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Endpoint to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve all products in the inventory.
    """
    return jsonify(inventory), 200

# Endpoint to retrieve a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a specific product by its ID.
    """
    product = next((item for item in inventory if item["id"] == product_id), None)
    if product is None:
        return error_response("Product not found", 404)
    return jsonify(product), 200

# Endpoint to retrieve pricing information for all products
@app.route('/api/products/pricing', methods=['GET'])
def get_pricing():
    """
    Retrieve pricing information for all products.
    """
    pricing = [{"id": item["id"], "name": item["name"], "price": item["price"]} for item in inventory]
    return jsonify(pricing), 200

# Endpoint to add a new product to the inventory
@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Add a new product to the inventory.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "price", "stock")):
            return error_response("Invalid product data", 400)
        
        new_product = {
            "id": max(item["id"] for item in inventory) + 1,
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "stock": data["stock"]
        }
        inventory.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product in the inventory.
    """
    product = next((item for item in inventory if item["id"] == product_id), None)
    if product is None:
        return error_response("Product not found", 404)
    
    try:
        data = request.get_json()
        if not data:
            return error_response("Invalid product data", 400)
        
        product.update({
            "name": data.get("name", product["name"]),
            "description": data.get("description", product["description"]),
            "price": data.get("price", product["price"]),
            "stock": data.get("stock", product["stock"])
        })
        return jsonify(product), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to delete a product from the inventory
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product from the inventory.
    """
    product = next((item for item in inventory if item["id"] == product_id), None)
    if product is None:
        return error_response("Product not found", 404)
    
    inventory.remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
