"""
Generated Code Metadata:
========================
Original URL: https://fxtasian.com
Prompt: "Write a Python script using libraries such as Flask or Django to create a simple REST API for a cryptocurrency exchange platform similar to IJEX Exchange."
Generated: DETERMINISTIC_ae2301fb9f2c5f8f
Batch ID: 20250622_212817
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Trade model
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cryptocurrency = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'cryptocurrency': self.cryptocurrency,
            'amount': self.amount,
            'price': self.price,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all trades
@app.route('/trades', methods=['GET'])
def get_trades():
    """Retrieve all trades from the database."""
    trades = Trade.query.all()
    return jsonify([trade.to_dict() for trade in trades]), 200

# Route to create a new trade
@app.route('/trades', methods=['POST'])
def create_trade():
    """Create a new trade in the database."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'cryptocurrency' not in data or 'amount' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_trade = Trade(
        cryptocurrency=data['cryptocurrency'],
        amount=data['amount'],
        price=data['price']
    )
    
    try:
        db.session.add(new_trade)
        db.session.commit()
        return jsonify(new_trade.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get a specific trade by ID
@app.route('/trades/<int:trade_id>', methods=['GET'])
def get_trade(trade_id):
    """Retrieve a specific trade by its ID."""
    trade = Trade.query.get(trade_id)
    if trade is None:
        return jsonify({'error': 'Trade not found'}), 404
    return jsonify(trade.to_dict()), 200

# Route to delete a trade by ID
@app.route('/trades/<int:trade_id>', methods=['DELETE'])
def delete_trade(trade_id):
    """Delete a specific trade by its ID."""
    trade = Trade.query.get(trade_id)
    if trade is None:
        return jsonify({'error': 'Trade not found'}), 404

    try:
        db.session.delete(trade)
        db.session.commit()
        return jsonify({'message': 'Trade deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
