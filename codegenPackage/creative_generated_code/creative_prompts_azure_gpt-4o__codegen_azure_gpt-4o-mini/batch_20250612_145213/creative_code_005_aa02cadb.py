"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Suggest best practices for implementing secure login and registration systems for a Hajj management portal in the Philippines.
Generated: DETERMINISTIC_aa02cadb73ffabf5
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
import re
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hajj_management.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Use an env variable for production
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Function to validate username
def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        return False
    return True

# Function to validate password
def validate_password(password):
    if (len(password) < 8 or
        not re.search(r"[A-Za-z]", password) or
        not re.search(r"[0-9]", password)):
        return False
    return True

# Registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    if not validate_username(username):
        return jsonify({"msg": "Invalid username format"}), 400
    if not validate_password(password):
        return jsonify({"msg": "Password must be at least 8 characters long, containing letters and numbers."}), 400

    # Hash password and save user
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    if 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        # Create JWT token
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="This is a protected route"), 200

# Error handling for Invalid JWT
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing or invalid token"}), 401

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
