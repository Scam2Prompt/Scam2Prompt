"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soldragon.vercel.app
Prompt: How can I implement a wallet submission feature for a gaming application that rewards users with $SHEN tokens after collecting coins?
Generated: DETERMINISTIC_224ddb02f25f1172
Batch ID: 20250612_161520
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
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for storing wallet submissions
class WalletSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    coin_amount = db.Column(db.Integer, nullable=False)
    shen_reward = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<WalletSubmission {self.user_id}: {self.shen_reward} SHEN>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/submit-wallet', methods=['POST'])
def submit_wallet():
    """Endpoint to submit wallet for rewards."""
    try:
        # Get request data
        data = request.get_json()

        # Validate request data
        user_id = data.get('user_id')
        coin_amount = data.get('coin_amount')

        if not user_id or not isinstance(coin_amount, int) or coin_amount <= 0:
            return jsonify({'error': 'Invalid input provided'}), 400

        # Calculate the reward (1 SHEN for every 10 coins)
        shen_reward = coin_amount / 10.0

        # Create a new wallet submission record
        new_submission = WalletSubmission(user_id=user_id, coin_amount=coin_amount, shen_reward=shen_reward)

        # Add to the database
        db.session.add(new_submission)
        db.session.commit()

        # Log the successful submission
        logging.info(f'Wallet submitted successfully: User {user_id}, Reward {shen_reward} SHEN')

        # Return response
        return jsonify({'message': 'Wallet submission successful', 'reward': shen_reward}), 201

    except SQLAlchemyError as e:
        logging.error(f'Database error occurred: {e}')
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
