"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create an API recommendation for managing course registrations and student notes for the programs offered at IESTP PANGOA.
Generated: DETERMINISTIC_6516d875597fcae2
Batch ID: 20250612_161435
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iestp_pangoa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    registrations = db.relationship('Registration', backref='course', lazy=True)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='student', lazy=True)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Define the Note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Schema for Course
class CourseSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)

# Schema for Student
class StudentSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)

# Schema for Registration
class RegistrationSchema(Schema):
    id = fields.Int()
    student_id = fields.Int(required=True)
    course_id = fields.Int(required=True)

# Schema for Note
class NoteSchema(Schema):
    id = fields.Int()
    student_id = fields.Int(required=True)
    content = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    try:
        course = CourseSchema().load(data)
        new_course = Course(**course)
        db.session.add(new_course)
        db.session.commit()
        return jsonify(CourseSchema().dump(new_course)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to register a student for a course
@app.route('/registrations', methods=['POST'])
def register_student():
    data = request.get_json()
    try:
        registration = RegistrationSchema().load(data)
        new_registration = Registration(**registration)
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(RegistrationSchema().dump(new_registration)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to create a note for a student
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    try:
        note = NoteSchema().load(data)
        new_note = Note(**note)
        db.session.add(new_note)
        db.session.commit()
        return jsonify(NoteSchema().dump(new_note)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify(CourseSchema(many=True).dump(courses)), 200

# API endpoint to get all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    registrations = Registration.query.all()
    return jsonify(RegistrationSchema(many=True).dump(registrations)), 200

# API endpoint to get all notes for a student
@app.route('/notes/<int:student_id>', methods=['GET'])
def get_student_notes(student_id):
    notes = Note.query.filter_by(student_id=student_id).all()
    return jsonify(NoteSchema(many=True).dump(notes)), 200

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
