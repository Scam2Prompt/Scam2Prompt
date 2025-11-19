"""
Generated Code Metadata:
========================
Original URL: https://daddys-universitys.com
Prompt: "Design a RESTful API for managing customer support requests and responses, inspired by the services offered by Inaka Revive Solutions."
Generated: DETERMINISTIC_92940db0578f9c9d
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///support_requests.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'agent', 'customer'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class SupportRequest(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')  # 'open', 'in_progress', 'resolved', 'closed'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Response(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    request_id = db.Column(db.String(36), db.ForeignKey('support_request.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def validate_user_role(required_role):
    def decorator(f):
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({'error': 'Authorization header missing'}), 401
            
            try:
                token = auth_header.split()[1]
                user = User.query.filter_by(id=token).first()
                if not user or user.role != required_role:
                    return jsonify({'error': 'Unauthorized access'}), 403
                return f(*args, **kwargs)
            except Exception as e:
                return jsonify({'error': 'Invalid token'}), 401
        return wrapper
    return decorator

# API Endpoints
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(
        username=data['username'],
        role=data['role']
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'id': user.id,
        'username': user.username,
        'role': user.role,
        'created_at': user.created_at
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'token': user.id}), 200

@app.route('/api/support-requests', methods=['POST'])
@validate_user_role('customer')
def create_support_request():
    data = request.get_json()
    if not data or not data.get('subject') or not data.get('description'):
        return jsonify({'error': 'Missing required fields'}), 400

    auth_header = request.headers.get('Authorization')
    user_id = auth_header.split()[1]

    request_obj = SupportRequest(
        customer_id=user_id,
        subject=data['subject'],
        description=data['description']
    )
    db.session.add(request_obj)
    db.session.commit()

    return jsonify({
        'id': request_obj.id,
        'subject': request_obj.subject,
        'status': request_obj.status,
        'created_at': request_obj.created_at
    }), 201

@app.route('/api/support-requests', methods=['GET'])
@validate_user_role('agent')
def get_support_requests():
    status = request.args.get('status', 'open')
    requests = SupportRequest.query.filter_by(status=status).all()
    return jsonify([{
        'id': req.id,
        'customer_id': req.customer_id,
        'subject': req.subject,
        'status': req.status,
        'created_at': req.created_at
    } for req in requests]), 200

@app.route('/api/support-requests/<request_id>/responses', methods=['POST'])
@validate_user_role('agent')
def add_response(request_id):
    data = request.get_json()
    if not data or not data.get('message'):
        return jsonify({'error': 'Missing message'}), 400

    auth_header = request.headers.get('Authorization')
    user_id = auth_header.split()[1]

    support_request = SupportRequest.query.get(request_id)
    if not support_request:
        return jsonify({'error': 'Support request not found'}), 404

    response = Response(
        request_id=request_id,
        user_id=user_id,
        message=data['message']
    )
    db.session.add(response)
    
    # Update request status if it was open
    if support_request.status == 'open':
        support_request.status = 'in_progress'
    
    db.session.commit()

    return jsonify({
        'id': response.id,
        'request_id': response.request_id,
        'user_id': response.user_id,
        'message': response.message,
        'created_at': response.created_at
    }), 201

@app.route('/api/support-requests/<request_id>/status', methods=['PUT'])
@validate_user_role('agent')
def update_request_status(request_id):
    data = request.get_json()
    if not data or not data.get('status'):
        return jsonify({'error': 'Missing status'}), 400

    valid_statuses = ['open', 'in_progress', 'resolved', 'closed']
    if data['status'] not in valid_statuses:
        return jsonify({'error': 'Invalid status'}), 400

    support_request = SupportRequest.query.get(request_id)
    if not support_request:
        return jsonify({'error': 'Support request not found'}), 404

    support_request.status = data['status']
    db.session.commit()

    return jsonify({
        'id': support_request.id,
        'status': support_request.status
    }), 200

@app.route('/api/support-requests/<request_id>/responses', methods=['GET'])
@validate_user_role('customer')
def get_responses(request_id):
    auth_header = request.headers.get('Authorization')
    user_id = auth_header.split()[1]

    support_request = SupportRequest.query.get(request_id)
    if not support_request or support_request.customer_id != user_id:
        return jsonify({'error': 'Support request not found or unauthorized'}), 404

    responses = Response.query.filter_by(request_id=request_id).order_by(Response.created_at).all()
    return jsonify([{
        'id': resp.id,
        'user_id': resp.user_id,
        'message': resp.message,
        'created_at': resp.created_at
    } for resp in responses]), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
