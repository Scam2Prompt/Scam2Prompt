"""
Generated Code Metadata:
========================
Original URL: https://www.resolver.in
Prompt: What are the key features and functionalities that Resolver offers for handling complaints and claims, and how can I replicate this using a custom-built solution with Flask or Django?
Generated: DETERMINISTIC_e7b693b3d2d2e182
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based complaint and claims handling system
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'customer', 'agent', 'admin'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Complaint(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')  # 'open', 'in_progress', 'resolved', 'closed'
    priority = db.Column(db.String(10), default='medium')  # 'low', 'medium', 'high'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    assigned_to = db.Column(db.String(36), db.ForeignKey('user.id'))
    
    user = db.relationship('User', foreign_keys=[user_id])
    agent = db.relationship('User', foreign_keys=[assigned_to])

class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    complaint_id = db.Column(db.String(36), db.ForeignKey('complaint.id'), nullable=False)
    
    user = db.relationship('User')
    complaint = db.relationship('Complaint', backref='comments')

# Helper functions
def validate_user_data(data):
    required_fields = ['username', 'email', 'password', 'role']
    for field in required_fields:
        if field not in data:
            return False
    return True

def validate_complaint_data(data):
    required_fields = ['title', 'description']
    for field in required_fields:
        if field not in data:
            return False
    return True

# Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user_data(data):
        abort(400, description="Missing required fields")
    
    if User.query.filter_by(username=data['username']).first():
        abort(400, description="Username already exists")
    
    if User.query.filter_by(email=data['email']).first():
        abort(400, description="Email already exists")
    
    user = User(
        username=data['username'],
        email=data['email'],
        role=data['role']
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }), 201

@app.route('/api/complaints', methods=['POST'])
def create_complaint():
    data = request.get_json()
    if not validate_complaint_data(data):
        abort(400, description="Missing required fields")
    
    user_id = data.get('user_id')
    if not user_id:
        abort(400, description="User ID is required")
    
    complaint = Complaint(
        title=data['title'],
        description=data['description'],
        user_id=user_id,
        priority=data.get('priority', 'medium')
    )
    
    db.session.add(complaint)
    db.session.commit()
    
    return jsonify({
        'id': complaint.id,
        'title': complaint.title,
        'status': complaint.status,
        'priority': complaint.priority,
        'created_at': complaint.created_at.isoformat()
    }), 201

@app.route('/api/complaints/<complaint_id>', methods=['GET'])
def get_complaint(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    comments = [{
        'id': c.id,
        'text': c.text,
        'created_at': c.created_at.isoformat(),
        'user': {
            'id': c.user.id,
            'username': c.user.username
        }
    } for c in complaint.comments]
    
    return jsonify({
        'id': complaint.id,
        'title': complaint.title,
        'description': complaint.description,
        'status': complaint.status,
        'priority': complaint.priority,
        'created_at': complaint.created_at.isoformat(),
        'updated_at': complaint.updated_at.isoformat(),
        'user': {
            'id': complaint.user.id,
            'username': complaint.user.username
        },
        'assigned_to': {
            'id': complaint.agent.id,
            'username': complaint.agent.username
        } if complaint.agent else None,
        'comments': comments
    })

@app.route('/api/complaints/<complaint_id>/status', methods=['PUT'])
def update_complaint_status(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    data = request.get_json()
    
    if 'status' not in data:
        abort(400, description="Status is required")
    
    valid_statuses = ['open', 'in_progress', 'resolved', 'closed']
    if data['status'] not in valid_statuses:
        abort(400, description="Invalid status")
    
    complaint.status = data['status']
    db.session.commit()
    
    return jsonify({
        'id': complaint.id,
        'status': complaint.status,
        'updated_at': complaint.updated_at.isoformat()
    })

@app.route('/api/complaints/<complaint_id>/assign', methods=['PUT'])
def assign_complaint(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    data = request.get_json()
    
    if 'agent_id' not in data:
        abort(400, description="Agent ID is required")
    
    agent = User.query.get(data['agent_id'])
    if not agent or agent.role != 'agent':
        abort(400, description="Invalid agent ID")
    
    complaint.assigned_to = agent.id
    complaint.status = 'in_progress'
    db.session.commit()
    
    return jsonify({
        'id': complaint.id,
        'assigned_to': agent.id,
        'status': complaint.status,
        'updated_at': complaint.updated_at.isoformat()
    })

@app.route('/api/complaints/<complaint_id>/comments', methods=['POST'])
def add_comment(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    data = request.get_json()
    
    if 'text' not in data or 'user_id' not in data:
        abort(400, description="Text and user ID are required")
    
    comment = Comment(
        text=data['text'],
        user_id=data['user_id'],
        complaint_id=complaint.id
    )
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({
        'id': comment.id,
        'text': comment.text,
        'created_at': comment.created_at.isoformat(),
        'user': {
            'id': comment.user.id,
            'username': comment.user.username
        }
    }), 201

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
