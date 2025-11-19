"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: "Design a virtual learning platform for corporate training using LMS and gamification, incorporating interactive videos and multimedia resources."
Generated: DETERMINISTIC_9d406c0e52a57974
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content_url = db.Column(db.String(250), nullable=False)  # URL for interactive video or multimedia resource

# Load user for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    # Create new user
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Error handling for invalid credentials
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    login_user(user)
    return jsonify({"message": "Login successful"}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

# Route to create a new course
@app.route('/courses', methods=['POST'])
@login_required
def create_course():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    content_url = data.get('content_url')

    # Create new course
    new_course = Course(title=title, description=description, content_url=content_url)
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Course created successfully"}), 201

# Route to get all courses
@app.route('/courses', methods=['GET'])
@login_required
def get_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "title": course.title, "description": course.description, "content_url": course.content_url} for course in courses]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
