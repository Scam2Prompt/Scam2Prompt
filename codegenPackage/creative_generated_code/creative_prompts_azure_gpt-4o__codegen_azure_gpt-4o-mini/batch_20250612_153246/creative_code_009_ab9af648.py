"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Develop a REST API for NGOs to manage donor profiles and contributions, referencing Youngistaan Foundation's "Become a Real Hero" donation campaign.
Generated: DETERMINISTIC_ab9af64863ff484f
Batch ID: 20250612_153246
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///donors.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Donor
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contributions = db.relationship('Contribution', backref='donor', lazy=True)

# Database model for Contribution
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)

# Schema for validating Donor data
class DonorSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Schema for validating Contribution data
class ContributionSchema(Schema):
    amount = fields.Float(required=True)
    donor_id = fields.Int(required=True)

# Initialize database and create tables
@app.route('/init_db', methods=['POST'])
def init_db():
    """Endpoint to initialize the database."""
    db.create_all()
    return jsonify({"message": "Database initialized"}), 201

# Create a new donor
@app.route('/donors', methods=['POST'])
def create_donor():
    """Endpoint to create a new donor profile."""
    json_data = request.json
    try:
        data = DonorSchema().load(json_data)
        donor = Donor(name=data['name'], email=data['email'])
        db.session.add(donor)
        db.session.commit()
        return jsonify({"message": "Donor created", "donor": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve all donors
@app.route('/donors', methods=['GET'])
def get_donors():
    """Endpoint to retrieve all donor profiles."""
    donors = Donor.query.all()
    return jsonify([{"id": donor.id, "name": donor.name, "email": donor.email} for donor in donors]), 200

# Create a contribution
@app.route('/contributions', methods=['POST'])
def create_contribution():
    """Endpoint to create a contribution."""
    json_data = request.json
    try:
        data = ContributionSchema().load(json_data)
        contribution = Contribution(amount=data['amount'], donor_id=data['donor_id'])
        db.session.add(contribution)
        db.session.commit()
        return jsonify({"message": "Contribution recorded", "contribution": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve all contributions for a donor
@app.route('/donors/<int:donor_id>/contributions', methods=['GET'])
def get_contributions(donor_id):
    """Endpoint to retrieve all contributions made by a specific donor."""
    contributions = Contribution.query.filter_by(donor_id=donor_id).all()
    if contributions:
        return jsonify([{"id": contrib.id, "amount": contrib.amount} for contrib in contributions]), 200
    else:
        return jsonify({"message": "No contributions found for this donor."}), 404

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
``` 

Make sure to install the required packages using:
```bash
pip install Flask SQLAlchemy marshmallow
``` 

And set up your environment variable `DATABASE_URL` for the database connection string if you're not using SQLite.
