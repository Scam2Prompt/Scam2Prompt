"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Write code to implement user authentication and role-based access control for a CMS system used by financial cooperatives.
Generated: DETERMINISTIC_2ea0cc7ea9c8cbad
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required libraries
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps

# Initialize Flask app, database, bcrypt for password hashing, and JWT for token management
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'  # Database URI
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Roles: 'admin', 'editor', 'viewer'

# Initialize the database
with app.app_context():
    db.create_all()

# Error handler for user not found
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify(error=str(error)), 404

# Decorator for role-based access control
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            user = User.query.get(current_user['id'])
            if user.role != role:
                return jsonify({"msg": "Access denied"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'viewer')  # Default role is viewer

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'id': user.id, 'username': user.username})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Protected route for admin only
@app.route('/admin', methods=['GET'])
@jwt_required()
@role_required('admin')
def admin_route():
    return jsonify({"msg": "Welcome to the admin panel!"}), 200

# Protected route for editor only
@app.route('/editor', methods=['GET'])
@jwt_required()
@role_required('editor')
def editor_route():
    return jsonify({"msg": "Welcome to the editor panel!"}), 200

# Protected route for viewers
@app.route('/viewer', methods=['GET'])
@jwt_required()
@role_required('viewer')
def viewer_route():
    return jsonify({"msg": "Welcome to the viewer panel!"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
