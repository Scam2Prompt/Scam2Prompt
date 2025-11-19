"""
Generated Code Metadata:
========================
Original URL: https://blockgenius.pages.dev
Prompt: "Design a simple API for an NFT marketplace like Blockgenius, including endpoints for creating, buying, and selling NFTs."
Generated: DETERMINISTIC_a4d6110c97b6bedb
Batch ID: 20250622_205836
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
    try:
        new_nft = NFT(name=data['name'], owner=data['owner'], price=data['price'])
        db.session.add(new_nft)
        db.session.commit()
        return jsonify(new_nft.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create NFT'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to buy an NFT
@app.route('/nfts/<int:nft_id>/buy', methods=['POST'])
def buy_nft(nft_id):
    data = request.json
    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    if data['buyer'] == nft.owner:
        return jsonify({'error': 'Buyer cannot be the current owner'}), 400

    nft.owner = data['buyer']
    try:
        db.session.commit()
        return jsonify(nft.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to sell an NFT
@app.route('/nfts/<int:nft_id>/sell', methods=['POST'])
def sell_nft(nft_id):
    data = request.json
    nft = NFT.query.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404

    if data['seller'] != nft.owner:
        return jsonify({'error': 'Only the owner can sell the NFT'}), 403

    nft.price = data['price']
    try:
        db.session.commit()
        return jsonify(nft.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
