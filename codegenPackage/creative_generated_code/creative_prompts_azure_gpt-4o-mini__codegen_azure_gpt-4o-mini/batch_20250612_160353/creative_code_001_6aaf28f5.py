"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgn-faucet.vercel.app
Prompt: What are the steps to customize the faucet code available on the Gitcoin Passport Gated Faucet page?
Generated: DETERMINISTIC_6aaf28f59c7d9a4a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# faucet.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///faucet.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the faucet requests
class FaucetRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(42), nullable=False)  # Ethereum address
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create a schema for request validation
class FaucetRequestSchema(Schema):
    address = fields.String(required=True)
    amount = fields.Float(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint for requesting funds from the faucet
@app.route('/request', methods=['POST'])
def request_funds():
    # Validate and deserialize input
    schema = FaucetRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new faucet request instance
    new_request = FaucetRequest(address=data['address'], amount=data['amount'])
    
    # Handle database operations
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Request successful", "id": new_request.id}), 201

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"error": str(error)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true', host='0.0.0.0')
```
