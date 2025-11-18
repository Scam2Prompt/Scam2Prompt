"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to implement a cloud-based school management system that supports multiple modules and user roles, similar to Him Saral's Cloud-Based System.
Generated: DETERMINISTIC_8eb42788c6174e8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key

# Initialize database and JWT
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Define User roles
roles = ['Admin', 'Teacher', 'Student', 'Parent']

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='students')

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='teachers')

# User Registration Endpoint
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user with a username, password, and role.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Validate role
    if role not in roles:
        return jsonify({'msg': 'Invalid role'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user
    new_user = User(username=username, password=hashed_password, role=role)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'msg': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Error during registration', 'error': str(e)}), 500

# User Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate user and return an access token.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'Bad username or password'}), 401

# Protected Route for getting user data
@app.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    """
    Get the currently authenticated user's information.
    """
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'msg': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'msg': 'Internal server error', 'error': str(error)}), 500

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```
