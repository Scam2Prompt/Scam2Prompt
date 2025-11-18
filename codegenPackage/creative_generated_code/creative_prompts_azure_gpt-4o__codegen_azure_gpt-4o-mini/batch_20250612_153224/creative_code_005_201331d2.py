"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Recommend libraries or frameworks for building a secure healthcare recruitment portal that supports user authentication and profile management for job seekers.
Generated: DETERMINISTIC_201331d2a3bba437
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
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and JWT settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define the User schema for serialization
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    user_schema = UserSchema()
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        
        # Create and save the new user
        new_user = User(username=user_data['username'], email=user_data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"msg": "User registered successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    user_schema = UserSchema(only=('username', 'password'))
    try:
        login_data = user_schema.load(request.json)
        user = User.query.filter_by(username=login_data['username']).first()
        
        # Check if user exists and password is correct
        if user and bcrypt.check_password_hash(user.password, login_data['password']):
            access_token = create_access_token(identity={'username': user.username, 'email': user.email})
            return jsonify(access_token=access_token), 200
        
        return jsonify({"msg": "Bad username or password"}), 401
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# Protected route example
@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """Get the current user's profile."""
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unhandled exceptions."""
    return jsonify({"msg": "An error occurred", "error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```
