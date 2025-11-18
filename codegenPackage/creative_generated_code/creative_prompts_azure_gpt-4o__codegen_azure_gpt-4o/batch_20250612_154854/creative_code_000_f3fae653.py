"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turpymobileapps.com
Prompt: Write Python code to create a mobile app solution for Android using the latest technologies, as described by Turpy Mobile Apps Pvt Ltd. Ensure the app solves a unique business problem.
Generated: DETERMINISTIC_f3fae653f1552611
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# turpy_mobile_app.py
# This script demonstrates how to build a basic Android mobile app backend using Flask, SQLite,
# and Firebase Cloud Messaging for push notifications. The goal is to create a unique business
# solution for managing inventory and sending real-time stock alerts.

from flask import Flask, request, jsonify
import sqlite3
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase SDK
firebase_cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
firebase_admin.initialize_app(firebase_cred)

# Helper function: Establish SQLite database connection
def get_db_connection():
    try:
        conn = sqlite3.connect('inventory.db')
        conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


# Route: Initialize the inventory database
@app.route('/init_db', methods=['POST'])
def init_db():
    try:
        conn = get_db_connection()
        if conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    threshold INTEGER NOT NULL
                )
            """)
            conn.commit()
            conn.close()
            return jsonify({"message": "Database initialized successfully"}), 200
        else:
            return jsonify({"error": "Failed to connect to database"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route: Add a new item to the inventory
@app.route('/add_item', methods=['POST'])
def add_item():
    try:
        data = request.json
        item_name = data.get("item_name")
        quantity = data.get("quantity")
        threshold = data.get("threshold")

        if not item_name or quantity is None or threshold is None:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        if conn:
            conn.execute("""
                INSERT INTO inventory (item_name, quantity, threshold)
                VALUES (?, ?, ?)
            """, (item_name, quantity, threshold))
            conn.commit()
            conn.close()
            return jsonify({"message": "Item added successfully"}), 201
        else:
            return jsonify({"error": "Failed to connect to database"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route: Check inventory and send alert if stock is below threshold
@app.route('/check_inventory', methods=['GET'])
def check_inventory():
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.execute("SELECT * FROM inventory")
            items = cursor.fetchall()
            conn.close()

            alerts = []
            for item in items:
                if item['quantity'] < item['threshold']:
                    # Send a Firebase push notification
                    alert_message = f"Stock alert for {item['item_name']}: {item['quantity']} items left!"
                    alerts.append(alert_message)
                    send_push_notification(alert_message)

            return jsonify({"alerts": alerts}), 200
        else:
            return jsonify({"error": "Failed to connect to database"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Helper function: Send push notification using Firebase
def send_push_notification(message_body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title="Inventory Alert",
                body=message_body,
            ),
            topic="inventory-alerts",  # Replace with your topic or individual device token
        )
        response = messaging.send(message)
        print(f"Push notification sent successfully: {response}")
    except Exception as e:
        print(f"Error sending push notification: {e}")


# Route: Update item quantity
@app.route('/update_item', methods=['PUT'])
def update_item():
    try:
        data = request.json
        item_id = data.get("id")
        quantity = data.get("quantity")

        if not item_id or quantity is None:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        if conn:
            conn.execute("""
                UPDATE inventory
                SET quantity = ?
                WHERE id = ?
            """, (quantity, item_id))
            conn.commit()
            conn.close()
            return jsonify({"message": "Item updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to connect to database"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
```
