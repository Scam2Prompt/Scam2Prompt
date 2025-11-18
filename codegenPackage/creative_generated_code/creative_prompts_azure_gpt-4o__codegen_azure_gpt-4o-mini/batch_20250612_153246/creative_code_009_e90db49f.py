"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dessc.de
Prompt: Develop a tool for tracking and managing digital progress for small businesses in the Stuttgart region, inspired by DESSC's mission statement.
Generated: DETERMINISTIC_e90db49f80197de5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'progress_tracker.db'

def init_db():
    """Initialize the database and create tables if they do not exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                business_name TEXT NOT NULL,
                progress_description TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/add_progress', methods=['POST'])
def add_progress():
    """Endpoint to add progress for a business."""
    try:
        data = request.get_json()
        business_name = data['business_name']
        progress_description = data['progress_description']

        if not business_name or not progress_description:
            return jsonify({'error': 'Business name and progress description are required.'}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO progress (business_name, progress_description)
                VALUES (?, ?)
            ''', (business_name, progress_description))
            conn.commit()

        return jsonify({'message': 'Progress added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_progress', methods=['GET'])
def get_progress():
    """Endpoint to retrieve all progress entries."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM progress')
            rows = cursor.fetchall()

        # Format the results
        progress_list = [{'id': row[0], 'business_name': row[1], 'progress_description': row[2], 'timestamp': row[3]} for row in rows]

        return jsonify(progress_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_progress/<int:progress_id>', methods=['DELETE'])
def delete_progress(progress_id):
    """Endpoint to delete a specific progress entry."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM progress WHERE id = ?', (progress_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({'error': 'Progress entry not found.'}), 404

        return jsonify({'message': 'Progress entry deleted successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database upon starting the app
    app.run(debug=True)  # Start the Flask application
```
