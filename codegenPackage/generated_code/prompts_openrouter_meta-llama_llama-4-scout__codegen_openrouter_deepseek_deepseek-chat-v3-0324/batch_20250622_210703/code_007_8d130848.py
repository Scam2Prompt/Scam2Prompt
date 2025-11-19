"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Generate a RESTful API for an online auction platform, including endpoints for creating, reading, updating, and deleting auctions, bids, and user information."
Generated: DETERMINISTIC_8d130848e7320d95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# auction_platform/api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auctions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Auction(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    start_price = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    seller_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    seller = db.relationship('User', backref=db.backref('auctions', lazy=True))
    is_active = db.Column(db.Boolean, default=True)

class Bid(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bidder_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    auction_id = db.Column(db.String(36), db.ForeignKey('auction.id'), nullable=False)
    bidder = db.relationship('User', backref=db.backref('bids', lazy=True))
    auction = db.relationship('Auction', backref=db.backref('bids', lazy=True))

# Helper Functions
def validate_user_data(data):
    required_fields = ['username', 'email', 'password']
    if not all(field in data for field in required_fields):
        return False
    return True

def validate_auction_data(data):
    required_fields = ['title', 'start_price', 'end_time', 'seller_id']
    if not all(field in data for field in required_fields):
        return False
    return True

def validate_bid_data(data):
    required_fields = ['amount', 'bidder_id', 'auction_id']
    if not all(field in data for field in required_fields):
        return False
    return True

# User Endpoints
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'user_id': user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    }), 200

@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    if 'username' in data and data['username'] != user.username:
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Username already exists'}), 400
        user.username = data['username']
    
    if 'email' in data and data['email'] != user.email:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists'}), 400
        user.email = data['email']
    
    if 'password' in data:
        user.set_password(data['password'])
    
    try:
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Auction Endpoints
@app.route('/api/auctions', methods=['POST'])
def create_auction():
    data = request.get_json()
    if not validate_auction_data(data):
        return jsonify({'error': 'Missing required fields'}), 400
    
    seller = User.query.get(data['seller_id'])
    if not seller:
        return jsonify({'error': 'Seller not found'}), 404
    
    try:
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Invalid end_time format. Use ISO format'}), 400
    
    auction = Auction(
        title=data['title'],
        description=data.get('description', ''),
        start_price=data['start_price'],
        current_price=data['start_price'],
        end_time=end_time,
        seller_id=data['seller_id']
    )
    
    try:
        db.session.add(auction)
        db.session.commit()
        return jsonify({
            'message': 'Auction created successfully',
            'auction_id': auction.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auctions/<auction_id>', methods=['GET'])
def get_auction(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    
    return jsonify({
        'id': auction.id,
        'title': auction.title,
        'description': auction.description,
        'start_price': auction.start_price,
        'current_price': auction.current_price,
        'end_time': auction.end_time.isoformat(),
        'created_at': auction.created_at.isoformat(),
        'seller_id': auction.seller_id,
        'is_active': auction.is_active
    }), 200

@app.route('/api/auctions/<auction_id>', methods=['PUT'])
def update_auction(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    
    data = request.get_json()
    if 'title' in data:
        auction.title = data['title']
    if 'description' in data:
        auction.description = data['description']
    if 'end_time' in data:
        try:
            auction.end_time = datetime.fromisoformat(data['end_time'])
        except ValueError:
            return jsonify({'error': 'Invalid end_time format. Use ISO format'}), 400
    
    try:
        db.session.commit()
        return jsonify({'message': 'Auction updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auctions/<auction_id>', methods=['DELETE'])
def delete_auction(auction_id):
    auction = Auction.query.get(auction_id)
    if not auction:
        return jsonify({'error': 'Auction not found'}), 404
    
    try:
        db.session.delete(auction)
        db.session
