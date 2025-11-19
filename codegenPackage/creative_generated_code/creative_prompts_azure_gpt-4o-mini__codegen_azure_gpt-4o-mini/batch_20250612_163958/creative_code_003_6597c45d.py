"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Provide an example of a web application that could manage student admissions for a school with facilities like those at Happy Boarding School.
Generated: DETERMINISTIC_6597c45dc69d4f35
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    admission_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Route to render the admission form
@app.route('/')
def index():
    return render_template('admission_form.html')

# Route to handle form submission
@app.route('/admit', methods=['POST'])
def admit_student():
    try:
        name = request.form['name']
        age = int(request.form['age'])
        grade = request.form['grade']

        # Validation
        if age < 5 or age > 18:
            return jsonify({'error': 'Age must be between 5 and 18.'}), 400

        # Create new student record
        new_student = Student(name=name, age=age, grade=grade)
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'Student admitted successfully!', 'student_id': new_student.id}), 201

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        # Log the error in a real application
        return jsonify({'error': 'An error occurred while admitting the student.'}), 500

# Route to get all admitted students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([{'id': student.id, 'name': student.name, 'age': student.age, 'grade': student.grade,
                         'admission_date': student.admission_date.strftime('%Y-%m-%d')} for student in students]), 200
    except Exception as e:
        # Log the error in a real application
        return jsonify({'error': 'An error occurred while fetching students.'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

**admission_form.html** (Template file):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Admission Form</title>
</head>
<body>
    <h1>Student Admission Form</h1>
    <form action="/admit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required>
        <br>
        <label for="grade">Grade:</label>
        <input type="text" id="grade" name="grade" required>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
``` 

**Note:** Ensure Flask and Flask-SQLAlchemy are installed in your environment. You can do this by running:
```bash
pip install Flask Flask-SQLAlchemy
```
