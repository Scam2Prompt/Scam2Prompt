"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Generate a backend API endpoint for handling admin login requests, including input validation and session creation.
Generated: DETERMINISTIC_cdae0ea1ba540f58
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import re

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration parameters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admins.db'  # Use SQLite for demo purposes
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in production
app.config['SESSION_COOKIE_NAME'] = 'admin_session'

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Admin model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Admin schema
class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Admin

# Create the database
with app.app_context():
    db.create_all()

# Input validation function
def validate_login_input(username, password):
    if not username or not password:
        return False, "Username and password are required."
    
    if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        return False, "Username must be alphanumeric and between 3 to 20 characters."
    
    return True, ""

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    # Request data
    data = request.get_json()

    # Validate request
    username = data.get('username')
    password = data.get('password')
    is_valid, message = validate_login_input(username, password)

    if not is_valid:
        return jsonify({"success": False, "message": message}), 400

    # Find the admin by username
    admin = Admin.query.filter_by(username=username).first()
    
    # Check if admin exists and password is correct
    if admin and check_password_hash(admin.password_hash, password):
        session['admin_id'] = admin.id  # Create session
        return jsonify({"success": True, "message": "Login successful."}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password."}), 401

# Logout endpoint
@app.route('/api/logout', methods=['POST'])
def logout():
    # Clear the session
    session.clear()
    return jsonify({"success": True, "message": "Logout successful."}), 200

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

Make sure to replace `your_secret_key` with a strong random key for production.
