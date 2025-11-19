"""
Generated Code Metadata:
========================
Original URL: https://mammoth-cxk.pages.dev
Prompt: Develop a brief API documentation for a service that provides information on token rewards for conservation efforts, inspired by the $MAMAI token's mission.
Generated: DETERMINISTIC_c90f27193576739b
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Token Rewards
class TokenReward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    tokens_earned = db.Column(db.Integer, nullable=False)
    conservation_effort = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the TokenReward object to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tokens_earned': self.tokens_earned,
            'conservation_effort': self.conservation_effort
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    """Retrieve all token rewards."""
    try:
        rewards = TokenReward.query.all()
        return jsonify([reward.to_dict() for reward in rewards]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/rewards', methods=['POST'])
def add_reward():
    """Add a new token reward."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'tokens_earned' not in data or 'conservation_effort' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_reward = TokenReward(
        user_id=data['user_id'],
        tokens_earned=data['tokens_earned'],
        conservation_effort=data['conservation_effort']
    )

    try:
        db.session.add(new_reward)
        db.session.commit()
        return jsonify(new_reward.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/rewards/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    """Delete a token reward by ID."""
    reward = TokenReward.query.get(reward_id)
    if not reward:
        return jsonify({'error': 'Reward not found'}), 404

    try:
        db.session.delete(reward)
        db.session.commit()
        return jsonify({'message': 'Reward deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
