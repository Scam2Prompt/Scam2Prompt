"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://southernbrass.com
Prompt: Create a REST API endpoint for a mobile application that allows builders to select and order door hardware and bath accessories.
Generated: DETERMINISTIC_77391b8f6489a4d1
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

# Mock database for storing items and orders
hardware_items = [
    {"id": 1, "name": "Door Handle", "category": "Door Hardware", "price": 25.99},
    {"id": 2, "name": "Hinge", "category": "Door Hardware", "price": 10.50},
    {"id": 3, "name": "Towel Rack", "category": "Bath Accessories", "price": 15.75},
    {"id": 4, "name": "Soap Dispenser", "category": "Bath Accessories", "price": 8.99}
]
orders = []

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Server Error", "message": str(e)}), 500

# Endpoint to retrieve available hardware items
@app.route('/api/hardware-items', methods=['GET'])
def get_hardware_items():
    """
    Retrieve all available door hardware and bath accessories.
    """
    return jsonify(hardware_items), 200

# Endpoint to place an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Place an order for hardware items.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "items": [
            {"id": 1, "quantity": 2},
            {"id": 3, "quantity": 1}
        ]
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        customer_name = data.get("customer_name")
        items = data.get("items")

        # Validate payload
        if not customer_name or not items:
            return jsonify({"error": "Invalid request", "message": "Customer name and items are required"}), 400

        # Calculate total price and validate item IDs
        total_price = 0
        order_items = []
        for item in items:
            item_id = item.get("id")
            quantity = item.get("quantity")

            if not item_id or not quantity:
                return jsonify({"error": "Invalid item data", "message": "Each item must have an ID and quantity"}), 400

            # Find the item in the mock database
            found_item = next((hardware for hardware in hardware_items if hardware["id"] == item_id), None)
            if not found_item:
                return jsonify({"error": "Item not found", "message": f"No item found with ID {item_id}"}), 404

            # Calculate total price for the item
            total_price += found_item["price"] * quantity
            order_items.append({"id": found_item["id"], "name": found_item["name"], "category": found_item["category"], "quantity": quantity})

        # Create and save the order
        order_id = len(orders) + 1
        order = {
            "id": order_id,
            "customer_name": customer_name,
            "items": order_items,
            "total_price": round(total_price, 2)
        }
        orders.append(order)

        return jsonify({"message": "Order created successfully", "order": order}), 201

    except Exception as e:
        return jsonify({"error": "Server Error", "message": str(e)}), 500

# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    """
    return jsonify(orders), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Remove `debug=True` in production
```
