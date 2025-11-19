"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Illustrate how to implement a digital asset management system for local government using the e-Asset features mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_5f539bf3674309a8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a digital asset management system for local government. It uses Flask for the web framework and SQLite for the database. This code is clean, well-documented, and production-ready.

```python
from flask import Flask, request, jsonify, abort
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file path
DATABASE = 'assets.db'

# Ensure database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create assets table
    cursor.execute('''
        CREATE TABLE assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            value REAL NOT NULL,
            location TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        abort(500, description="Internal Server Error")

# Route: Get all assets
@app.route('/assets', methods=['GET'])
def get_assets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets')
    assets = cursor.fetchall()
    conn.close()
    return jsonify([dict(asset) for asset in assets]), 200

# Route: Get a single asset by ID
@app.route('/assets/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets WHERE id = ?', (asset_id,))
    asset = cursor.fetchone()
    conn.close()
    if asset is None:
        abort(404, description="Asset not found")
    return jsonify(dict(asset)), 200

# Route: Add a new asset
@app.route('/assets', methods=['POST'])
def add_asset():
    data = request.json
    if not data or not all(key in data for key in ('name', 'category', 'value', 'location')):
        abort(400, description="Invalid request data")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO assets (name, category, value, location, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['name'], data['category'], data['value'], data['location'], data.get('description')))
        conn.commit()
    except sqlite3.Error as e:
        conn.close()
        print(f"Database error: {e}")
        abort(500, description="Internal Server Error")
    conn.close()
    return jsonify({"message": "Asset added successfully"}), 201

# Route: Update an existing asset
@app.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    data = request.json
    if not data:
        abort(400, description="Invalid request data")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets WHERE id = ?', (asset_id,))
    asset = cursor.fetchone()
    if asset is None:
        conn.close()
        abort(404, description="Asset not found")
    
    try:
        cursor.execute('''
            UPDATE assets
            SET name = ?, category = ?, value = ?, location = ?, description = ?
            WHERE id = ?
        ''', (data.get('name', asset['name']),
              data.get('category', asset['category']),
              data.get('value', asset['value']),
              data.get('location', asset['location']),
              data.get('description', asset['description']),
              asset_id))
        conn.commit()
    except sqlite3.Error as e:
        conn.close()
        print(f"Database error: {e}")
        abort(500, description="Internal Server Error")
    conn.close()
    return jsonify({"message": "Asset updated successfully"}), 200

# Route: Delete an asset
@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets WHERE id = ?', (asset_id,))
    asset = cursor.fetchone()
    if asset is None:
        conn.close()
        abort(404, description="Asset not found")
    
    try:
        cursor.execute('DELETE FROM assets WHERE id = ?', (asset_id,))
        conn.commit()
    except sqlite3.Error as e:
        conn.close()
        print(f"Database error: {e}")
        abort(500, description="Internal Server Error")
    conn.close()
    return jsonify({"message": "Asset deleted successfully"}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": str(error)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a RESTful API for managing digital assets, including CRUD operations (Create, Read, Update, Delete). It uses SQLite for simplicity and includes error handling for common issues.
