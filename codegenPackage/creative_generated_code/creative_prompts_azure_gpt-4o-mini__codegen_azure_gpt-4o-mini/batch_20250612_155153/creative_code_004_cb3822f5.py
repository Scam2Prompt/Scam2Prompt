"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shriramakrishnacollege.com
Prompt: Suggest a library for building a student registration system that aligns with the goals of fostering social responsibility and all-round development at Shri Rama Krishna College of Education.
Generated: DETERMINISTIC_cb3822f52f5e1f81
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
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
    email = db.Column(db.String(100), unique=True, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Student {self.name}>'

# Define a schema for validating input data
class StudentSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Str(required=True, validate=validate.Email())
    course = fields.Str(required=True, validate=validate.Length(min=1))

# Instantiate the schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to register a new student
@app.route('/register', methods=['POST'])
def register_student():
    """Register a new student in the system."""
    try:
        # Validate and deserialize input data
        student_data = student_schema.load(request.json)
        
        # Create a new student instance
        new_student = Student(
            name=student_data['name'],
            email=student_data['email'],
            course=student_data['course']
        )
        
        # Add the new student to the session and commit
        db.session.add(new_student)
        db.session.commit()
        
        return student_schema.jsonify(new_student), 201  # Return success response
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return general error

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    """Get a list of all registered students."""
    try:
        all_students = Student.query.all()
        return students_schema.jsonify(all_students), 200  # Return success response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return general error

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```
