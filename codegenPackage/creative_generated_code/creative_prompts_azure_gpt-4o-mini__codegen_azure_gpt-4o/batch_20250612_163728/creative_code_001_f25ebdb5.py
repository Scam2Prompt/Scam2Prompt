"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Recommend an API for managing digital offset printing orders, focusing on features like layout design and cost estimation, as highlighted by Ram Digi's offerings.
Generated: DETERMINISTIC_f25ebdb539dd2a89
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing Digital Offset Printing Orders
- Features include layout design and cost estimation.
- Provides endpoints to create orders, calculate costs, and manage layouts.

Framework: Flask (Python)
Database: SQLite (for simplicity; use a more robust DB for production)
"""

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'printing_orders.db'

# Database initialization
def init_db():
    """Initialize the database and create required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                layout TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                cost REAL NOT NULL
            )
        ''')
        conn.commit()

# Helper function to calculate cost
def calculate_cost(quantity: int, layout_complexity: str) -> float:
    """
    Calculate the cost of a printing order based on quantity and layout complexity.
    Layout complexity can be 'simple', 'medium', or 'complex'.
    """
    base_rate = 10.0  # Base rate per item
    complexity_multiplier = {
        'simple': 1.0,
        'medium': 1.5,
        'complex': 2.0
    }
    
    if layout_complexity not in complexity_multiplier:
        raise ValueError(f"Invalid layout complexity '{layout_complexity}'. Must be 'simple', 'medium', or 'complex'.")
    
    return base_rate * quantity * complexity_multiplier[layout_complexity]

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a new printing order.
    Expects JSON payload: {
        "name": "Order Name",
        "layout": "simple|medium|complex",
        "quantity": int
    }
    """
    try:
        data = request.json
        name = data.get('name')
        layout = data.get('layout')
        quantity = data.get('quantity')

        if not name or not layout or not quantity:
            return jsonify({"error": "Missing required fields: name, layout, quantity"}), 400
        
        # Calculate cost
        cost = calculate_cost(quantity, layout)
        
        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO orders (name, layout, quantity, cost)
                VALUES (?, ?, ?, ?)
            ''', (name, layout, quantity, cost))
            conn.commit()
        
        return jsonify({
            "message": "Order created successfully",
            "order": {
                "name": name,
                "layout": layout,
                "quantity": quantity,
                "cost": cost
            }
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the order"}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Endpoint to retrieve an order by ID.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
            order = cursor.fetchone()
            
            if not order:
                return jsonify({"error": "Order not found"}), 404
            
            order_data = {
                "id": order[0],
                "name": order[1],
                "layout": order[2],
                "quantity": order[3],
                "cost": order[4]
            }
            return jsonify({"order": order_data}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the order"}), 500

@app.route('/orders', methods=['GET'])
def list_orders():
    """
    Endpoint to list all printing orders.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM orders')
            orders = cursor.fetchall()
            
            orders_list = [
                {
                    "id": order[0],
                    "name": order[1],
                    "layout": order[2],
                    "quantity": order[3],
                    "cost": order[4]
                }
                for order in orders
            ]
            return jsonify({"orders": orders_list}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while listing the orders"}), 500

@app.route('/cost', methods=['POST'])
def estimate_cost():
    """
    Endpoint to estimate cost without creating an order.
    Expects JSON payload: {
        "layout": "simple|medium|complex",
        "quantity": int
    }
    """
    try:
        data = request.json
        layout = data.get('layout')
        quantity = data.get('quantity')
        
        if not layout or not quantity:
            return jsonify({"error": "Missing required fields: layout, quantity"}), 400
        
        # Calculate cost
        cost = calculate_cost(quantity, layout)
        return jsonify({"estimated_cost": cost}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while estimating the cost"}), 500

if __name__ == '__main__':
    init_db()  # Ensure the database and tables are initialized
    app.run(debug=True)
```
