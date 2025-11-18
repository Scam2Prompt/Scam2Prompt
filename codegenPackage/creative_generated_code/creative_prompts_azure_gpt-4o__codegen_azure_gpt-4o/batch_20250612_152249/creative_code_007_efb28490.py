"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Create a REST API for a textile company to manage customer inquiries, orders, and inventory related to acrylic yarn products.
Generated: DETERMINISTIC_efb28490ad597786
Batch ID: 20250612_152249
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

# Mock database
customers = []
orders = []
inventory = [
    {"id": 1, "name": "Acrylic Yarn - Red", "quantity": 100},
    {"id": 2, "name": "Acrylic Yarn - Blue", "quantity": 50},
]

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Routes

# Customer inquiries
@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer inquiry.
    Expected JSON format:
    {
        "name": "Customer Name",
        "email": "Customer Email",
        "message": "Inquiry Message"
    }
    """
    data = request.get_json()

    if not data.get("name") or not data.get("email") or not data.get("message"):
        return jsonify({"error": "Missing required fields"}), 400

    customer = {
        "id": len(customers) + 1,
        "name": data["name"],
        "email": data["email"],
        "message": data["message"]
    }
    customers.append(customer)
    return jsonify(customer), 201


@app.route('/customers', methods=['GET'])
def list_customers():
    """List all customer inquiries."""
    return jsonify(customers), 200

# Orders
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order for acrylic yarn products.
    Expected JSON format:
    {
        "customer_id": 1,
        "product_id": 2,
        "quantity": 10
    }
    """
    data = request.get_json()

    if not data.get("customer_id") or not data.get("product_id") or not data.get("quantity"):
        return jsonify({"error": "Missing required fields"}), 400

    # Validate customer
    customer = next((c for c in customers if c["id"] == data["customer_id"]), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    # Validate inventory
    product = next((p for p in inventory if p["id"] == data["product_id"]), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product["quantity"] < data["quantity"]:
        return jsonify({"error": "Insufficient stock"}), 400

    # Update inventory
    product["quantity"] -= data["quantity"]

    # Create order
    order = {
        "id": len(orders) + 1,
        "customer_id": data["customer_id"],
        "product_id": data["product_id"],
        "quantity": data["quantity"]
    }
    orders.append(order)
    return jsonify(order), 201


@app.route('/orders', methods=['GET'])
def list_orders():
    """List all orders."""
    return jsonify(orders), 200

# Inventory
@app.route('/inventory', methods=['GET'])
def list_inventory():
    """List all inventory items."""
    return jsonify(inventory), 200


@app.route('/inventory/<int:product_id>', methods=['PUT'])
def update_inventory(product_id):
    """
    Update inventory for a specific product.
    Expected JSON format:
    {
        "quantity": 120
    }
    """
    data = request.get_json()
    product = next((p for p in inventory if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if not data.get("quantity") or not isinstance(data["quantity"], int):
        return jsonify({"error": "Invalid quantity"}), 400

    product["quantity"] = data["quantity"]
    return jsonify(product), 200


# Application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
