"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Create a RESTful API in Flask to handle customer inquiries for machinery parts and technical assistance, referencing the brands and services offered by Track Diesel Peru.
Generated: DETERMINISTIC_d61c0f7cffc9c240
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trackdiesel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    brand = db.Column(db.String(50), nullable=False)
    part_number = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    if check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/api/inquiries', methods=['GET'])
@token_required
def get_inquiries(current_user):
    inquiries = Inquiry.query.all()
    
    output = []
    for inquiry in inquiries:
        inquiry_data = {
            'id': inquiry.id,
            'customer_name': inquiry.customer_name,
            'email': inquiry.email,
            'phone': inquiry.phone,
            'brand': inquiry.brand,
            'part_number': inquiry.part_number,
            'description': inquiry.description,
            'status': inquiry.status,
            'created_at': inquiry.created_at
        }
        output.append(inquiry_data)
    
    return jsonify({'inquiries': output})

@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    data = request.get_json()
    
    if not data or not data.get('customer_name') or not data.get('email') or not data.get('brand') or not data.get('description'):
        return jsonify({'message': 'Required fields are missing!'}), 400
    
    new_inquiry = Inquiry(
        customer_name=data['customer_name'],
        email=data['email'],
        phone=data.get('phone', ''),
        brand=data['brand'],
        part_number=data.get('part_number', ''),
        description=data['description'],
        user_id=data.get('user_id')
    )
    
    db.session.add(new_inquiry)
    db.session.commit()
    
    return jsonify({'message': 'Inquiry created successfully!'}), 201

@app.route('/api/inquiries/<int:id>', methods=['PUT'])
@token_required
def update_inquiry(current_user, id):
    inquiry = Inquiry.query.get(id)
    
    if not inquiry:
        return jsonify({'message': 'Inquiry not found!'}), 404
    
    data = request.get_json()
    
    if 'status' in data:
        if not current_user.is_admin:
            return jsonify({'message': 'Only admins can update status!'}), 403
        inquiry.status = data['status']
    
    if 'description' in data:
        inquiry.description = data['description']
    
    db.session.commit()
    
    return jsonify({'message': 'Inquiry updated successfully!'})

@app.route('/api/inquiries/<int:id>', methods=['DELETE'])
@token_required
def delete_inquiry(current_user, id):
    if not current_user.is_admin:
        return jsonify({'message': 'Only admins can delete inquiries!'}), 403
    
    inquiry = Inquiry.query.get(id)
    
    if not inquiry:
        return jsonify({'message': 'Inquiry not found!'}), 404
    
    db.session.delete(inquiry)
    db.session.commit()
    
    return jsonify({'message': 'Inquiry deleted successfully!'})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error!'}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
