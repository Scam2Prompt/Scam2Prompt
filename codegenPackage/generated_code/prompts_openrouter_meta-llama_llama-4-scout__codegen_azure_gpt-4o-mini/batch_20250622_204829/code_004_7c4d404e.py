"""
Generated Code Metadata:
========================
Original URL: https://ethbod.com
Prompt: "Design an API for tracking Ethereum pledges, including endpoints for making pledges and retrieving pledge history."
Generated: DETERMINISTIC_7c4d404e85955993
Batch ID: 20250622_204829
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pledges.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Pledge model
class Pledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(42), nullable=False)  # Ethereum address
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Pledge object to a dictionary."""
        return {
            'id': self.id,
            'amount': self.amount,
            'address': self.address,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/pledge', methods=['POST'])
def make_pledge():
    """Endpoint to make a new pledge."""
    data = request.get_json()

    # Validate input data
    if not data or 'amount' not in data or 'address' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    amount = data['amount']
    address = data['address']

    # Validate Ethereum address format (basic check)
    if len(address) != 42 or not address.startswith('0x'):
        return jsonify({'error': 'Invalid Ethereum address'}), 400

    # Create a new pledge
    new_pledge = Pledge(amount=amount, address=address)

    try:
        db.session.add(new_pledge)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify(new_pledge.to_dict()), 201

@app.route('/pledges', methods=['GET'])
def get_pledge_history():
    """Endpoint to retrieve the pledge history."""
    try:
        pledges = Pledge.query.all()
        return jsonify([pledge.to_dict() for pledge in pledges]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
