"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Generate a code snippet for a web application that allows users to enroll in aviation security courses, such as the Avsec Instructors Course and Basic Avsec Course, offered by Welwitschia Aviation.
Generated: DETERMINISTIC_0324a69e43cbb179
Batch ID: 20250612_155233
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
# File: app.py
# Description: Web application for enrolling in aviation security courses offered by Welwitschia Aviation.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure, randomly generated key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'  # Database connection (SQLite for simplicity)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Course model to represent course details in the database
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)

# Define the Enrollment model to represent user enrollments in courses
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # User's name
    email = db.Column(db.String(120), nullable=False)  # User's email
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Home route for displaying available courses
@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

# Route for handling course enrollment
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            course_id = request.form['course_id']

            # Validate form inputs
            if not name or not email or not course_id:
                flash('All fields are required!', 'error')
                return redirect(url_for('index'))

            enrollment = Enrollment(name=name, email=email, course_id=course_id)
            db.session.add(enrollment)
            db.session.commit()
            flash('Enrollment successful!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            # Handle any unexpected errors gracefully
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('index'))
    return redirect(url_for('index'))

# Initialize the database with sample data if not already present
@app.before_first_request
def setup():
    db.create_all()
    if Course.query.count() == 0:
        # Populate the database with sample courses
        sample_courses = [
            Course(name="Avsec Instructors Course", description="Learn to instruct aviation security courses."),
            Course(name="Basic Avsec Course", description="Introduction to aviation security fundamentals.")
        ]
        db.session.bulk_save_objects(sample_courses)
        db.session.commit()

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- File: templates/index.html -->
<!-- Description: Template for displaying courses and enrollment form -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welwitschia Aviation - Courses</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Aviation Security Courses</h1>
        
        <!-- Display list of available courses -->
        <div class="mb-5">
            <h2>Available Courses:</h2>
            <ul class="list-group">
                {% for course in courses %}
                    <li class="list-group-item">
                        <strong>{{ course.name }}</strong>: {{ course.description }}
                        <form action="{{ url_for('enroll') }}" method="POST" class="mt-2">
                            <input type="hidden" name="course_id" value="{{ course.id }}">
                            <div class="mb-3">
                                <input type="text" name="name" placeholder="Your Name" class="form-control" required>
                            </div>
                            <div class="mb-3">
                                <input type="email" name="email" placeholder="Your Email" class="form-control" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Enroll</button>
                        </form>
                    </li>
                {% endfor %}
            </ul>
        </div>

        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-5">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```
