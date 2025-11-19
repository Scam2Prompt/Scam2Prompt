"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Provide an API recommendation for tracking presale contributions in a token sale like the BOI Coin presale.
Generated: DETERMINISTIC_694332377618b2b5
Batch ID: 20250612_135202
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presale.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the PresaleContribution model
class PresaleContribution(db.Model):
    __tablename__ = 'presale_contributions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_address = db.Column(db.String(42), nullable=False)  # Ethereum address
    amount_contributed = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_address': self.user_address,
            'amount_contributed': self.amount_contributed,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/contribute', methods=['POST'])
def contribute():
    """
    Endpoint to track presale contributions.
    
    Request Body:
    - user_address (str): The Ethereum address of the contributor.
    - amount_contributed (float): The amount contributed in tokens.

    Returns:
    - JSON response with a success message and contribution details.
    """

    data = request.get_json()

    # Validate request data
    if not data or 'user_address' not in data or 'amount_contributed' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    user_address = data['user_address']
    amount_contributed = data['amount_contributed']

    # Validate input types
    if not isinstance(user_address, str) or not isinstance(amount_contributed, (int, float)):
        return jsonify({'error': 'Invalid input types'}), 400

    # Create a new presale contribution record
    new_contribution = PresaleContribution(
        user_address=user_address,
        amount_contributed=amount_contributed
    )

    try:
        db.session.add(new_contribution)
        db.session.commit()
        logging.info(f"New contribution recorded: {new_contribution.to_dict()}")
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error while recording contribution: {e}")
        return jsonify({'error': 'Database error'}), 500

    return jsonify({'message': 'Contribution recorded successfully', 'contribution': new_contribution.to_dict()}), 201

@app.route('/api/contributions', methods=['GET'])
def get_contributions():
    """
    Endpoint to retrieve all presale contributions.

    Returns:
    - JSON response containing a list of contributions.
    """

    contributions = PresaleContribution.query.all()
    return jsonify({'contributions': [contribution.to_dict() for contribution in contributions]}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
