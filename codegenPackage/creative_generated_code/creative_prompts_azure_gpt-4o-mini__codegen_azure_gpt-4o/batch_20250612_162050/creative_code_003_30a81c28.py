"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Create a web application that facilitates project-based learning activities, incorporating features from the educational practices at Heart of Jesus College.
Generated: DETERMINISTIC_30a81c28265bc6e8
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a simplified web application built using Python's Flask framework for the backend, HTML/CSS/JavaScript for the frontend, and SQLite for data persistence. The application facilitates project-based learning activities, incorporating basic features like course creation, student enrollment, and project submission. 

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Used for session management and flash messages

DATABASE = 'project_learning.db'

# Helper function to interact with the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Initialize the database with required tables
def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (course_id) REFERENCES courses (id)
    );
    ''')
    conn.commit()
    conn.close()

# Route: Home Page
@app.route('/')
def index():
    courses = query_db("SELECT * FROM courses")
    return render_template('index.html', courses=courses)

# Route: Add a new course
@app.route('/add_course', methods=['POST'])
def add_course():
    name = request.form.get('name')
    description = request.form.get('description')
    if not name:
        flash("Course name is required!", "error")
        return redirect(url_for('index'))
    query_db("INSERT INTO courses (name, description) VALUES (?, ?)", (name, description))
    flash("Course added successfully!", "success")
    return redirect(url_for('index'))

# Route: Student Enrollment
@app.route('/enroll_student', methods=['POST'])
def enroll_student():
    name = request.form.get('name')
    email = request.form.get('email')
    if not name or not email:
        flash("Both name and email are required!", "error")
        return redirect(url_for('index'))
    try:
        query_db("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        flash("Student enrolled successfully!", "success")
    except sqlite3.IntegrityError:
        flash("Email already exists!", "error")
    return redirect(url_for('index'))

# Route: Submit a Project
@app.route('/submit_project', methods=['POST'])
def submit_project():
    title = request.form.get('title')
    description = request.form.get('description')
    student_id = request.form.get('student_id')
    course_id = request.form.get('course_id')
    if not title or not student_id or not course_id:
        flash("All fields are required for project submission!", "error")
        return redirect(url_for('index'))
    query_db("INSERT INTO projects (title, description, student_id, course_id) VALUES (?, ?, ?, ?)",
             (title, description, student_id, course_id))
    flash("Project submitted successfully!", "success")
    return redirect(url_for('index'))

# Start the Flask application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project-Based Learning</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Project-Based Learning Application</h1>
        <hr>

        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}

        <!-- Add Course Form -->
        <h2>Add a New Course</h2>
        <form method="POST" action="/add_course" class="mb-4">
            <div class="mb-3">
                <label for="name" class="form-label">Course Name</label>
                <input type="text" id="name" name="name" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea id="description" name="description" class="form-control"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Add Course</button>
        </form>

        <!-- Enroll Student Form -->
        <h2>Enroll a Student</h2>
        <form method="POST" action="/enroll_student" class="mb-4">
            <div class="mb-3">
                <label for="name" class="form-label">Student Name</label>
                <input type="text" id="name" name="name" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" id="email" name="email" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Enroll Student</button>
        </form>

        <!-- Submit Project Form -->
        <h2>Submit a Project</h2>
        <form method="POST" action="/submit_project" class="mb-4">
            <div class="mb-3">
                <label for="title" class="form-label">Project Title</label>
                <input type="text" id="title" name="title" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea id="description" name="description" class="form-control"></textarea>
            </div>
            <div class="mb-3">
                <label for="student_id" class="form-label">Student ID</label>
                <input type="number" id="student_id" name="student_id" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="course_id" class="form-label">Course ID</label>
                <input type="number" id="course_id" name="course_id" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit Project</button>
        </form>

        <!-- Display Courses -->
        <h2>Available Courses</h2>
        <ul class="list-group">
            {% for course in courses %}
            <li class="list-group-item">
                <strong>{{ course.name }}</strong><br>
                {{ course.description }}
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

This code creates a basic project-based learning application with functionality for adding courses, enrolling students, and submitting projects. It uses Flask for the backend and SQLite for persistence. Ensure you install necessary dependencies (`pip install flask`) and run the `app.py` file to start the application.
