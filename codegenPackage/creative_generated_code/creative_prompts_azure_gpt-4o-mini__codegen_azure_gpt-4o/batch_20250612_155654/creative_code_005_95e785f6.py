"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: How can I create a digital asset marketplace for Cornucopias that allows trading of vehicles and land plots?
Generated: DETERMINISTIC_95e785f6865d692f
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a digital asset marketplace for Cornucopias, allowing trading of vehicles and land plots. This solution is written in Python and uses Flask as the web framework with SQLAlchemy for database management.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Asset model for vehicles and land plots
class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Asset name (e.g., vehicle name or land plot ID)
    asset_type = db.Column(db.String(50), nullable=False)  # Type of asset ('vehicle' or 'land_plot')
    owner = db.Column(db.String(100), nullable=False)  # Owner of the asset
    price = db.Column(db.Float, nullable=False)  # Listing price for the asset

    def to_dict(self):
        """Convert Asset object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'asset_type': self.asset_type,
            'owner': self.owner,
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def setup_database():
    db.create_all()

# Route to list all assets
@app.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.to_dict() for asset in assets]), 200

# Route to list assets by type
@app.route('/assets/<asset_type>', methods=['GET'])
def get_assets_by_type(asset_type):
    assets = Asset.query.filter_by(asset_type=asset_type).all()
    return jsonify([asset.to_dict() for asset in assets]), 200

# Route to create a new asset
@app.route('/assets', methods=['POST'])
def create_asset():
    try:
        data = request.json
        asset = Asset(
            name=data['name'],
            asset_type=data['asset_type'],
            owner=data['owner'],
            price=data['price']
        )
        db.session.add(asset)
        db.session.commit()
        return jsonify(asset.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred'}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400

# Route to update an asset's price
@app.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset_price(asset_id):
    try:
        data = request.json
        asset = Asset.query.get(asset_id)
        if not asset:
            return jsonify({'error': 'Asset not found'}), 404
        asset.price = data['price']
        db.session.commit()
        return jsonify(asset.to_dict()), 200
    except KeyError:
        return jsonify({'error': 'Missing price field in request data'}), 400

# Route to delete an asset
@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404
    db.session.delete(asset)
    db.session.commit()
    return jsonify({'message': 'Asset deleted successfully'}), 200

# Error handling for generic server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'An internal server error occurred'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements for Running the Code:
1. Install Flask and SQLAlchemy:
   ```bash
   pip install flask flask-sqlalchemy
   ```

2. Run the application:
   ```bash
   python app.py
   ```

### Notes:
- This example uses SQLite for simplicity, but in production, replace it with a more robust database (e.g., PostgreSQL).
- Implement authentication and authorization for real-world applications to ensure secure trading of assets.
