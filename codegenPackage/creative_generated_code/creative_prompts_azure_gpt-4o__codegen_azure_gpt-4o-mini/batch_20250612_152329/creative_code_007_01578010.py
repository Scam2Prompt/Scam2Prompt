"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Develop a backend API to facilitate "Jelly Trade" transactions between users within the Rascals NFT ecosystem.
Generated: DETERMINISTIC_01578010cb8e64ce
Batch ID: 20250612_152329
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
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jelly_trade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for a User in the Rascals NFT ecosystem
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Model for a Jelly Trade transaction
class JellyTrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    jelly_amount = db.Column(db.Integer, nullable=False)

    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new Jelly Trade transaction
@app.route('/api/trade', methods=['POST'])
def create_trade():
    """Creates a new Jelly Trade transaction between users."""
    data = request.get_json()

    # Validate request data
    if not data or 'sender_id' not in data or 'receiver_id' not in data or 'jelly_amount' not in data:
        raise BadRequest("Missing required fields: sender_id, receiver_id, jelly_amount.")

    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    jelly_amount = data['jelly_amount']

    # Basic validation
    if jelly_amount <= 0:
        raise BadRequest("jelly_amount must be greater than 0.")

    # Create a new trade transaction
    new_trade = JellyTrade(sender_id=sender_id, receiver_id=receiver_id, jelly_amount=jelly_amount)

    try:
        db.session.add(new_trade)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest("Trade transaction failed. Ensure both users exist and the trade is valid.")

    return jsonify({"message": "Trade created successfully.", "trade_id": new_trade.id}), 201

# Endpoint to get all trades for a user
@app.route('/api/trades/<int:user_id>', methods=['GET'])
def get_user_trades(user_id):
    """Retrieves all Jelly Trade transactions for a specific user."""
    trades = JellyTrade.query.filter((JellyTrade.sender_id == user_id) | (JellyTrade.receiver_id == user_id)).all()

    if not trades:
        raise NotFound("No trades found for this user.")

    return jsonify([{
        "trade_id": trade.id,
        "sender_id": trade.sender_id,
        "receiver_id": trade.receiver_id,
        "jelly_amount": trade.jelly_amount
    } for trade in trades]), 200

# Error handling
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
