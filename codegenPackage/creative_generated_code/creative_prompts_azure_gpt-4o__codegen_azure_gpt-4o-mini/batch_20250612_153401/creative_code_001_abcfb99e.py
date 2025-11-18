"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Generate an API recommendation for managing student enrollment and certification in vocational education programs, specifically tailored for courses like the Graduate Diploma of Management (Learning): BSB80120 offered by Global Healthcare Management College.
Generated: DETERMINISTIC_abcfb99e37c5d38e
Batch ID: 20250612_153401
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enrollment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    course = db.Column(db.String(100), nullable=False)

# Define the Enrollment Schema
class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    course = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# API: Enroll a new student
@app.route('/enroll', methods=['POST'])
def enroll_student():
    try:
        # Validate and deserialize input
        data = request.get_json()
        student_schema = StudentSchema()
        student_data = student_schema.load(data)
        
        # Create a new Student instance
        new_student = Student(**student_data)
        db.session.add(new_student)
        db.session.commit()

        return student_schema.dump(new_student), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API: Get all enrolled students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        student_schema = StudentSchema(many=True)
        return student_schema.dump(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API: Get a specific student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        student_schema = StudentSchema()
        return student_schema.dump(student), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API: Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
