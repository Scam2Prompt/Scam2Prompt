"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprotocolcoin.pages.dev
Prompt: Write code to enable NFT collection management and viewing, as described in the "My NFTs" section of the SmartProtocolCoin website.
Generated: DETERMINISTIC_db62d5c82f18dee4
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the NFT model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(50), nullable=False)
    token_id = db.Column(db.String(50), nullable=False, unique=True)
    metadata = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<NFT {self.token_id}, Owner {self.owner_id}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Web3 provider setup
def get_web3():
    infura_url = os.getenv('INFURA_URL')
    return Web3(Web3.HTTPProvider(infura_url))

# Route to create a new NFT
@app.route('/nfts', methods=['POST'])
def create_nft():
    """
    Create a new NFT in the collection.
    Body Parameters:
        - owner_id: The owner of the NFT
        - token_id: The unique identifier for the NFT
        - metadata: Additional information about the NFT
    """
    data = request.get_json()
    
    if not data or not 'owner_id' in data or not 'token_id' in data:
        abort(400, 'Invalid input: owner_id and token_id are required.')
    
    # Create and save the NFT
    nft = NFT(owner_id=data['owner_id'], token_id=data['token_id'], metadata=data.get('metadata'))
    
    try:
        db.session.add(nft)
        db.session.commit()
        return jsonify({'message': 'NFT created successfully!', 'nft': nft.token_id}), 201
    except Exception as e:
        db.session.rollback()
        abort(500, f'Error creating NFT: {str(e)}')

# Route to get all NFTs for a specific owner
@app.route('/nfts/<string:owner_id>', methods=['GET'])
def get_nfts(owner_id):
    """
    Get all NFTs owned by the specified owner.
    URL Parameters:
        - owner_id: The ID of the NFT owner
    """
    nfts = NFT.query.filter_by(owner_id=owner_id).all()
    
    if not nfts:
        return jsonify({'message': 'No NFTs found for this owner'}), 404
    
    return jsonify([{'token_id': nft.token_id, 'metadata': nft.metadata} for nft in nfts]), 200

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    response = {
        'error': str(e),
        'message': 'An error occurred processing your request.'
    }
    return jsonify(response), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
