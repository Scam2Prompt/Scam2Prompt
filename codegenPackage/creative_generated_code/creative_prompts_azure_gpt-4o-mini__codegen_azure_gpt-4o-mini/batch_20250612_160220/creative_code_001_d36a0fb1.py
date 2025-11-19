"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clais.pages.dev
Prompt: Write a code snippet to create a first-come, first-served airdrop claim system similar to the one described for $BROCK.
Generated: DETERMINISTIC_d36a0fb1610b5b4f
Batch ID: 20250612_160220
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
from datetime import datetime
import os

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///airdrop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the AirdropClaim model
class AirdropClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)  # Ethereum address format
    claimed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<AirdropClaim {self.wallet_address}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to claim airdrop
@app.route('/claim_airdrop', methods=['POST'])
def claim_airdrop():
    data = request.json
    wallet_address = data.get('wallet_address')

    # Validate wallet address format
    if not wallet_address or len(wallet_address) != 42 or not wallet_address.startswith('0x'):
        return jsonify({'error': 'Invalid wallet address'}), 400

    # Check if the wallet has already claimed the airdrop
    existing_claim = AirdropClaim.query.filter_by(wallet_address=wallet_address).first()
    if existing_claim:
        return jsonify({'error': 'Airdrop already claimed by this wallet'}), 400

    # Create a new airdrop claim
    new_claim = AirdropClaim(wallet_address=wallet_address)
    try:
        db.session.add(new_claim)
        db.session.commit()
        return jsonify({'message': 'Airdrop claimed successfully', 'wallet_address': wallet_address}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to claim airdrop', 'details': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```

### Notes:
- Ensure that the environment variable `DATABASE_URL` is set to point to the desired database.
- This example uses Flask and SQLAlchemy. You need to have these dependencies installed in your Python environment.
- Please replace the database URL appropriately for your production environment.
- Error handling is included for invalid wallet address formats, duplicate claims, and database errors.
