"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Suggest a library or API for managing high-pressure washing equipment and tracking its usage in poultry farming buildings, as described in the services offered by "Lavage désinfection de bâtiments d’élevage."
Generated: DETERMINISTIC_a89efa6a85ddfe04
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Flask for building an API to manage high-pressure washing equipment and track its usage in poultry farming buildings. This example uses SQLite for the database and includes error handling.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE = "equipment_usage.db"

# Ensure database is created if it doesn't exist
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            status TEXT NOT NULL,
            last_used TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE usage_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment_id INTEGER NOT NULL,
            building TEXT NOT NULL,
            usage_duration INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (equipment_id) REFERENCES equipment (id)
        )
    """)
    conn.commit()
    conn.close()


# Helper function to connect to the database
def db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None


# Endpoint to add new equipment
@app.route('/equipment', methods=['POST'])
def add_equipment():
    try:
        data = request.json
        name = data.get("name")
        type = data.get("type")
        status = data.get("status", "available")

        if not name or not type:
            return jsonify({"error": "Name and type are required"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO equipment (name, type, status) VALUES (?, ?, ?)",
                       (name, type, status))
        conn.commit()
        equipment_id = cursor.lastrowid
        conn.close()

        return jsonify({"message": "Equipment added successfully", "id": equipment_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to log equipment usage
@app.route('/usage', methods=['POST'])
def log_usage():
    try:
        data = request.json
        equipment_id = data.get("equipment_id")
        building = data.get("building")
        usage_duration = data.get("usage_duration")

        if not equipment_id or not building or not usage_duration:
            return jsonify({"error": "Equipment ID, building, and usage duration are required"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usage_log (equipment_id, building, usage_duration) VALUES (?, ?, ?)",
                       (equipment_id, building, usage_duration))
        conn.commit()
        usage_id = cursor.lastrowid
        conn.close()

        return jsonify({"message": "Usage logged successfully", "id": usage_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to list equipment
@app.route('/equipment', methods=['GET'])
def list_equipment():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment")
        equipment = cursor.fetchall()
        conn.close()

        equipment_list = [
            {"id": row[0], "name": row[1], "type": row[2], "status": row[3], "last_used": row[4]}
            for row in equipment
        ]
        return jsonify(equipment_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to list usage logs
@app.route('/usage', methods=['GET'])
def list_usage_logs():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usage_log")
        usage_logs = cursor.fetchall()
        conn.close()

        logs = [
            {"id": row[0], "equipment_id": row[1], "building": row[2], "usage_duration": row[3], "timestamp": row[4]}
            for row in usage_logs
        ]
        return jsonify(logs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

This is a production-ready API example and can be extended further as needed.
