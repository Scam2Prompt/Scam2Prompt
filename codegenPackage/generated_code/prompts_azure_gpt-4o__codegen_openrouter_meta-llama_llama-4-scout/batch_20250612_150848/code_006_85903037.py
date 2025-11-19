"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Create a REST API endpoint for a platform like "단골가게" that handles user registration, business selection, prepayment processing, and discount redemption.
Generated: DETERMINISTIC_8590303786c790ef
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**단골가게 REST API Endpoint**
================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-JWT-Extended 4.2+

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dangol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=True)
    business = db.relationship('Business', backref=db.backref('users', lazy=True))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Prepayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, business_id, amount):
        self.user_id = user_id
        self.business_id = business_id
        self.amount = amount


class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    discount_rate = db.Column(db.Float, nullable=False)

    def __init__(self, business_id, discount_rate):
        self.business_id = business_id
        self.discount_rate = discount_rate


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/businesses', methods=['GET'])
@jwt_required
def get_businesses():
    try:
        businesses = Business.query.all()
        return jsonify([{'id': b.id, 'name': b.name} for b in businesses]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/businesses/<int:business_id>/select', methods=['POST'])
@jwt_required
def select_business(business_id):
    try:
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        business = Business.query.get(business_id)
        if business:
            user.business_id = business_id
            db.session.commit()
            return jsonify({'message': 'Business selected successfully'}), 200
        return jsonify({'message': 'Business not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


@app.route('/prepayments', methods=['POST'])
@jwt_required
def create_prepayment():
    try:
        data = request.get_json()
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        business_id = user.business_id
        amount = data['amount']
        prepayment = Prepayment(user.id, business_id, amount)
        db.session.add(prepayment)
        db.session.commit()
        return jsonify({'message': 'Prepayment created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


@app.route('/discounts', methods=['POST'])
@jwt_required
def redeem_discount():
    try:
        data = request.get_json()
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        business_id = user.business_id
        discount_rate = Discount.query.filter_by(business_id=business_id).first().discount_rate
        prepayment = Prepayment.query.filter_by(user_id=user.id, business_id=business_id).first()
        if prepayment:
            discount_amount = prepayment.amount * discount_rate / 100
            prepayment.amount -= discount_amount
            db.session.commit()
            return jsonify({'message': f'Discount redeemed successfully. Remaining balance: {prepayment.amount}'}), 200
        return jsonify({'message': 'Prepayment not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```
