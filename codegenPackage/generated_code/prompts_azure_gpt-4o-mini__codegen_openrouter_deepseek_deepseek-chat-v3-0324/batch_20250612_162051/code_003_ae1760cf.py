"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Develop a RESTful API that manages travel packages and itineraries, ensuring it includes features for group travel and local community engagement, as emphasized by Rehiletes.
Generated: DETERMINISTIC_ae1760cf5022d42c
Batch ID: 20250612_162051
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
from flask_marshmallow import Marshmallow
import uuid
import datetime
from functools import wraps
import jwt

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class TravelPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in days
    group_size = db.Column(db.Integer, nullable=False)
    community_engagement = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    travel_package_id = db.Column(db.Integer, db.ForeignKey('travel_package.id'), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    activities = db.Column(db.String(500))

# Marshmallow Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'name', 'email', 'admin')

class TravelPackageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'duration', 'group_size', 'community_engagement')

class ItinerarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'travel_package_id', 'day', 'description', 'activities')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
travel_package_schema = TravelPackageSchema()
travel_packages_schema = TravelPackageSchema(many=True)
itinerary_schema = ItinerarySchema()
itineraries_schema = ItinerarySchema(many=True)

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
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        admin=False
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    return user_schema.jsonify(user)

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    result = users_schema.dump(users)

    return jsonify(result)

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

# Login Route
@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return jsonify({'message': 'Could not verify'}), 401

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify'}), 401

# Travel Package Routes
@app.route('/package', methods=['POST'])
@token_required
def create_package(current_user):
    data = request.get_json()

    new_package = TravelPackage(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        duration=data['duration'],
        group_size=data['group_size'],
        community_engagement=data.get('community_engagement', False),
        created_by=current_user.id
    )

    db.session.add(new_package)
    db.session.commit()

    return travel_package_schema.jsonify(new_package)

@app.route('/package', methods=['GET'])
def get_all_packages():
    packages = TravelPackage.query.all()
    result = travel_packages_schema.dump(packages)

    return jsonify(result)

@app.route('/package/<package_id>', methods=['GET'])
def get_one_package(package_id):
    package = TravelPackage.query.get(package_id)

    if not package:
        return jsonify({'message': 'No package found!'})

    return travel_package_schema.jsonify(package)

@app.route('/package/<package_id>', methods=['PUT'])
@token_required
def update_package(current_user, package_id):
    package = TravelPackage.query.get(package_id)

    if not package:
        return jsonify({'message': 'No package found!'})

    if package.created_by != current_user.id and not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    package.name = data.get('name', package.name)
    package.description = data.get('description', package.description)
    package.price = data.get('price', package.price)
    package.duration = data.get('duration', package.duration)
    package.group_size = data.get('group_size', package.group_size)
    package.community_engagement = data.get('community_engagement', package.community_engagement)

    db.session.commit()

    return travel_package_schema.jsonify(package)

@app.route('/package/<package_id>', methods=['DELETE'])
@token_required
def delete_package(current_user, package_id):
    package = TravelPackage.query.get(package_id)

    if not package:
        return jsonify({'message': 'No package found!'})

    if package.created_by != current_user.id and not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    db.session.delete(package)
    db.session.commit()

    return jsonify({'message': 'Package deleted!'})

# Itinerary Routes
@app.route('/package/<package_id>/itinerary', methods=['POST'])
@token_required
def create_itinerary(current_user, package_id):
    package = TravelPackage.query.get(package_id)

    if not package:
        return jsonify({'message': 'No package found!'})

    if package.created_by != current_user.id and not current_user.admin
