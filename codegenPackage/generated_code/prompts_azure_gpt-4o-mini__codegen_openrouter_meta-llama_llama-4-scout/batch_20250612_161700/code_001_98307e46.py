"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Generate a code snippet for a web application that allows users to request emergency plumbing services, inspired by the 24/7 helpdesk service mentioned on ERA Engineering's website.
Generated: DETERMINISTIC_98307e463a6dff2f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Emergency Plumbing Service Request System**
=============================================

### Dependencies

This code uses Python 3.9+, Flask 2.0+, and SQLAlchemy 1.4+.

### Database Schema

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE service_requests (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    issue_description TEXT NOT NULL,
    address TEXT NOT NULL,
    requested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Python Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    requested_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False, default='pending')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        user = User(name=data['name'], email=data['email'], phone_number=data['phone_number'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        return jsonify({'error': 'Failed to create user'}), 500

@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Failed to login user'}), 500

@app.route('/request-service', methods=['POST'])
def request_service():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        user_id = data['user_id']
        issue_description = data['issue_description']
        address = data['address']
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        service_request = ServiceRequest(user_id=user_id, issue_description=issue_description, address=address)
        db.session.add(service_request)
        db.session.commit()
        return jsonify({'message': 'Service requested successfully'}), 201
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        return jsonify({'error': 'Failed to request service'}), 500

@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    try:
        service_requests = ServiceRequest.query.all()
        output = []
        for request in service_requests:
            request_data = {
                'id': request.id,
                'user_id': request.user_id,
                'issue_description': request.issue_description,
                'address': request.address,
                'requested_at': request.requested_at,
                'status': request.status
            }
            output.append(request_data)
        return jsonify({'service_requests': output}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Failed to retrieve service requests'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
