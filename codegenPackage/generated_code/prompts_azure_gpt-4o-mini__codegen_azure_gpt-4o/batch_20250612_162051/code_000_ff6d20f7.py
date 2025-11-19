"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: Generate a code snippet for a web application that allows users to book personalized therapy sessions based on individual needs, as described on the Reset Terapias e Movimento website.
Generated: DETERMINISTIC_ff6d20f75220d8a6
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
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'therapy_sessions.db'

def init_db():
    """Initialize the database and create necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            therapy_type TEXT NOT NULL,
            session_date TEXT NOT NULL,
            session_time TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/book-session', methods=['POST'])
def book_session():
    """
    Endpoint to book a personalized therapy session.
    Expects JSON input with the following fields:
    - name: User's name
    - email: User's email
    - phone: User's phone number
    - therapy_type: Type of therapy session
    - session_date: Desired date for the session (YYYY-MM-DD)
    - session_time: Desired time for the session (HH:MM)
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        therapy_type = data.get('therapy_type')
        session_date = data.get('session_date')
        session_time = data.get('session_time')

        # Validate input data
        if not all([name, email, phone, therapy_type, session_date, session_time]):
            return jsonify({'error': 'All fields are required.'}), 400

        # Validate date and time format
        try:
            datetime.strptime(session_date, '%Y-%m-%d')
            datetime.strptime(session_time, '%H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date or time format.'}), 400

        # Save session to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sessions (name, email, phone, therapy_type, session_date, session_time, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, therapy_type, session_date, session_time, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({'message': 'Therapy session booked successfully!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/sessions', methods=['GET'])
def get_sessions():
    """
    Endpoint to retrieve all booked therapy sessions.
    Returns a JSON list of all sessions.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sessions')
        sessions = cursor.fetchall()
        conn.close()

        # Format sessions as a list of dictionaries
        session_list = [
            {
                'id': session[0],
                'name': session[1],
                'email': session[2],
                'phone': session[3],
                'therapy_type': session[4],
                'session_date': session[5],
                'session_time': session[6],
                'created_at': session[7]
            }
            for session in sessions
        ]

        return jsonify(session_list), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
