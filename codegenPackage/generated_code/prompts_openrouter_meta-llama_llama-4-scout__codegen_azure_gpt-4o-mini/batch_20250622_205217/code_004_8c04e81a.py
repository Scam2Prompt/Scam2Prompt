"""
Generated Code Metadata:
========================
Original URL: https://tradevault.live
Prompt: Create a RESTful API endpoint for handling admin login requests, including authentication and authorization, inspired by the Currencia dashboard.
Generated: DETERMINISTIC_8c04e81adf84c0dd
Batch ID: 20250622_205217
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
from functools import wraps
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///admin.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Admin model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Custom decorator for admin role check
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Here you would check if the user has admin privileges
        # This is a placeholder for actual role checking logic
        return fn(*args, **kwargs)
    return wrapper

# Endpoint for admin login
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    """Handles admin login requests."""
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400

    # Fetch admin from the database
    admin = Admin.query.filter_by(username=data['username']).first()

    # Check if admin exists and password is correct
    if admin and check_password_hash(admin.password, data['password']):
        # Create JWT token
        access_token = create_access_token(identity=admin.username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Protected endpoint example
@app.route('/api/admin/protected', methods=['GET'])
@jwt_required()
@admin_required
def protected_route():
    """A protected route that requires admin authentication."""
    return jsonify({"msg": "Welcome to the protected admin route!"}), 200

# Error handling for JWT errors
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing authorization header"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"msg": "Invalid token"}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
