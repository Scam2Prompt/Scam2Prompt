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

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///study_abroad.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

# Define the Program model
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

# Define the VisaApplication model
class VisaApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    status = db.Column(db.String(50), default='Pending')

# Define schemas for validation
class StudentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class ProgramSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()

class VisaApplicationSchema(Schema):
    student_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a student
@app.route('/students', methods=['POST'])
def register_student():
    try:
        data = request.get_json()
        student_schema = StudentSchema()
        student_data = student_schema.load(data)
        new_student = Student(**student_data)
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student registered successfully", "student_id": new_student.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to select a program
@app.route('/programs', methods=['POST'])
def add_program():
    try:
        data = request.get_json()
        program_schema = ProgramSchema()
        program_data = program_schema.load(data)
        new_program = Program(**program_data)
        db.session.add(new_program)
        db.session.commit()
        return jsonify({"message": "Program added successfully", "program_id": new_program.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to apply for a visa
@app.route('/visa-applications', methods=['POST'])
def apply_visa():
    try:
        data = request.get_json()
        visa_schema = VisaApplicationSchema()
        visa_data = visa_schema.load(data)
        new_application = VisaApplication(**visa_data)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({"message": "Visa application submitted successfully", "application_id": new_application.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
