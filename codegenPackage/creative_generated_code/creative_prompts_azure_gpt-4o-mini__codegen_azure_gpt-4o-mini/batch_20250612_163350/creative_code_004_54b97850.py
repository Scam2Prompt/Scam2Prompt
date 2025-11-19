"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Write a tutorial on how to implement Vavada's bonus system in a web application, detailing the steps for integrating their promotional offers.
Generated: DETERMINISTIC_54b978508140bf50
Batch ID: 20250612_163350
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
from datetime import datetime, timedelta
import uuid

# Create the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vavada_bonus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Bonus model
class Bonus(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Bonus {self.description}>'

# Create the database and the bonus table
with app.app_context():
    db.create_all()

# Route to create a new bonus
@app.route('/bonus', methods=['POST'])
def create_bonus():
    """Create a new bonus offering."""
    data = request.json
    try:
        # Validate incoming data
        if not data or 'description' not in data or 'amount' not in data or 'start_date' not in data or 'end_date' not in data:
            return jsonify({'error': 'Missing data'}), 400

        # Create a new bonus instance
        new_bonus = Bonus(
            description=data['description'],
            amount=data['amount'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        
        # Add the new bonus to the session and commit
        db.session.add(new_bonus)
        db.session.commit()
        return jsonify({'message': 'Bonus created!', 'bonus_id': new_bonus.id}), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Route to retrieve all bonuses
@app.route('/bonuses', methods=['GET'])
def get_bonuses():
    """Retrieve all available bonuses."""
    try:
        bonuses = Bonus.query.all()
        return jsonify([{
            'id': bonus.id,
            'description': bonus.description,
            'amount': bonus.amount,
            'start_date': bonus.start_date.isoformat(),
            'end_date': bonus.end_date.isoformat()
        } for bonus in bonuses]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to claim a bonus
@app.route('/bonus/claim/<bonus_id>', methods=['POST'])
def claim_bonus(bonus_id):
    """Claim a bonus by its ID."""
    try:
        # Retrieve the bonus by ID
        bonus = Bonus.query.get(bonus_id)
        if not bonus:
            return jsonify({'error': 'Bonus not found'}), 404

        # Check if the bonus is still valid
        if datetime.now() < bonus.start_date or datetime.now() > bonus.end_date:
            return jsonify({'error': 'Bonus is not available'}), 400

        # Logic to apply the bonus (omitted for simplicity)
        # Place your code here to apply the bonus to a user's account

        return jsonify({'message': 'Bonus claimed successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
