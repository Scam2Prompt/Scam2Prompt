"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Recommend an API or library for implementing time-tracking functionality tailored for legal professionals, inspired by the features of BillYourTime.com.
Generated: DETERMINISTIC_04a19588817fba41
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This implementation uses Flask (a lightweight web framework for Python) 
to create a REST API for time-tracking functionality tailored for legal professionals. 
The code demonstrates how to track tasks/work sessions and calculate billable hours.

Dependencies:
- Flask: Install via `pip install flask`
- SQLite: Used as the database for storing time-tracking data

Features:
1. Add a new time entry (start time, end time, task description, hourly rate).
2. Retrieve all time entries with calculated billable amounts.
3. Error handling for invalid data inputs.

Production-ready notes:
- Ensure to handle authentication and authorization for legal professionals.
- Extend database schema for users, cases, etc., as needed.
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'time_tracking.db'

# Database initialization script
def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS time_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            task_description TEXT,
            hourly_rate REAL NOT NULL,
            billable_amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/time_entries', methods=['POST'])
def add_time_entry():
    """
    Endpoint to add a new time-tracking entry.
    Payload should include:
        - start_time (ISO format string)
        - end_time (ISO format string)
        - task_description (optional string)
        - hourly_rate (float)
    """
    try:
        data = request.json
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        task_description = data.get('task_description', '')
        hourly_rate = data.get('hourly_rate')

        # Validate input data
        if not (start_time and end_time and hourly_rate):
            return jsonify({'error': 'Missing required fields'}), 400

        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
        duration_hours = (end - start).total_seconds() / 3600

        if duration_hours <= 0:
            return jsonify({'error': 'End time must be after start time'}), 400

        billable_amount = round(duration_hours * hourly_rate, 2)

        # Store the time entry in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO time_entries (start_time, end_time, task_description, hourly_rate, billable_amount)
            VALUES (?, ?, ?, ?, ?)
        ''', (start_time, end_time, task_description, hourly_rate, billable_amount))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Time entry added successfully', 'billable_amount': billable_amount}), 201
    except ValueError as e:
        return jsonify({'error': f'Invalid data format: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/time_entries', methods=['GET'])
def get_time_entries():
    """
    Endpoint to retrieve all time-tracking entries.
    Returns a list of entries with calculated billable amounts.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM time_entries')
        rows = cursor.fetchall()
        conn.close()

        entries = [
            {
                'id': row[0],
                'start_time': row[1],
                'end_time': row[2],
                'task_description': row[3],
                'hourly_rate': row[4],
                'billable_amount': row[5]
            } for row in rows
        ]

        return jsonify(entries), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Run the Flask app
    app.run(debug=True)
```
