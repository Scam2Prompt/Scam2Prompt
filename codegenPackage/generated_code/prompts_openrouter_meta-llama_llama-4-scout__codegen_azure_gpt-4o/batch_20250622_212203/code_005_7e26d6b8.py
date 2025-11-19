"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: "Design a RESTful API for a service like Rarecrew that might involve managing inventory and sales through an online shop."
Generated: DETERMINISTIC_7e26d6b8a8994c99
Batch ID: 20250622_212203
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

# Mock database
inventory = [
    {"id": 1, "name": "Laptop", "quantity": 10, "price": 1000.00},
    {"id": 2, "name": "Smartphone", "quantity": 20, "price": 500.00},
]

sales = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to get all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

# Route to get a specific inventory item by ID
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Not Found", "message": "Item not found"}), 404
    return jsonify(item), 200

# Route to add a new inventory item
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    if not data or "name" not in data or "quantity" not in data or "price" not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400
    new_item = {
        "id": max(item["id"] for item in inventory) + 1 if inventory else 1,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

# Route to update an inventory item
@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    data = request.get_json()
    item = next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Not Found", "message": "Item not found"}), 404
    if not data or "name" not in data or "quantity" not in data or "price" not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400
    item.update({
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    })
    return jsonify(item), 200

# Route to delete an inventory item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Not Found", "message": "Item not found"}), 404
    inventory.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200

# Route to record a sale
@app.route('/sales', methods=['POST'])
def record_sale():
    data = request.get_json()
    if not data or "item_id" not in data or "quantity" not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400
    item = next((item for item in inventory if item["id"] == data["item_id"]), None)
    if not item:
        return jsonify({"error": "Not Found", "message": "Item not found"}), 404
    if item["quantity"] < data["quantity"]:
        return jsonify({"error": "Bad Request", "message": "Insufficient stock"}), 400
    item["quantity"] -= data["quantity"]
    sale = {
        "id": len(sales) + 1,
        "item_id": data["item_id"],
        "quantity": data["quantity"],
        "total_price": item["price"] * data["quantity"]
    }
    sales.append(sale)
    return jsonify(sale), 201

# Route to get all sales
@app.route('/sales', methods=['GET'])
def get_sales():
    return jsonify(sales), 200

# Route to get a specific sale by ID
@app.route('/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = next((sale for sale in sales if sale["id"] == sale_id), None)
    if not sale:
        return jsonify({"error": "Not Found", "message": "Sale not found"}), 404
    return jsonify(sale), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
