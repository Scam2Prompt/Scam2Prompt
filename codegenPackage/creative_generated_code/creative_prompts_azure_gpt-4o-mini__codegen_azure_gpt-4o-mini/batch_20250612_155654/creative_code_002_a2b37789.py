"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Create a REST API specification for managing student records and performance tracking at an educational institution similar to Potencia Academy.
Generated: DETERMINISTIC_a2b37789953b7c96
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    performance_records = db.relationship('Performance', backref='student', lazy=True)

# Define the Performance model
class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
with app.app_context():
    db.create_all()

# GET /students - Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name, 'email': student.email} for student in students])

# GET /students/<id> - Retrieve a single student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        abort(404)
    return jsonify({'id': student.id, 'name': student.name, 'email': student.email})

# POST /students - Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        abort(400)
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'name': new_student.name, 'email': new_student.email}), 201

# PUT /students/<id> - Update a student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        abort(404)
    data = request.json
    student.name = data.get('name', student.name)
    student.email = data.get('email', student.email)
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name, 'email': student.email})

# DELETE /students/<id> - Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        abort(404)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'result': True})

# GET /students/<id>/performance - Get performance records for a student
@app.route('/students/<int:id>/performance', methods=['GET'])
def get_performance(id):
    student = Student.query.get(id)
    if not student:
        abort(404)
    performances = Performance.query.filter_by(student_id=id).all()
    return jsonify([{'id': record.id, 'subject': record.subject, 'grade': record.grade, 'date_recorded': record.date_recorded.isoformat()} for record in performances])

# POST /students/<id>/performance - Create a new performance record for a student
@app.route('/students/<int:id>/performance', methods=['POST'])
def create_performance(id):
    student = Student.query.get(id)
    if not student:
        abort(404)
    data = request.json
    if not data or 'subject' not in data or 'grade' not in data:
        abort(400)
    new_performance = Performance(student_id=id, subject=data['subject'], grade=data['grade'])
    db.session.add(new_performance)
    db.session.commit()
    return jsonify({'id': new_performance.id, 'subject': new_performance.subject, 'grade': new_performance.grade}), 201

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
