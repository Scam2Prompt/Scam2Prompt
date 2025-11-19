"""
Generated Code Metadata:
========================
Original URL: https://bayc.team
Prompt: "Design a simple NFT marketplace API inspired by BAYC."
Generated: DETERMINISTIC_431ed2ea0eed6985
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# NFT Model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    owner = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# NFT Schema for serialization
class NFTSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    owner = fields.Str(required=True)
    price = fields.Float(required=True)

nft_schema = NFTSchema()
nfts_schema = NFTSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new NFT
@app.route('/nfts', methods=['POST'])
def create_nft():
    try:
        # Validate and deserialize input
        nft_data = nft_schema.load(request.json)
        new_nft = NFT(**nft_data)
        db.session.add(new_nft)
        db.session.commit()
        return nft_schema.dump(new_nft), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "NFT with this name already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all NFTs
@app.route('/nfts', methods=['GET'])
def get_nfts():
    nfts = NFT.query.all()
    return nfts_schema.dump(nfts), 200

# Endpoint to get a specific NFT by ID
@app.route('/nfts/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    nft = NFT.query.get(nft_id)
    if nft is None:
        return jsonify({"error": "NFT not found."}), 404
    return nft_schema.dump(nft), 200

# Endpoint to update an NFT
@app.route('/nfts/<int:nft_id>', methods=['PUT'])
def update_nft(nft_id):
    nft = NFT.query.get(nft_id)
    if nft is None:
        return jsonify({"error": "NFT not found."}), 404

    try:
        # Validate and deserialize input
        nft_data = nft_schema.load(request.json)
        for key, value in nft_data.items():
            setattr(nft, key, value)
        db.session.commit()
        return nft_schema.dump(nft), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an NFT
@app.route('/nfts/<int:nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    nft = NFT.query.get(nft_id)
    if nft is None:
        return jsonify({"error": "NFT not found."}), 404

    db.session.delete(nft)
    db.session.commit()
    return jsonify({"message": "NFT deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
