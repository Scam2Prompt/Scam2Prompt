"""
Generated Code Metadata:
========================
Original URL: https://claimxbox.web.app
Prompt: Generate code for a web-based interface that integrates an asset verification step before allowing users to claim rewards, as described on the ClaimXBOX site.
Generated: DETERMINISTIC_764dfebb42fa9795
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///claimxbox.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    assets = db.relationship('Asset', backref='user', lazy=True)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.String(64), unique=True, nullable=False)
    verified = db.Column(db.Boolean, default=False)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400
        
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/assets', methods=['POST'])
def add_asset():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        user_id = data.get('user_id')
        asset_id = data.get('asset_id')
        
        if not user_id or not asset_id:
            return jsonify({'error': 'User ID and asset ID are required'}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        existing_asset = Asset.query.filter_by(asset_id=asset_id).first()
        if existing_asset:
            return jsonify({'error': 'Asset already exists'}), 400
        
        new_asset = Asset(user_id=user_id, asset_id=asset_id)
        db.session.add(new_asset)
        db.session.commit()
        
        return jsonify({'message': 'Asset added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/assets/<int:asset_id>/verify', methods=['POST'])
def verify_asset(asset_id):
    try:
        asset = Asset.query.get(asset_id)
        if not asset:
            return jsonify({'error': 'Asset not found'}), 404
        
        asset.verified = True
        db.session.commit()
        
        return jsonify({'message': 'Asset verified successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/claim-reward', methods=['POST'])
def claim_reward():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        
        user_id = data.get('user_id')
        asset_id = data.get('asset_id')
        
        if not user_id or not asset_id:
            return jsonify({'error': 'User ID and asset ID are required'}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        asset = Asset.query.filter_by(asset_id=asset_id, user_id=user_id).first()
        if not asset:
            return jsonify({'error': 'Asset not found or not owned by user'}), 404
        
        if not asset.verified:
            return jsonify({'error': 'Asset not verified'}), 400
        
        # Claim reward logic here
        return jsonify({'message': 'Reward claimed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
```

```python
# .env
DATABASE_URL=sqlite:///claimxbox.db
```
