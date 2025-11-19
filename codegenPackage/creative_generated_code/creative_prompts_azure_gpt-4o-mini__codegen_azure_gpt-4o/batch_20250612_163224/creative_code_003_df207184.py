"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://putrastarboy.github.io
Prompt: Develop a RESTful API design for managing coffee orders, based on the user experience highlighted on 8 Coffee's site.
Generated: DETERMINISTIC_df207184c88669de
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database for coffee orders
orders = []
order_id_counter = 1


# Helper function to find an order by ID
def find_order(order_id):
    return next((order for order in orders if order["id"] == order_id), None)


@app.route("/orders", methods=["GET"])
def get_orders():
    """
    GET /orders
    Retrieve all coffee orders.
    """
    return jsonify(orders), 200


@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """
    GET /orders/<order_id>
    Retrieve a specific coffee order by ID.
    """
    order = find_order(order_id)
    if order is None:
        abort(404, description="Order not found")
    return jsonify(order), 200


@app.route("/orders", methods=["POST"])
def create_order():
    """
    POST /orders
    Create a new coffee order.
    Request body should include 'customer_name', 'coffee_type', and 'size'.
    """
    global order_id_counter

    if not request.json or not all(
        key in request.json for key in ("customer_name", "coffee_type", "size")
    ):
        abort(400, description="Invalid request: Missing required fields")

    new_order = {
        "id": order_id_counter,
        "customer_name": request.json["customer_name"],
        "coffee_type": request.json["coffee_type"],
        "size": request.json["size"],
        "status": "Pending",  # Default status
    }
    orders.append(new_order)
    order_id_counter += 1
    return jsonify(new_order), 201


@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    """
    PUT /orders/<order_id>
    Update an existing coffee order's details.
    Request body can include 'customer_name', 'coffee_type', 'size', or 'status'.
    """
    order = find_order(order_id)
    if order is None:
        abort(404, description="Order not found")

    if not request.json:
        abort(400, description="Invalid request: Missing body")

    # Update fields if provided
    order["customer_name"] = request.json.get("customer_name", order["customer_name"])
    order["coffee_type"] = request.json.get("coffee_type", order["coffee_type"])
    order["size"] = request.json.get("size", order["size"])
    order["status"] = request.json.get("status", order["status"])
    return jsonify(order), 200


@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    """
    DELETE /orders/<order_id>
    Delete an existing coffee order by ID.
    """
    order = find_order(order_id)
    if order is None:
        abort(404, description="Order not found")
    orders.remove(order)
    return jsonify({"message": "Order deleted successfully"}), 200


# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
