"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Develop a system for scheduling translation courses offered by Parrotrans, including user registration and course management functionalities.
Generated: DETERMINISTIC_373975657ea67e8c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parrotrans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model for registration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Define the Course model for course management
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    schedule_date = db.Column(db.DateTime, nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    
    # Validate input data
    if not data or not 'username' in data or not 'email' in data or not 'password' in data:
        abort(400, 'Missing user registration data.')

    # Check for existing user
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        abort(400, 'Username or email already exists.')

    # Create new user
    new_user = User(username=data['username'], email=data['email'], password=data['password'])  # Note: Password should be hashed in production
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Course creation endpoint
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    
    # Validate input data
    if not data or not 'title' in data or not 'schedule_date' in data:
        abort(400, 'Missing course data.')

    try:
        schedule_date = datetime.fromisoformat(data['schedule_date'])
    except ValueError:
        abort(400, 'Invalid date format. Use ISO format.')

    # Create new course
    new_course = Course(title=data['title'], description=data.get('description'), schedule_date=schedule_date)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'message': 'Course created successfully'}), 201

# Get all courses endpoint
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'title': course.title, 'description': course.description, 'schedule_date': course.schedule_date.isoformat()} for course in courses]), 200

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Main execution
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', default=False))
```
