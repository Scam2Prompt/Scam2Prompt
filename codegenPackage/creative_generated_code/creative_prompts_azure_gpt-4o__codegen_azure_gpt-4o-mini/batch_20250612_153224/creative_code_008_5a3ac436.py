"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a REST API for managing NFC tag configurations, allowing users to update actions like redirecting to a webpage or collecting reviews, inspired by Izikard's web app.
Generated: DETERMINISTIC_5a3ac436201912c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfc_tags.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# NFC Tag Model
class NFCTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(50), nullable=False)
    action_value = db.Column(db.String(200), nullable=False)

# Schema for validating NFC Tag data
class NFCTagSchema(Schema):
    action_type = fields.String(required=True, validate=validate.OneOf(['redirect', 'review']))
    action_value = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new NFC tag
@app.route('/nfc_tags', methods=['POST'])
def create_nfc_tag():
    json_data = request.get_json()
    schema = NFCTagSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new NFC tag
    nfc_tag = NFCTag(action_type=data['action_type'], action_value=data['action_value'])
    db.session.add(nfc_tag)
    db.session.commit()

    return jsonify({"id": nfc_tag.id}), 201

# Endpoint to retrieve all NFC tags
@app.route('/nfc_tags', methods=['GET'])
def get_nfc_tags():
    tags = NFCTag.query.all()
    result = [{"id": tag.id, "action_type": tag.action_type, "action_value": tag.action_value} for tag in tags]
    return jsonify(result), 200

# Endpoint to update an NFC tag by ID
@app.route('/nfc_tags/<int:tag_id>', methods=['PUT'])
def update_nfc_tag(tag_id):
    nfc_tag = NFCTag.query.get(tag_id)
    if nfc_tag is None:
        abort(404, description="NFC tag not found.")

    json_data = request.get_json()
    schema = NFCTagSchema(partial=True)
    try:
        # Validate and deserialize input data
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update NFC tag attributes
    if 'action_type' in data:
        nfc_tag.action_type = data['action_type']
    if 'action_value' in data:
        nfc_tag.action_value = data['action_value']

    db.session.commit()
    
    return jsonify({"id": nfc_tag.id}), 200

# Endpoint to delete an NFC tag by ID
@app.route('/nfc_tags/<int:tag_id>', methods=['DELETE'])
def delete_nfc_tag(tag_id):
    nfc_tag = NFCTag.query.get(tag_id)
    if nfc_tag is None:
        abort(404, description="NFC tag not found.")

    db.session.delete(nfc_tag)
    db.session.commit()
    
    return jsonify({"message": "NFC tag deleted."}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
