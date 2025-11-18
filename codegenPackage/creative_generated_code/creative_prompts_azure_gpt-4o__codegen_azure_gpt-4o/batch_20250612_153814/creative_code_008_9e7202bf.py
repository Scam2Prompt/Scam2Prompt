"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Implement a secure backend system to handle reward distribution ("サンクス列") when invite codes are used, as described on https://wc.innovie-corp.com.
Generated: DETERMINISTIC_9e7202bf4eb85792
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Models
class User(db.Model):
    """
    Represents a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    invite_code = db.Column(db.String(64), unique=True, nullable=False)
    rewards = db.Column(db.Integer, default=0)

class RewardLog(db.Model):
    """
    Logs the reward transactions for audit and tracking purposes.
    """
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(64), nullable=False)
    reward_amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Helper functions
def generate_invite_code(username):
    """
    Generate a secure invite code based on the username.
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(f"{username}{salt}".encode()).hexdigest()

def distribute_rewards(invite_code, reward_amount):
    """
    Distribute rewards to the user associated with the given invite code.
    """
    user = User.query.filter_by(invite_code=invite_code).first()
    if not user:
        return None, "Invalid invite code."
    
    user.rewards += reward_amount
    reward_log = RewardLog(invite_code=invite_code, reward_amount=reward_amount)
    
    db.session.add(reward_log)
    db.session.commit()
    
    return user, None

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user and generate an invite code for them.
    """
    data = request.json
    username = data.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        invite_code = generate_invite_code(username)
        new_user = User(username=username, invite_code=invite_code)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "invite_code": invite_code}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 400
    except Exception as e:
        logger.error(f"Error during registration: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/distribute_rewards', methods=['POST'])
def distribute_rewards_endpoint():
    """
    Endpoint to distribute rewards based on an invite code.
    """
    data = request.json
    invite_code = data.get('invite_code')
    reward_amount = data.get('reward_amount')
    
    if not invite_code or reward_amount is None:
        return jsonify({"error": "Invite code and reward amount are required"}), 400

    try:
        user, error = distribute_rewards(invite_code, reward_amount)
        if error:
            return jsonify({"error": error}), 400

        return jsonify({
            "message": "Reward distributed successfully",
            "username": user.username,
            "new_rewards_balance": user.rewards
        }), 200
    except Exception as e:
        logger.error(f"Error during reward distribution: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point
if __name__ == '__main__':
    # Ensure tables exist before running the app
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```
