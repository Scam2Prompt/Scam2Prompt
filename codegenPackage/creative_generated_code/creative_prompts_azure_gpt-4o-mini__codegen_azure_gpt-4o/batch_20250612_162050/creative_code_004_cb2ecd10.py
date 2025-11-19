"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Design a web application that integrates with the MIMSR's student feedback system, allowing users to submit and view feedback on courses and faculty.
Generated: DETERMINISTIC_cb2ecd10d7347b55
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database configuration
DB_FILE = 'feedback.db'

# Initialize the database
def init_db():
    """
    Creates necessary tables if they don't exist.
    This function runs at the start of the application.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            faculty_name TEXT NOT NULL,
            student_name TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback for a course and faculty.
    Expects JSON payload with course_name, faculty_name, student_name, and feedback.
    """
    try:
        # Extract data from the request
        data = request.json
        course_name = data.get('course_name')
        faculty_name = data.get('faculty_name')
        student_name = data.get('student_name')
        feedback = data.get('feedback')

        # Validate input data
        if not all([course_name, faculty_name, student_name, feedback]):
            return jsonify({"error": "All fields are required"}), 400

        # Insert feedback into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (course_name, faculty_name, student_name, feedback)
            VALUES (?, ?, ?, ?)
        ''', (course_name, faculty_name, student_name, feedback))
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        # Handle unexpected error gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/view-feedback', methods=['GET'])
def view_feedback():
    """
    Endpoint to view all feedback in the system.
    Returns a list of feedback as JSON.
    """
    try:
        # Connect to the database and retrieve feedback
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, course_name, faculty_name, student_name, feedback FROM feedback')
        feedback_list = cursor.fetchall()
        conn.close()

        # Structure the feedback for JSON response
        feedback_data = [
            {
                "id": row[0],
                "course_name": row[1],
                "faculty_name": row[2],
                "student_name": row[3],
                "feedback": row[4]
            }
            for row in feedback_list
        ]

        return jsonify(feedback_data), 200
    except Exception as e:
        # Handle unexpected error gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    """
    Basic home endpoint to confirm the server is running.
    """
    return jsonify({"message": "Welcome to the MIMSR Student Feedback System API!"})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- **Dependencies**: Install Flask and SQLite3 (`pip install flask`) before running the application.
- **Database Initialization**: Ensure the `feedback.db` file is created in the same directory as the app upon running.
- **Production Considerations**: Remove `debug=True` in production and consider configuring a better database (e.g., PostgreSQL/MySQL).
