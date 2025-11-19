"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: What are the key components to consider when developing a web application for DBT therapy that includes both individual and group sessions?
Generated: DETERMINISTIC_e6d0de49aed95194
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dbt_therapy_app.py
# A web application for DBT therapy that includes individual and group sessions.
# This code demonstrates the key components to consider when developing such an application.

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'dbt_therapy.db'

def init_db():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            session_type TEXT NOT NULL, -- 'individual' or 'group'
            session_date TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    Expected JSON payload: {"name": "John Doe", "email": "john@example.com"}
    """
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/schedule_session', methods=['POST'])
def schedule_session():
    """
    Schedule a DBT therapy session.
    Expected JSON payload: {"user_id": 1, "session_type": "individual", "session_date": "2023-10-01", "notes": "Focus on mindfulness"}
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        session_type = data.get('session_type')
        session_date = data.get('session_date')
        notes = data.get('notes')

        if not user_id or not session_type or not session_date:
            return jsonify({"error": "User ID, session type, and session date are required"}), 400

        # Validate session type
        if session_type not in ['individual', 'group']:
            return jsonify({"error": "Invalid session type. Must be 'individual' or 'group'"}), 400

        # Validate session date
        try:
            datetime.strptime(session_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sessions (user_id, session_type, session_date, notes)
            VALUES (?, ?, ?, ?)
        ''', (user_id, session_type, session_date, notes))
        conn.commit()
        conn.close()

        return jsonify({"message": "Session scheduled successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User ID does not exist"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_sessions', methods=['GET'])
def get_sessions():
    """
    Retrieve all sessions for a user.
    Query parameter: user_id (e.g., /get_sessions?user_id=1)
    """
    try:
        user_id = request.args.get('user_id')

        if not user_id:
            return jsonify({"error": "User ID is required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sessions WHERE user_id = ?', (user_id,))
        sessions = cursor.fetchall()
        conn.close()

        if not sessions:
            return jsonify({"message": "No sessions found for the user"}), 404

        # Format the response
        session_list = [
            {
                "id": session[0],
                "user_id": session[1],
                "session_type": session[2],
                "session_date": session[3],
                "notes": session[4]
            }
            for session in sessions
        ]

        return jsonify({"sessions": session_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
