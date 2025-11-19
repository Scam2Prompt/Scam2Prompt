"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Create an API endpoint for a virtual training platform that allows users to enroll in courses focused on personal and organizational change, as highlighted by Virtual5.
Generated: DETERMINISTIC_92194a17179dd69d
Batch ID: 20250612_163423
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)

# Model for Enrollments
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    course = db.relationship('Course', backref='enrollments')

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/enroll', methods=['POST'])
def enroll_in_course():
    """
    Enroll a user in a specified course.

    Request JSON should include:
    - email (str): The user's email address.
    - course_title (str): The title of the course to enroll in.
    
    Returns:
    - JSON response indicating success or failure.
    """
    try:
        # Get data from request
        data = request.get_json()
        user_email = data.get('email')
        course_title = data.get('course_title')

        # Validate input
        if not user_email or not course_title:
            return jsonify({'error': 'Email and course title are required.'}), 400

        # Find the course
        course = Course.query.filter_by(title=course_title).first()
        if not course:
            return jsonify({'error': 'Course not found.'}), 404

        # Create a new enrollment
        new_enrollment = Enrollment(user_email=user_email, course_id=course.id)
        db.session.add(new_enrollment)
        db.session.commit()

        return jsonify({'message': 'Successfully enrolled in course.', 'course': course_title}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User is already enrolled in this course.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
