"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ujimasters.com
Prompt: Create a REST API endpoint that provides details about the Uji Masters dental science programs, including the faculty information and course structure for 2024-2026.
Generated: DETERMINISTIC_3aa45f49fad1db6f
Batch ID: 20250612_164214
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

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uji_masters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Faculty model
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(200), nullable=True)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

# Define the Program schema for serialization
class ProgramSchema(Schema):
    faculty = fields.List(fields.Nested(lambda: FacultySchema()))
    courses = fields.List(fields.Nested(lambda: CourseSchema()))

class FacultySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    title = fields.Str()
    expertise = fields.Str()

class CourseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    credits = fields.Int()

# Endpoint to get Uji Masters dental science program details
@app.route('/api/programs/uji_masters', methods=['GET'])
def get_program_details():
    try:
        # Fetch faculty and courses related to the Masters program
        faculties = Faculty.query.all()
        courses = Course.query.all()

        # Serialize the data
        faculty_schema = FacultySchema(many=True)
        course_schema = CourseSchema(many=True)

        program_details = {
            'faculty': faculty_schema.dump(faculties),
            'courses': course_schema.dump(courses),
            'duration': '2024-2026'
        }

        return jsonify(program_details), 200

    except Exception as e:
        # Return error response in case of any failure
        return jsonify({'error': str(e)}), 500

# Initialize the database and create tables if they do not exist
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
