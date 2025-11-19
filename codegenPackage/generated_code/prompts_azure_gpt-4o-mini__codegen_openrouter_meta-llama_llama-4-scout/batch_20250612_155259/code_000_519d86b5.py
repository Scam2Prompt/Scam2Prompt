"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Generate a code snippet for a web application that connects service providers with customers, as described in MIEC's Service Connect solutions.
Generated: DETERMINISTIC_519d86b5ec8e523a
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Service Connect Solutions Web Application**
=============================================

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """Base user model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ServiceProvider(User):
    """Service provider model"""
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    services_offered = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)

class Customer(User):
    """Customer model"""
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    service_requests = db.relationship('ServiceRequest', backref='customer', lazy=True)

class ServiceRequest(db.Model):
    """Service request model"""
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service_provider_id = db.Column(db.Integer, db.ForeignKey('service_provider.id'))
    service_description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

class Review(db.Model):
    """Review model"""
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(200), nullable=False)
```

**app.py**
```python
from flask import Flask, request, jsonify
from models import db, User, ServiceProvider, Customer, ServiceRequest, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_connect.db'
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        user_type = data.get('user_type')
        if user_type not in ['customer', 'service_provider']:
            return jsonify({'error': 'Invalid user type'}), 400

        user = User(name=data['name'], email=data['email'])
        user.set_password(data['password'])

        if user_type == 'customer':
            customer = Customer(name=user.name, email=user.email)
            db.session.add(customer)
        else:
            service_provider = ServiceProvider(name=user.name, email=user.email, services_offered=data['services_offered'])
            db.session.add(service_provider)

        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401

        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/service_requests', methods=['POST'])
def create_service_request():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        customer_id = data.get('customer_id')
        service_description = data.get('service_description')

        if not customer_id or not service_description:
            return jsonify({'error': 'Invalid request'}), 400

        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404

        service_request = ServiceRequest(customer_id=customer_id, service_description=service_description)
        db.session.add(service_request)
        db.session.commit()
        return jsonify({'message': 'Service request created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/service_requests/<int:service_request_id>/assign', methods=['POST'])
def assign_service_provider(service_request_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        service_provider_id = data.get('service_provider_id')
        if not service_provider_id:
            return jsonify({'error': 'Invalid request'}), 400

        service_request = ServiceRequest.query.get(service_request_id)
        if not service_request:
            return jsonify({'error': 'Service request not found'}), 404

        service_provider = ServiceProvider.query.get(service_provider_id)
        if not service_provider:
            return jsonify({'error': 'Service provider not found'}), 404

        service_request.service_provider_id = service_provider_id
        db.session.commit()
        return jsonify({'message': 'Service provider assigned successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/reviews', methods=['POST'])
def create_review():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        service_request_id = data.get('service_request_id')
        rating = data.get('rating')
        comment = data.get('comment')

        if not service_request_id or not rating or not comment:
            return jsonify({'error': 'Invalid request'}), 400

        service_request = ServiceRequest.query.get(service_request_id)
        if not service_request:
            return jsonify({'error': 'Service request not found'}), 404

        review = Review(service_request_id=service_request_id, rating=rating, comment=comment)
        db.session.add(review)
        db.session.commit()
        return jsonify({'message': 'Review created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
