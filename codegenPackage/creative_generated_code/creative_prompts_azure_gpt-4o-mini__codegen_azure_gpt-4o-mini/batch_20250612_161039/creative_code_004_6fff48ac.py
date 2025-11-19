"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memefi-club.pages.dev
Prompt: Illustrate how to implement a social key trading feature in a web application that mirrors the mechanics described in the MemeFi Club.
Generated: DETERMINISTIC_6fff48ac9f842dac
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading.db'
db = SQLAlchemy(app)

# Define a model for Social Key trades
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    key_id = db.Column(db.String(50), nullable=False)
    trade_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Trade {self.id}>'


# Initialize the database
with app.app_context():
    db.create_all()


@app.route('/trade', methods=['POST'])
def create_trade():
    """
    Endpoint to create a new trade.
    Expects JSON data with user_id, key_id, and trade_amount.
    """
    data = request.json

    # Validate input data
    user_id = data.get('user_id')
    key_id = data.get('key_id')
    trade_amount = data.get('trade_amount')

    if not user_id or not key_id or trade_amount is None:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new trade record
    new_trade = Trade(user_id=user_id, key_id=key_id, trade_amount=trade_amount)

    try:
        db.session.add(new_trade)
        db.session.commit()
        return jsonify({'message': 'Trade created successfully', 'trade_id': new_trade.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Trade already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/trades/<user_id>', methods=['GET'])
def get_user_trades(user_id):
    """
    Endpoint to retrieve all trades for a specific user.
    """
    trades = Trade.query.filter_by(user_id=user_id).all()
    return jsonify([{'trade_id': trade.id, 'key_id': trade.key_id, 'trade_amount': trade.trade_amount} for trade in trades]), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment (`pip install Flask Flask-SQLAlchemy`).
- The SQLite database will be created in the same directory as the script when the application is run for the first time.
- The API expects JSON payloads for creating trades and uses standard HTTP status codes for responses.
