"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Develop a dashboard using Python and Flask to track the progress of students in Debridge Advisory's sales training programs, segmented by industry type.
Generated: DETERMINISTIC_d843d9be3d8e3880
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database connection setup
DATABASE = 'student_progress.db'


def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
    return conn


def initialize_database():
    """Initialize the database with required tables if they don't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            industry TEXT NOT NULL,
            completion_percentage INTEGER NOT NULL CHECK (completion_percentage BETWEEN 0 AND 100),
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


# Initialize the database on application start
initialize_database()


@app.route('/')
def dashboard():
    """
    Render the main dashboard page, displaying student progress segmented by industry.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT industry, name, completion_percentage, last_updated 
        FROM students 
        ORDER BY industry, name
    ''')
    students = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', students=students)


@app.route('/add_student', methods=['POST'])
def add_student():
    """
    Add a new student to the database.
    Expects JSON data: { "name": "John Doe", "industry": "Finance", "completion_percentage": 45 }
    """
    try:
        data = request.json
        name = data.get('name')
        industry = data.get('industry')
        completion_percentage = data.get('completion_percentage')

        if not name or not industry or completion_percentage is None:
            return jsonify({"error": "Invalid input"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, industry, completion_percentage) 
            VALUES (?, ?, ?)
        ''', (name, industry, completion_percentage))
        conn.commit()
        conn.close()

        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/update_progress/<int:student_id>', methods=['PUT'])
def update_progress(student_id):
    """
    Update the completion percentage for a specific student.
    Expects JSON data: { "completion_percentage": 80 }
    """
    try:
        data = request.json
        completion_percentage = data.get('completion_percentage')

        if completion_percentage is None or not (0 <= completion_percentage <= 100):
            return jsonify({"error": "Invalid completion percentage"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students
            SET completion_percentage = ?, last_updated = ?
            WHERE id = ?
        ''', (completion_percentage, datetime.now(), student_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Progress updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student from the database.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_students_by_industry/<industry>', methods=['GET'])
def get_students_by_industry(industry):
    """
    Retrieve students filtered by industry.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT name, completion_percentage, last_updated 
            FROM students 
            WHERE industry = ?
            ORDER BY name
        ''', (industry,))
        students = cursor.fetchall()
        conn.close()

        if not students:
            return jsonify({"message": "No students found for the specified industry"}), 404

        return jsonify([dict(student) for student in students]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

--- 

### `dashboard.html` Template:
Below is an example template for rendering the dashboard.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Progress Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Student Progress Dashboard</h1>
        <table class="table table-striped mt-4">
            <thead>
                <tr>
                    <th>Industry</th>
                    <th>Name</th>
                    <th>Completion Percentage</th>
                    <th>Last Updated</th>
                </tr>
            </thead>
            <tbody>
                {% for student in students %}
                <tr>
                    <td>{{ student['industry'] }}</td>
                    <td>{{ student['name'] }}</td>
                    <td>{{ student['completion_percentage'] }}%</td>
                    <td>{{ student['last_updated'] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```
