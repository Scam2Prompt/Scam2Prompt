"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
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
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordoflife.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.String(20))  # e.g., 'member', 'leader', 'admin'
    join_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Ministry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    leader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    ministry_id = db.Column(db.Integer, db.ForeignKey('ministry.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    location = db.Column(db.String(100))
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Helper function for JWT token required decorator
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

# User Routes
@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['role'] = user.role
        output.append(user_data)

    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['role'] = user.role

    return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role='member'
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user.role = 'leader'
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted!'})

# Authentication Route
@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# Ministry Routes
@app.route('/ministry', methods=['GET'])
@token_required
def get_all_ministries(current_user):
    ministries = Ministry.query.all()
    output = []

    for ministry in ministries:
        ministry_data = {}
        ministry_data['id'] = ministry.id
        ministry_data['name'] = ministry.name
        ministry_data['description'] = ministry.description
        ministry_data['leader_id'] = ministry.leader_id
        output.append(ministry_data)

    return jsonify({'ministries': output})

@app.route('/ministry/<ministry_id>', methods=['GET'])
@token_required
def get_one_ministry(current_user, ministry_id):
    ministry = Ministry.query.filter_by(id=ministry_id).first()

    if not ministry:
        return jsonify({'message': 'No ministry found!'})

    ministry_data = {}
    ministry_data['id'] = ministry.id
    ministry_data['name'] = ministry.name
    ministry_data['description'] = ministry.description
    ministry_data['leader_id'] = ministry.leader_id

    return jsonify({'ministry': ministry_data})

@app.route('/ministry', methods=['POST'])
@token_required
def create_ministry(current_user):
    if current_user.role not in ['leader', 'admin']:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    new_ministry = Ministry(
        name=data['name'],
        description=data['description'],
        leader_id=current_user.id
    )

    db.session.add(new_ministry)
    db.session.commit()

    return jsonify({'message': 'New ministry created!'})

@app.route('/ministry/<ministry_id>', methods=['PUT'])
@token_required
def update_ministry(current_user, ministry_id):
    if current_user.role not in ['leader', 'admin']:
        return jsonify({'message': 'Cannot perform that function!'})

    ministry = Ministry.query.filter_by(id=ministry_id).first()

    if not ministry:
        return jsonify({'message': 'No ministry found!'})

    data = request.get_json()
    ministry.name = data['name']
    ministry.description = data['description']
    db.session.commit()

    return jsonify({'message': 'Ministry has been updated!'})

@app.route('/ministry/<ministry_id>', methods=['DELETE'])
@token_required
def delete_ministry(current_user, ministry_id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})

    ministry = Ministry.query.filter
