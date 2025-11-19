"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Write a code snippet that integrates mobile and web functionalities for agricultural activity monitoring, similar to Azagros.
Generated: DETERMINISTIC_1fae262499c6ff23
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify  # Web framework for API
from datetime import datetime              # For timestamping activities
import sqlite3                             # Database for storing activity data

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'agriculture_monitoring.db'

def init_db():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_type TEXT NOT NULL,
            description TEXT,
            timestamp TEXT NOT NULL,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/log_activity', methods=['POST'])
def log_activity():
    """
    Endpoint to log agricultural activities.
    Expects JSON payload with 'activity_type', 'description', and 'location'.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        activity_type = data.get('activity_type')
        description = data.get('description', '')
        location = data.get('location', '')
        timestamp = datetime.now().isoformat()

        # Validate required fields
        if not activity_type:
            return jsonify({'error': 'Activity type is required'}), 400

        # Insert activity into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO activities (activity_type, description, timestamp, location)
            VALUES (?, ?, ?, ?)
        ''', (activity_type, description, timestamp, location))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Activity logged successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_activities', methods=['GET'])
def get_activities():
    """
    Endpoint to retrieve logged agricultural activities.
    Supports optional query parameters for filtering by 'activity_type' or 'location'.
    """
    try:
        # Get query parameters
        activity_type = request.args.get('activity_type')
        location = request.args.get('location')

        # Fetch activities from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = 'SELECT * FROM activities WHERE 1=1'
        params = []

        if activity_type:
            query += ' AND activity_type = ?'
            params.append(activity_type)
        if location:
            query += ' AND location = ?'
            params.append(location)

        cursor.execute(query, params)
        activities = cursor.fetchall()
        conn.close()

        # Format response
        response = [
            {
                'id': row[0],
                'activity_type': row[1],
                'description': row[2],
                'timestamp': row[3],
                'location': row[4]
            }
            for row in activities
        ]

        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_activity/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    """
    Endpoint to delete a specific agricultural activity by ID.
    """
    try:
        # Delete activity from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM activities WHERE id = ?', (activity_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Activity not found'}), 404

        return jsonify({'message': 'Activity deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
