"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Write Python code to integrate a mobile application with a web platform for agricultural production management, ensuring offline functionality as described in Azagros' solution.
Generated: DETERMINISTIC_bdad24a574a0a2eb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database setup
DATABASE = 'agriculture_management.db'

def init_db():
    """Initialize the SQLite database with required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/api/crops', methods=['GET', 'POST'])
def manage_crops():
    """Manage crops: retrieve all crops or add a new crop."""
    if request.method == 'GET':
        return get_crops()
    elif request.method == 'POST':
        return add_crop()

def get_crops():
    """Retrieve all crops from the database."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM crops')
            crops = cursor.fetchall()
            return jsonify(crops), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_crop():
    """Add a new crop to the database."""
    try:
        data = request.json
        name = data.get('name')
        quantity = data.get('quantity')

        if not name or not isinstance(quantity, int):
            return jsonify({"error": "Invalid input"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO crops (name, quantity) VALUES (?, ?)', (name, quantity))
            conn.commit()
            return jsonify({"message": "Crop added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/sync', methods=['POST'])
def sync_data():
    """Sync local data with the server."""
    try:
        local_data = request.json.get('local_data', [])
        if not isinstance(local_data, list):
            return jsonify({"error": "Invalid data format"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            for crop in local_data:
                name = crop.get('name')
                quantity = crop.get('quantity')
                if name and isinstance(quantity, int):
                    cursor.execute('INSERT OR REPLACE INTO crops (name, quantity) VALUES (?, ?)', (name, quantity))
            conn.commit()
            return jsonify({"message": "Data synced successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure the database is initialized before starting the app
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code provides a simple Flask application that allows for managing crops in an agricultural production management system. It includes endpoints for retrieving and adding crops, as well as syncing local data with the server. The SQLite database is used for offline functionality, ensuring that data can be stored locally and synchronized when online.
