"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Design a RESTful API for a uniform manufacturing service, including endpoints for creating and managing orders, retrieving product information (e.g., available uniform designs, materials), and interacting with customers, similar to Real Garment's services.
Generated: DETERMINISTIC_4d2894cb517dba3b
Batch ID: 20250622_210650
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

# Mock database
products = [
    {"id": 1, "name": "Classic Uniform", "material": "Cotton", "price": 50},
    {"id": 2, "name": "Premium Uniform", "material": "Polyester", "price": 75},
]
orders = []
customers = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Endpoint to retrieve a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    if not data or 'customer_id' not in data or 'product_id' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    product = next((p for p in products if p['id'] == data['product_id']), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    order = {
        "id": len(orders) + 1,
        "customer_id": data['customer_id'],
        "product_id": data['product_id'],
        "quantity": data.get('quantity', 1),
        "total_price": product['price'] * data.get('quantity', 1),
    }
    orders.append(order)
    return jsonify(order), 201

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

# Endpoint to retrieve a single order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    customer = {
        "id": len(customers) + 1,
        "name": data['name'],
        "email": data['email'],
    }
    customers.append(customer)
    return jsonify(customer), 201

# Endpoint to retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

# Endpoint to retrieve a single customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
