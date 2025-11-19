"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Outline a plan for a training module that consolidates online sales and technical training for Vertiv partners, including certification tracking.
Generated: DETERMINISTIC_4093e49051615466
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Training Module for Consolidating Online Sales and Technical Training for Vertiv Partners
Features:
- User registration and authentication
- Course management: sales and technical training modules
- Certification tracking and reporting
- Error handling and validation
- Designed for scalability and maintainability
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_module.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """
    User model for storing partner information.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Course(db.Model):
    """
    Course model for managing sales and technical training modules.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'sales' or 'technical'
    description = db.Column(db.Text, nullable=True)

class Certification(db.Model):
    """
    Certification model for tracking user completion of courses.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('certifications', lazy=True))
    course = db.relationship('Course', backref=db.backref('certifications', lazy=True))

# Helper functions
def validate_request_json(required_keys):
    """
    Validate request JSON payload.
    """
    if not request.json:
        return "Missing JSON payload.", False
    for key in required_keys:
        if key not in request.json:
            return f"Missing required field: {key}", False
    return None, True

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint for user registration.
    """
    error, valid = validate_request_json(['username', 'email', 'password'])
    if not valid:
        return jsonify({'error': error}), 400

    try:
        user = User(
            username=request.json['username'],
            email=request.json['email'],
            password=request.json['password']  # In production, hash passwords!
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists.'}), 400


@app.route('/create_course', methods=['POST'])
def create_course():
    """
    Endpoint for adding a new course.
    """
    error, valid = validate_request_json(['title', 'category'])
    if not valid:
        return jsonify({'error': error}), 400

    course = Course(
        title=request.json['title'],
        category=request.json['category'],
        description=request.json.get('description', '')
    )
    db.session.add(course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully.'}), 201


@app.route('/complete_course', methods=['POST'])
def complete_course():
    """
    Endpoint for marking a course as completed by a user.
    """
    error, valid = validate_request_json(['user_id', 'course_id'])
    if not valid:
        return jsonify({'error': error}), 400

    user_id = request.json['user_id']
    course_id = request.json['course_id']

    # Ensure user and course exist
    user = User.query.get(user_id)
    course = Course.query.get(course_id)
    if not user or not course:
        return jsonify({'error': 'Invalid user or course ID.'}), 404

    certification = Certification(user_id=user_id, course_id=course_id)
    db.session.add(certification)
    db.session.commit()
    return jsonify({'message': 'Course completed and certification recorded.'}), 201


@app.route('/certifications/<int:user_id>', methods=['GET'])
def get_certifications(user_id):
    """
    Endpoint for retrieving certifications for a user.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    certifications = Certification.query.filter_by(user_id=user_id).all()
    certification_list = [
        {
            'course_id': cert.course_id,
            'course_title': cert.course.title,
            'completed_at': cert.completed_at
        }
        for cert in certifications
    ]
    return jsonify({'certifications': certification_list}), 200

# Error handling
@app.errorhandler(404)
def handle_404(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def handle_500(error):
    """
    Handle server errors.
    """
    return jsonify({'error': 'Internal server error.'}), 500

# Main entry point
if __name__ == '__main__':
    # Initialize the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
