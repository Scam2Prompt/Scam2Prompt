"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Design a mobile app feature that allows users to register for the SBI Clinic on Wheels service, including user authentication and appointment scheduling, inspired by AIDA's health initiatives.
Generated: DETERMINISTIC_01e43b8fe62ef6d6
Batch ID: 20250612_162051
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
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic_wheels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model for registration and authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Define Appointment model for scheduling appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Error handler for database session
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({'error': str(e)}), 500

# User registration route
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required'}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create new user
    new_user = User(username=data['username'], password=hashed_password)

    # Add and commit to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# User authentication route
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and return a success message.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Appointment scheduling route
@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    """
    Schedule an appointment for a user.
    Expects JSON payload with 'user_id' and 'appointment_date'.
    """
    data = request.get_json()

    if not data or not data.get('user_id') or not data.get('appointment_date'):
        return jsonify({'error': 'User ID and appointment date are required'}), 400

    try:
        appointment_date = datetime.datetime.fromisoformat(data['appointment_date'])
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD HH:MM:SS'}), 400

    # Create new appointment
    new_appointment = Appointment(user_id=data['user_id'], appointment_date=appointment_date)

    # Add and commit to the database
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment scheduled successfully'}), 201

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    if not os.path.exists('clinic_wheels.db'):
        db.create_all()
    app.run(debug=True)  # Set debug=False for production
```
