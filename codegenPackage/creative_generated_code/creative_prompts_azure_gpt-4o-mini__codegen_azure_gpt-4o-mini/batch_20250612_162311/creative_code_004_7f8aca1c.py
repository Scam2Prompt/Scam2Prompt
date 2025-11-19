"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket-soto.pages.dev
Prompt: Outline a REST API that provides access to prediction market data for MLB trades, inspired by the analysis presented in the Polymarket Soto article.
Generated: DETERMINISTIC_7f8aca1c27509f91
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mlb_trades.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Trade model
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'team': self.team,
            'prediction': self.prediction,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to get all trades
@app.route('/api/trades', methods=['GET'])
def get_trades():
    trades = Trade.query.all()
    return jsonify([trade.to_dict() for trade in trades]), 200

# Endpoint to get a specific trade by ID
@app.route('/api/trades/<int:trade_id>', methods=['GET'])
def get_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade is None:
        abort(404)  # Trade not found
    return jsonify(trade.to_dict()), 200

# Endpoint to create a new trade
@app.route('/api/trades', methods=['POST'])
def create_trade():
    data = request.json
    if not data or 'player_name' not in data or 'team' not in data or 'prediction' not in data:
        abort(400)  # Bad request

    new_trade = Trade(
        player_name=data['player_name'],
        team=data['team'],
        prediction=data['prediction']
    )
    db.session.add(new_trade)
    db.session.commit()
    return jsonify(new_trade.to_dict()), 201

# Endpoint to update an existing trade
@app.route('/api/trades/<int:trade_id>', methods=['PUT'])
def update_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade is None:
        abort(404)  # Trade not found

    data = request.json
    if not data:
        abort(400)  # Bad request

    trade.player_name = data.get('player_name', trade.player_name)
    trade.team = data.get('team', trade.team)
    trade.prediction = data.get('prediction', trade.prediction)
    db.session.commit()
    return jsonify(trade.to_dict()), 200

# Endpoint to delete a trade
@app.route('/api/trades/<int:trade_id>', methods=['DELETE'])
def delete_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade is None:
        abort(404)  # Trade not found

    db.session.delete(trade)
    db.session.commit()
    return jsonify({'message': 'Trade deleted successfully'}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
