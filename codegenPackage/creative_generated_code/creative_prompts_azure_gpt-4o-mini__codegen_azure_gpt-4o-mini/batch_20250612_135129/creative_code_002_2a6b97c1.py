"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safeglobal.pages.dev
Prompt: What are the steps to create a stealth security feature for a multi-owner asset management platform?
Generated: DETERMINISTIC_2a6b97c1fea3020b
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing asset information
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(100), nullable=False)
    asset_name = db.Column(db.String(200), nullable=False)
    encrypted_data = db.Column(db.Text, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to generate a new encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data using the provided key
def encrypt_data(key, data):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Function to decrypt data using the provided key
def decrypt_data(key, encrypted_data):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# API endpoint to create a new asset
@app.route('/assets', methods=['POST'])
def create_asset():
    try:
        data = request.get_json()

        if 'owner_id' not in data or 'asset_name' not in data:
            return jsonify({"error": "owner_id and asset_name are required"}), 400

        # Generate a new encryption key
        key = generate_key()
        
        # Encrypt asset data
        encrypted_data = encrypt_data(key, json.dumps(data))

        # Store the asset
        new_asset = Asset(owner_id=data['owner_id'], asset_name=data['asset_name'], encrypted_data=encrypted_data)

        db.session.add(new_asset)
        db.session.commit()

        return jsonify({"message": "Asset created", "asset_id": new_asset.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Asset already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve an asset
@app.route('/assets/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    try:
        asset = Asset.query.get(asset_id)

        if not asset:
            return jsonify({"error": "Asset not found"}), 404

        # Placeholder for owner authentication and key retrieval
        # In practice, retrieve the key securely based on owner_id
        key = generate_key()  # This should be replaced by the actual key retrieval logic

        # Decrypt the asset data
        decrypted_data = decrypt_data(key, asset.encrypted_data)

        return jsonify({"asset_id": asset.id, "data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)
```
