"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Create a REST API specification for a comic book store, including endpoints for retrieving comic details, checking stock for limited editions, and placing orders.
Generated: DETERMINISTIC_5a2d1a4cc7e5cb6c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing comics in the store
comics = [
    {"id": 1, "title": "Spider-Man: Homecoming", "author": "Stan Lee", "stock": 100, "limited_edition": False},
    {"id": 2, "title": "Batman: Year One", "author": "Frank Miller", "stock": 50, "limited_edition": True},
    {"id": 3, "title": "Wonder Woman: The Hiketeia", "author": "Greg Rucka", "stock": 5, "limited_edition": True},
]

orders = []  # List to store orders


@app.route('/comics', methods=['GET'])
def get_comics():
    """
    Endpoint to retrieve all comic details.
    """
    return jsonify({"comics": comics}), 200


@app.route('/comics/<int:comic_id>', methods=['GET'])
def get_comic_details(comic_id):
    """
    Endpoint to retrieve details for a single comic by ID.
    """
    comic = next((comic for comic in comics if comic["id"] == comic_id), None)
    if comic is None:
        return jsonify({"error": "Comic not found"}), 404
    return jsonify({"comic": comic}), 200


@app.route('/comics/<int:comic_id>/stock', methods=['GET'])
def check_stock(comic_id):
    """
    Endpoint to check stock for a comic by ID.
    """
    comic = next((comic for comic in comics if comic["id"] == comic_id), None)
    if comic is None:
        return jsonify({"error": "Comic not found"}), 404
    return jsonify({"stock": comic["stock"], "limited_edition": comic["limited_edition"]}), 200


@app.route('/orders', methods=['POST'])
def place_order():
    """
    Endpoint to place an order for a comic.
    """
    try:
        # Parse the request data
        data = request.get_json()
        comic_id = data.get("comic_id")
        quantity = data.get("quantity")

        # Error handling for missing or invalid data
        if comic_id is None or quantity is None:
            return jsonify({"error": "comic_id and quantity are required"}), 400
        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Quantity must be a positive integer"}), 400

        # Validate the comic ID and stock availability
        comic = next((comic for comic in comics if comic["id"] == comic_id), None)
        if comic is None:
            return jsonify({"error": "Comic not found"}), 404
        if comic["stock"] < quantity:
            return jsonify({"error": "Insufficient stock"}), 400

        # Deduct stock and record the order
        comic["stock"] -= quantity
        order_id = len(orders) + 1
        order = {"order_id": order_id, "comic_id": comic_id, "quantity": quantity}
        orders.append(order)

        return jsonify({"message": "Order placed successfully", "order": order}), 201
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders.
    """
    return jsonify({"orders": orders}), 200


# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```
