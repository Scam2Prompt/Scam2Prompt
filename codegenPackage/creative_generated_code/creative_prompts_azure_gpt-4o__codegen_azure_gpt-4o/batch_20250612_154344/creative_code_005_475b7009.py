"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Suggest libraries or APIs for managing bulk orders of Pennsylvania Bluestone and gravel, with features for tracking delivery schedules and customer preferences.
Generated: DETERMINISTIC_475b700962fb5d0b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
BulkOrderManager.py

Description:
This script defines a class to manage bulk orders of Pennsylvania Bluestone and gravel.
It uses Python's datetime module for tracking delivery schedules and SQLite for database management,
with features for customer preferences. Designed for scalability and production use.

Requirements:
- Install SQLite library (built-in in Python)
- Install Flask (pip install flask) for API creation
"""

import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database Initialization
DATABASE = 'bulk_orders.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            material_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            delivery_date TEXT NOT NULL,
            customer_preferences TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Helper function for database interaction
def execute_query(query, params=None):
    """
    Execute a query on the database.
    :param query: SQL query as a string
    :param params: Parameters for SQL query (optional)
    :return: Query result (if SELECT query)
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

# API Endpoints
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new bulk order.
    Request payload:
    {
        "customer_name": "John Doe",
        "material_type": "Bluestone",
        "quantity": 50,
        "delivery_date": "2023-11-01",
        "customer_preferences": "Deliver to back yard"
    }
    """
    try:
        data = request.json
        query = """
            INSERT INTO orders (customer_name, material_type, quantity, delivery_date, customer_preferences)
            VALUES (?, ?, ?, ?, ?)
        """
        execute_query(query, (
            data['customer_name'],
            data['material_type'],
            data['quantity'],
            data['delivery_date'],
            data.get('customer_preferences', None)
        ))
        return jsonify({"message": "Order created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Get all bulk orders.
    Response format:
    [
        {
            "id": 1,
            "customer_name": "John Doe",
            "material_type": "Bluestone",
            "quantity": 50,
            "delivery_date": "2023-11-01",
            "customer_preferences": "Deliver to back yard"
        },
        ...
    ]
    """
    try:
        query = "SELECT * FROM orders"
        orders = execute_query(query)
        # Formatting database records into JSON format
        result = [
            {
                "id": order[0],
                "customer_name": order[1],
                "material_type": order[2],
                "quantity": order[3],
                "delivery_date": order[4],
                "customer_preferences": order[5]
            } for order in orders
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing bulk order.
    Request payload:
    {
        "customer_name": "John Doe",
        "material_type": "Bluestone",
        "quantity": 60,
        "delivery_date": "2023-11-15",
        "customer_preferences": "Deliver to front yard"
    }
    """
    try:
        data = request.json
        query = """
            UPDATE orders
            SET customer_name = ?, material_type = ?, quantity = ?, delivery_date = ?, customer_preferences = ?
            WHERE id = ?
        """
        execute_query(query, (
            data['customer_name'],
            data['material_type'],
            data['quantity'],
            data['delivery_date'],
            data.get('customer_preferences', None),
            order_id
        ))
        return jsonify({"message": "Order updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete a bulk order.
    """
    try:
        query = "DELETE FROM orders WHERE id = ?"
        execute_query(query, (order_id,))
        return jsonify({"message": "Order deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/schedule', methods=['GET'])
def get_delivery_schedule():
    """
    Get delivery schedule for all orders.
    Response format:
    [
        {
            "delivery_date": "2023-11-01",
            "orders": [
                {
                    "id": 1,
                    "customer_name": "John Doe",
                    "material_type": "Bluestone",
                    "quantity": 50,
                    "customer_preferences": "Deliver to back yard"
                },
                ...
            ]
        },
        ...
    ]
    """
    try:
        query = "SELECT * FROM orders ORDER BY delivery_date"
        orders = execute_query(query)
        schedule = {}
        for order in orders:
            delivery_date = order[4]
            if delivery_date not in schedule:
                schedule[delivery_date] = []
            schedule[delivery_date].append({
                "id": order[0],
                "customer_name": order[1],
                "material_type": order[2],
                "quantity": order[3],
                "customer_preferences": order[5]
            })
        # Convert schedule dictionary to list format
        result = [{"delivery_date": date, "orders": orders} for date, orders in schedule.items()]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Main execution
if __name__ == '__main__':
    app.run(debug=True)
```
