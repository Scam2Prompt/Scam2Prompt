"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Design a RESTful API for managing NDT services, including endpoints for customer registration, service requests, and employee management."
Generated: DETERMINISTIC_5fac08cec8510245
Batch ID: 20250622_211142
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
from functools import wraps
import uuid
import jwt
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ndt_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100))
    hired_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='Pending')
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    completed_on = db.Column(db.DateTime)

# Helper Functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Employee.query.filter_by(public_id=data['public_id']).first()
            if not current_user:
                return jsonify({'message': 'Invalid token!'}), 401
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Customer Endpoints
@app.route('/api/customer/register', methods=['POST'])
def register_customer():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    try:
        new_customer = Customer(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone=data.get('phone'),
            address=data.get('address')
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed!', 'error': str(e)}), 400

@app.route('/api/customer/login', methods=['POST'])
def login_customer():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify!'}), 401
    customer = Customer.query.filter_by(email=auth.username).first()
    if not customer:
        return jsonify({'message': 'Customer not found!'}), 404
    if check_password_hash(customer.password, auth.password):
        token = jwt.encode({
            'public_id': customer.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

# Employee Endpoints
@app.route('/api/employee/register', methods=['POST'])
@token_required
def register_employee(current_user):
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required!'}), 403
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    try:
        new_employee = Employee(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone=data.get('phone'),
            position=data.get('position'),
            is_admin=data.get('is_admin', False)
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed!', 'error': str(e)}), 400

@app.route('/api/employee/login', methods=['POST'])
def login_employee():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify!'}), 401
    employee = Employee.query.filter_by(email=auth.username).first()
    if not employee:
        return jsonify({'message': 'Employee not found!'}), 404
    if check_password_hash(employee.password, auth.password):
        token = jwt.encode({
            'public_id': employee.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

# Service Request Endpoints
@app.route('/api/service_request', methods=['POST'])
@token_required
def create_service_request(current_user):
    data = request.get_json()
    try:
        new_request = ServiceRequest(
            public_id=str(uuid.uuid4()),
            customer_id=data['customer_id'],
            service_type=data['service_type'],
            description=data.get('description'),
            status='Pending'
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Service request created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Request creation failed!', 'error': str(e)}), 400

@app.route('/api/service_request/<public_id>', methods=['PUT'])
@token_required
def update_service_request(current_user, public_id):
    request_data = ServiceRequest.query.filter_by(public_id=public_id).first()
    if not request_data:
        return jsonify({'message': 'Service request not found!'}), 404
    data = request.get_json()
    try:
        if 'employee_id' in data:
            request_data.employee_id = data['employee_id']
        if 'status' in data:
            request_data.status = data['status']
            if data['status'] == 'Completed':
                request_data.completed_on = datetime.datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'Service request updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Update failed!', 'error': str(e)}), 400

@app.route('/api/service_request', methods=['GET'])
@token_required
def get_all_service_requests(current_user):
    requests = ServiceRequest.query.all()
    output = []
    for req in requests:
        req_data = {
            'public_id': req.public_id,
            'customer_id': req.customer_id,
            'employee_id': req.employee_id,
            'service_type': req.service_type,
            'status': req.status,
            'created_on': req.created_on
        }
        output.append(req_data)
    return jsonify({'service_requests': output}), 200

# Main Entry Point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
