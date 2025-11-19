"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a code snippet for a multipurpose CMS that integrates with a cooperative management system, similar to Nexelit.
Generated: DETERMINISTIC_d83b856b3545ca3f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
from datetime import datetime, timedelta

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cms.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='member')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(20), default='draft')

# Define Cooperative model
class Cooperative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('User', secondary='cooperative_members', backref='cooperatives')

# Association table for cooperative members
cooperative_members = db.Table('cooperative_members',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('cooperative_id', db.Integer, db.ForeignKey('cooperative.id'), primary_key=True)
)

# JWT token required decorator
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

# User registration endpoint
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# User login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user or not user.check_password(auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

# Content management endpoints
@app.route('/api/content', methods=['GET'])
@token_required
def get_all_content(current_user):
    contents = Content.query.filter_by(author_id=current_user.id).all()
    output = []
    
    for content in contents:
        content_data = {
            'id': content.id,
            'title': content.title,
            'body': content.body,
            'status': content.status,
            'created_at': content.created_at,
            'updated_at': content.updated_at
        }
        output.append(content_data)
    
    return jsonify({'contents': output}), 200

@app.route('/api/content', methods=['POST'])
@token_required
def create_content(current_user):
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('body'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    content = Content(
        title=data['title'],
        body=data['body'],
        author_id=current_user.id,
        status=data.get('status', 'draft')
    )
    
    db.session.add(content)
    db.session.commit()
    
    return jsonify({'message': 'Content created successfully'}), 201

# Cooperative management endpoints
@app.route('/api/cooperatives', methods=['GET'])
@token_required
def get_cooperatives(current_user):
    cooperatives = current_user.cooperatives
    output = []
    
    for coop in cooperatives:
        coop_data = {
            'id': coop.id,
            'name': coop.name,
            'description': coop.description,
            'created_at': coop.created_at
        }
        output.append(coop_data)
    
    return jsonify({'cooperatives': output}), 200

@app.route('/api/cooperatives', methods=['POST'])
@token_required
def create_cooperative(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    if not data or not data.get('name'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    cooperative = Cooperative(
        name=data['name'],
        description=data.get('description', '')
    )
    
    db.session.add(cooperative)
    db.session.commit()
    
    return jsonify({'message': 'Cooperative created successfully'}), 201

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
