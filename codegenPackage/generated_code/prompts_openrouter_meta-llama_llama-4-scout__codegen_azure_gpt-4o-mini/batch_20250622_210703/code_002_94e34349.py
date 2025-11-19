"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Design a simple system to track student attendance and daily meals for a preschool, including a basic data model and potential API endpoints.
Generated: DETERMINISTIC_94e3434992e909fe
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///preschool.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attendance_records = db.relationship('Attendance', backref='student', lazy=True)

# Define the Attendance model
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    meals = db.Column(db.String(200), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    try:
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to record attendance and meals for a student
@app.route('/attendance', methods=['POST'])
def record_attendance():
    data = request.get_json()
    try:
        student_id = data['student_id']
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        meals = data['meals']
        
        attendance_record = Attendance(student_id=student_id, date=date, meals=meals)
        db.session.add(attendance_record)
        db.session.commit()
        return jsonify({'message': 'Attendance recorded successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to get attendance records for a specific student
@app.route('/attendance/<int:student_id>', methods=['GET'])
def get_attendance(student_id):
    try:
        records = Attendance.query.filter_by(student_id=student_id).all()
        return jsonify([{'date': record.date.isoformat(), 'meals': record.meals} for record in records]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
