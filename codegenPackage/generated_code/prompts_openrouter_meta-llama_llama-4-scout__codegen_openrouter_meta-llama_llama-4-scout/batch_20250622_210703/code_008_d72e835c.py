"""
Generated Code Metadata:
========================
Original URL: https://dromhusab.se
Prompt: "Develop a basic strategy for implementing user authentication and authorization in a casino website, similar to those found on 1xbet or Mostbet."
Generated: DETERMINISTIC_d72e835c4d751dc7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Authentication and Authorization System**
====================================================

**dependencies:**
* `flask`: Web framework
* `flask_sqlalchemy`: Database ORM
* `werkzeug`: Password hashing
* `flask_jwt_extended`: JSON Web Tokens

**requirements.txt:**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
Flask-JWT-Extended==4.2.0
```

**models.py:**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

class UserPermission(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), primary_key=True)
```

**auth.py:**
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import User, db

auth = Blueprint('auth', __name__)
jwt = JWTManager()

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@auth.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({'message': f'Hello, {user.username}'}), 200
```

**app.py:**
```python
from flask import Flask
from models import db
from auth import auth, jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
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
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/register', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def test_protected(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'password'})
        access_token = response.json['access_token']
        response = self.app.get('/protected', headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
