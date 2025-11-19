"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Illustrate how to implement a secure login system for students accessing the online learning platform of California National University, focusing on cybersecurity best practices.
Generated: DETERMINISTIC_469cfefdbec7d0fb
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import re

# Initialize Flask application
app = Flask(__name__)

# Setup secret key for session management and database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Use a random secret key for security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # Change this for production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and bcrypt for password hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Student model for the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Student {self.username}>'

# Create database tables
db.create_all()

# Function to validate username
def validate_username(username):
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        raise ValueError("Username can only contain letters, numbers, underscores, periods, and dashes.")

# Route for registering a new student
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate username
    try:
        validate_username(username)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Hash the password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create new student record
    new_student = Student(username=username, password_hash=password_hash)
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student registered successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred during registration."}), 500

# Route for student login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Fetch student record
    student = Student.query.filter_by(username=username).first()
    if not student or not bcrypt.check_password_hash(student.password_hash, password):
        return jsonify({"error": "Invalid username or password."}), 401

    # Store user session
    session['user_id'] = student.id
    return jsonify({"message": "Login successful!"}), 200

# Route for student logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully!"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Change debug to False in production
```

### Key Points:
- This code implements a secure login system using Flask, SQLAlchemy, and Flask-Bcrypt.
- It includes user registration and login functionality with password hashing.
- Validation is performed on the username to ensure it only contains allowed characters.
- Proper error handling is implemented for database operations and user inputs.
