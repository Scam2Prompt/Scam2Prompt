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
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Course(db.Model):
    """Model for Course entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    students = db.relationship('Student', backref='course', lazy=True)


class Student(db.Model):
    """Model for Student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


@app.route('/')
def index():
    """Render the index page with available courses."""
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@app.route('/register', methods=['POST'])
def register_student():
    """Register a student for a course."""
    data = request.json
    if not data or 'name' not in data or 'email' not in data or 'course_id' not in data:
        return jsonify({'error': 'Bad Request: Missing fields'}), 400

    new_student = Student(name=data['name'], email=data['email'], course_id=data['course_id'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Conflict: Student already registered or invalid course'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Internal Server Error: {str(e)}'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Registration</title>
</head>
<body>
    <h1>Course Registration</h1>
    <h2>Available Courses</h2>
    <ul>
        {% for course in courses %}
        <li>{{ course.name }} <button onclick="register('{{ course.id }}')">Register</button></li>
        {% endfor %}
    </ul>

    <h2>Register a Student</h2>
    <form id="registrationForm">
        <input type="text" id="studentName" placeholder="Student Name" required>
        <input type="email" id="studentEmail" placeholder="Student Email" required>
        <select id="courseSelect" required>
            <option value="">Select Course</option>
            {% for course in courses %}
            <option value="{{ course.id }}">{{ course.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Register</button>
    </form>

    <script>
        document.getElementById('registrationForm').onsubmit = async function(e) {
            e.preventDefault();
            const name = document.getElementById('studentName').value;
            const email = document.getElementById('studentEmail').value;
            const courseId = document.getElementById('courseSelect').value;

            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, email, course_id: courseId })
            });

            const result = await response.json();
            alert(result.message || result.error);  // Display success or error message
        };
    </script>
</body>
</html>
```
