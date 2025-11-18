"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Write code to build a membership area with course management features, including unlimited video hosting and user access, using InfinitiAI's tools.
Generated: DETERMINISTIC_13fa08ff33919ea4
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'  # Change this to your actual database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for managing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Course model for managing course data
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    video_url = db.Column(db.String(200), nullable=False)  # URL to the hosted video
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required.'}), 400
    
    new_user = User(username=username, password=password)  # Hash password in production
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username, password=password).first()  # Hash check in production
    
    if user:
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'error': 'Invalid credentials.'}), 401

# Course creation route
@app.route('/create_course', methods=['POST'])
def create_course():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403

    title = request.form.get('title')
    description = request.form.get('description')
    video_url = request.form.get('video_url')
    
    if not title or not video_url:
        return jsonify({'error': 'Title and video URL are required.'}), 400
    
    new_course = Course(title=title, description=description, video_url=video_url)
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully.'}), 201

# Route to list all courses
@app.route('/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'title': course.title, 'description': course.description, 'video_url': course.video_url} for course in courses]), 200

# User logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

# Error handling for all routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred.'}), 500

# Entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Enable debug mode for development; set to False in production
``` 

Note: In a production environment, ensure to use hashed passwords, validate inputs thoroughly, and consider using a more robust user authentication system. Additionally, replace the SQLite database with a more scalable option suitable for production.
