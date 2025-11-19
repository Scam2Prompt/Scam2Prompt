"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://umbrella-d96b1.web.app
Prompt: Generate a code example for a web application that allows users to manage their digital assets effectively, based on the principles outlined by Umbrella.
Generated: DETERMINISTIC_214631a4d408ac45
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Digital Asset
class DigitalAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        """Serialize the asset object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new digital asset
@app.route('/assets', methods=['POST'])
def create_asset():
    try:
        data = request.get_json()
        new_asset = DigitalAsset(name=data['name'], value=data['value'])
        db.session.add(new_asset)
        db.session.commit()
        return jsonify(new_asset.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all digital assets
@app.route('/assets', methods=['GET'])
def get_assets():
    try:
        assets = DigitalAsset.query.all()
        return jsonify([asset.serialize() for asset in assets]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a specific digital asset
@app.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    try:
        data = request.get_json()
        asset = DigitalAsset.query.get_or_404(asset_id)
        asset.name = data['name']
        asset.value = data['value']
        db.session.commit()
        return jsonify(asset.serialize()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a specific digital asset
@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    try:
        asset = DigitalAsset.query.get_or_404(asset_id)
        db.session.delete(asset)
        db.session.commit()
        return jsonify({'message': 'Asset deleted successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
Make sure to install the required packages using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

### Note
- This application uses SQLite as the database.
- The database will be created automatically on the first request if it does not exist.
- Ensure to run the app in a proper environment for production.
