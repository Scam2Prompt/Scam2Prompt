"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-combo.ru
Prompt: Create a REST API endpoint for a PixelVerse-inspired game that allows users to trade NFTs and PIXFI tokens securely.
Generated: DETERMINISTIC_94bff695c760b19b
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import uuid

app = Flask(__name__)

# Configure the database (replace with your actual database URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pixelverse.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)

class NFT(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)

class Trade(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nft_id = db.Column(db.String(36), db.ForeignKey('nft.id'), nullable=False)
    sender_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    pixfi_tokens = db.Column(db.Float, nullable=False)

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# Routes

@app.route('/trade', methods=['POST'])
def trade_nft():
    """
    Trade NFTs between users securely.
    Users must specify the NFT ID, sender, receiver, and PIXFI tokens.
    """
    try:
        # Parse request data
        data = request.json
        nft_id = data.get('nft_id')
        sender_id = data.get('sender_id')
        receiver_id = data.get('receiver_id')
        pixfi_tokens = data.get('pixfi_tokens')
        
        # Validate input data
        if not (nft_id and sender_id and receiver_id and pixfi_tokens):
            return error_response('Missing required fields')
        
        # Check if sender, receiver, and NFT exist
        sender = User.query.get(sender_id)
        receiver = User.query.get(receiver_id)
        nft = NFT.query.get(nft_id)

        if not sender:
            return error_response('Sender not found')
        if not receiver:
            return error_response('Receiver not found')
        if not nft:
            return error_response('NFT not found')
        if nft.owner_id != sender_id:
            return error_response('Sender does not own the NFT')

        # Perform the trade
        nft.owner_id = receiver_id  # Transfer NFT ownership
        trade = Trade(nft_id=nft.id, sender_id=sender.id, receiver_id=receiver.id, pixfi_tokens=pixfi_tokens)

        # Commit changes to the database
        db.session.add(trade)
        db.session.commit()

        return jsonify({'message': 'Trade successful', 'trade_id': trade.id}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return error_response(f'Database error: {str(e)}', 500)

    except Exception as e:
        return error_response(f'Unexpected error: {str(e)}', 500)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Main execution point
if __name__ == '__main__':
    app.run(debug=True)
```
