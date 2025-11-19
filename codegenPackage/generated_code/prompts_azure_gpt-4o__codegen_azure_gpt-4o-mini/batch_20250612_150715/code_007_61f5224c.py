"""
Generated Code Metadata:
========================
Original URL: https://galaxyfoxs.live
Prompt: Design a REST API for the Galaxy Fox NFT marketplace that allows users to list, buy, and sell NFTs, while ensuring transactions contribute to the ecosystem's treasury.
Generated: DETERMINISTIC_61f5224c864af6e2
Batch ID: 20250612_150715
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///galaxy_fox_nft.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFTs
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for NFT validation
class NFTSchema(Schema):
    name = fields.Str(required=True)
    owner = fields.Str(required=True)
    price = fields.Float(required=True)

nft_schema = NFTSchema()
nfts_schema = NFTSchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to list all NFTs
@app.route('/nfts', methods=['GET'])
def list_nfts():
    """Retrieve all NFTs in the marketplace."""
    nfts = NFT.query.all()
    return nfts_schema.dump(nfts), 200

# Endpoint to create a new NFT
@app.route('/nfts', methods=['POST'])
def create_nft():
    """Create a new NFT listing."""
    try:
        nft_data = nft_schema.load(request.json)
        new_nft = NFT(**nft_data)
        db.session.add(new_nft)
        db.session.commit()
        return nft_schema.dump(new_nft), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "NFT already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to buy an NFT
@app.route('/nfts/<int:nft_id>/buy', methods=['POST'])
def buy_nft(nft_id):
    """Purchase an NFT and transfer ownership."""
    nft = NFT.query.get_or_404(nft_id)
    buyer = request.json.get('buyer')

    if not buyer:
        return jsonify({"error": "Buyer information is required."}), 400

    # Simulate treasury contribution
    treasury_contribution = nft.price * 0.05  # 5% to treasury
    # Here you would implement the logic to handle the treasury contribution

    nft.owner = buyer
    db.session.commit()
    return nft_schema.dump(nft), 200

# Endpoint to sell an NFT
@app.route('/nfts/<int:nft_id>/sell', methods=['PUT'])
def sell_nft(nft_id):
    """Update the price of an NFT for sale."""
    nft = NFT.query.get_or_404(nft_id)
    new_price = request.json.get('price')

    if new_price is None or new_price <= 0:
        return jsonify({"error": "Valid price is required."}), 400

    nft.price = new_price
    db.session.commit()
    return nft_schema.dump(nft), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
