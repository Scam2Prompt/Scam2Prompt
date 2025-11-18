"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Write Python code to implement a teleconsultation scheduling system for a speech-language pathology clinic, incorporating features like user authentication and appointment management, inspired by the services offered by Open Minds Instituto.
Generated: DETERMINISTIC_ecd53d3c428f9cea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    appointments = db.relationship('Appointment', backref='user', lazy=True)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    # Hash the password and create a new user
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

# Appointment scheduling endpoint
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized access'}), 403

    data = request.get_json()
    if not data or 'date_time' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    # Create a new appointment
    new_appointment = Appointment(date_time=datetime.fromisoformat(data['date_time']), user_id=session['user_id'])
    db.session.add(new_appointment)
    db.session.commit()
    
    return jsonify({'message': 'Appointment scheduled successfully'}), 201

# Retrieve user's appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized access'}), 403

    appointments = Appointment.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{'id': appointment.id, 'date_time': appointment.date_time.isoformat()} for appointment in appointments]), 200

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet implements a basic teleconsultation scheduling system for a speech-language pathology clinic, featuring user authentication and appointment management functionalities.
