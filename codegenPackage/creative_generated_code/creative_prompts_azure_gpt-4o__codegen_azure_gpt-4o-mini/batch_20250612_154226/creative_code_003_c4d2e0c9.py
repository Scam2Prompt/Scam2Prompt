"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethn.cc
Prompt: Recommend Python libraries for creating a web app that displays gravel cycling destinations, inspired by the "PREMIUMY" section of ETNH Gravel Magazine.
Generated: DETERMINISTIC_c4d2e0c9e1b6b142
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'gravel_destinations.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Render the main page with gravel cycling destinations."""
    conn = get_db_connection()
    destinations = conn.execute('SELECT * FROM destinations').fetchall()
    conn.close()
    return render_template('index.html', destinations=destinations)

@app.route('/destination/<int:destination_id>', methods=['GET'])
def destination(destination_id):
    """Retrieve and display details of a specific destination."""
    conn = get_db_connection()
    destination = conn.execute('SELECT * FROM destinations WHERE id = ?', (destination_id,)).fetchone()
    conn.close()
    
    if destination is None:
        return jsonify({"error": "Destination not found"}), 404
    
    return render_template('destination.html', destination=destination)

@app.route('/api/destinations', methods=['GET'])
def api_destinations():
    """API endpoint to get a list of all destinations in JSON format."""
    conn = get_db_connection()
    destinations = conn.execute('SELECT * FROM destinations').fetchall()
    conn.close()
    
    return jsonify([dict(destination) for destination in destinations])

@app.route('/add_destination', methods=['POST'])
def add_destination():
    """Endpoint to add a new destination to the database."""
    try:
        new_destination = request.json
        name = new_destination['name']
        description = new_destination['description']
        location = new_destination['location']

        conn = get_db_connection()
        conn.execute('INSERT INTO destinations (name, description, location) VALUES (?, ?, ?)',
                     (name, description, location))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Destination added successfully"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def init_db():
    """Initialize the database with the required schema."""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        conn.execute('''
            CREATE TABLE destinations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)  # Start the Flask application
```
