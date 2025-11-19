"""
Generated Code Metadata:
========================
Original URL: https://a.aciumreward.com
Prompt: Suggest best practices for developing an API for a rewards management system based on Acium Reward's functionalities.
Generated: DETERMINISTIC_145e56de1e3cc161
Batch ID: 20250612_155651
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Reward model
class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    points = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Reward object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'points': self.points
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/rewards', methods=['POST'])
def create_reward():
    """Create a new reward."""
    data = request.get_json()
    if not data or 'name' not in data or 'points' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_reward = Reward(name=data['name'], points=data['points'])
    try:
        db.session.add(new_reward)
        db.session.commit()
        return jsonify(new_reward.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Reward already exists'}), 409

@app.route('/rewards', methods=['GET'])
def get_rewards():
    """Retrieve all rewards."""
    rewards = Reward.query.all()
    return jsonify([reward.to_dict() for reward in rewards]), 200

@app.route('/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    """Retrieve a specific reward by ID."""
    reward = Reward.query.get(reward_id)
    if reward is None:
        return jsonify({'error': 'Reward not found'}), 404
    return jsonify(reward.to_dict()), 200

@app.route('/rewards/<int:reward_id>', methods=['PUT'])
def update_reward(reward_id):
    """Update an existing reward."""
    reward = Reward.query.get(reward_id)
    if reward is None:
        return jsonify({'error': 'Reward not found'}), 404

    data = request.get_json()
    if 'name' in data:
        reward.name = data['name']
    if 'points' in data:
        reward.points = data['points']

    db.session.commit()
    return jsonify(reward.to_dict()), 200

@app.route('/rewards/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    """Delete a reward."""
    reward = Reward.query.get(reward_id)
    if reward is None:
        return jsonify({'error': 'Reward not found'}), 404

    db.session.delete(reward)
    db.session.commit()
    return jsonify({'message': 'Reward deleted successfully'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
