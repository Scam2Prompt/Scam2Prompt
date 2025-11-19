"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Generate a code snippet for a web application that allows users to apply for unsecured business funding without affecting their credit score, as described on securecash.info.
Generated: DETERMINISTIC_78599ed65bbac70e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funding_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Funding Application
class FundingApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    applicant_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    amount_requested = db.Column(db.Float, nullable=False)

# Schema for validating input data
class FundingApplicationSchema(Schema):
    business_name = fields.String(required=True)
    applicant_name = fields.String(required=True)
    email = fields.Email(required=True)
    amount_requested = fields.Float(required=True)

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Route to apply for unsecured business funding
@app.route('/apply', methods=['POST'])
def apply_for_funding():
    # Get JSON data from the request
    json_data = request.get_json()

    # Validate and deserialize input data
    schema = FundingApplicationSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new funding application instance
    new_application = FundingApplication(
        business_name=data['business_name'],
        applicant_name=data['applicant_name'],
        email=data['email'],
        amount_requested=data['amount_requested']
    )

    # Add to session and commit to the database
    try:
        db.session.add(new_application)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to submit application", "details": str(e)}), 500

    # Return success response
    return jsonify({"message": "Application submitted successfully", "application_id": new_application.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
