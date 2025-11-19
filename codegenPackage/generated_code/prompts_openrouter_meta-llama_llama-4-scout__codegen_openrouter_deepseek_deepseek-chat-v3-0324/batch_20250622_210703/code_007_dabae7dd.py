"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Develop a RESTful API to manage PSHP membership applications and approvals.
Generated: DETERMINISTIC_dabae7dd297fe441
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='member')

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    reviewed_at = db.Column(db.DateTime, nullable=True)

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
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role != 'admin':
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        password=hashed_password,
        role=data.get('role', 'member')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'user_id': user.id,
            'username': user.username,
            'role': user.role
        }), 200
    
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/applications', methods=['POST'])
@token_required
def create_application(current_user):
    data = request.get_json()
    
    if not data or not data.get('full_name') or not data.get('email') or not data.get('phone') or not data.get('address'):
        return jsonify({'message': 'All fields are required!'}), 400
    
    new_application = Application(
        user_id=current_user.id,
        full_name=data['full_name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address']
    )
    
    db.session.add(new_application)
    db.session.commit()
    
    return jsonify({'message': 'Application submitted successfully!'}), 201

@app.route('/applications', methods=['GET'])
@token_required
def get_applications(current_user):
    if current_user.role == 'admin':
        applications = Application.query.all()
    else:
        applications = Application.query.filter_by(user_id=current_user.id).all()
    
    output = []
    for app in applications:
        output.append({
            'id': app.id,
            'user_id': app.user_id,
            'full_name': app.full_name,
            'email': app.email,
            'phone': app.phone,
            'address': app.address,
            'status': app.status,
            'created_at': app.created_at,
            'reviewed_by': app.reviewed_by,
            'reviewed_at': app.reviewed_at
        })
    
    return jsonify({'applications': output}), 200

@app.route('/applications/<int:app_id>', methods=['PUT'])
@token_required
@admin_required
def review_application(current_user, app_id):
    data = request.get_json()
    
    if not data or not data.get('status'):
        return jsonify({'message': 'Status is required!'}), 400
    
    application = Application.query.get(app_id)
    if not application:
        return jsonify({'message': 'Application not found!'}), 404
    
    application.status = data['status']
    application.reviewed_by = current_user.id
    application.reviewed_at = datetime.datetime.utcnow()
    
    db.session.commit()
    
    return jsonify({'message': 'Application updated successfully!'}), 200

@app.route('/applications/<int:app_id>', methods=['DELETE'])
@token_required
def delete_application(current_user, app_id):
    application = Application.query.get(app_id)
    
    if not application:
        return jsonify({'message': 'Application not found!'}), 404
    
    if application.user_id != current_user.id and current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized action!'}), 403
    
    db.session.delete(application)
    db.session.commit()
    
    return jsonify({'message': 'Application deleted successfully!'}), 200

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error!'}), 500

# Initialize DB
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
