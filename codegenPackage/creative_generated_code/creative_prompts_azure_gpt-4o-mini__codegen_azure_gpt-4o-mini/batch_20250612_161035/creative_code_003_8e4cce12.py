"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lumos-airdrop.pages.dev
Prompt: Develop an API endpoint for a platform that allows users to borrow against their crypto assets without selling, inspired by Lumos Capital's Instant Crypto Credit Lines service.
Generated: DETERMINISTIC_8e4cce12b9f20740
Batch ID: 20250612_161035
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///crypto_credit.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database model for crypto assets
class CryptoAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    asset_type = db.Column(db.String(50), nullable=False)
    asset_value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for serialization
class CryptoAssetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CryptoAsset

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a new credit line
@app.route('/api/credit_line', methods=['POST'])
def create_credit_line():
    """
    Create a new credit line against crypto assets.
    Expects a JSON body with user_id, asset_type, and asset_value.
    """
    try:
        # Get JSON request data
        data = request.json
        user_id = data.get('user_id')
        asset_type = data.get('asset_type')
        asset_value = data.get('asset_value')

        # Validate input
        if not user_id or not asset_type or not asset_value:
            return jsonify({"error": "Missing required fields"}), 400

        # Create new CryptoAsset instance
        new_asset = CryptoAsset(user_id=user_id, asset_type=asset_type, asset_value=asset_value)

        # Add to session and commit to the database
        db.session.add(new_asset)
        db.session.commit()

        # Serialize the created asset
        asset_schema = CryptoAssetSchema()
        return jsonify(asset_schema.dump(new_asset)), 201

    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all credit lines for a user
@app.route('/api/credit_lines/<int:user_id>', methods=['GET'])
def get_credit_lines(user_id):
    """
    Retrieve all credit lines for a specific user.
    Expects user_id as a path parameter.
    """
    try:
        # Query the database for assets linked to the user
        assets = CryptoAsset.query.filter_by(user_id=user_id).all()

        # Serialize the assets
        asset_schema = CryptoAssetSchema(many=True)
        return jsonify(asset_schema.dump(assets)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```
