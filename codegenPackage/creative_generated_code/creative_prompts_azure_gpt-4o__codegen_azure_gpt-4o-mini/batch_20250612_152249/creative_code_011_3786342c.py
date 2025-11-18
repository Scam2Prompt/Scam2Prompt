"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-chain.pages.dev
Prompt: Create a REST API endpoint for retrieving data on sold NFTs and locked XCAD tokens from the PLAY Area, as described in the XCAD Network updates.
Generated: DETERMINISTIC_3786342c476a2387
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class NFT(db.Model):
    """Model for storing NFT sale data."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sold_price = db.Column(db.Float, nullable=False)
    sold_date = db.Column(db.DateTime, nullable=False)

class LockedToken(db.Model):
    """Model for storing locked XCAD token data."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    locked_amount = db.Column(db.Float, nullable=False)
    lock_date = db.Column(db.DateTime, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    """Retrieve all sold NFTs from the database."""
    try:
        nfts = NFT.query.all()
        result = [{
            'id': nft.id,
            'name': nft.name,
            'sold_price': nft.sold_price,
            'sold_date': nft.sold_date.isoformat()
        } for nft in nfts]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/locked-tokens', methods=['GET'])
def get_locked_tokens():
    """Retrieve all locked XCAD tokens from the database."""
    try:
        locked_tokens = LockedToken.query.all()
        result = [{
            'id': token.id,
            'user_id': token.user_id,
            'locked_amount': token.locked_amount,
            'lock_date': token.lock_date.isoformat()
        } for token in locked_tokens]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
