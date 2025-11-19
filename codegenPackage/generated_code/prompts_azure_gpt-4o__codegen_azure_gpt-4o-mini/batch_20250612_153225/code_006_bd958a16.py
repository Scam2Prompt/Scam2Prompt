"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Develop a REST API to manage donations for a platform like Perú Makers, including endpoints for creating, retrieving, updating, and deleting donation records.
Generated: DETERMINISTIC_bd958a164b9f300d
Batch ID: 20250612_153225
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Donation model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(255), nullable=True)

# Donation schema for validation and serialization
class DonationSchema(Schema):
    id = fields.Int(dump_only=True)
    donor_name = fields.Str(required=True)
    amount = fields.Float(required=True)
    message = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# Create a donation
@app.route('/donations', methods=['POST'])
def create_donation():
    """Create a new donation record."""
    try:
        donation_data = request.get_json()
        donation_schema = DonationSchema()
        donation = donation_schema.load(donation_data)
        new_donation = Donation(**donation)
        db.session.add(new_donation)
        db.session.commit()
        return donation_schema.dump(new_donation), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    """Retrieve all donation records."""
    donations = Donation.query.all()
    donation_schema = DonationSchema(many=True)
    return donation_schema.dump(donations), 200

# Retrieve a specific donation by ID
@app.route('/donations/<int:donation_id>', methods=['GET'])
def get_donation(donation_id):
    """Retrieve a donation record by ID."""
    donation = Donation.query.get(donation_id)
    if donation is None:
        abort(404)
    donation_schema = DonationSchema()
    return donation_schema.dump(donation), 200

# Update a donation
@app.route('/donations/<int:donation_id>', methods=['PUT'])
def update_donation(donation_id):
    """Update an existing donation record."""
    donation = Donation.query.get(donation_id)
    if donation is None:
        abort(404)
    
    try:
        donation_data = request.get_json()
        donation_schema = DonationSchema()
        updated_donation = donation_schema.load(donation_data)
        for key, value in updated_donation.items():
            setattr(donation, key, value)
        db.session.commit()
        return donation_schema.dump(donation), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete a donation
@app.route('/donations/<int:donation_id>', methods=['DELETE'])
def delete_donation(donation_id):
    """Delete a donation record."""
    donation = Donation.query.get(donation_id)
    if donation is None:
        abort(404)
    
    try:
        db.session.delete(donation)
        db.session.commit()
        return jsonify({"message": "Donation deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
