"""
Generated Code Metadata:
========================
Original URL: https://a.aciumreward.com
Prompt: Generate a code snippet for implementing a reward system API similar to Acium Reward.
Generated: DETERMINISTIC_114d70e96d08c9ab
Batch ID: 20250612_155651
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
    user_id = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reward {self.id} for User {self.user_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/rewards', methods=['POST'])
def create_reward():
    """Create a new reward for a user."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'user_id' not in data or 'points' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_reward = Reward(user_id=data['user_id'], points=data['points'])
    
    try:
        db.session.add(new_reward)
        db.session.commit()
        return jsonify({'message': 'Reward created successfully', 'reward': new_reward.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create reward, user may not exist'}), 400

@app.route('/rewards/<int:user_id>', methods=['GET'])
def get_rewards(user_id):
    """Retrieve all rewards for a specific user."""
    rewards = Reward.query.filter_by(user_id=user_id).all()
    return jsonify({'user_id': user_id, 'rewards': [{'id': r.id, 'points': r.points} for r in rewards]}), 200

@app.route('/rewards/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    """Delete a specific reward by ID."""
    reward = Reward.query.get(reward_id)
    
    if reward is None:
        return jsonify({'error': 'Reward not found'}), 404

    db.session.delete(reward)
    db.session.commit()
    return jsonify({'message': 'Reward deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
