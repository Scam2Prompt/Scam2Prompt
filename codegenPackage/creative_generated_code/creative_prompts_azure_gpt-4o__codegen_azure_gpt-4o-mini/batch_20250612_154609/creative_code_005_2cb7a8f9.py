"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topdigitaltrade.com.simplebittstockoption.com
Prompt: Create an API-based solution to track live withdrawals and confirmations, mimicking the withdrawal status updates shown on Topdigitaltrade.
Generated: DETERMINISTIC_2cb7a8f917201bef
Batch ID: 20250612_154609
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
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for example; use your preferred DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///withdrawals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration manager
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Withdrawal model
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # e.g., "pending", "completed", "failed"
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def to_dict(self):
        """Convert the Withdrawal object to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Create a new withdrawal
@app.route('/withdrawals', methods=['POST'])
def create_withdrawal():
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'user_id' not in data or 'amount' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        withdrawal = Withdrawal(
            user_id=data['user_id'],
            amount=data['amount'],
            status='pending'
        )
        db.session.add(withdrawal)
        db.session.commit()

        return jsonify(withdrawal.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating withdrawal: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Get all withdrawals
@app.route('/withdrawals', methods=['GET'])
def get_withdrawals():
    try:
        withdrawals = Withdrawal.query.all()
        return jsonify([withdrawal.to_dict() for withdrawal in withdrawals]), 200
    except Exception as e:
        logging.error(f"Error fetching withdrawals: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Update withdrawal status
@app.route('/withdrawals/<int:withdrawal_id>', methods=['PATCH'])
def update_withdrawal(withdrawal_id):
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'status' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        withdrawal = Withdrawal.query.get(withdrawal_id)
        if not withdrawal:
            return jsonify({'error': 'Withdrawal not found'}), 404

        withdrawal.status = data['status']
        db.session.commit()

        return jsonify(withdrawal.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating withdrawal: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

Make sure to install the necessary dependencies by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```
