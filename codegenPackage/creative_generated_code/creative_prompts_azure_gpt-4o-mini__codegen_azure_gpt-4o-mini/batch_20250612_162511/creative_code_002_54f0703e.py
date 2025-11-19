"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Create a REST API for managing student records and academic results, incorporating features that reflect the mission and vision of Param Gyan Niketan.
Generated: DETERMINISTIC_54f0703e845666ca
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the student records
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    results = db.relationship('Result', backref='student', lazy=True)

# Define a model for the academic results
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# Student Schema for input validation and serialization
class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    grade = fields.Str(required=True)

# Result Schema for input validation and serialization
class ResultSchema(Schema):
    id = fields.Int(dump_only=True)
    subject = fields.Str(required=True)
    score = fields.Float(required=True)
    student_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        student_schema = StudentSchema()
        student = student_schema.load(data)  # Validate input
        new_student = Student(**student)
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_schema = StudentSchema(many=True)
    return student_schema.dump(students), 200

# Route to get a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    student_schema = StudentSchema()
    return student_schema.dump(student), 200

# Route to update a student record
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.get_json()
        student = Student.query.get_or_404(id)
        student_schema = StudentSchema()
        updated_data = student_schema.load(data)  # Validate input
        for key, value in updated_data.items():
            setattr(student, key, value)
        db.session.commit()
        return student_schema.dump(student), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a student record
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 204

# Route to add academic results
@app.route('/results', methods=['POST'])
def add_result():
    try:
        data = request.get_json()
        result_schema = ResultSchema()
        result = result_schema.load(data)  # Validate input
        new_result = Result(**result)
        db.session.add(new_result)
        db.session.commit()
        return result_schema.dump(new_result), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get results for a specific student
@app.route('/students/<int:student_id>/results', methods=['GET'])
def get_results(student_id):
    results = Result.query.filter_by(student_id=student_id).all()
    result_schema = ResultSchema(many=True)
    return result_schema.dump(results), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
