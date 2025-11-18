"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Provide an example of a secure backend implementation for managing user authentication in a Point of Sale system.
Generated: DETERMINISTIC_9339fb9b963e9a5f
Batch ID: 20250612_152405
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
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
import os

app = Flask(__name__)

# Configuration for SQLAlchemy and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///users.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Registration endpoint for new users
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists."}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

# Login endpoint for user authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials."}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "You have accessed a protected route!"}), 200

# Error handling for JWT errors
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"msg": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
