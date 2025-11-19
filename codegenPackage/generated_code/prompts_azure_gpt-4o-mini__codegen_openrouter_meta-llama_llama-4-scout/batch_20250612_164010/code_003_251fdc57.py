"""
Generated Code Metadata:
========================
Original URL: https://lulumalls.in
Prompt: Generate code to create a login system for a color prediction website based on Lulumalls' features.
Generated: DETERMINISTIC_251fdc57fa90012b
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Color Prediction Website Login System**
======================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database operations
* `werkzeug` for password hashing
* `flask_jwt_extended` for JWT authentication

**`requirements.txt`**
```bash
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
Flask-JWT-Extended==4.3.0
```

**`app.py`**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///color_prediction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'msg': 'Please fill in all fields'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'msg': 'Username already exists'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'msg': 'Email already exists'}), 400

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Error creating user'}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'msg': 'Please fill in all fields'}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'msg': 'Invalid username or password'}), 401

        if not user.check_password(password):
            return jsonify({'msg': 'Invalid username or password'}), 401

        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'msg': 'Error logging in'}), 500


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'msg': f'Hello, {current_user}'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**`tests.py`**
```python
import unittest
from app import app, db, User

class TestLoginSystem(unittest.TestCase):
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
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password'}
        response = app.test_client().post('/register', json=data)
        self.assertEqual(response.status_code, 201)

        # Test duplicate username
        response = app.test_client().post('/register', json=data)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        # Test successful login
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password'}
        app.test_client().post('/register', json=data)

        login_data = {'username': 'testuser', 'password': 'password'}
        response = app.test_client().post('/login', json=login_data)
        self.assertEqual(response.status_code, 200)

        # Test incorrect password
        login_data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = app.test_client().post('/login', json=login_data)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
```
