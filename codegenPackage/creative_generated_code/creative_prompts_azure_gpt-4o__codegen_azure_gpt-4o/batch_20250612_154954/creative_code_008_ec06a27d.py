"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Create a maintenance tracking system for rice mill spares such as strainers, baffles, and conveyors, using the services described by Mechano Solutions.
Generated: DETERMINISTIC_ec06a27d266b77a4
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Maintenance Tracking System for Rice Mill Spares
Author: [Your Name]
Date: [Today's Date]

This script implements a basic maintenance tracking system for rice mill spares
such as strainers, baffles, and conveyors. It uses Mechano Solutions' services
to update and retrieve maintenance data. The system supports adding new spares,
tracking maintenance status, and querying maintenance history.

Dependencies:
- Flask: Lightweight web framework for API services
- SQLite: Database for storing spare parts and maintenance data

Instructions:
1. Install required Python libraries: `pip install flask sqlite3`
2. Run the script: `python maintenance_tracking.py`
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database file
DATABASE = 'maintenance.db'

# Error messages
SPARE_NOT_FOUND_MSG = "Spare not found in the database."
GENERAL_ERROR_MSG = "An error occurred. Please try again later."


# Helper function to connect to the database
def connect_db():
    """Establishes connection with the SQLite database."""
    return sqlite3.connect(DATABASE)


# Initialize the database
def initialize_database():
    """Creates tables in the database if they don't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    # Create the spares table to track spare parts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            last_maintenance_date TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()


# Endpoint to list all spares
@app.route('/spares', methods=['GET'])
def list_spares():
    """Fetches the list of all spare parts."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM spares")
        spares = cursor.fetchall()
        conn.close()
        return jsonify([{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'last_maintenance_date': row[3],
            'status': row[4]
        } for row in spares])
    except Exception as e:
        conn.close()
        return jsonify({'error': GENERAL_ERROR_MSG}), 500


# Endpoint to add a new spare
@app.route('/spares', methods=['POST'])
def add_spare():
    """Adds a new spare part to the database."""
    data = request.json
    name = data.get('name')
    description = data.get('description', '')
    status = data.get('status', 'Needs Maintenance')

    if not name:
        return jsonify({'error': 'Spare name is required.'}), 400

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO spares (name, description, last_maintenance_date, status)
            VALUES (?, ?, NULL, ?)
        """, (name, description, status))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Spare added successfully.'}), 201
    except Exception as e:
        conn.close()
        return jsonify({'error': GENERAL_ERROR_MSG}), 500


# Endpoint to update maintenance status
@app.route('/spares/<int:spare_id>/maintenance', methods=['PUT'])
def update_maintenance(spare_id):
    """Updates the maintenance status of a spare part."""
    data = request.json
    status = data.get('status')
    maintenance_date = data.get('maintenance_date')

    if not status or not maintenance_date:
        return jsonify({'error': 'Status and maintenance date are required.'}), 400

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE spares
            SET status = ?, last_maintenance_date = ?
            WHERE id = ?
        """, (status, maintenance_date, spare_id))
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'error': SPARE_NOT_FOUND_MSG}), 404
        conn.commit()
        conn.close()
        return jsonify({'message': 'Maintenance updated successfully.'}), 200
    except Exception as e:
        conn.close()
        return jsonify({'error': GENERAL_ERROR_MSG}), 500


# Endpoint to delete a spare
@app.route('/spares/<int:spare_id>', methods=['DELETE'])
def delete_spare(spare_id):
    """Deletes a spare part from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM spares WHERE id = ?", (spare_id,))
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'error': SPARE_NOT_FOUND_MSG}), 404
        conn.commit()
        conn.close()
        return jsonify({'message': 'Spare deleted successfully.'}), 200
    except Exception as e:
        conn.close()
        return jsonify({'error': GENERAL_ERROR_MSG}), 500


# Main function to start the application
if __name__ == '__main__':
    # Initialize the database
    initialize_database()
    # Run the Flask application
    app.run(debug=True)
```
