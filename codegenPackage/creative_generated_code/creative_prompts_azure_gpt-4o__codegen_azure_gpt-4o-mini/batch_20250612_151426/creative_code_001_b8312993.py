"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-prime-kongz.web.app
Prompt: Generate code to create an NFT allowlist marketplace where users can safely buy and sell allowlists, similar to the functionality described on Atlas3.
Generated: DETERMINISTIC_b8312993852a53ea
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# NFT Allowlist Marketplace
# This code implements a simple marketplace for buying and selling NFT allowlists
# using Flask for the web framework and SQLAlchemy for database handling.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for the Allowlist
class Allowlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    nft_name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Allowlist {self.nft_name}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/allowlist', methods=['POST'])
def create_allowlist():
    """Create a new NFT allowlist for sale."""
    data = request.json
    if not data or 'user_id' not in data or 'nft_name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    allowlist = Allowlist(user_id=data['user_id'], nft_name=data['nft_name'], price=data['price'])
    db.session.add(allowlist)
    
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Allowlist already exists'}), 400

    return jsonify({'message': 'Allowlist created successfully'}), 201

@app.route('/allowlist/<int:id>', methods=['GET'])
def get_allowlist(id):
    """Get details of a specific allowlist by ID."""
    allowlist = Allowlist.query.get(id)
    if not allowlist:
        return jsonify({'error': 'Allowlist not found'}), 404

    return jsonify({
        'id': allowlist.id,
        'user_id': allowlist.user_id,
        'nft_name': allowlist.nft_name,
        'price': allowlist.price
    }), 200

@app.route('/allowlist/<int:id>', methods=['DELETE'])
def delete_allowlist(id):
    """Delete a specific allowlist by ID."""
    allowlist = Allowlist.query.get(id)
    if not allowlist:
        return jsonify({'error': 'Allowlist not found'}), 404

    db.session.delete(allowlist)
    db.session.commit()
    return jsonify({'message': 'Allowlist deleted successfully'}), 200

@app.route('/allowlist', methods=['GET'])
def list_allowlists():
    """List all allowlists available for sale."""
    allowlists = Allowlist.query.all()
    return jsonify([
        {
            'id': allowlist.id,
            'user_id': allowlist.user_id,
            'nft_name': allowlist.nft_name,
            'price': allowlist.price
        } for allowlist in allowlists
    ]), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask and SQLAlchemy before running this code:

```bash
pip install Flask SQLAlchemy
```
