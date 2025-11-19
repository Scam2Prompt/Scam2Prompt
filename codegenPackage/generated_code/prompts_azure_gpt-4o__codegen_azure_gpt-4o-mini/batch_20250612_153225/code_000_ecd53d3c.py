"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Write Python code to implement a teleconsultation scheduling system for a speech-language pathology clinic, incorporating features like user authentication and appointment management, inspired by the services offered by Open Minds Instituto.
Generated: DETERMINISTIC_ecd53d3c428f9cea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Appointment model for managing appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'message': 'Invalid username or password.'}), 401

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful.'}), 200

# Schedule an appointment endpoint
@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    if 'user_id' not in session:
        return jsonify({'message': 'User not authenticated.'}), 401

    data = request.json
    date_time = data.get('date_time')

    if not date_time:
        return jsonify({'message': 'Date and time are required.'}), 400

    appointment = Appointment(user_id=session['user_id'], date_time=datetime.fromisoformat(date_time))
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment scheduled successfully.'}), 201

# Get user's appointments endpoint
@app.route('/appointments', methods=['GET'])
def get_appointments():
    if 'user_id' not in session:
        return jsonify({'message': 'User not authenticated.'}), 401

    appointments = Appointment.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{'id': appt.id, 'date_time': appt.date_time.isoformat()} for appt in appointments]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
