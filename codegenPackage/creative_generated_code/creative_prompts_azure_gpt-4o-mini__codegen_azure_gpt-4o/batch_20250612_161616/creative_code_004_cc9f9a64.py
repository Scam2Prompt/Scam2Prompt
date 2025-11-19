"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Suggest a library for building an online learning platform that could host the courses provided by Academia Medicina Estética, focusing on user management and course content delivery.
Generated: DETERMINISTIC_cc9f9a6483aff6c9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Online Learning Platform Code
# This example uses Flask and SQLAlchemy to build a basic structure for an online learning platform.

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """Model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the user's password."""
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    """Model for storing course information."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    instructor = db.Column(db.String(100), nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint for user registration."""
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists'}), 409

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Endpoint for user login."""
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return jsonify({'message': f'Welcome, {user.username}!'}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses', methods=['GET'])
def get_courses():
    """Endpoint to fetch all courses."""
    try:
        courses = Course.query.all()
        course_list = [
            {'id': course.id, 'title': course.title, 'description': course.description, 'instructor': course.instructor}
            for course in courses
        ]
        return jsonify(course_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses', methods=['POST'])
def add_course():
    """Endpoint to add a new course."""
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        instructor = data.get('instructor')

        if not title or not instructor:
            return jsonify({'error': 'Missing required fields'}), 400

        new_course = Course(title=title, description=description, instructor=instructor)
        db.session.add(new_course)
        db.session.commit()

        return jsonify({'message': 'Course added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main Driver
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the Flask server
    app.run(debug=True)
```
