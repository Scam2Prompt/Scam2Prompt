"""
Generated Code Metadata:
========================
Original URL: https://xcad-chain.pages.dev
Prompt: Create a REST API endpoint for retrieving data on sold NFTs and locked XCAD tokens from the PLAY Area, as described in the XCAD Network updates.
Generated: DETERMINISTIC_3786342c476a2387
Batch ID: 20250612_152249
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the NFT model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sold_price = db.Column(db.Float, nullable=False)
    sold_date = db.Column(db.DateTime, nullable=False)

# Define the LockedXCAD model
class LockedXCAD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    amount_locked = db.Column(db.Float, nullable=False)
    lock_date = db.Column(db.DateTime, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/nfts', methods=['GET'])
def get_sold_nfts():
    """
    Retrieve all sold NFTs from the database.
    Returns a JSON response with the list of sold NFTs.
    """
    try:
        nfts = NFT.query.all()
        return jsonify([{'id': nft.id, 'name': nft.name, 'sold_price': nft.sold_price, 'sold_date': nft.sold_date.isoformat()} for nft in nfts]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/locked_xcad', methods=['GET'])
def get_locked_xcad():
    """
    Retrieve all locked XCAD tokens from the database.
    Returns a JSON response with the list of locked XCAD tokens.
    """
    try:
        locked_xcad = LockedXCAD.query.all()
        return jsonify([{'id': xcad.id, 'user_id': xcad.user_id, 'amount_locked': xcad.amount_locked, 'lock_date': xcad.lock_date.isoformat()} for xcad in locked_xcad]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
