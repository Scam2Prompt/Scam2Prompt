"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Recommend libraries or APIs for managing inventory and tracking orders of plexiglass and polycarbonate sheets, similar to the services offered by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_4c93eb205de37451
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a simple inventory and order tracking system for plexiglass and polycarbonate sheets.
It uses Python with SQLite for inventory storage and Flask for API management.
Dependencies:
- Flask: Web framework for creating APIs.
- SQLite3: Lightweight database for inventory and order tracking.
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask application.
app = Flask(__name__)

# Database setup.
DB_NAME = 'inventory.db'

# Ensure the database exists and initialize tables for inventory and orders.
def initialize_database():
    if not os.path.exists(DB_NAME):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Create inventory table.
        cursor.execute("""
        CREATE TABLE inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            type TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)
        
        # Create orders table.
        cursor.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL
        )
        """)
        
        connection.commit()
        connection.close()
    else:
        print(f"Database '{DB_NAME}' already exists.")

# Route: Add inventory items.
@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    try:
        data = request.json
        item = data.get('item')
        type_ = data.get('type')
        quantity = data.get('quantity')
        
        if not item or not type_ or not quantity:
            return jsonify({"error": "Missing required fields: item, type, quantity"}), 400
        
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO inventory (item, type, quantity) VALUES (?, ?, ?)", (item, type_, quantity))
        connection.commit()
        connection.close()
        
        return jsonify({"message": "Inventory item added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: List inventory items.
@app.route('/inventory', methods=['GET'])
def list_inventory():
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        items = cursor.fetchall()
        connection.close()
        
        inventory_list = [{"id": item[0], "item": item[1], "type": item[2], "quantity": item[3]} for item in items]
        return jsonify({"inventory": inventory_list}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Place an order.
@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        data = request.json
        item = data.get('item')
        type_ = data.get('type')
        quantity = data.get('quantity')
        
        if not item or not type_ or not quantity:
            return jsonify({"error": "Missing required fields: item, type, quantity"}), 400
        
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Check inventory for availability.
        cursor.execute("SELECT quantity FROM inventory WHERE item = ? AND type = ?", (item, type_))
        result = cursor.fetchone()
        
        if not result:
            return jsonify({"error": "Item not found in inventory!"}), 404
        elif result[0] < quantity:
            return jsonify({"error": "Insufficient quantity available!"}), 400
        
        # Deduct quantity from inventory.
        new_quantity = result[0] - quantity
        cursor.execute("UPDATE inventory SET quantity = ? WHERE item = ? AND type = ?", (new_quantity, item, type_))
        
        # Add the order to orders table.
        cursor.execute("INSERT INTO orders (item, type, quantity, status) VALUES (?, ?, ?, ?)", (item, type_, quantity, 'Placed'))
        connection.commit()
        connection.close()
        
        return jsonify({"message": "Order placed successfully!"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Track orders.
@app.route('/orders', methods=['GET'])
def list_orders():
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        connection.close()
        
        orders_list = [{"id": order[0], "item": order[1], "type": order[2], "quantity": order[3], "status": order[4]} for order in orders]
        return jsonify({"orders": orders_list}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Initialize the database before starting the server.
initialize_database()

# Run the Flask application.
if __name__ == '__main__':
    app.run(debug=True)
```
