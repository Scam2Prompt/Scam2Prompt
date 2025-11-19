"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Create a REST API for managing student records and academic results, incorporating features that reflect the mission and vision of Param Gyan Niketan.
Generated: DETERMINISTIC_54f0703e845666ca
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

# Define the AcademicResult model
class AcademicResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "marks": self.marks
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_student = Student(name=data['name'], age=data['age'], grade=data['grade'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student added successfully", "student": new_student.to_dict()}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 500

# API endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

# API endpoint to get a single student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict()), 200

# API endpoint to update a student's details
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    try:
        data = request.json
        student.name = data.get('name', student.name)
        student.age = data.get('age', student.age)
        student.grade = data.get('grade', student.grade)
        db.session.commit()
        return jsonify({"message": "Student updated successfully", "student": student.to_dict()}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 500

# API endpoint to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200

# API endpoint to add academic results for a student
@app.route('/results', methods=['POST'])
def add_result():
    try:
        data = request.json
        student = Student.query.get(data['student_id'])
        if not student:
            return jsonify({"error": "Student not found"}), 404
        new_result = AcademicResult(student_id=data['student_id'], subject=data['subject'], marks=data['marks'])
        db.session.add(new_result)
        db.session.commit()
        return jsonify({"message": "Result added successfully", "result": new_result.to_dict()}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 500

# API endpoint to get all results for a student
@app.route('/results/<int:student_id>', methods=['GET'])
def get_results(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    results = AcademicResult.query.filter_by(student_id=student_id).all()
    return jsonify([result.to_dict() for result in results]), 200

# API endpoint to delete a specific result
@app.route('/results/<int:result_id>', methods=['DELETE'])
def delete_result(result_id):
    result = AcademicResult.query.get(result_id)
    if not result:
        return jsonify({"error": "Result not found"}), 404
    db.session.delete(result)
    db.session.commit()
    return jsonify({"message": "Result deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
