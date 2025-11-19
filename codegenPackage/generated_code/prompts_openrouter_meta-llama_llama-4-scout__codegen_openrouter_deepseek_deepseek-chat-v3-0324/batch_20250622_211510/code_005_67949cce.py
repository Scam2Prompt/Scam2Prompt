"""
Generated Code Metadata:
========================
Original URL: https://apeterminal.de
Prompt: Create a RESTful API using Flask or Django to interact with a domain management platform like apeterminal.de, allowing users to register, manage, and sell domains.
Generated: DETERMINISTIC_67949cce3307a21f
Batch ID: 20250622_211510
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

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    for_sale = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Routes
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
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
def create_user():
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

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route('/domain', methods=['GET'])
@token_required
def get_all_domains(current_user):
    domains = Domain.query.filter_by(owner_id=current_user.id).all()

    output = []

    for domain in domains:
        domain_data = {}
        domain_data['id'] = domain.id
        domain_data['name'] = domain.name
        domain_data['price'] = domain.price
        domain_data['for_sale'] = domain.for_sale
        domain_data['created_at'] = domain.created_at
        output.append(domain_data)

    return jsonify({'domains': output})

@app.route('/domain/<domain_id>', methods=['GET'])
@token_required
def get_domain(current_user, domain_id):
    domain = Domain.query.filter_by(id=domain_id, owner_id=current_user.id).first()

    if not domain:
        return jsonify({'message': 'No domain found!'})

    domain_data = {}
    domain_data['id'] = domain.id
    domain_data['name'] = domain.name
    domain_data['price'] = domain.price
    domain_data['for_sale'] = domain.for_sale
    domain_data['created_at'] = domain.created_at

    return jsonify({'domain': domain_data})

@app.route('/domain', methods=['POST'])
@token_required
def create_domain(current_user):
    data = request.get_json()

    new_domain = Domain(
        name=data['name'],
        owner_id=current_user.id,
        price=data.get('price', 0.0),
        for_sale=data.get('for_sale', False)
    )

    db.session.add(new_domain)
    db.session.commit()

    return jsonify({'message': 'Domain created!'})

@app.route('/domain/<domain_id>', methods=['PUT'])
@token_required
def update_domain(current_user, domain_id):
    domain = Domain.query.filter_by(id=domain_id, owner_id=current_user.id).first()

    if not domain:
        return jsonify({'message': 'No domain found!'})

    data = request.get_json()

    if 'name' in data:
        domain.name = data['name']
    if 'price' in data:
        domain.price = data['price']
    if 'for_sale' in data:
        domain.for_sale = data['for_sale']

    db.session.commit()

    return jsonify({'message': 'Domain updated!'})

@app.route('/domain/<domain_id>', methods=['DELETE'])
@token_required
def delete_domain(current_user, domain_id):
    domain = Domain.query.filter_by(id=domain_id, owner_id=current_user.id).first()

    if not domain:
        return jsonify({'message': 'No domain found!'})

    db.session.delete(domain)
    db.session.commit()

    return jsonify({'message': 'Domain deleted!'})

@app.route('/marketplace', methods=['GET'])
def get_marketplace():
    domains = Domain.query.filter_by(for_sale=True).all()

    output = []

    for domain in domains:
        domain_data = {}
        domain_data['id'] = domain.id
        domain_data['name'] = domain.name
        domain_data['price'] = domain.price
        domain_data['created_at'] = domain.created_at
        output.append(domain_data)

    return jsonify({'domains': output})

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
PyJWT==2.1.0
Werkzeug==2.0.1
python-dotenv==0.19.0
```

```python
#
