"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Design a RESTful API for a school information system, including endpoints for managing student admissions, curriculum, and exam schedules, inspired by the features of জি. কে. মাধ্যমিক বিদ্যালয়'s website.
Generated: DETERMINISTIC_a537d18f000a0f0e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

# Define the Curriculum model
class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)

# Define the ExamSchedule model
class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    exam_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

# Schemas for serialization
class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    grade = fields.Str(required=True)

class CurriculumSchema(Schema):
    id = fields.Int(dump_only=True)
    subject = fields.Str(required=True)
    grade = fields.Str(required=True)

class ExamScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    subject = fields.Str(required=True)
    exam_date = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to manage student admissions
@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student to the system."""
    try:
        student_data = request.get_json()
        student_schema = StudentSchema()
        student = student_schema.load(student_data)
        new_student = Student(**student)
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    student_schema = StudentSchema(many=True)
    return student_schema.dump(students), 200

# Endpoint to manage curriculum
@app.route('/curriculum', methods=['POST'])
def add_curriculum():
    """Add a new curriculum subject."""
    try:
        curriculum_data = request.get_json()
        curriculum_schema = CurriculumSchema()
        curriculum = curriculum_schema.load(curriculum_data)
        new_curriculum = Curriculum(**curriculum)
        db.session.add(new_curriculum)
        db.session.commit()
        return curriculum_schema.dump(new_curriculum), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/curriculum', methods=['GET'])
def get_curriculum():
    """Retrieve all curriculum subjects."""
    curriculum = Curriculum.query.all()
    curriculum_schema = CurriculumSchema(many=True)
    return curriculum_schema.dump(curriculum), 200

# Endpoint to manage exam schedules
@app.route('/exams', methods=['POST'])
def add_exam_schedule():
    """Add a new exam schedule."""
    try:
        exam_data = request.get_json()
        exam_schema = ExamScheduleSchema()
        exam = exam_schema.load(exam_data)
        new_exam = ExamSchedule(**exam)
        db.session.add(new_exam)
        db.session.commit()
        return exam_schema.dump(new_exam), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/exams', methods=['GET'])
def get_exam_schedule():
    """Retrieve all exam schedules."""
    exams = ExamSchedule.query.all()
    exam_schema = ExamScheduleSchema(many=True)
    return exam_schema.dump(exams), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
