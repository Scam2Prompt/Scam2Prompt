"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Outline a REST API design for managing user applications and NFT assets in the MetaLeagues platform.
Generated: DETERMINISTIC_51ff134089735bca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metaleagues.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    applications = db.relationship('Application', backref='user', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nfts = db.relationship('NFT', backref='application', lazy=True)

class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_id = db.Column(db.String(120), unique=True, nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)

# Schemas for validation
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)

class ApplicationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    user_id = fields.Int(required=True)

class NftSchema(Schema):
    id = fields.Int(dump_only=True)
    token_id = fields.Str(required=True)
    application_id = fields.Int(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# User routes
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    user_schema = UserSchema()
    try:
        user_data = user_schema.load(request.json)
        new_user = User(username=user_data['username'])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by ID."""
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()
    return user_schema.dump(user)

# Application routes
@app.route('/applications', methods=['POST'])
def create_application():
    """Create a new application for a user."""
    app_schema = ApplicationSchema()
    try:
        app_data = app_schema.load(request.json)
        new_app = Application(name=app_data['name'], user_id=app_data['user_id'])
        db.session.add(new_app)
        db.session.commit()
        return app_schema.dump(new_app), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/applications/<int:app_id>', methods=['GET'])
def get_application(app_id):
    """Retrieve an application by ID."""
    application = Application.query.get_or_404(app_id)
    app_schema = ApplicationSchema()
    return app_schema.dump(application)

# NFT routes
@app.route('/nfts', methods=['POST'])
def create_nft():
    """Create a new NFT for an application."""
    nft_schema = NftSchema()
    try:
        nft_data = nft_schema.load(request.json)
        new_nft = NFT(token_id=nft_data['token_id'], application_id=nft_data['application_id'])
        db.session.add(new_nft)
        db.session.commit()
        return nft_schema.dump(new_nft), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/nfts/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    """Retrieve an NFT by ID."""
    nft = NFT.query.get_or_404(nft_id)
    nft_schema = NftSchema()
    return nft_schema.dump(nft)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
