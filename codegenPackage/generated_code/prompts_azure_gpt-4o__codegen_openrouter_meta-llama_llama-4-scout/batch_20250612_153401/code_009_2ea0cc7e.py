"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Write code to implement user authentication and role-based access control for a CMS system used by financial cooperatives.
Generated: DETERMINISTIC_2ea0cc7ea9c8cbad
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Authentication and Role-Based Access Control for CMS System**
===========================================================

**dependencies:**
* `flask`: For building the web application
* `flask_sqlalchemy`: For database operations
* `flask_bcrypt`: For password hashing
* `flask_jwt_extended`: For JSON Web Tokens

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def __init__(self, username, email, password, role_id):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.role_id = role_id

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
```

**auth.py**
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import User, db

auth = Blueprint('auth', __name__)
jwt = JWTManager()

@auth.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        return jsonify(error='Invalid credentials'), 401
    except Exception as e:
        return jsonify(error=str(e)), 500

@auth.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        role_id = request.json.get('role_id')
        user = User(username, email, password, role_id)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500

@auth.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f'Hello, {current_user}'), 200
```

**rbac.py**
```python
from flask import Blueprint, request, jsonify
from models import User, Role, db

rbac = Blueprint('rbac', __name__)

def has_role(user, role_name):
    return user.role.name == role_name

@rbac.route('/roles', methods=['GET'])
def get_roles():
    try:
        roles = Role.query.all()
        return jsonify([{'id': role.id, 'name': role.name, 'description': role.description} for role in roles]), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@rbac.route('/roles/<int:role_id>/users', methods=['GET'])
def get_users_by_role(role_id):
    try:
        users = User.query.filter_by(role_id=role_id).all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@rbac.route('/check-role', methods=['POST'])
@jwt_required
def check_role():
    try:
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first()
        role_name = request.json.get('role_name')
        if has_role(user, role_name):
            return jsonify(message=f'User has role {role_name}'), 200
        return jsonify(error=f'User does not have role {role_name}'), 403
    except Exception as e:
        return jsonify(error=str(e)), 500
```

**app.py**
```python
from flask import Flask
from models import db
from auth import auth, jwt
from rbac import rbac

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(rbac)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
