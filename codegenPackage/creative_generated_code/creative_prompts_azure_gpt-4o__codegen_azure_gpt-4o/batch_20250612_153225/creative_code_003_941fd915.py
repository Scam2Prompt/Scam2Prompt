"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate code for a web application that tracks attendance for DBT therapy sessions, ensuring weekly participation in individual and group therapy, as required for effective treatment according to the Mente Sana Psicología website.
Generated: DETERMINISTIC_941fd91599f2d6a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'attendance.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            session_type TEXT NOT NULL,
            session_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Helper function to connect to the database
def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/attendance', methods=['POST'])
def record_attendance():
    """
    Endpoint to record attendance for a DBT therapy session.
    Expects 'user_id', 'session_type' ('individual' or 'group'), and 'session_date' in the request JSON.
    """
    try:
        # Parse request data
        data = request.get_json()
        user_id = data.get('user_id')
        session_type = data.get('session_type')
        session_date = data.get('session_date')

        # Validate input
        if not user_id or not session_type or not session_date:
            return jsonify({'error': 'Missing required fields'}), 400
        if session_type not in ['individual', 'group']:
            return jsonify({'error': 'Invalid session type. Must be "individual" or "group"'}), 400

        # Save attendance record to database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO attendance (user_id, session_type, session_date)
            VALUES (?, ?, ?)
        ''', (user_id, session_type, session_date))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Attendance recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/attendance/<int:user_id>', methods=['GET'])
def get_attendance(user_id):
    """
    Endpoint to retrieve attendance records for a specific user.
    Returns all individual and group sessions attended.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT session_type, session_date
            FROM attendance
            WHERE user_id = ?
        ''', (user_id,))
        records = cursor.fetchall()
        conn.close()

        if not records:
            return jsonify({'message': 'No attendance records found for the user'}), 404

        return jsonify({
            'user_id': user_id,
            'attendance_records': [dict(record) for record in records]
        }), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/attendance/weekly_report', methods=['POST'])
def weekly_report():
    """
    Endpoint to generate a weekly report for user attendance.
    Expects 'user_id' and 'week_start_date' in the request JSON.
    """
    try:
        # Parse request data
        data = request.get_json()
        user_id = data.get('user_id')
        week_start_date = data.get('week_start_date')
        
        # Validate input
        if not user_id or not week_start_date:
            return jsonify({'error': 'Missing required fields'}), 400
        try:
            week_start = datetime.strptime(week_start_date, '%Y-%m-%d')
            week_end = week_start + timedelta(days=6)
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # Query attendance records for the week
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT session_type, session_date
            FROM attendance
            WHERE user_id = ? AND session_date BETWEEN ? AND ?
        ''', (user_id, week_start_date, week_end.strftime('%Y-%m-%d')))
        records = cursor.fetchall()
        conn.close()

        # Summarize weekly attendance
        individual_sessions = sum(1 for record in records if record['session_type'] == 'individual')
        group_sessions = sum(1 for record in records if record['session_type'] == 'group')

        return jsonify({
            'user_id': user_id,
            'week_start_date': week_start_date,
            'week_end_date': week_end.strftime('%Y-%m-%d'),
            'individual_sessions': individual_sessions,
            'group_sessions': group_sessions,
            'attendance_records': [dict(record) for record in records]
        }), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
