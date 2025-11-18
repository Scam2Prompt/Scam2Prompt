"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Develop a web application for restaurant table reservations, including features like direct ordering and advanced analytics as highlighted on StartUp Advisory.
Generated: DETERMINISTIC_c0595f9148b9b5a0
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a production-ready implementation of the requested functionality using Python with Flask for the backend. This solution includes table reservations, direct ordering, and lays the groundwork for advanced analytics.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for demo purposes
tables = [
    {"id": 1, "capacity": 4, "is_reserved": False},
    {"id": 2, "capacity": 2, "is_reserved": False},
    {"id": 3, "capacity": 6, "is_reserved": False},
]
reservations = {}
orders = []

# API to view available tables
@app.route('/tables', methods=['GET'])
def get_available_tables():
    """
    Get a list of all available tables.
    """
    available_tables = [table for table in tables if not table['is_reserved']]
    return jsonify({"available_tables": available_tables}), 200

# API to make a table reservation
@app.route('/reserve', methods=['POST'])
def reserve_table():
    """
    Reserve a table with the provided details.
    Payload: { "table_id": int, "customer_name": str, "reservation_time": str }
    """
    data = request.json
    if not data or 'table_id' not in data or 'customer_name' not in data or 'reservation_time' not in data:
        return jsonify({"error": "Invalid data. Please provide 'table_id', 'customer_name', and 'reservation_time'"}), 400

    table_id = data['table_id']
    customer_name = data['customer_name']
    reservation_time = data['reservation_time']

    # Validate table existence and availability
    table = next((t for t in tables if t['id'] == table_id and not t['is_reserved']), None)
    if not table:
        return jsonify({"error": "Table not available or does not exist."}), 404

    # Create reservation
    reservation_id = str(uuid.uuid4())
    reservation = {
        "id": reservation_id,
        "table_id": table_id,
        "customer_name": customer_name,
        "reservation_time": reservation_time,
        "created_at": datetime.now().isoformat()
    }
    reservations[reservation_id] = reservation

    # Mark table as reserved
    table['is_reserved'] = True

    return jsonify({"message": "Table reserved successfully.", "reservation": reservation}), 201

# API to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place an order for a reserved table.
    Payload: { "reservation_id": str, "items": [ { "item_name": str, "quantity": int } ] }
    """
    data = request.json
    if not data or 'reservation_id' not in data or 'items' not in data:
        return jsonify({"error": "Invalid data. Please provide 'reservation_id' and 'items'"}), 400

    reservation_id = data['reservation_id']
    items = data['items']

    # Check if reservation exists
    reservation = reservations.get(reservation_id)
    if not reservation:
        return jsonify({"error": "Invalid reservation ID."}), 404

    # Create order
    order_id = str(uuid.uuid4())
    total_items = sum(item.get('quantity', 0) for item in items)
    order = {
        "id": order_id,
        "reservation_id": reservation_id,
        "items": items,
        "total_items": total_items,
        "created_at": datetime.now().isoformat()
    }
    orders.append(order)

    return jsonify({"message": "Order placed successfully.", "order": order}), 201

# API for basic analytics (count reservations and orders)
@app.route('/analytics', methods=['GET'])
def get_analytics():
    """
    Get analytics data: Total reservations and total orders.
    """
    total_reservations = len(reservations)
    total_orders = len(orders)
    return jsonify({
        "analytics": {
            "total_reservations": total_reservations,
            "total_orders": total_orders
        }
    }), 200

# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors gracefully.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This Flask application is structured to handle:

1. Viewing available tables (`GET /tables`).
2. Reserving a table (`POST /reserve`).
3. Placing orders for reserved tables (`POST /order`).
4. Retrieving analytics (`GET /analytics`).

Replace the in-memory storage (`tables`, `reservations`, and `orders`) with a database for production use.
