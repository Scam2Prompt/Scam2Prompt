"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Recommend libraries or APIs for implementing an online Islamic course platform similar to Darul Raza's Online Academy, with features for virtual classes and course management.
Generated: DETERMINISTIC_dbf0f258d5c779be
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for the application
CORS(app)

# Configuration for SQLAlchemy and Flask-Login
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Database Models
class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Course(db.Model):
    """Course model for managing course information."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ClassSession(db.Model):
    """Model for managing virtual class sessions."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    link = db.Column(db.String(255), nullable=False)

# API Endpoints
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Retrieve a list of all courses."""
    try:
        courses = Course.query.all()
        return jsonify([{'id': course.id, 'title': course.title, 'description': course.description} for course in courses]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/courses', methods=['POST'])
def add_course():
    """Add a new course."""
    try:
        data = request.json
        new_course = Course(title=data['title'], description=data['description'], instructor_id=data['instructor_id'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully.', 'course_id': new_course.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/classes', methods=['POST'])
def add_class_session():
    """Add a new class session for a specific course."""
    try:
        data = request.json
        new_session = ClassSession(course_id=data['course_id'], date_time=data['date_time'], link=data['link'])
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Class session created successfully.', 'session_id': new_session.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

This code sets up a minimal Flask application for an online Islamic course platform with user and course management. It includes endpoints for retrieving and adding courses and sessions, structured for maintainability and error handling.
