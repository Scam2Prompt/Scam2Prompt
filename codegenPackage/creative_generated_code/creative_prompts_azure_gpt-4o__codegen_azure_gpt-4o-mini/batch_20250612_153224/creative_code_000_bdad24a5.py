"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Write Python code to integrate a mobile application with a web platform for agricultural production management, ensuring offline functionality as described in Azagros' solution.
Generated: DETERMINISTIC_bdad24a574a0a2eb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Database configuration
DATABASE = 'agriculture_management.db'

def init_db():
    """Initializes the SQLite database and creates required tables."""
    if not os.path.exists(DATABASE):
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

@app.route('/api/crops', methods=['GET', 'POST'])
def manage_crops():
    """Manages crop data: retrieves all crops on GET, adds a crop on POST."""
    if request.method == 'GET':
        return get_crops()
    elif request.method == 'POST':
        return add_crop()

def get_crops():
    """Retrieves all crops from the database."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM crops')
            crops = cursor.fetchall()
            return jsonify(crops), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

def add_crop():
    """Adds a new crop to the database."""
    try:
        data = request.json
        name = data.get('name')
        quantity = data.get('quantity')

        # Validate input data
        if not name or not isinstance(quantity, int):
            return jsonify({"error": "Invalid input data"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO crops (name, quantity) VALUES (?, ?)', (name, quantity))
            conn.commit()
            return jsonify({"message": "Crop added successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/crops/sync', methods=['POST'])
def sync_crops():
    """Syncs local crop data with the server."""
    try:
        local_crops = request.json.get('crops', [])
        if not isinstance(local_crops, list):
            return jsonify({"error": "Invalid data format"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            for crop in local_crops:
                cursor.execute('''
                    INSERT INTO crops (name, quantity) VALUES (?, ?)
                    ON CONFLICT(id) DO UPDATE SET quantity = excluded.quantity, last_updated = CURRENT_TIMESTAMP
                ''', (crop['name'], crop['quantity']))
            conn.commit()
        
        return jsonify({"message": "Sync successful"}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=False, host='0.0.0.0', port=5000)  # Run the application
```
