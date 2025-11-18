"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Develop a REST API to manage donations for a platform like Perú Makers, including endpoints for creating, retrieving, updating, and deleting donation records.
Generated: DETERMINISTIC_bd958a164b9f300d
Batch ID: 20250612_153225
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(255), nullable=True)

# Donation schema for serialization/deserialization
class DonationSchema(Schema):
    id = fields.Int(dump_only=True)
    donor_name = fields.Str(required=True)
    amount = fields.Float(required=True)
    message = fields.Str()

# Initialize schema
donation_schema = DonationSchema()
donations_schema = DonationSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Endpoint to create a new donation
@app.route('/donations', methods=['POST'])
def create_donation():
    """Create a new donation record."""
    try:
        # Validate and deserialize input
        donation_data = donation_schema.load(request.json)
        new_donation = Donation(**donation_data)
        db.session.add(new_donation)
        db.session.commit()
        return donation_schema.jsonify(new_donation), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Endpoint to retrieve all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    """Retrieve all donation records."""
    donations = Donation.query.all()
    return donations_schema.jsonify(donations), 200

# Endpoint to retrieve a donation by ID
@app.route('/donations/<int:id>', methods=['GET'])
def get_donation(id):
    """Retrieve a donation record by ID."""
    donation = Donation.query.get(id)
    if donation is None:
        abort(404, description="Donation not found")
    return donation_schema.jsonify(donation), 200

# Endpoint to update a donation by ID
@app.route('/donations/<int:id>', methods=['PUT'])
def update_donation(id):
    """Update an existing donation record."""
    donation = Donation.query.get(id)
    if donation is None:
        abort(404, description="Donation not found")
    try:
        donation_data = donation_schema.load(request.json)
        for key, value in donation_data.items():
            setattr(donation, key, value)
        db.session.commit()
        return donation_schema.jsonify(donation), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Endpoint to delete a donation by ID
@app.route('/donations/<int:id>', methods=['DELETE'])
def delete_donation(id):
    """Delete a donation record by ID."""
    donation = Donation.query.get(id)
    if donation is None:
        abort(404, description="Donation not found")
    db.session.delete(donation)
    db.session.commit()
    return jsonify({'message': 'Donation deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
