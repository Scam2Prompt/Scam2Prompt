"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the rewards system mentioned on Opteris Global's website.
Generated: DETERMINISTIC_a0b1689beb3e8f52
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
from functools import wraps
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referral_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    referral_code = db.Column(db.String(10), unique=True)
    points = db.Column(db.Integer, default=0)
    referred_by = db.Column(db.String(10))
    is_active = db.Column(db.Boolean, default=True)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    referee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_verified = db.Column(db.Boolean, default=False)
    points_awarded = db.Column(db.Integer, default=0)

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    points_used = db.Column(db.Integer)
    reward_item = db.Column(db.String(100))
    date_redeemed = db.Column(db.DateTime, default=datetime.datetime.utcnow)

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
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

def generate_referral_code():
    return str(uuid.uuid4())[:8].upper()

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    referral_code = generate_referral_code()
    while User.query.filter_by(referral_code=referral_code).first():
        referral_code = generate_referral_code()
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    referred_by = data.get('referred_by')
    if referred_by:
        referrer = User.query.filter_by(referral_code=referred_by).first()
        if not referrer:
            return jsonify({'message': 'Invalid referral code'}), 400
    
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        referral_code=referral_code,
        referred_by=referred_by
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    if referred_by:
        new_referral = Referral(
            referrer_id=referrer.id,
            referee_id=new_user.id
        )
        db.session.add(new_referral)
        db.session.commit()
    
    return jsonify({'message': 'User registered successfully', 'referral_code': referral_code}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token, 'referral_code': user.referral_code})
    
    return jsonify({'message': 'Wrong credentials'}), 401

@app.route('/referrals', methods=['GET'])
@token_required
def get_referrals(current_user):
    referrals = Referral.query.filter_by(referrer_id=current_user.id).all()
    
    output = []
    for referral in referrals:
        referee = User.query.get(referral.referee_id)
        output.append({
            'referee_username': referee.username,
            'referee_email': referee.email,
            'date_referred': referral.date_created,
            'is_verified': referral.is_verified,
            'points_awarded': referral.points_awarded
        })
    
    return jsonify({'referrals': output})

@app.route('/verify_referral/<int:referral_id>', methods=['PUT'])
@token_required
def verify_referral(current_user, referral_id):
    referral = Referral.query.get(referral_id)
    
    if not referral:
        return jsonify({'message': 'Referral not found'}), 404
    
    if referral.referrer_id != current_user.id:
        return jsonify({'message': 'Unauthorized action'}), 403
    
    if referral.is_verified:
        return jsonify({'message': 'Referral already verified'}), 400
    
    referral.is_verified = True
    referral.points_awarded = 100  # Example: 100 points per successful referral
    
    referrer = User.query.get(referral.referrer_id)
    referrer.points += referral.points_awarded
    
    db.session.commit()
    
    return jsonify({'message': 'Referral verified and points awarded'})

@app.route('/rewards', methods=['GET'])
@token_required
def get_rewards(current_user):
    rewards = Reward.query.filter_by(user_id=current_user.id).all()
    
    output = []
    for reward in rewards:
        output.append({
            'points_used': reward.points_used,
            'reward_item': reward.reward_item,
            'date_redeemed': reward.date_redeemed
        })
    
    return jsonify({'rewards': output})

@app.route('/redeem', methods=['POST'])
@token_required
def redeem_reward(current_user):
    data = request.get_json()
    
    if not data or not data.get('reward_item'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    points_required = 0
    reward_items = {
        'discount_10': 100,
        'discount_20': 200,
        'free_shipping': 50
    }
    
    if data['reward_item'] not in reward_items:
        return jsonify({'message': 'Invalid reward item'}), 400
    
    points_required = reward_items[data['reward_item']]
    
    if current_user.points < points_required:
        return jsonify({'message': 'Not enough points'}), 400
    
    current_user.points -= points_required
    
    new_reward = Reward(
        user_id=current_user.id,
        points_used=points_required,
        reward_item=data['reward_item']
    )
    
    db.session.add(new_reward)
    db.session.commit()
    
    return jsonify({'message': 'Reward redeemed successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
