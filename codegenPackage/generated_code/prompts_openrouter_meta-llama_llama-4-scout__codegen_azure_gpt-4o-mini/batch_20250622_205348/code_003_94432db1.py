"""
Generated Code Metadata:
========================
Original URL: https://enterart.rpmltech.com
Prompt: "Design a RESTful API for interacting with an NFT marketplace like Enter Art, including endpoints for creating, buying, and selling NFTs."
Generated: DETERMINISTIC_94432db19ae7e86c
Batch ID: 20250622_205348
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for NFT
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner,
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new NFT
@app.route('/nfts', methods=['POST'])
def create_nft():
    data = request.json
    new_nft = NFT(name=data['name'], owner=data['owner'], price=data['price'])
    db.session.add(new_nft)
    try:
        db.session.commit()
        return jsonify(new_nft.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create NFT'}), 400

# Endpoint to buy an NFT
@app.route('/nfts/<int:nft_id>/buy', methods=['POST'])
def buy_nft(nft_id):
    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    data = request.json
    buyer = data['buyer']
    
    # Check if buyer has enough funds (this is a placeholder for actual payment logic)
    if data['funds'] < nft.price:
        return jsonify({'error': 'Insufficient funds'}), 400

    nft.owner = buyer
    db.session.commit()
    return jsonify(nft.to_dict()), 200

# Endpoint to sell an NFT
@app.route('/nfts/<int:nft_id>/sell', methods=['POST'])
def sell_nft(nft_id):
    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    data = request.json
    new_price = data['price']
    
    # Update the price of the NFT
    nft.price = new_price
    db.session.commit()
    return jsonify(nft.to_dict()), 200

# Endpoint to list all NFTs
@app.route('/nfts', methods=['GET'])
def list_nfts():
    nfts = NFT.query.all()
    return jsonify([nft.to_dict() for nft in nfts]), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
