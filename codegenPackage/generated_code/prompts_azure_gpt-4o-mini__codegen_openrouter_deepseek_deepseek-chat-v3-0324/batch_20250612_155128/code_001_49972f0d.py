"""
Generated Code Metadata:
========================
Original URL: https://delta.money
Prompt: Write a code snippet for a web application that allows users to make offers on domain names, inspired by the Delta.Money acquisition model.
Generated: DETERMINISTIC_49972f0d04d9038c
Batch ID: 20250612_155128
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import re
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Domain name validation regex
DOMAIN_REGEX = re.compile(
    r'^([a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$'
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DomainOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(255), nullable=False)
    offer_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='USD')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('offers', lazy=True))

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400

    user = User(email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/api/offers', methods=['POST'])
@jwt_required()
def create_offer():
    data = request.get_json()
    if not data or 'domain_name' not in data or 'offer_amount' not in data:
        return jsonify({'error': 'Domain name and offer amount are required'}), 400

    if not DOMAIN_REGEX.match(data['domain_name']):
        return jsonify({'error': 'Invalid domain name format'}), 400

    try:
        offer_amount = float(data['offer_amount'])
        if offer_amount <= 0:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Offer amount must be a positive number'}), 400

    user_id = get_jwt_identity()
    offer = DomainOffer(
        domain_name=data['domain_name'],
        offer_amount=offer_amount,
        currency=data.get('currency', 'USD'),
        user_id=user_id
    )
    db.session.add(offer)
    db.session.commit()

    return jsonify({
        'message': 'Offer created successfully',
        'offer_id': offer.id
    }), 201

@app.route('/api/offers', methods=['GET'])
@jwt_required()
def get_user_offers():
    user_id = get_jwt_identity()
    offers = DomainOffer.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': offer.id,
        'domain_name': offer.domain_name,
        'offer_amount': offer.offer_amount,
        'currency': offer.currency,
        'status': offer.status,
        'created_at': offer.created_at.isoformat()
    } for offer in offers]), 200

@app.route('/api/offers/<int:offer_id>', methods=['DELETE'])
@jwt_required()
def delete_offer(offer_id):
    user_id = get_jwt_identity()
    offer = DomainOffer.query.filter_by(id=offer_id, user_id=user_id).first()
    if not offer:
        return jsonify({'error': 'Offer not found'}), 404

    db.session.delete(offer)
    db.session.commit()
    return jsonify({'message': 'Offer deleted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
