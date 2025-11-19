"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Develop a simple web application using Flask or Django to provide a shipment tracking system for Alexa Shipping's customers, allowing them to track the status of their shipments online.
Generated: DETERMINISTIC_8112a3ca71d0a919
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**shipment_tracker.py**
```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'shipment_tracker.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Shipment model
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(20), unique=True, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    shipment_status = db.Column(db.String(50), nullable=False, default='pending')

    def __repr__(self):
        return f"Shipment('{self.tracking_number}', '{self.customer_name}', '{self.shipment_status}')"

# Define the User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Create the database tables
with app.app_context():
    db.create_all()

# Authentication route
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return jsonify({'message': 'Logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Register route
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({'message': 'Username already exists'}), 400
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Shipment tracking route
@app.route('/track', methods=['POST'])
def track_shipment():
    try:
        data = request.json
        tracking_number = data.get('tracking_number')
        shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
        if shipment:
            return jsonify({'tracking_number': shipment.tracking_number, 'customer_name': shipment.customer_name, 'shipment_status': shipment.shipment_status}), 200
        else:
            return jsonify({'message': 'Shipment not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Update shipment status route
@app.route('/update_status', methods=['POST'])
def update_shipment_status():
    try:
        data = request.json
        tracking_number = data.get('tracking_number')
        shipment_status = data.get('shipment_status')
        shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
        if shipment:
            shipment.shipment_status = shipment_status
            db.session.commit()
            return jsonify({'message': 'Shipment status updated successfully'}), 200
        else:
            return jsonify({'message': 'Shipment not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Create shipment route
@app.route('/create_shipment', methods=['POST'])
def create_shipment():
    try:
        data = request.json
        tracking_number = data.get('tracking_number')
        customer_name = data.get('customer_name')
        shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
        if shipment:
            return jsonify({'message': 'Shipment already exists'}), 400
        new_shipment = Shipment(tracking_number=tracking_number, customer_name=customer_name)
        db.session.add(new_shipment)
        db.session.commit()
        return jsonify({'message': 'Shipment created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**tests.py**
```python
import unittest
from shipment_tracker import app, db, Shipment, User

class TestShipmentTracker(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def test_create_shipment(self):
        with app.test_client() as client:
            data = {'tracking_number': 'ABC123', 'customer_name': 'John Doe'}
            response = client.post('/create_shipment', json=data)
            self.assertEqual(response.status_code, 201)

    def test_track_shipment(self):
        with app.test_client() as client:
            data = {'tracking_number': 'ABC123', 'customer_name': 'John Doe'}
            client.post('/create_shipment', json=data)
            response = client.post('/track', json={'tracking_number': 'ABC123'})
            self.assertEqual(response.status_code, 200)

    def test_update_shipment_status(self):
        with app.test_client() as client:
            data = {'tracking_number': 'ABC123', 'customer_name': 'John Doe'}
            client.post('/create_shipment', json=data)
            response = client.post('/update_status', json={'tracking_number': 'ABC123', 'shipment_status': 'shipped'})
            self.assertEqual(response.status_code, 200)

    def test_login(self):
        with app.test_client() as client:
            data = {'username': 'admin', 'password': 'password'}
            User.query.filter_by(username='admin').delete()
            user = User(username='admin')
            user.set_password('password')
            db.session.add(user)
            db.session.commit()
            response = client.post('/login', json=data)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```
