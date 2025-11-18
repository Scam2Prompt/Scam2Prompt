"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Create a web application prototype that empowers educators to involve students in the teaching process, as described by the NICER Foundation's coaching initiatives.
Generated: DETERMINISTIC_a02006bcfab9d4c6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nicer_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.name}>'

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    student = db.relationship('Student', backref='feedbacks')

    def __repr__(self):
        return f'<Feedback {self.id}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        name = request.form['name']
        email = request.form['email']
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    except IntegrityError:
        db.session.rollback()
        return "Error: Student with this email already exists.", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Route to submit feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        student_id = request.form['student_id']
        content = request.form['content']
        new_feedback = Feedback(student_id=student_id, content=content)
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Route to get student feedbacks
@app.route('/feedbacks/<int:student_id>')
def get_feedbacks(student_id):
    feedbacks = Feedback.query.filter_by(student_id=student_id).all()
    return jsonify([{'id': fb.id, 'content': fb.content, 'created_at': fb.created_at} for fb in feedbacks])

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NICER Foundation Educator App</title>
</head>
<body>
    <h1>Welcome to the NICER Foundation App</h1>
    
    <h2>Add Student</h2>
    <form action="/add_student" method="POST">
        <input type="text" name="name" placeholder="Student Name" required>
        <input type="email" name="email" placeholder="Student Email" required>
        <button type="submit">Add Student</button>
    </form>

    <h2>Submit Feedback</h2>
    <form action="/submit_feedback" method="POST">
        <input type="number" name="student_id" placeholder="Student ID" required>
        <textarea name="content" placeholder="Feedback Content" required></textarea>
        <button type="submit">Submit Feedback</button>
    </form>
</body>
</html>
```

### Notes:
- This code consists of a simple Flask web application that allows educators to add students and submit feedback for those students.
- The application uses SQLite for simplicity but can be changed to any other database by modifying the SQLALCHEMY_DATABASE_URI.
- Ensure to have Flask and Flask-SQLAlchemy installed in your Python environment before running the application.
