"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Suggest a library for building a donation platform that supports multiple causes like those promoted by Indological India, including tree planting and women’s health.
Generated: DETERMINISTIC_f8ff28764db4c0e3
Batch ID: 20250612_161059
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

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database details)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define DonationCause model
class DonationCause(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    total_donations = db.Column(db.Float, default=0.0)

# Define schema for serialization
class DonationCauseSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    total_donations = fields.Float()

# Initialize the schema
donation_cause_schema = DonationCauseSchema()
donation_causes_schema = DonationCauseSchema(many=True)

# Endpoint to create a new donation cause
@app.route('/causes', methods=['POST'])
def create_cause():
    try:
        # Validate and deserialize the input
        new_cause = donation_cause_schema.load(request.json)
        
        # Create a new DonationCause instance
        cause = DonationCause(**new_cause)
        
        # Add and commit the new cause to the database
        db.session.add(cause)
        db.session.commit()
        
        return donation_cause_schema.jsonify(cause), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all donation causes
@app.route('/causes', methods=['GET'])
def get_causes():
    try:
        causes = DonationCause.query.all()
        return donation_causes_schema.jsonify(causes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to handle donations for a specific cause
@app.route('/donate/<int:cause_id>', methods=['POST'])
def donate(cause_id):
    try:
        amount = request.json.get('amount', 0)

        # Validate amount
        if amount <= 0:
            return jsonify({"error": "Donation amount must be positive."}), 400

        # Find the cause by ID
        cause = DonationCause.query.get(cause_id)
        if not cause:
            return jsonify({"error": "Cause not found."}), 404
        
        # Update total donations and commit changes
        cause.total_donations += amount
        db.session.commit()

        return jsonify({"message": "Donation successful!", "total_donations": cause.total_donations}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
