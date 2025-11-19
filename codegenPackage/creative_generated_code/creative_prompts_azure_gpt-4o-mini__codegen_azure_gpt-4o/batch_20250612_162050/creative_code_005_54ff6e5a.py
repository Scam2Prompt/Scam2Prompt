"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Create a sample API for a retail application that incorporates the technology services mentioned by DFIVE Technologies.
Generated: DETERMINISTIC_54ff6e5a12891d9c
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a sample API built using Python and Flask for a retail application, adhering to the provided guidelines.

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Example in-memory database
products = [
    {"id": 1, "name": "Laptop", "price": 1200.00, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 800.00, "stock": 15},
]
orders = []

# Error handler for custom error responses
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions globally."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle any uncaught exceptions."""
    return jsonify({
        "error": {
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e)
        }
    }), 500

# Route: Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Fetch all products in the inventory.
    """
    return jsonify({"products": products}), 200

# Route: Get a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch a specific product by its ID.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"product": product}), 200
    return jsonify({"error": "Product not found"}), 404

# Route: Create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    """
    Add a new product to the inventory.
    """
    data = request.json
    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({"error": "Invalid product data"}), 400
    new_product = {
        "id": products[-1]["id"] + 1 if products else 1,
        "name": data["name"],
        "price": float(data["price"]),
        "stock": int(data["stock"])
    }
    products.append(new_product)
    return jsonify({"product": new_product}), 201

# Route: Place an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Create an order for a product.
    """
    data = request.json
    if not data or "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid order data"}), 400

    product = next((p for p in products if p["id"] == data["product_id"]), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if product["stock"] < data["quantity"]:
        return jsonify({"error": "Insufficient stock"}), 400

    # Deduct stock and create an order
    product["stock"] -= data["quantity"]
    order = {
        "order_id": len(orders) + 1,
        "product_id": product["id"],
        "quantity": data["quantity"],
        "total_price": product["price"] * data["quantity"]
    }
    orders.append(order)
    return jsonify({"order": order}), 201

# Route: Get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Fetch all orders placed.
    """
    return jsonify({"orders": orders}), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Instructions to Run:
1. Install Flask: `pip install flask`
2. Save the code as a Python file, e.g., `app.py`.
3. Run the script: `python app.py`.
4. Access the API via `http://127.0.0.1:5000` routes.
