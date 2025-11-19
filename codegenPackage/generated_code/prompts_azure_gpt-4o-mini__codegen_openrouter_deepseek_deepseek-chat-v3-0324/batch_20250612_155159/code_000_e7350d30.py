"""
Generated Code Metadata:
========================
Original URL: https://neami.shop
Prompt: Generate a code snippet that demonstrates how to create a collaborative platform for business opportunities among friends, emphasizing mutual trust and communication.
Generated: DETERMINISTIC_e7350d30e33c5614
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opportunities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    friends = db.relationship('Friendship', foreign_keys='Friendship.user_id', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Friendship(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<Friendship {self.user_id} -> {self.friend_id}>'

class Opportunity(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='open')  # open, in_progress, completed
    collaborators = db.relationship('OpportunityCollaborator', backref='opportunity', lazy=True)
    
    def __repr__(self):
        return f'<Opportunity {self.title}>'

class OpportunityCollaborator(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    opportunity_id = db.Column(db.String(36), db.ForeignKey('opportunity.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='invited')  # invited, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<OpportunityCollaborator {self.opportunity_id} -> {self.user_id}>'

class Message(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    opportunity_id = db.Column(db.String(36), db.ForeignKey('opportunity.id'), nullable=False)
    sender_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.sender_id} -> {self.opportunity_id}>'

# Create tables
with app.app_context():
    db.create_all()

# Authentication decorator
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
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

@app.route('/friends', methods=['GET'])
@token_required
def get_friends(current_user):
    friends = Friendship.query.filter(
        (Friendship.user_id == current_user.id) | (Friendship.friend_id == current_user.id),
        Friendship.status == 'accepted'
    ).all()
    
    friend_list = []
    for friendship in friends:
        if friendship.user_id == current_user.id:
            friend = User.query.get(friendship.friend_id)
        else:
            friend = User.query.get(friendship.user_id)
        
        friend_list.append({
            'id': friend.id,
            'username': friend.username,
            'email': friend.email
        })
    
    return jsonify({'friends': friend_list}), 200

@app.route('/friends/add', methods=['POST'])
@token_required
def add_friend(current_user):
    data = request.get_json()
    
    if not data or not data.get('friend_username'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    friend = User.query.filter_by(username=data['friend_username']).first()
    
    if not friend:
        return jsonify({'message': 'User not found!'}), 404
    
    if friend.id == current_user.id:
        return jsonify({'message': 'Cannot add yourself as a friend!'}), 400
    
    existing_friendship = Friendship.query.filter(
        ((Friendship.user_id == current_user.id) & (Friendship.friend_id == friend.id)) |
        ((Friendship.user_id == friend.id) & (Friendship.friend_id == current_user.id))
    ).first()
    
    if existing_friendship:
        return jsonify({'message': 'Friendship already exists or is pending!'}), 400
    
    new_friendship = Friendship(
        user_id=current_user.id,
        friend_id=friend.id
    )
    
    db.session.add(new_friendship)
    db.session.commit()
    
    return jsonify({'message': 'Friend request sent!'}), 201

@app.route('/opportunities', methods=['GET'])
@token_required
def get_opportunities(current_user):
    opportunities = Opportunity.query.filter(
        (Opportunity.created_by == current_user.id) |
        (Opportunity.collaborators.any(OpportunityCollaborator.user_id == current_user.id))
    ).all()
    
    opportunity_list = []
    for opportunity in opportunities:
        opportunity_list.append({
            'id': opportunity.id,
            'title': opportunity.title,
            'description': opportunity.description,
            'created_by': opportunity.created_by,
            'status': opportunity.status,
            'created_at': opportunity.created_at
        })
    
    return jsonify({'opportunities': opportunity_list}), 200

@app.route('/opportunities/create', methods=['POST'])
@token_required
def create_opportunity(current_user):
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('description'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    new_opportunity = Opportunity(
