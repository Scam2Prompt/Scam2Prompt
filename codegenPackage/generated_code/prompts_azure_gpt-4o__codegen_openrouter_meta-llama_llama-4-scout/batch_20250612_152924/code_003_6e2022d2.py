"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Create a web application prototype for a multidisciplinary university like Uni4Kashmir, integrating course offerings in fields such as Robotics, Biotechnology, and Environmental Studies.
Generated: DETERMINISTIC_6e2022d27048cb6a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**uni4kashmir_prototype**
=========================

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    field_of_study = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.field_of_study}')"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    courses = db.relationship('Course', secondary='enrollments')

    def __repr__(self):
        return f"Student('{self.name}', '{self.email}')"

class Enrollment(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

    def __repr__(self):
        return f"Enrollment('{self.student_id}', '{self.course_id}')"
```

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from models import db, Course, Student, Enrollment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uni4kashmir.db'
db.init_app(app)

@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/courses/<int:course_id>')
def course_details(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course_details.html', course=course)

@app.route('/enroll', methods=['POST'])
def enroll():
    try:
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        student = Student.query.get(student_id)
        course = Course.query.get(course_id)
        if student and course:
            enrollment = Enrollment(student_id=student_id, course_id=course_id)
            db.session.add(enrollment)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return 'Invalid student or course', 400
    except Exception as e:
        return str(e), 500

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Uni4Kashmir</title>
</head>
<body>
    <h1>Courses</h1>
    <ul>
    {% for course in courses %}
        <li>
            {{ course.name }} ({{ course.field_of_study }})
            <a href="{{ url_for('course_details', course_id=course.id) }}">View Details</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/course_details.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Course Details</title>
</head>
<body>
    <h1>{{ course.name }}</h1>
    <p>{{ course.description }}</p>
    <p>Field of Study: {{ course.field_of_study }}</p>
    <form action="{{ url_for('enroll') }}" method="post">
        <input type="hidden" name="course_id" value="{{ course.id }}">
        <input type="text" name="student_id" placeholder="Enter Student ID">
        <input type="submit" value="Enroll">
    </form>
</body>
</html>
```

**templates/students.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
</head>
<body>
    <h1>Students</h1>
    <ul>
    {% for student in students %}
        <li>
            {{ student.name }} ({{ student.email }})
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```

**run.sh**
```bash
#!/bin/bash

# Create database
flask db init
flask db migrate
flask db upgrade

# Run application
flask run
```
