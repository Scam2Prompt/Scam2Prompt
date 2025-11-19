"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasenow.org
Prompt: What are the best practices for developing a sports betting platform that supports Bitcoin transactions for users in Korea?
Generated: DETERMINISTIC_7214ebbd2437bb94
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sports_betting_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///betting_platform.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Bet Model
class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    outcome = db.Column(db.String(120), nullable=False)

# Endpoint to create a user
@app.route('/api/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data.get('username')
        
        if not username:
            return jsonify({"error": "Username is required"}), 400

        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        
        logger.info(f"User {username} registered successfully.")
        return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201

    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({"error": "An error occurred while registering the user."}), 500

# Endpoint to place a bet
@app.route('/api/bet', methods=['POST'])
def place_bet():
    try:
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')
        outcome = data.get('outcome')

        if not user_id or amount is None or not outcome:
            return jsonify({"error": "user_id, amount, and outcome are required"}), 400

        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        if user.balance < amount:
            return jsonify({"error": "Insufficient balance"}), 400

        # Deduct from user's balance
        user.balance -= amount
        new_bet = Bet(user_id=user_id, amount=amount, outcome=outcome)
        db.session.add(new_bet)
        db.session.commit()

        logger.info(f"User {user.username} placed a bet of {amount} on {outcome}.")
        return jsonify({"message": "Bet placed successfully", "bet_id": new_bet.id}), 201

    except Exception as e:
        logger.error(f"Error placing bet: {e}")
        return jsonify({"error": "An error occurred while placing the bet."}), 500

# Endpoint to get user balance
@app.route('/api/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"balance": user.balance}), 200

    except Exception as e:
        logger.error(f"Error retrieving balance for user {user_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the balance."}), 500

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-CORS

### Environment Variables
- DATABASE_URI: Set this variable to your preferred database URI for production use.
