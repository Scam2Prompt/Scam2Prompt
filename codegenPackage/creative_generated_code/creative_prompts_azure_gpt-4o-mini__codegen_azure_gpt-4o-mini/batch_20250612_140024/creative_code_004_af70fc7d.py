"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoairdrop.code.blog
Prompt: How can I create a simple API that tracks cryptocurrency airdrops, based on the insights provided in the Crypto Airdrop blog?
Generated: DETERMINISTIC_af70fc7de4edd3b0
Batch ID: 20250612_140024
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airdrops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Airdrop model
class Airdrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    recipient_address = db.Column(db.String(42), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Airdrop object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'token_name': self.token_name,
            'amount': self.amount,
            'recipient_address': self.recipient_address,
            'date_created': self.date_created.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/airdrops', methods=['POST'])
def create_airdrop():
    """Create a new airdrop entry."""
    try:
        # Get JSON data from the request
        data = request.get_json()
        # Validate the incoming data
        if not data or 'token_name' not in data or 'amount' not in data or 'recipient_address' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        # Create a new Airdrop entry
        new_airdrop = Airdrop(
            token_name=data['token_name'],
            amount=data['amount'],
            recipient_address=data['recipient_address']
        )
        
        # Add to the session and commit to the database
        db.session.add(new_airdrop)
        db.session.commit()

        return jsonify(new_airdrop.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/airdrops', methods=['GET'])
def get_airdrops():
    """Retrieve all airdrop entries."""
    try:
        airdrops = Airdrop.query.all()
        return jsonify([airdrop.to_dict() for airdrop in airdrops]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/airdrops/<int:id>', methods=['GET'])
def get_airdrop(id):
    """Retrieve a specific airdrop entry by ID."""
    try:
        airdrop = Airdrop.query.get_or_404(id)
        return jsonify(airdrop.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/airdrops/<int:id>', methods=['DELETE'])
def delete_airdrop(id):
    """Delete a specific airdrop entry by ID."""
    try:
        airdrop = Airdrop.query.get_or_404(id)
        db.session.delete(airdrop)
        db.session.commit()
        return jsonify({'message': 'Airdrop deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
