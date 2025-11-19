"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Illustrate how to implement a digital asset management system for local government using the e-Asset features mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_5f539bf3674309a8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Digital Asset Management System for Local Government
This implementation provides a simplified digital asset management system
based on the e-Asset features, such as tracking, adding, updating, and deleting assets.

Language: Python
Database: SQLite (for simplicity)
Frameworks: Flask (for web application)

Author: Expert Programmer
Date: YYYY-MM-DD
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database initialization
DB_FILE = "assets.db"


def init_db():
    """Initialize the SQLite database and create the 'assets' table."""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                value REAL NOT NULL,
                location TEXT NOT NULL,
                date_acquired TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()


# Initialize database on startup
init_db()


@app.route('/assets', methods=['GET'])
def get_assets():
    """
    Retrieve all assets from the database.
    Returns a JSON list of assets.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assets")
        assets = cursor.fetchall()
        conn.close()
        return jsonify([{
            "id": asset[0],
            "name": asset[1],
            "category": asset[2],
            "value": asset[3],
            "location": asset[4],
            "date_acquired": asset[5]
        } for asset in assets])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/assets', methods=['POST'])
def add_asset():
    """
    Add a new asset to the database.
    Expected JSON body: { "name": ..., "category": ..., "value": ..., "location": ..., "date_acquired": ... }
    """
    try:
        data = request.json
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO assets (name, category, value, location, date_acquired)
            VALUES (?, ?, ?, ?, ?)
        """, (data['name'], data['category'], data['value'], data['location'], data['date_acquired']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Asset added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    """
    Update an existing asset in the database.
    Expected JSON body: { "name": ..., "category": ..., "value": ..., "location": ..., "date_acquired": ... }
    """
    try:
        data = request.json
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE assets
            SET name = ?, category = ?, value = ?, location = ?, date_acquired = ?
            WHERE id = ?
        """, (data['name'], data['category'], data['value'], data['location'], data['date_acquired'], asset_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Asset updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """
    Delete an asset from the database.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM assets WHERE id = ?", (asset_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Asset deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Replace `DB_FILE = "assets.db"` with a secure database connection in production (e.g., PostgreSQL or MySQL).
- Disable `debug=True` in production to secure application details.
