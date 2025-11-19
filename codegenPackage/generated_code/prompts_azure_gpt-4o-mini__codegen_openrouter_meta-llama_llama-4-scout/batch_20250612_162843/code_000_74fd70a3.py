"""
Generated Code Metadata:
========================
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Generate code for a secure user authentication system for a TMS (Transportation Management System) similar to MultiTMS.
Generated: DETERMINISTIC_74fd70a3be733f4b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**TMS User Authentication System**
=====================================

**dependencies:**
* `flask`: Web framework
* `flask_sqlalchemy`: Database ORM
* `flask_bcrypt`: Password hashing
* `flask_jwt_extended`: JSON Web Tokens

**requirements.txt:**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Flask-Bcrypt==1.0.1
Flask-JWT-Extended==4.2.0
```

**models.py:**
```python
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False, default='user')

    def __init__(self, username, email, password, role='user'):
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.role = role

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"
```

**auth.py:**
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import User, db, bcrypt

auth = Blueprint('auth', __name__)
jwt = JWTManager()

@auth.route('/register', methods=['POST'])
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

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Error creating user'}), 500

@auth.route('/login', methods=['POST'])
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
        if not user or not user.check_password(password):
            return jsonify({'msg': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({'msg': 'Error logging in'}), 500

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    if not user:
        return jsonify({'msg': 'User not found'}), 404

    return jsonify(logged_in_as=current_user), 200
```

**app.py:**
```python
from flask import Flask
from auth import auth, jwt
from models import db, bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**tests.py:**
```python
import unittest
from app import app, db
from models import User

class TestAuthSystem(unittest.TestCase):
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
        response = app.test_client().post('/login', json={'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

        # Test invalid credentials
        response = app.test_client().post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
```
