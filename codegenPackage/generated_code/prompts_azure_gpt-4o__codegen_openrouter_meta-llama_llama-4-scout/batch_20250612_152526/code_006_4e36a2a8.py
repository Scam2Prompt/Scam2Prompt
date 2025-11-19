"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a system that enables communication between bookkeepers and clients, allowing clients to make smart business decisions based on real-time financial data, as emphasized by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_4e36a2a8da98f9d6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Create a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookkeeping.db'
app.config['SECRET_KEY'] = 'secret_key_here'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"

# Define the FinancialData model
class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, client_id, data):
        self.client_id = client_id
        self.data = data

    def __repr__(self):
        return f"FinancialData('{self.client_id}', '{self.data}')"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        new_user = User(data['username'], data['email'], data['password'], data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Login a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get financial data for a client
@app.route('/financial_data', methods=['GET'])
def get_financial_data():
    try:
        token = request.headers['Authorization'].split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        if user.role == 'client':
            financial_data = FinancialData.query.filter_by(client_id=user.id).all()
            return jsonify([{'data': data.data, 'timestamp': data.timestamp} for data in financial_data]), 200
        else:
            return jsonify({'message': 'Forbidden'}), 403
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Add financial data for a client
@app.route('/financial_data', methods=['POST'])
def add_financial_data():
    try:
        token = request.headers['Authorization'].split()[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        if user.role == 'bookkeeper':
            data = request.json
            new_data = FinancialData(data['client_id'], data['data'])
            db.session.add(new_data)
            db.session.commit()
            return jsonify({'message': 'Financial data added successfully'}), 201
        else:
            return jsonify({'message': 'Forbidden'}), 403
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
