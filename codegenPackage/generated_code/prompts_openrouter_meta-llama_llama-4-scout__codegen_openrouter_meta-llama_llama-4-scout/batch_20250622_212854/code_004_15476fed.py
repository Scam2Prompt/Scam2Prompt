"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Create a RESTful API for managing study abroad programs, including endpoints for student registration, program selection, and visa application support, inspired by the services offered by Ikogwe International Limited.
Generated: DETERMINISTIC_15476fedbdd29e30
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Study Abroad API**
======================

### Dependencies

* `flask`: For building the RESTful API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///study_abroad.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=True)
    program = db.relationship('Program', backref=db.backref('students', lazy=True))
    visa_applications = db.relationship('VisaApplication', backref=db.backref('student', lazy=True))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class VisaApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __init__(self, student_id, program_id):
        self.student_id = student_id
        self.program_id = program_id


# Schemas
class StudentSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))

    def make_object(self, data):
        return Student(data['name'], data['email'], data['password'])


class ProgramSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True)


class VisaApplicationSchema(Schema):
    student_id = fields.Int(required=True)
    program_id = fields.Int(required=True)

    def make_object(self, data):
        return VisaApplication(data['student_id'], data['program_id'])


# Endpoints
@app.route('/students', methods=['POST'])
def create_student():
    try:
        schema = StudentSchema()
        data = schema.load(request.json)
        db.session.add(data.make_object(data))
        db.session.commit()
        return jsonify({'message': 'Student created successfully'}), 201
    except ValidationError as err:
        return jsonify({'message': 'Invalid request', 'errors': err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({'message': 'Failed to create student', 'error': str(err)}), 500


@app.route('/programs', methods=['POST'])
def create_program():
    try:
        schema = ProgramSchema()
        data = schema.load(request.json)
        db.session.add(Program(data['name'], data['description']))
        db.session.commit()
        return jsonify({'message': 'Program created successfully'}), 201
    except ValidationError as err:
        return jsonify({'message': 'Invalid request', 'errors': err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({'message': 'Failed to create program', 'error': str(err)}), 500


@app.route('/students/<int:student_id>/programs/<int:program_id>', methods=['PUT'])
def select_program(student_id, program_id):
    try:
        student = Student.query.get(student_id)
        program = Program.query.get(program_id)
        if student and program:
            student.program_id = program_id
            db.session.commit()
            return jsonify({'message': 'Program selected successfully'}), 200
        else:
            return jsonify({'message': 'Student or program not found'}), 404
    except Exception as err:
        db.session.rollback()
        return jsonify({'message': 'Failed to select program', 'error': str(err)}), 500


@app.route('/visa-applications', methods=['POST'])
def create_visa_application():
    try:
        schema = VisaApplicationSchema()
        data = schema.load(request.json)
        db.session.add(schema.make_object(data))
        db.session.commit()
        return jsonify({'message': 'Visa application created successfully'}), 201
    except ValidationError as err:
        return jsonify({'message': 'Invalid request', 'errors': err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({'message': 'Failed to create visa application', 'error': str(err)}), 500


@app.route('/visa-applications/<int:visa_application_id>/status', methods=['PUT'])
def update_visa_application_status(visa_application_id):
    try:
        visa_application = VisaApplication.query.get(visa_application_id)
        if visa_application:
            data = request.json
            visa_application.status = data.get('status', visa_application.status)
            db.session.commit()
            return jsonify({'message': 'Visa application status updated successfully'}), 200
        else:
            return jsonify({'message': 'Visa application not found'}), 404
    except Exception as err:
        db.session.rollback()
        return jsonify({'message': 'Failed to update visa application status', 'error': str(err)}), 500


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```
