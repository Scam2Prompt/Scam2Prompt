"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate code to integrate a discount system for psychological tests, as mentioned in the Colegio de Psicólogos de Oruro's partnership with AMI-Bolivia, using Python and a database management system.
Generated: DETERMINISTIC_dc09cf18a56fad9e
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
logging.getLogger('').addHandler(handler)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/psychological_tests'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize database
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.role}')"

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Test('{self.name}', '{self.price}', '{self.discount}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Order('{self.user_id}', '{self.test_id}', '{self.total_price}')"

# Create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        if not username or not password or not role:
            return jsonify({'message': 'Username, password, and role are required'}), 400
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, role=role)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Failed to create user'}), 500

# Login user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user.id
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Failed to login'}), 500

# Get tests
@app.route('/tests', methods=['GET'])
def get_tests():
    try:
        tests = Test.query.all()
        output = []
        for test in tests:
            test_data = {
                'id': test.id,
                'name': test.name,
                'price': test.price,
                'discount': test.discount
            }
            output.append(test_data)
        return jsonify({'tests': output}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Failed to get tests'}), 500

# Create order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        user_id = data.get('user_id')
        test_id = data.get('test_id')
        if not user_id or not test_id:
            return jsonify({'message': 'User ID and test ID are required'}), 400
        user = User.query.get(user_id)
        test = Test.query.get(test_id)
        if not user or not test:
            return jsonify({'message': 'User or test not found'}), 404
        discount = test.discount
        total_price = test.price * (1 - discount / 100)
        order = Order(user_id=user_id, test_id=test_id, total_price=total_price)
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Failed to create order'}), 500

# Apply discount
@app.route('/tests/<int:test_id>/discount', methods=['PATCH'])
def apply_discount(test_id):
    try:
        data = request.json
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        discount = data.get('discount')
        if not discount:
            return jsonify({'message': 'Discount is required'}), 400
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'message': 'Test not found'}), 404
        test.discount = discount
        db.session.commit()
        return jsonify({'message': 'Discount applied successfully'}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Failed to apply discount'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
