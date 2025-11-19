"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: Write a code snippet for an API that allows users to access their wages instantly, like Earnifi's instant earnings feature.
Generated: DETERMINISTIC_b79836605b0438c7
Batch ID: 20250612_135517
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Wage model
class Wage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'date': self.date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/wages', methods=['GET'])
def get_wages():
    """
    Retrieve the wages for a specific user.
    Query parameter: user_id (int) - The ID of the user whose wages are to be retrieved.
    Returns a JSON response with the user's wages or an error message.
    """
    user_id = request.args.get('user_id', type=int)

    if user_id is None:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        wages = Wage.query.filter_by(user_id=user_id).all()
        return jsonify([wage.to_dict() for wage in wages]), 200
    except Exception as e:
        logging.error(f"Error retrieving wages: {e}")
        return jsonify({'error': 'An error occurred while retrieving wages'}), 500

@app.route('/api/wages', methods=['POST'])
def add_wage():
    """
    Add a new wage entry for a user.
    Expects a JSON body with user_id (int) and amount (float).
    Returns a JSON response with the created wage or an error message.
    """
    data = request.get_json()

    if not data or 'user_id' not in data or 'amount' not in data:
        return jsonify({'error': 'user_id and amount are required'}), 400

    user_id = data['user_id']
    amount = data['amount']

    if not isinstance(user_id, int) or not isinstance(amount, (int, float)):
        return jsonify({'error': 'Invalid user_id or amount type'}), 400

    try:
        new_wage = Wage(user_id=user_id, amount=amount)
        db.session.add(new_wage)
        db.session.commit()
        return jsonify(new_wage.to_dict()), 201
    except Exception as e:
        logging.error(f"Error adding wage: {e}")
        return jsonify({'error': 'An error occurred while adding the wage'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
