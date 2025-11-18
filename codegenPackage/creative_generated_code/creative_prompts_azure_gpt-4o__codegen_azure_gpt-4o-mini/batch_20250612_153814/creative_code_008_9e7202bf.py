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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import logging

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///rewards.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(100), unique=True, nullable=False)
    rewards = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.id}, Invite Code: {self.invite_code}, Rewards: {self.rewards}>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/invite', methods=['POST'])
def handle_invite():
    """
    Handle the reward distribution when an invite code is used.
    Expects JSON body with 'invite_code', 'user_id', and 'reward_amount'.
    """
    data = request.json
    
    # Validate input data
    invite_code = data.get('invite_code')
    user_id = data.get('user_id')
    reward_amount = data.get('reward_amount')

    if not invite_code or not user_id or not isinstance(reward_amount, int):
        return jsonify({'error': 'Invalid input data.'}), 400

    try:
        # Find the user with the provided invite code
        user = User.query.filter_by(invite_code=invite_code).first()
        
        if user is None:
            return jsonify({'error': 'Invite code not found.'}), 404

        # Update rewards
        user.rewards += reward_amount
        db.session.commit()

        return jsonify({'message': 'Rewards successfully distributed.', 'new_rewards': user.rewards}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error occurred.'}), 500
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the app in production mode
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), threaded=True)
```
