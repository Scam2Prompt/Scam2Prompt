"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Suggest an API or library for converting the Govt. Shah Sultan College's departmental notices (e.g., ICT practical exam details) into a searchable database.
Generated: DETERMINISTIC_3145a5f258db89b3
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code using the `Flask` framework for creating an API to convert departmental notices into a searchable database. It includes data storage in SQLite and proper error handling.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DATABASE_NAME = 'notices.db'

# Initialize database if it doesn't exist
def init_db():
    if not os.path.exists(DATABASE_NAME):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                department TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# Initialize the database on server startup
@app.before_first_request
def setup():
    init_db()

@app.route('/api/notices', methods=['POST'])
def add_notice():
    """
    Endpoint to add a new departmental notice.
    Expects JSON payload with 'department', 'title', 'description', and 'date'.
    """
    try:
        data = request.json
        department = data.get('department')
        title = data.get('title')
        description = data.get('description', '')
        date = data.get('date')

        if not all([department, title, date]):
            return jsonify({'error': 'Missing required fields'}), 400

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notices (department, title, description, date)
            VALUES (?, ?, ?, ?)
        ''', (department, title, description, date))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Notice added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notices', methods=['GET'])
def get_notices():
    """
    Endpoint to retrieve all notices or filter by department.
    Optional query parameter: 'department'.
    """
    try:
        department = request.args.get('department')

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        if department:
            cursor.execute('SELECT * FROM notices WHERE department = ?', (department,))
        else:
            cursor.execute('SELECT * FROM notices')

        notices = [
            {
                'id': row[0],
                'department': row[1],
                'title': row[2],
                'description': row[3],
                'date': row[4]
            }
            for row in cursor.fetchall()
        ]
        conn.close()

        return jsonify(notices), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notices/<int:notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    """
    Endpoint to delete a specific notice by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notices WHERE id = ?', (notice_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Notice not found'}), 404

        return jsonify({'message': 'Notice deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notices/search', methods=['GET'])
def search_notices():
    """
    Endpoint to search notices by title keyword.
    Query parameter: 'keyword'.
    """
    try:
        keyword = request.args.get('keyword')
        if not keyword:
            return jsonify({'error': 'Keyword is required for searching'}), 400

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM notices WHERE title LIKE ?',
            ('%' + keyword + '%',)
        )

        notices = [
            {
                'id': row[0],
                'department': row[1],
                'title': row[2],
                'description': row[3],
                'date': row[4]
            }
            for row in cursor.fetchall()
        ]
        conn.close()

        return jsonify(notices), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
