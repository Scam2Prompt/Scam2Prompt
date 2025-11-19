"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: "Design an API for managing Rascals NFT utilities and rarity, including endpoints for Jelly staking and trading."
Generated: DETERMINISTIC_f94ce74a045442d2
Batch ID: 20250622_205926
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_utilities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Rascals NFT
class RascalNFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    rarity = db.Column(db.String(50), nullable=False)
    owner = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rarity': self.rarity,
            'owner': self.owner
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/nfts', methods=['POST'])
def create_nft():
    """Create a new Rascal NFT."""
    data = request.json
    new_nft = RascalNFT(name=data['name'], rarity=data['rarity'], owner=data['owner'])
    
    try:
        db.session.add(new_nft)
        db.session.commit()
        return jsonify(new_nft.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'NFT with this name already exists.'}), 400

@app.route('/nfts/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    """Retrieve a Rascal NFT by its ID."""
    nft = RascalNFT.query.get_or_404(nft_id)
    return jsonify(nft.to_dict()), 200

@app.route('/nfts/<int:nft_id>', methods=['PUT'])
def update_nft(nft_id):
    """Update the owner of a Rascal NFT."""
    nft = RascalNFT.query.get_or_404(nft_id)
    data = request.json
    nft.owner = data['owner']
    
    db.session.commit()
    return jsonify(nft.to_dict()), 200

@app.route('/nfts/<int:nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    """Delete a Rascal NFT."""
    nft = RascalNFT.query.get_or_404(nft_id)
    db.session.delete(nft)
    db.session.commit()
    return jsonify({'message': 'NFT deleted successfully.'}), 204

@app.route('/stake', methods=['POST'])
def stake_nft():
    """Stake a Rascal NFT."""
    data = request.json
    nft = RascalNFT.query.get_or_404(data['nft_id'])
    
    # Here you would implement staking logic
    return jsonify({'message': f'NFT {nft.name} staked successfully.'}), 200

@app.route('/trade', methods=['POST'])
def trade_nft():
    """Trade a Rascal NFT."""
    data = request.json
    nft = RascalNFT.query.get_or_404(data['nft_id'])
    
    # Here you would implement trading logic
    return jsonify({'message': f'NFT {nft.name} traded successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
