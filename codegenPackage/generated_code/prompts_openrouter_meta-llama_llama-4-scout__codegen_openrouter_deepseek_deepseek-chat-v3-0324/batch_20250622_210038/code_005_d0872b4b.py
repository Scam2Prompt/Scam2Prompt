"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Develop a RESTful API for managing IPTV services, including user authentication, package management, and streaming content delivery, using a framework like Flask or Django.
Generated: DETERMINISTIC_d0872b4b1ef23fb4
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iptv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Float)
    channels = db.Column(db.Integer)
    description = db.Column(db.String(200))

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(200))
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'))

# Decorator for token verification
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
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data['username'],
        password=hashed_password,
        admin=False
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
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

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# Package Routes
@app.route('/package', methods=['GET'])
@token_required
def get_all_packages(current_user):
    packages = Package.query.all()
    output = []

    for package in packages:
        package_data = {}
        package_data['id'] = package.id
        package_data['name'] = package.name
        package_data['price'] = package.price
        package_data['channels'] = package.channels
        package_data['description'] = package.description
        output.append(package_data)

    return jsonify({'packages': output})

@app.route('/package/<package_id>', methods=['GET'])
@token_required
def get_one_package(current_user, package_id):
    package = Package.query.filter_by(id=package_id).first()

    if not package:
        return jsonify({'message': 'No package found!'})

    package_data = {}
    package_data['id'] = package.id
    package_data['name'] = package.name
    package_data['price'] = package.price
    package_data['channels'] = package.channels
    package_data['description'] = package.description

    return jsonify({'package': package_data})

@app.route('/package', methods=['POST'])
@token_required
def create_package(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    new_package = Package(
        name=data['name'],
        price=data['price'],
        channels=data['channels'],
        description=data['description']
    )
    db.session.add(new_package)
    db.session.commit()

    return jsonify({'message': 'New package created!'})

@app.route('/package/<package_id>', methods=['PUT'])
@token_required
def update_package(current_user, package_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    package = Package.query.filter_by(id=package_id).first()

    if not package:
        return jsonify({'message': 'No package found!'})

    data = request.get_json()
    package.name = data['name']
    package.price = data['price']
    package.channels = data['channels']
    package.description = data['description']
    db.session.commit()

    return jsonify({'message': 'Package has been updated!'})

@app.route('/package/<package_id>', methods=['DELETE'])
@token_required
def delete_package(current_user, package_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    package = Package.query.filter_by(id=package_id).first()

    if not package:
        return jsonify({'message': 'No package found!'})

    db.session.delete(package)
    db.session.commit()

    return jsonify({'message': 'Package has been deleted!'})

# Channel Routes
@app.route('/channel', methods=['GET'])
@token_required
def get_all_channels(current_user):
    channels = Channel.query.all()
    output = []

    for channel in channels:
        channel_data = {}
        channel_data['id'] = channel.id
        channel_data['name'] = channel.name
        channel_data['url'] = channel.url
        channel_data['package_id'] = channel.package_id
        output.append(channel_data)

    return jsonify({'channels': output})

@app.route('/channel/<channel_id>', methods=['GET'])
@token_required
def get_one_channel(current_user,
