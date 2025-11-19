"""
Generated Code Metadata:
========================
Original URL: https://icchatva.com
Prompt: "Create a web application for a client in the education industry using Icchatva's web development services and incorporating cyber security measures."
Generated: DETERMINISTIC_40be43102f9e4f1c
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Education Industry Web Application**
=====================================

**dependencies:**
*   `flask`: For creating the web application
*   `flask_sqlalchemy`: For database operations
*   `werkzeug`: For password hashing and verification
*   `pyjwt`: For JSON Web Tokens

**Installation:**
```bash
pip install flask flask_sqlalchemy werkzeug pyjwt
```

**Code:**
```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education.db'
app.config['SECRET_KEY'] = 'secret_key_here'

db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"


# Authentication Functions
def generate_token(user):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user.id
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')


def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return User.query.get(payload['sub'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


# Routes
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'Invalid username or password'}), 401

        if not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        token = generate_token(user)
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        user = verify_token(token)
        if not user:
            return jsonify({'error': 'Invalid token'}), 401

        courses = Course.query.all()
        output = []
        for course in courses:
            course_data = {
                'id': course.id,
                'name': course.name,
                'description': course.description
            }
            output.append(course_data)

        return jsonify({'courses': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses', methods=['POST'])
def create_course():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        user = verify_token(token)
        if not user:
            return jsonify({'error': 'Invalid token'}), 401

        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            return jsonify({'error': 'Please provide all required fields'}), 400

        new_course = Course(
            name=name,
            description=description
        )
        db.session.add(new_course)
        db.session.commit()

        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Testing:**
```python
# tests.py
import unittest
from app import app, db, User, Course

class TestEducationApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        # Test successful registration
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = app.test_client().post('/register', json=data)
        self.assertEqual(response.status_code, 201)

        # Test duplicate username
        response = app.test_client().post('/register', json=data)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        # Test successful login
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'password123'
        }
        app.test_client().post('/register', json=data)

        login_data = {
            'username': 'test_user',
            'password': 'password123'
        }
        response = app.test_client().post('/login', json=login_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
