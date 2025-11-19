"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://focuscompoundingpharm.com
Prompt: What libraries are recommended for creating a user authentication system for a medical application?
Generated: DETERMINISTIC_ad85a0b32d89e392
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a user authentication system
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional, get_jwt_identity

# Initialize the Flask application
app = Flask(__name__)

# Configuration for database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this in a production environment
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database tables if they do not exist
with app.app_context():
    db.create_all()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Error handling for missing data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400
    
    # Check if username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400
    
    # Hash the password and create a new user
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User registered successfully"}), 201

# Route to log in an existing user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Error handling for missing data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    # Check if user exists and password matches
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid username or password"}), 401

# Route to get the current user's information (requires authentication)
@app.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    return jsonify({"username": current_user}), 200

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=False in production
```
