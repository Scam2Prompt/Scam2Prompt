"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Develop a plan for implementing a workshop or program for youth development, incorporating the principles and goals outlined on smplanka.lk, and suggest relevant tools or platforms for management.
Generated: DETERMINISTIC_81c5871d5c328830
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Youth Development Workshop Planner

This script provides a framework for planning and managing a youth development workshop or program.
It incorporates principles and goals that can be customized based on the guidelines provided on smplanka.lk.
The script includes tools for scheduling, participant management, and feedback collection.

Dependencies:
- Python 3.x
- Flask (for web-based management)
- SQLite (for database management)
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file path
DB_FILE = "workshop.db"

# Ensure the database exists
def initialize_database():
    """
    Initialize the SQLite database with necessary tables.
    """
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create participants table
        cursor.execute("""
        CREATE TABLE participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """)
        # Create schedule table
        cursor.execute("""
        CREATE TABLE schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            activity TEXT NOT NULL
        )
        """)
        # Create feedback table
        cursor.execute("""
        CREATE TABLE feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_id INTEGER NOT NULL,
            comments TEXT NOT NULL,
            FOREIGN KEY (participant_id) REFERENCES participants (id)
        )
        """)
        conn.commit()
        conn.close()

# Route: Add participant
@app.route('/add_participant', methods=['POST'])
def add_participant():
    """
    Add a new participant to the workshop.
    Expects JSON data with 'name', 'age', and 'email'.
    """
    try:
        data = request.json
        name = data['name']
        age = data['age']
        email = data['email']

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO participants (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "Participant added successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add schedule
@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    """
    Add a new activity to the workshop schedule.
    Expects JSON data with 'date', 'time', and 'activity'.
    """
    try:
        data = request.json
        date = data['date']
        time = data['time']
        activity = data['activity']

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO schedule (date, time, activity) VALUES (?, ?, ?)", (date, time, activity))
        conn.commit()
        conn.close()

        return jsonify({"message": "Schedule added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Submit feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Submit feedback for the workshop.
    Expects JSON data with 'participant_id' and 'comments'.
    """
    try:
        data = request.json
        participant_id = data['participant_id']
        comments = data['comments']

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (participant_id, comments) VALUES (?, ?)", (participant_id, comments))
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Invalid participant ID!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View participants
@app.route('/view_participants', methods=['GET'])
def view_participants():
    """
    Retrieve a list of all participants.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM participants")
        participants = cursor.fetchall()
        conn.close()

        return jsonify({"participants": participants}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View schedule
@app.route('/view_schedule', methods=['GET'])
def view_schedule():
    """
    Retrieve the workshop schedule.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM schedule")
        schedule = cursor.fetchall()
        conn.close()

        return jsonify({"schedule": schedule}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View feedback
@app.route('/view_feedback', methods=['GET'])
def view_feedback():
    """
    Retrieve all feedback submitted by participants.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedback = cursor.fetchall()
        conn.close()

        return jsonify({"feedback": feedback}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Initialize the database
    initialize_database()
    # Run the Flask app
    app.run(debug=True)
```
