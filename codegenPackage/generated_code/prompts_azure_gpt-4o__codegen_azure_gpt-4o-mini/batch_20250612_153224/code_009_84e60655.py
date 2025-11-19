"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for an API that handles user authentication and access control for an organizational portal, ensuring secure access to sensitive sections like "محاضر مجلس الإدارة" and "قرارات الاستثمار والتملك".
Generated: DETERMINISTIC_84e60655b54bc8e8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'admin', 'user'

# Create the database
with app.app_context():
    db.create_all()

# Decorator for role-based access control
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            user = User.query.filter_by(username=current_user).first()
            if user.role != role:
                return jsonify({"msg": "Access forbidden: insufficient permissions"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({"msg": "Missing username, password, or role"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Protected endpoint for "محاضر مجلس الإدارة"
@app.route('/minutes', methods=['GET'])
@jwt_required()
@role_required('admin')  # Only admin can access
def get_minutes():
    return jsonify({"msg": "Access granted to محاضر مجلس الإدارة"}), 200

# Protected endpoint for "قرارات الاستثمار والتملك"
@app.route('/investment-decisions', methods=['GET'])
@jwt_required()
@role_required('admin')  # Only admin can access
def get_investment_decisions():
    return jsonify({"msg": "Access granted to قرارات الاستثمار والتملك"}), 200

# Error handling for JWT
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing or invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"msg": "Token has expired"}), 401

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
