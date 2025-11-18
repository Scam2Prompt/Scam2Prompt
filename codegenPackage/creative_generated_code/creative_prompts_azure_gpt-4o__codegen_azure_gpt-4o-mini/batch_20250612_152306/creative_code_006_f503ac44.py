"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write code to implement an online registration system for vocational courses, including validation for fields like course type, duration, and student details.
Generated: DETERMINISTIC_f503ac4465baaa28
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError, validates
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Course Registration
class CourseRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    course_type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(50), nullable=False)

# Schema for input validation
class CourseRegistrationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    course_type = fields.Str(required=True)
    duration = fields.Str(required=True)

    @validates('course_type')
    def validate_course_type(self, value):
        if value not in ['Full-time', 'Part-time', 'Online']:
            raise ValidationError('Invalid course type. Choose from Full-time, Part-time, or Online.')

    @validates('duration')
    def validate_duration(self, value):
        if not re.match(r'^\d+\s+(days|weeks|months)$', value):
            raise ValidationError('Duration must be in the format of "<number> <days|weeks|months>".')

# Endpoint to register courses
@app.route('/register', methods=['POST'])
def register_course():
    json_data = request.get_json()
    
    # Validate and deserialize input
    try:
        course_registration_schema = CourseRegistrationSchema()
        validated_data = course_registration_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return 400 for validation errors

    # Check for existing registration
    existing_registration = CourseRegistration.query.filter_by(email=validated_data['email']).first()
    if existing_registration:
        return jsonify({'error': 'Email already registered.'}), 409  # Conflict error

    # Create new course registration
    new_registration = CourseRegistration(
        name=validated_data['name'],
        email=validated_data['email'],
        course_type=validated_data['course_type'],
        duration=validated_data['duration']
    )

    # Add to database
    try:
        db.session.add(new_registration)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while registering the course.'}), 500  # Internal server error

    return jsonify({'message': 'Course registered successfully!'}), 201  # Created

# Run database migrations
@app.before_first_request
def create_tables():
    db.create_all()

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
