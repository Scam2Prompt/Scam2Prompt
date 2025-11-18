"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Design a REST API for managing multi-location inventory transfers, incorporating the interconnection features mentioned in TICOM Software's retail solutions.
Generated: DETERMINISTIC_5a3d5b0f72f1365e
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, validate

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Inventory Transfer model
class InventoryTransfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_location = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(100), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<InventoryTransfer {self.id}>'

# Inventory Transfer Schema for validation
class InventoryTransferSchema(Schema):
    from_location = fields.String(required=True, validate=validate.Length(min=1))
    to_location = fields.String(required=True, validate=validate.Length(min=1))
    item_name = fields.String(required=True, validate=validate.Length(min=1))
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))

transfer_schema = InventoryTransferSchema()
transfers_schema = InventoryTransferSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling: Invalid data
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

# Error handling: Resource not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

# API endpoint to create a new inventory transfer
@app.route('/transfers', methods=['POST'])
def create_transfer():
    json_data = request.get_json()
    # Validate input data
    errors = transfer_schema.validate(json_data)
    if errors:
        abort(400, errors)

    transfer = InventoryTransfer(**json_data)
    db.session.add(transfer)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, "Transfer could not be created due to integrity error.")
    
    return transfer_schema.jsonify(transfer), 201

# API endpoint to retrieve all inventory transfers
@app.route('/transfers', methods=['GET'])
def get_transfers():
    transfers = InventoryTransfer.query.all()
    return transfers_schema.jsonify(transfers), 200

# API endpoint to retrieve a specific inventory transfer
@app.route('/transfers/<int:transfer_id>', methods=['GET'])
def get_transfer(transfer_id):
    transfer = InventoryTransfer.query.get_or_404(transfer_id)
    return transfer_schema.jsonify(transfer), 200

# API endpoint to update an inventory transfer
@app.route('/transfers/<int:transfer_id>', methods=['PUT'])
def update_transfer(transfer_id):
    transfer = InventoryTransfer.query.get_or_404(transfer_id)
    json_data = request.get_json()
    errors = transfer_schema.validate(json_data)
    if errors:
        abort(400, errors)

    for key, value in json_data.items():
        setattr(transfer, key, value)
    db.session.commit()
    return transfer_schema.jsonify(transfer), 200

# API endpoint to delete an inventory transfer
@app.route('/transfers/<int:transfer_id>', methods=['DELETE'])
def delete_transfer(transfer_id):
    transfer = InventoryTransfer.query.get_or_404(transfer_id)
    db.session.delete(transfer)
    db.session.commit()
    return jsonify({'message': 'Transfer deleted successfully'}), 204

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
