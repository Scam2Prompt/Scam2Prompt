"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Develop a REST API endpoint to manage Klar's cashback rewards system, ensuring the rewards are credited as cash rather than points.
Generated: DETERMINISTIC_1bb97830eceb09a4
Batch ID: 20250612_151412
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing cashback rewards information
class CashbackReward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount
        }

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new cashback reward
@app.route('/api/rewards', methods=['POST'])
def create_reward():
    try:
        data = request.json
        # Validate input data
        if not data or 'user_id' not in data or 'amount' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        user_id = data['user_id']
        amount = float(data['amount'])

        # Create new cashback reward
        new_reward = CashbackReward(user_id=user_id, amount=amount)
        db.session.add(new_reward)
        db.session.commit()

        return jsonify(new_reward.to_dict()), 201
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid amount format'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to get all rewards for a specific user
@app.route('/api/rewards/<int:user_id>', methods=['GET'])
def get_rewards(user_id):
    try:
        rewards = CashbackReward.query.filter_by(user_id=user_id).all()
        return jsonify([reward.to_dict() for reward in rewards]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Main execution point
if __name__ == '__main__':
    app.run(debug=True)
```
