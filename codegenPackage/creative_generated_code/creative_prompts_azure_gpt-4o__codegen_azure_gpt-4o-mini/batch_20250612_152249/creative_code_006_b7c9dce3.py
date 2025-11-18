"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawfuryclaim.pages.dev
Prompt: Create a referral system for the PawFury platform that tracks referrals and rewards users based on the referral information provided on the website.
Generated: DETERMINISTIC_b7c9dce3b5aa36a7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import uuid

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Referral model
class Referral(db.Model):
    id = db.Column(db.String(36), primary_key=True)  # UUID for unique identification
    referrer_email = db.Column(db.String(120), nullable=False)  # Email of the referrer
    referred_email = db.Column(db.String(120), nullable=False)  # Email of the referred user
    reward_claimed = db.Column(db.Boolean, default=False)  # Status of reward claim

    def __repr__(self):
        return f'<Referral {self.id}>'

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to handle referrals
@app.route('/referral', methods=['POST'])
def create_referral():
    '''Creates a new referral entry in the database.'''
    data = request.json
    
    # Validate input data
    if 'referrer_email' not in data or 'referred_email' not in data:
        return jsonify({'error': 'referrer_email and referred_email are required'}), 400
    
    referrer_email = data['referrer_email']
    referred_email = data['referred_email']

    # Generate a unique referral ID
    referral_id = str(uuid.uuid4())

    # Create a new referral instance
    new_referral = Referral(id=referral_id, referrer_email=referrer_email, referred_email=referred_email)

    try:
        # Add the new referral to the session and commit
        db.session.add(new_referral)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Referral already exists'}), 409

    # Return success response
    return jsonify({'message': 'Referral created successfully', 'referral_id': referral_id}), 201

# Endpoint to claim a reward
@app.route('/referral/claim/<string:referral_id>', methods=['POST'])
def claim_reward(referral_id):
    '''Claims the reward for a specific referral.'''
    referral = Referral.query.get(referral_id)
    
    # Check if the referral exists
    if referral is None:
        return jsonify({'error': 'Referral not found'}), 404
    
    # Check if reward is already claimed
    if referral.reward_claimed:
        return jsonify({'error': 'Reward already claimed'}), 400

    # Update the reward status
    referral.reward_claimed = True
    db.session.commit()

    # Return success response
    return jsonify({'message': 'Reward claimed successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
