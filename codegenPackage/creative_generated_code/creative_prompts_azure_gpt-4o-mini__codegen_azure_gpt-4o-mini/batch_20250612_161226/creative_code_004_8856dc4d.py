"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Suggest an API for monitoring cryptocurrency mining performance specifically for BTC, XRP, and SOL, including user deposit and withdrawal activities.
Generated: DETERMINISTIC_8856dc4d26d42a84
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_mining.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the User model for deposit and withdrawal activities
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    btc_balance = db.Column(db.Float, default=0.0)
    xrp_balance = db.Column(db.Float, default=0.0)
    sol_balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f"<User {self.username}>"

# Define the endpoint for creating a user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 409

# Define the endpoint for depositing cryptocurrency
@app.route('/api/users/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    
    # Update the user's balance based on the cryptocurrency and amount
    crypto_type = data['crypto_type']
    amount = data['amount']
    
    if crypto_type == 'BTC':
        user.btc_balance += amount
    elif crypto_type == 'XRP':
        user.xrp_balance += amount
    elif crypto_type == 'SOL':
        user.sol_balance += amount
    else:
        return jsonify({'error': 'Invalid cryptocurrency type'}), 400

    db.session.commit()
    return jsonify({'message': 'Deposit successful'}), 200

# Define the endpoint for withdrawing cryptocurrency
@app.route('/api/users/<int:user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    
    # Update the user's balance based on the cryptocurrency and amount
    crypto_type = data['crypto_type']
    amount = data['amount']
    
    if crypto_type == 'BTC':
        if user.btc_balance < amount:
            return jsonify({'error': 'Insufficient BTC balance'}), 400
        user.btc_balance -= amount
    elif crypto_type == 'XRP':
        if user.xrp_balance < amount:
            return jsonify({'error': 'Insufficient XRP balance'}), 400
        user.xrp_balance -= amount
    elif crypto_type == 'SOL':
        if user.sol_balance < amount:
            return jsonify({'error': 'Insufficient SOL balance'}), 400
        user.sol_balance -= amount
    else:
        return jsonify({'error': 'Invalid cryptocurrency type'}), 400

    db.session.commit()
    return jsonify({'message': 'Withdrawal successful'}), 200

# Define the endpoint for monitoring mining performance
@app.route('/api/mining/performance', methods=['GET'])
def get_mining_performance():
    # Example performance metrics (dummy data)
    performance_metrics = {
        'BTC': {'hashrate': '100 TH/s', 'uptime': '99.9%'},
        'XRP': {'hashrate': '10 TH/s', 'uptime': '99.8%'},
        'SOL': {'hashrate': '30 TH/s', 'uptime': '99.7%'}
    }
    return jsonify(performance_metrics), 200

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True, host='0.0.0.0', port=5000)
```
