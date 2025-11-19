"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Design a mobile app feature that allows users to register for the SBI Clinic on Wheels service, including user authentication and appointment scheduling, inspired by AIDA's health initiatives.
Generated: DETERMINISTIC_01e43b8fe62ef6d6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import hashlib
import logging
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# Initialize Flask app and configure logging
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sbi_clinic.db'
app.config['SECRET_KEY'] = 'secret_key_here'
db = SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')

        if not all([username, email, password, phone_number]):
            return jsonify({'error': 'All fields are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(username=username, email=email, phone_number=phone_number)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        password = data.get('password')

        if not all([username, password]):
            return jsonify({'error': 'All fields are required'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401

        token = jwt.encode({'user_id': user.id}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

# Appointment scheduling endpoint
@app.route('/schedule-appointment', methods=['POST'])
def schedule_appointment():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        token = token.split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = payload['user_id']

        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        date = data.get('date')
        time = data.get('time')
        symptoms = data.get('symptoms')

        if not all([date, time, symptoms]):
            return jsonify({'error': 'All fields are required'}), 400

        appointment = Appointment(user_id=user_id, date=datetime.datetime.strptime(date, '%Y-%m-%d').date(), time=time, symptoms=symptoms)
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment scheduled successfully'}), 201
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
