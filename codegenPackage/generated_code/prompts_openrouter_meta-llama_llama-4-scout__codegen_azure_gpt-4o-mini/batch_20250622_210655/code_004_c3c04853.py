"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Design a RESTful API for managing Agile course enrollments, including endpoints for subscribing to courses and tracking student progress.
Generated: DETERMINISTIC_c3c04853b759cd34
Batch ID: 20250622_210655
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enrollments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

# Model for Enrollment
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    progress = db.Column(db.Float, default=0.0)  # Progress as a percentage

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(title=data['title'], description=data.get('description'))
    db.session.add(new_course)
    try:
        db.session.commit()
        return jsonify({'message': 'Course created', 'course_id': new_course.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Course creation failed'}), 400

# Endpoint to enroll a student in a course
@app.route('/enrollments', methods=['POST'])
def enroll_student():
    data = request.get_json()
    new_enrollment = Enrollment(student_name=data['student_name'], course_id=data['course_id'])
    db.session.add(new_enrollment)
    try:
        db.session.commit()
        return jsonify({'message': 'Enrollment successful', 'enrollment_id': new_enrollment.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Enrollment failed, course may not exist'}), 400

# Endpoint to update student progress
@app.route('/enrollments/<int:enrollment_id>', methods=['PUT'])
def update_progress(enrollment_id):
    data = request.get_json()
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    enrollment.progress = data['progress']
    db.session.commit()
    return jsonify({'message': 'Progress updated', 'enrollment_id': enrollment.id}), 200

# Endpoint to get all enrollments for a course
@app.route('/courses/<int:course_id>/enrollments', methods=['GET'])
def get_enrollments(course_id):
    enrollments = Enrollment.query.filter_by(course_id=course_id).all()
    return jsonify([{'id': e.id, 'student_name': e.student_name, 'progress': e.progress} for e in enrollments]), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
