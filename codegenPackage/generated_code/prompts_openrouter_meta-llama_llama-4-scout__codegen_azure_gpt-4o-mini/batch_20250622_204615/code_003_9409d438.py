"""
Generated Code Metadata:
========================
Original URL: https://p-1px.pages.dev
Prompt: Design an API for interacting with the Over Protocol, including endpoints for user registration, wallet management, and node operation.
Generated: DETERMINISTIC_9409d43818944f9b
Batch ID: 20250622_204615
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
import uuid

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///over_protocol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for registration and authentication
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Wallet model for managing user wallets
class Wallet(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Node operation model for tracking node status
class NodeOperation(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    operation_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Wallet management endpoint
@app.route('/wallet/<user_id>', methods=['GET', 'POST'])
def manage_wallet(user_id):
    if request.method == 'POST':
        data = request.get_json()
        amount = data.get('amount', 0.0)

        if amount < 0:
            return jsonify({'error': 'Amount must be non-negative.'}), 400

        wallet = Wallet.query.filter_by(user_id=user_id).first()
        if not wallet:
            wallet = Wallet(user_id=user_id)
            db.session.add(wallet)

        wallet.balance += amount
        db.session.commit()

        return jsonify({'message': 'Wallet updated successfully.', 'balance': wallet.balance}), 200

    elif request.method == 'GET':
        wallet = Wallet.query.filter_by(user_id=user_id).first()
        if not wallet:
            return jsonify({'error': 'Wallet not found.'}), 404

        return jsonify({'balance': wallet.balance}), 200

# Node operation endpoint
@app.route('/node/<user_id>', methods=['POST'])
def operate_node(user_id):
    data = request.get_json()
    operation_type = data.get('operation_type')

    if not operation_type:
        return jsonify({'error': 'Operation type is required.'}), 400

    new_operation = NodeOperation(user_id=user_id, operation_type=operation_type, status='initiated')
    db.session.add(new_operation)
    db.session.commit()

    return jsonify({'message': 'Node operation initiated.', 'operation_id': new_operation.id}), 201

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
