"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Write a code snippet for a web application that allows students to register for courses at a technical institute, incorporating features mentioned on the Trentino website.
Generated: DETERMINISTIC_22c6a4671e04afeb
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'students_courses.db'

def create_tables():
    """Create tables for students and courses if they do not exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)
    conn.commit()
    conn.close()

create_tables()

# Routes
@app.route('/register_student', methods=['POST'])
def register_student():
    """
    Registers a new student in the database.
    Expected JSON input: { "name": "Student Name", "email": "student@example.com" }
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "Student registered successfully."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists."}), 400
    except KeyError:
        return jsonify({"error": "Invalid input. 'name' and 'email' are required."}), 400

@app.route('/add_course', methods=['POST'])
def add_course():
    """
    Adds a new course to the database.
    Expected JSON input: { "name": "Course Name", "description": "Course Description" }
    """
    try:
        data = request.json
        name = data['name']
        description = data['description']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        conn.close()

        return jsonify({"message": "Course added successfully."}), 201
    except KeyError:
        return jsonify({"error": "Invalid input. 'name' and 'description' are required."}), 400

@app.route('/register_for_course', methods=['POST'])
def register_for_course():
    """
    Registers a student for a course.
    Expected JSON input: { "student_id": 1, "course_id": 2 }
    """
    try:
        data = request.json
        student_id = data['student_id']
        course_id = data['course_id']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registrations (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Student registered for course successfully."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Student is already registered for this course or invalid IDs provided."}), 400
    except KeyError:
        return jsonify({"error": "Invalid input. 'student_id' and 'course_id' are required."}), 400

@app.route('/courses', methods=['GET'])
def list_courses():
    """
    Lists all available courses along with their descriptions.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM courses")
    courses = cursor.fetchall()
    conn.close()

    return jsonify({"courses": [{"id": course[0], "name": course[1], "description": course[2]} for course in courses]}), 200

@app.route('/students', methods=['GET'])
def list_students():
    """
    Lists all registered students.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM students")
    students = cursor.fetchall()
    conn.close()

    return jsonify({"students": [{"id": student[0], "name": student[1], "email": student[2]} for student in students]}), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handles invalid routes with a 404 error."""
    return jsonify({"error": "Resource not found."}), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Handles server errors with a 500 error."""
    return jsonify({"error": "Internal server error."}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```
