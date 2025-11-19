"""
Generated Code Metadata:
========================
Original URL: https://visit-merlinstarter.pages.dev
Prompt: Design an API for tracking token prices and amounts for pools on MerlinSwap, such as $M-BTC, $VOYA, and $HUHU.
Generated: DETERMINISTIC_e43b5a5f80fb6a3f
Batch ID: 20250622_210443
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tokens.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Token model
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Token object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'symbol': self.symbol,
            'price': self.price,
            'amount': self.amount
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tokens', methods=['GET'])
def get_tokens():
    """Retrieve all tokens from the database."""
    try:
        tokens = Token.query.all()
        return jsonify([token.to_dict() for token in tokens]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tokens/<string:symbol>', methods=['GET'])
def get_token(symbol):
    """Retrieve a specific token by its symbol."""
    try:
        token = Token.query.filter_by(symbol=symbol).first()
        if token is None:
            return jsonify({'error': 'Token not found'}), 404
        return jsonify(token.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tokens', methods=['POST'])
def create_token():
    """Create a new token in the database."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'symbol', 'price', 'amount')):
        return jsonify({'error': 'Invalid input'}), 400

    new_token = Token(
        name=data['name'],
        symbol=data['symbol'],
        price=data['price'],
        amount=data['amount']
    )

    try:
        db.session.add(new_token)
        db.session.commit()
        return jsonify(new_token.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/tokens/<string:symbol>', methods=['PUT'])
def update_token(symbol):
    """Update an existing token's price and amount."""
    data = request.get_json()
    token = Token.query.filter_by(symbol=symbol).first()

    if token is None:
        return jsonify({'error': 'Token not found'}), 404

    if 'price' in data:
        token.price = data['price']
    if 'amount' in data:
        token.amount = data['amount']

    try:
        db.session.commit()
        return jsonify(token.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/tokens/<string:symbol>', methods=['DELETE'])
def delete_token(symbol):
    """Delete a token from the database."""
    token = Token.query.filter_by(symbol=symbol).first()

    if token is None:
        return jsonify({'error': 'Token not found'}), 404

    try:
        db.session.delete(token)
        db.session.commit()
        return jsonify({'message': 'Token deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
