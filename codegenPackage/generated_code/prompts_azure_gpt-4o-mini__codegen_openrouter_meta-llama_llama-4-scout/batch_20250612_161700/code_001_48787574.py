"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Recommend APIs or libraries that can be used to develop an online platform for a community-driven university, similar to Uni4Kashmir, emphasizing features like course management and student engagement.
Generated: DETERMINISTIC_48787574186ad01f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Create a Flask application instance
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize SQLAlchemy and Marshmallow instances
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    instructor = db.relationship('User', backref=db.backref('courses', lazy=True))

    def __init__(self, title, description, instructor_id):
        self.title = title
        self.description = description
        self.instructor_id = instructor_id

# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Define the Course schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        new_user = User(data['name'], data['email'], data['password'], data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Login a user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password, data['password']):
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.get_json()
        new_course = Course(data['title'], data['description'], data['instructor_id'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        course_schema = CourseSchema(many=True)
        return jsonify(course_schema.dump(courses)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
