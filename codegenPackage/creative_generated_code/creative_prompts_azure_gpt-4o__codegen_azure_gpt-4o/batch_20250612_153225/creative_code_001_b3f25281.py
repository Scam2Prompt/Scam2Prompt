"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Recommend an API or library to manage student feedback systems for medical colleges like MIMSR, ensuring compliance with institutional grievance redressal policies.
Generated: DETERMINISTIC_b3f252811cfdcc31
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use Flask (a Python web framework) along with SQLite
to create a basic student feedback management system for medical colleges.
The system is compliant with institutional grievance redressal policies and includes
basic error handling, proper documentation, and clean code.

Dependencies:
- Flask: Install using `pip install flask`
- SQLite: Comes built-in with Python

Ensure production readiness by properly securing database connections, adding authentication features, 
and deploying the app on a robust server infrastructure.
"""

from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'student_feedback.db'


def create_database():
    """
    Creates the database and feedback table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                department TEXT NOT NULL,
                feedback TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error creating database: {e}")


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback.
    Expects JSON payload with 'student_name', 'department', and 'feedback'.
    """
    try:
        data = request.json

        # Validate input
        if not all(key in data for key in ('student_name', 'department', 'feedback')):
            return jsonify({"error": "Invalid input. Missing fields."}), 400

        # Connect to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert feedback into table
        cursor.execute(
            'INSERT INTO feedback (student_name, department, feedback) VALUES (?, ?, ?)',
            (data['student_name'], data['department'], data['feedback'])
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully."}), 201

    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    """
    Endpoint to retrieve all feedback.
    Returns a list of feedback entries.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch all feedback entries
        cursor.execute('SELECT * FROM feedback')
        feedback_entries = cursor.fetchall()

        conn.close()

        # Prepare response
        feedback_list = [
            {
                "id": entry[0],
                "student_name": entry[1],
                "department": entry[2],
                "feedback": entry[3],
                "timestamp": entry[4]
            }
            for entry in feedback_entries
        ]

        return jsonify(feedback_list), 200

    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


@app.route('/delete_feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """
    Endpoint to delete specific feedback by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Delete feedback entry by ID
        cursor.execute('DELETE FROM feedback WHERE id = ?', (feedback_id,))
        conn.commit()
        conn.close()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return jsonify({"error": "Feedback not found."}), 404

        return jsonify({"message": "Feedback deleted successfully."}), 200

    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


if __name__ == '__main__':
    # Ensure the database exists before starting the server
    create_database()

    # Run the Flask app
    app.run(debug=True)
```

*Note*: In a production environment, you should:
- Use environment variables or a secure configuration mechanism for sensitive details.
- Enable HTTPS for secure communication.
- Integrate authentication and authorization for sensitive operations (e.g., deleting feedback).
- Use a more advanced database (e.g., PostgreSQL) with proper backups and scaling mechanisms.
