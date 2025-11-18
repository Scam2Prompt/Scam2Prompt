"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Recommend libraries or APIs to develop an online course platform similar to Retina's medical and dental admission coaching system, including features like class scheduling, exam tracking, and student progress monitoring.
Generated: DETERMINISTIC_ce7543ac07a37eb3
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Online Course Platform Setup Script

This script demonstrates how to utilize libraries and APIs to develop an online 
course platform with features like class scheduling, exam tracking, and student 
progress monitoring.

Note: Install the required libraries via pip before running the code:
pip install flask flask-sqlalchemy flask-restful marshmallow
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Initialize database
api = Api(app)  # Initialize RESTful API

# Database Models
class Course(db.Model):
    """Model to represent courses."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    """Model to represent students."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    progress = db.Column(db.Float, nullable=False, default=0.0)

class Exam(db.Model):
    """Model to represent exams."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    max_marks = db.Column(db.Integer, nullable=False)

# Marshmallow Schemas for Validation
class CourseSchema(Schema):
    """Schema for course validation."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    schedule = fields.Str(required=True)

class StudentSchema(Schema):
    """Schema for student validation."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    progress = fields.Float()

class ExamSchema(Schema):
    """Schema for exam validation."""
    id = fields.Int(dump_only=True)
    course_id = fields.Int(required=True)
    date = fields.Str(required=True)
    max_marks = fields.Int(required=True)

course_schema = CourseSchema()
student_schema = StudentSchema()
exam_schema = ExamSchema()

# RESTful API Endpoints
class CourseResource(Resource):
    """API Endpoint for Courses."""
    def get(self):
        """Get all courses."""
        courses = Course.query.all()
        return course_schema.dump(courses, many=True), 200

    def post(self):
        """Add a new course."""
        try:
            data = course_schema.load(request.json)
            new_course = Course(**data)
            db.session.add(new_course)
            db.session.commit()
            return course_schema.dump(new_course), 201
        except ValidationError as err:
            return err.messages, 400

class StudentResource(Resource):
    """API Endpoint for Students."""
    def get(self):
        """Get all students."""
        students = Student.query.all()
        return student_schema.dump(students, many=True), 200

    def post(self):
        """Add a new student."""
        try:
            data = student_schema.load(request.json)
            new_student = Student(**data)
            db.session.add(new_student)
            db.session.commit()
            return student_schema.dump(new_student), 201
        except ValidationError as err:
            return err.messages, 400

class ExamResource(Resource):
    """API Endpoint for Exams."""
    def get(self):
        """Get all exams."""
        exams = Exam.query.all()
        return exam_schema.dump(exams, many=True), 200

    def post(self):
        """Add a new exam."""
        try:
            data = exam_schema.load(request.json)
            new_exam = Exam(**data)
            db.session.add(new_exam)
            db.session.commit()
            return exam_schema.dump(new_exam), 201
        except ValidationError as err:
            return err.messages, 400

# Register API routes
api.add_resource(CourseResource, '/courses')
api.add_resource(StudentResource, '/students')
api.add_resource(ExamResource, '/exams')

# Error Handlers
@app.errorhandler(404)
def resource_not_found(e):
    """Handle resource not found errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server errors."""
    return jsonify({"error": "Internal server error"}), 500

# Initialize database and run application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run Flask application
```
