"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Create a REST API for managing Agile courses that includes endpoints for user enrollment and course completion tracking, similar to the services provided by CrestAgile.
Generated: DETERMINISTIC_e5e9891436a89b6d
Batch ID: 20250612_162051
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agile_courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

# Define the Enrollment model
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course"""
    try:
        data = request.get_json()
        new_course = Course(title=data['title'], description=data.get('description'))
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created', 'course_id': new_course.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Course title must be unique'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses/<int:course_id>/enroll', methods=['POST'])
def enroll_user(course_id):
    """Enroll a user in a course"""
    try:
        data = request.get_json()
        new_enrollment = Enrollment(user_email=data['user_email'], course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        return jsonify({'message': 'User enrolled', 'enrollment_id': new_enrollment.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already enrolled in this course'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses/<int:course_id>/completion', methods=['PUT'])
def mark_completion(course_id):
    """Mark a user's enrollment as complete"""
    try:
        data = request.get_json()
        enrollment = Enrollment.query.filter_by(course_id=course_id, user_email=data['user_email']).first()
        if not enrollment:
            return jsonify({'error': 'Enrollment not found'}), 404
        enrollment.completed = True
        db.session.commit()
        return jsonify({'message': 'Course completion marked'}), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error while marking completion'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses/<int:course_id>/enrollments', methods=['GET'])
def list_enrollments(course_id):
    """List all enrollments for a specific course"""
    try:
        enrollments = Enrollment.query.filter_by(course_id=course_id).all()
        return jsonify([{'user_email': enrollment.user_email, 'completed': enrollment.completed} for enrollment in enrollments]), 200
    except SQLAlchemyError:
        return jsonify({'error': 'Database error while retrieving enrollments'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
