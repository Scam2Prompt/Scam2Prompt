"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Develop a REST API for NGOs to manage donor profiles and contributions, referencing Youngistaan Foundation's "Become a Real Hero" donation campaign.
Generated: DETERMINISTIC_ab9af64863ff484f
Batch ID: 20250612_153246
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Donor model
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contributions = db.relationship('Contribution', backref='donor', lazy=True)

# Define the Contribution model
class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)

# Create a schema for validation using Marshmallow
class DonorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class ContributionSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    donor_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new donor
@app.route('/donors', methods=['POST'])
def create_donor():
    json_data = request.get_json()
    try:
        data = DonorSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_donor = Donor(name=data['name'], email=data['email'])
    db.session.add(new_donor)
    db.session.commit()
    return DonorSchema().dump(new_donor), 201

# Route to get all donors
@app.route('/donors', methods=['GET'])
def get_donors():
    donors = Donor.query.all()
    return DonorSchema(many=True).dump(donors), 200

# Route to create a new contribution
@app.route('/contributions', methods=['POST'])
def create_contribution():
    json_data = request.get_json()
    try:
        data = ContributionSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    donor = Donor.query.get(data['donor_id'])
    if not donor:
        return jsonify({"message": "Donor not found"}), 404

    new_contribution = Contribution(amount=data['amount'], donor_id=data['donor_id'])
    db.session.add(new_contribution)
    db.session.commit()
    return ContributionSchema().dump(new_contribution), 201

# Route to get all contributions
@app.route('/contributions', methods=['GET'])
def get_contributions():
    contributions = Contribution.query.all()
    return ContributionSchema(many=True).dump(contributions), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
