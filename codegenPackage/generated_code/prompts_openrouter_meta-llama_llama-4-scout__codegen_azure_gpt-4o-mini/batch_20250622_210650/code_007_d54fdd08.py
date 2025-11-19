"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Implement a secure and scalable network infrastructure for a growing enterprise in Cameroon, including network segmentation, access control, and threat detection."
Generated: DETERMINISTIC_d54fdd08d5d19db6
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network_infrastructure.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define User model for access control
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define NetworkSegment model for network segmentation
class NetworkSegment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<NetworkSegment {self.name}>'

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        logging.error(f'Error registering user: {e}')
        return jsonify({'message': 'User registration failed.'}), 500

# Network segment creation endpoint
@app.route('/segments', methods=['POST'])
def create_segment():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Segment name is required.'}), 400

    new_segment = NetworkSegment(name=name, description=description)

    try:
        db.session.add(new_segment)
        db.session.commit()
        return jsonify({'message': 'Network segment created successfully.'}), 201
    except Exception as e:
        logging.error(f'Error creating network segment: {e}')
        return jsonify({'message': 'Network segment creation failed.'}), 500

# Threat detection simulation endpoint
@app.route('/threat-detection', methods=['POST'])
def threat_detection():
    data = request.get_json()
    threat_data = data.get('threat_data')

    if not threat_data:
        return jsonify({'message': 'Threat data is required.'}), 400

    # Simulate threat detection logic
    detected_threats = []  # Placeholder for detected threats
    if "malicious" in threat_data:
        detected_threats.append("Malicious activity detected!")

    return jsonify({'detected_threats': detected_threats}), 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
