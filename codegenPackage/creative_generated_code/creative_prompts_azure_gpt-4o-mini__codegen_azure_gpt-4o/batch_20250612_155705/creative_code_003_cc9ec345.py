"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beets-fi.com
Prompt: Develop an API recommendation for integrating neighborhood community information into a real estate platform, reflecting the insights from AndySellsVegas.com.
Generated: DETERMINISTIC_cc9ec345047a408f
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import sqlite3

# Flask application setup
app = Flask(__name__)

# Database setup (SQLite for simplicity)
DATABASE = 'community_info.db'

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows dictionary-like row access
    return conn

# Function to initialize the database
def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS neighborhoods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        avg_home_price INTEGER,
        nearby_schools TEXT
    )
    """)
    conn.commit()
    conn.close()

# API endpoint: Get neighborhood information
@app.route('/api/neighborhoods', methods=['GET'])
def get_neighborhoods():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM neighborhoods")
        neighborhoods = cursor.fetchall()
        conn.close()

        # Return data in JSON format
        return jsonify([dict(row) for row in neighborhoods]), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to fetch neighborhoods.", "details": str(e)}), 500

# API endpoint: Add new neighborhood information
@app.route('/api/neighborhoods', methods=['POST'])
def add_neighborhood():
    try:
        data = request.json

        # Validate input
        if not data or 'name' not in data or 'avg_home_price' not in data:
            return jsonify({"error": "Invalid input. 'name' and 'avg_home_price' are required."}), 400

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO neighborhoods (name, description, avg_home_price, nearby_schools)
        VALUES (?, ?, ?, ?)
        """, (data['name'], data.get('description', ''), data['avg_home_price'], data.get('nearby_schools', '')))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": f"Neighborhood '{data['name']}' added successfully."}), 201
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to add neighborhood.", "details": str(e)}), 500

# API endpoint: Get specific neighborhood information
@app.route('/api/neighborhoods/<int:neighborhood_id>', methods=['GET'])
def get_neighborhood_by_id(neighborhood_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM neighborhoods WHERE id = ?", (neighborhood_id,))
        neighborhood = cursor.fetchone()
        conn.close()

        if not neighborhood:
            return jsonify({"error": "Neighborhood not found."}), 404

        # Return data in JSON format
        return jsonify(dict(neighborhood)), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to fetch neighborhood.", "details": str(e)}), 500

# API endpoint: Update neighborhood information
@app.route('/api/neighborhoods/<int:neighborhood_id>', methods=['PUT'])
def update_neighborhood(neighborhood_id):
    try:
        data = request.json

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE neighborhoods
        SET name = ?, description = ?, avg_home_price = ?, nearby_schools = ?
        WHERE id = ?
        """, (data.get('name'), data.get('description'), data.get('avg_home_price'), data.get('nearby_schools'), neighborhood_id))
        conn.commit()
        conn.close()

        # Check if the update was successful
        if cursor.rowcount == 0:
            return jsonify({"error": "Neighborhood not found or no changes made."}), 404

        # Return success response
        return jsonify({"message": f"Neighborhood with ID '{neighborhood_id}' updated successfully."}), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to update neighborhood.", "details": str(e)}), 500

# API endpoint: Delete specific neighborhood information
@app.route('/api/neighborhoods/<int:neighborhood_id>', methods=['DELETE'])
def delete_neighborhood(neighborhood_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM neighborhoods WHERE id = ?", (neighborhood_id,))
        conn.commit()
        conn.close()

        # Check if the deletion was successful
        if cursor.rowcount == 0:
            return jsonify({"error": "Neighborhood not found."}), 404

        # Return success response
        return jsonify({"message": f"Neighborhood with ID '{neighborhood_id}' deleted successfully."}), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to delete neighborhood.", "details": str(e)}), 500

# Initialize the database
initialize_db()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
