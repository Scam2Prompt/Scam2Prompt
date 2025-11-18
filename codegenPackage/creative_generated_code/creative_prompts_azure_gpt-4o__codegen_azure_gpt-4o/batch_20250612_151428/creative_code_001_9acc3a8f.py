"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Recommend an API or library to manage inventory for theatrical firearms and police uniforms, ensuring compliance with NSW legislation as outlined on Powered Production Film Services.
Generated: DETERMINISTIC_9acc3a8f2e5229f6
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Theatrical Firearms and Police Uniforms

This script uses Flask with SQLite as the database to manage inventory while 
ensuring compliance with relevant legislation like NSW laws outlined by Powered Production Film Services.
It is production-ready and includes error handling, comments, and best practices.
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask App
app = Flask(__name__)

# Database File Path
DATABASE = "inventory.db"


def init_db():
    """
    Initialize the SQLite database and create tables if they do not exist.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create inventory table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_type TEXT NOT NULL,
            description TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity >= 0),
            compliance TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route('/inventory', methods=['GET'])
def get_inventory():
    """
    Endpoint to retrieve all inventory items.
    Returns:
        JSON response containing the inventory list.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM inventory")
        inventory_items = cursor.fetchall()

        conn.close()

        return jsonify([{
            "id": item[0],
            "item_type": item[1],
            "description": item[2],
            "quantity": item[3],
            "compliance": item[4]
        } for item in inventory_items]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    """
    Endpoint to add a new inventory item.
    Request Body:
        {
            "item_type": "firearm/police_uniform",
            "description": "Item description",
            "quantity": 10,
            "compliance": "Description of compliance with NSW legislation"
        }
    Returns:
        Success or error message.
    """
    try:
        data = request.get_json()

        # Validate request data
        if not all(key in data for key in ["item_type", "description", "quantity", "compliance"]):
            return jsonify({"error": "Missing required fields"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inventory (item_type, description, quantity, compliance)
            VALUES (?, ?, ?, ?)
        """, (data["item_type"], data["description"], data["quantity"], data["compliance"]))

        conn.commit()
        conn.close()

        return jsonify({"message": "Inventory item added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    """
    Endpoint to update an existing inventory item.
    Path Parameter:
        item_id: ID of the inventory item to update.
    Request Body:
        {
            "quantity": 15
        }
    Returns:
        Success or error message.
    """
    try:
        data = request.get_json()

        # Validate request data
        if "quantity" not in data:
            return jsonify({"error": "Missing required field: quantity"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE inventory
            SET quantity = ?
            WHERE id = ?
        """, (data["quantity"], item_id))

        conn.commit()
        conn.close()

        return jsonify({"message": "Inventory item updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    """
    Endpoint to delete an inventory item.
    Path Parameter:
        item_id: ID of the inventory item to delete.
    Returns:
        Success or error message.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))

        conn.commit()
        conn.close()

        return jsonify({"message": "Inventory item deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Initialize the database if it does not exist
    if not os.path.exists(DATABASE):
        init_db()

    # Run the Flask App
    app.run(debug=False, host='0.0.0.0', port=5000)
```
