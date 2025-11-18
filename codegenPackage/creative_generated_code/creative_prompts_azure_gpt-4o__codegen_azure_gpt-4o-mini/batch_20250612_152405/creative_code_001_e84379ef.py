"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Recommend libraries or APIs for integrating a Point of Sale login system with a web application, ensuring secure authentication.
Generated: DETERMINISTIC_e84379eff7e5875b
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web application and authentication
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required

# Initialize the Flask application
app = Flask(__name__)

# Configuration for database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pos_system.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"msg": "User created successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid username or password"}), 401

# Protecting a route to demonstrate secured access
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "This is a protected route"}), 200

# Error handling for any unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
