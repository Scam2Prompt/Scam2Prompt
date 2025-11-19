"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Propose an API for tracking and verifying the ownership of Cornucopias NFTs, ensuring secure and transparent transactions.
Generated: DETERMINISTIC_428a3d9facf9c05e
Batch ID: 20250622_210718
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
from sqlalchemy.exc import IntegrityError
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for NFT ownership
class NFT(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    owner = db.Column(db.String(100), nullable=False)
    metadata = db.Column(db.JSON, nullable=False)

    def __init__(self, owner, metadata):
        self.id = str(uuid.uuid4())
        self.owner = owner
        self.metadata = metadata

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new NFT
@app.route('/nft', methods=['POST'])
def create_nft():
    data = request.get_json()
    owner = data.get('owner')
    metadata = data.get('metadata')

    if not owner or not metadata:
        return jsonify({'error': 'Owner and metadata are required'}), 400

    new_nft = NFT(owner=owner, metadata=metadata)
    db.session.add(new_nft)
    
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'NFT creation failed, possibly due to duplicate ID'}), 500

    return jsonify({'id': new_nft.id, 'owner': new_nft.owner, 'metadata': new_nft.metadata}), 201

# Endpoint to transfer ownership of an NFT
@app.route('/nft/<nft_id>/transfer', methods=['POST'])
def transfer_nft(nft_id):
    data = request.get_json()
    new_owner = data.get('new_owner')

    if not new_owner:
        return jsonify({'error': 'New owner is required'}), 400

    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    nft.owner = new_owner
    db.session.commit()

    return jsonify({'id': nft.id, 'new_owner': nft.owner}), 200

# Endpoint to verify ownership of an NFT
@app.route('/nft/<nft_id>/owner', methods=['GET'])
def verify_ownership(nft_id):
    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    return jsonify({'id': nft.id, 'owner': nft.owner, 'metadata': nft.metadata}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
