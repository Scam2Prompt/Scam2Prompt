"""
Generated Code Metadata:
========================
Original URL: https://seelenschnell.site
Prompt: Create a RESTful API endpoint to handle coffin transfer requests, including parameters for transfer type (e.g., within Germany, within Europe), distance, and customer details.
Generated: DETERMINISTIC_8297928c70b949e3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffin_transfers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for coffin transfer requests
class CoffinTransfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transfer_type = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)

# Schema for validating incoming requests
class CoffinTransferSchema(Schema):
    transfer_type = fields.String(required=True)
    distance = fields.Float(required=True)
    customer_name = fields.String(required=True)
    customer_email = fields.Email(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to handle coffin transfer requests
@app.route('/api/coffin_transfer', methods=['POST'])
def create_coffin_transfer():
    # Validate incoming JSON data
    schema = CoffinTransferSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new coffin transfer request
    new_transfer = CoffinTransfer(
        transfer_type=data['transfer_type'],
        distance=data['distance'],
        customer_name=data['customer_name'],
        customer_email=data['customer_email']
    )

    # Add to the database and commit
    try:
        db.session.add(new_transfer)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create transfer request", "details": str(e)}), 500

    # Return success response
    return jsonify({"message": "Coffin transfer request created successfully", "id": new_transfer.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
