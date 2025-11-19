"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoins.one
Prompt: What are some potential use cases for a cryptocurrency-related website that could be built on the domain 99bitcoins.one?
Generated: DETERMINISTIC_bd2a349ff5f68313
Batch ID: 20250612_163243
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptocurrency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for storing cryptocurrency data
class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Cryptocurrency {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Define a route to get all cryptocurrencies
@app.route('/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    """Return a list of all cryptocurrencies."""
    try:
        cryptos = Cryptocurrency.query.all()
        return jsonify([{
            'id': crypto.id,
            'name': crypto.name,
            'symbol': crypto.symbol,
            'market_cap': crypto.market_cap,
            'price': crypto.price
        } for crypto in cryptos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to add a new cryptocurrency
@app.route('/cryptocurrency', methods=['POST'])
def add_cryptocurrency():
    """Add a new cryptocurrency to the database."""
    data = request.get_json()
    if not data or 'name' not in data or 'symbol' not in data or 'market_cap' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_crypto = Cryptocurrency(
        name=data['name'],
        symbol=data['symbol'],
        market_cap=data['market_cap'],
        price=data['price']
    )
    
    try:
        db.session.add(new_crypto)
        db.session.commit()
        return jsonify({'message': 'Cryptocurrency added', 'id': new_crypto.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback session in case of error
        return jsonify({'error': str(e)}), 500

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a custom response."""
    return jsonify({
        'error': e.description,
        'code': e.code
    }), e.code

# Define a main method to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
