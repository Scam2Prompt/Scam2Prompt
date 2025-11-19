"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: Create a REST API that allows users to enroll in online courses like the "Máster Universitario en Educación Bilingüe" from Unimel Educación.
Generated: DETERMINISTIC_0a6d92d718f9e813
Batch ID: 20250612_162051
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for a course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

# Database model for a user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

# Database model for enrollment
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))

# Create database tables
with app.app_context():
    db.create_all()

# Route to enroll a user in a course
@app.route('/enroll', methods=['POST'])
def enroll_user():
    try:
        # Parse JSON request data
        data = request.get_json()
        user_name = data.get('user_name')
        user_email = data.get('user_email')
        course_name = data.get('course_name')

        # Validate input
        if not user_name or not user_email or not course_name:
            return jsonify({'error': 'Missing required fields'}), 400

        # Find or create user
        user = User.query.filter_by(email=user_email).first()
        if not user:
            user = User(name=user_name, email=user_email)
            db.session.add(user)

        # Find course
        course = Course.query.filter_by(name=course_name).first()
        if not course:
            return jsonify({'error': 'Course not found'}), 404

        # Check if user is already enrolled
        existing_enrollment = Enrollment.query.filter_by(user_id=user.id, course_id=course.id).first()
        if existing_enrollment:
            return jsonify({'message': 'User is already enrolled in this course'}), 200

        # Enroll user in course
        enrollment = Enrollment(user_id=user.id, course_id=course.id)
        db.session.add(enrollment)
        db.session.commit()

        return jsonify({'message': f'User {user_name} successfully enrolled in {course_name}'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new course
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        # Parse JSON request data
        data = request.get_json()
        course_name = data.get('course_name')

        # Validate input
        if not course_name:
            return jsonify({'error': 'Course name is required'}), 400

        # Check if course already exists
        if Course.query.filter_by(name=course_name).first():
            return jsonify({'error': 'Course already exists'}), 400

        # Add new course
        course = Course(name=course_name)
        db.session.add(course)
        db.session.commit()

        return jsonify({'message': f'Course {course_name} added successfully'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all courses
@app.route('/courses', methods=['GET'])
def list_courses():
    try:
        # Fetch all courses
        courses = Course.query.all()
        course_list = [{'id': course.id, 'name': course.name} for course in courses]

        return jsonify({'courses': course_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all enrollments
@app.route('/enrollments', methods=['GET'])
def list_enrollments():
    try:
        # Fetch all enrollments
        enrollments = Enrollment.query.all()
        enrollment_list = [
            {
                'id': enrollment.id,
                'user_name': enrollment.user.name,
                'user_email': enrollment.user.email,
                'course_name': enrollment.course.name
            }
            for enrollment in enrollments
        ]

        return jsonify({'enrollments': enrollment_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
