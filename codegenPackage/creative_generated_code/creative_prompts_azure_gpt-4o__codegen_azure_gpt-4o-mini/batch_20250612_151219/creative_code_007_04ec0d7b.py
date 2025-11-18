"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Develop a REST API endpoint for querying virtual real estate data from the EarthMeta Marketplace, including NFT city details and transaction history.
Generated: DETERMINISTIC_04ec0d7bb9e3bb02
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///earthmeta_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFT city details
class NFTCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Database model for transaction history
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('nft_city.id'), nullable=False)
    buyer_address = db.Column(db.String(42), nullable=False)
    seller_address = db.Column(db.String(42), nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# API endpoint to query NFT city details
@app.route('/api/nft-cities', methods=['GET'])
def get_nft_cities():
    try:
        cities = NFTCity.query.all()
        result = [
            {
                'id': city.id,
                'name': city.name,
                'description': city.description,
                'location': city.location
            }
            for city in cities
        ]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to query transaction history for a specific NFT city
@app.route('/api/nft-cities/<int:city_id>/transactions', methods=['GET'])
def get_transaction_history(city_id):
    try:
        transactions = Transaction.query.filter_by(city_id=city_id).all()
        result = [
            {
                'id': transaction.id,
                'buyer_address': transaction.buyer_address,
                'seller_address': transaction.seller_address,
                'price': transaction.price,
                'timestamp': transaction.timestamp.isoformat()  # Convert to ISO format for JSON
            }
            for transaction in transactions
        ]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug to False for production
```
