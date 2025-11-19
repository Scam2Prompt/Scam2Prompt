"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Construct a RESTful API endpoint that provides tailored funding options for property finance based on user input regarding project type and funding needs.
Generated: DETERMINISTIC_4af6d5b72b597e50
Batch ID: 20250612_160158
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

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funding_options.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the FundingOption model
class FundingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_type = db.Column(db.String(50), nullable=False)
    funding_amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Schema for validating input
class FundingOptionSchema(Schema):
    project_type = fields.Str(required=True)
    funding_amount = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get tailored funding options
@app.route('/api/funding-options', methods=['POST'])
def get_funding_options():
    # Validate and parse incoming JSON data
    try:
        data = request.get_json()
        validated_data = FundingOptionSchema().load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    # Fetch funding options based on user input
    project_type = validated_data['project_type']
    funding_amount = validated_data['funding_amount']

    try:
        options = FundingOption.query.filter_by(project_type=project_type).all()
        if not options:
            return jsonify({"message": "No funding options found for the given criteria."}), 404

        # Filter options based on funding amount
        tailored_options = [
            {"id": option.id, "project_type": option.project_type,
             "funding_amount": option.funding_amount, "description": option.description}
            for option in options if option.funding_amount <= funding_amount
        ]

        return jsonify(tailored_options), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while fetching funding options.", "details": str(e)}), 500

# Example route to add funding options for testing purposes
@app.route('/api/funding-options/add', methods=['POST'])
def add_funding_option():
    data = request.get_json()
    new_option = FundingOption(
        project_type=data['project_type'],
        funding_amount=data['funding_amount'],
        description=data['description']
    )
    db.session.add(new_option)
    db.session.commit()
    return jsonify({"message": "Funding option added successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
