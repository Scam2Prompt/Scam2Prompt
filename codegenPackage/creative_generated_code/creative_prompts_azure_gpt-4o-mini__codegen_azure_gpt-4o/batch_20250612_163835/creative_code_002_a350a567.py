"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdevent.com
Prompt: How can I implement a user authentication system for event organizers on usdevent.com?
Generated: DETERMINISTIC_a350a56774b9be19
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication System for Event Organizers on usdevent.com.
This implementation uses Flask (a Python web framework) for building the API,
SQLAlchemy for database handling, and bcrypt for password hashing.

To run this code, make sure to install the required dependencies:
pip install flask sqlalchemy flask-sqlalchemy bcrypt

This example assumes you have basic knowledge of Python web development.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity; replace with production DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_organizers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key in production

# Initialize the database
db = SQLAlchemy(app)

# Database model for Event Organizer
class Organizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Utility decorator to check JWT token authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Organizer.query.filter_by(username=data['username']).first()
        except:
            return jsonify({'message': 'Invalid token!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing data in request'}), 400

    # Check if username or email is already taken
    if Organizer.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    if Organizer.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    # Hash the password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create new organizer
    new_organizer = Organizer(
        username=data['username'],
        email=data['email'],
        password_hash=hashed_password
    )
    db.session.add(new_organizer)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing data in request'}), 400

    organizer = Organizer.query.filter_by(username=data['username']).first()
    if not organizer or not check_password_hash(organizer.password_hash, data['password']):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Generate JWT token
    token = jwt.encode(
        {'username': organizer.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return jsonify({'token': token}), 200

# Route to access protected resource
@app.route('/dashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    return jsonify({
        'message': f'Welcome {current_user.username}! This is your dashboard.',
        'email': current_user.email
    }), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    db.create_all()

    # Run the Flask application
    app.run(debug=True)  # Disable debug mode in production
```
