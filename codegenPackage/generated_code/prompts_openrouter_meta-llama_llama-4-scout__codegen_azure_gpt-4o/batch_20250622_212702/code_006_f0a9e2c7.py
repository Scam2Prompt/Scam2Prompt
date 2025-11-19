"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Develop a RESTful API endpoint to handle coffee product orders, including request and response body schema.
Generated: DETERMINISTIC_f0a9e2c730d37b27
Batch ID: 20250622_212702
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

# In-memory database for coffee products and orders
coffee_products = [
    {"id": 1, "name": "Espresso", "price": 2.5},
    {"id": 2, "name": "Latte", "price": 3.5},
    {"id": 3, "name": "Cappuccino", "price": 3.0},
]
orders = []

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
    return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to place an order
@app.route('/api/orders', methods=['POST'])
def place_order():
    """
    Handles placing a coffee order.
    Request Body Schema:
    {
        "product_id": int,
        "quantity": int
    }
    Response Body Schema:
    {
        "order_id": int,
        "product_id": int,
        "quantity": int,
        "total_price": float
    }
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data or "product_id" not in data or "quantity" not in data:
            return jsonify({"error": "Invalid request body"}), 400

        product_id = data["product_id"]
        quantity = data["quantity"]

        if not isinstance(product_id, int) or not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Invalid product_id or quantity"}), 400

        # Find the product
        product = next((p for p in coffee_products if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Calculate total price
        total_price = product["price"] * quantity

        # Create the order
        order_id = len(orders) + 1
        order = {
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        }
        orders.append(order)

        # Return the order details
        return jsonify(order), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the order"}), 500

# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Retrieves all coffee orders.
    Response Body Schema:
    [
        {
            "order_id": int,
            "product_id": int,
            "quantity": int,
            "total_price": float
        }
    ]
    """
    return jsonify(orders), 200

# Endpoint to retrieve coffee products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieves all coffee products.
    Response Body Schema:
    [
        {
            "id": int,
            "name": str,
            "price": float
        }
    ]
    """
    return jsonify(coffee_products), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
