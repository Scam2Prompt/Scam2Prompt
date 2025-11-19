"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rfd.claims
Prompt: What libraries are recommended for building a claims management system as described on rfd.claims?
Generated: DETERMINISTIC_65eb718f0c013516
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# claims_management_system.py

"""
Claims Management System
This script sets up a basic framework for a claims management system using recommended libraries.
"""

# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///claims.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Claim model
class Claim(db.Model):
    """Model representing a claim."""
    id = db.Column(db.Integer, primary_key=True)
    claimant_name = db.Column(db.String(100), nullable=False)
    claim_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Create a schema for input validation
class ClaimSchema(Schema):
    """Schema for validating claim input."""
    claimant_name = fields.String(required=True)
    claim_amount = fields.Float(required=True)
    status = fields.String()

# Initialize schema
claim_schema = ClaimSchema()
claims_schema = ClaimSchema(many=True)

# Endpoint to create a new claim
@app.route('/claims', methods=['POST'])
def create_claim():
    """Create a new claim."""
    try:
        # Validate and deserialize input
        claim_data = claim_schema.load(request.json)
        
        # Create a new claim instance
        new_claim = Claim(**claim_data)
        
        # Add to the session and commit to the database
        db.session.add(new_claim)
        db.session.commit()
        
        return claim_schema.jsonify(new_claim), 201
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Failed to create claim: {str(e)}")
        return jsonify({"error": "Failed to create claim"}), 500

# Endpoint to retrieve all claims
@app.route('/claims', methods=['GET'])
def get_claims():
    """Retrieve all claims."""
    try:
        claims = Claim.query.all()
        return claims_schema.jsonify(claims), 200
    except Exception as e:
        logging.error(f"Failed to retrieve claims: {str(e)}")
        return jsonify({"error": "Failed to retrieve claims"}), 500

# Endpoint to update a claim status
@app.route('/claims/<int:id>', methods=['PUT'])
def update_claim(id):
    """Update the status of a claim."""
    try:
        claim = Claim.query.get_or_404(id)
        claim_data = claim_schema.load(request.json)

        # Update claim attributes
        for key, value in claim_data.items():
            setattr(claim, key, value)

        # Commit changes to the database
        db.session.commit()
        
        return claim_schema.jsonify(claim), 200
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Failed to update claim: {str(e)}")
        return jsonify({"error": "Failed to update claim"}), 500

# Endpoint to delete a claim
@app.route('/claims/<int:id>', methods=['DELETE'])
def delete_claim(id):
    """Delete a claim by ID."""
    try:
        claim = Claim.query.get_or_404(id)
        db.session.delete(claim)
        db.session.commit()
        
        return jsonify({"message": "Claim deleted successfully"}), 204
    except Exception as e:
        logging.error(f"Failed to delete claim: {str(e)}")
        return jsonify({"error": "Failed to delete claim"}), 500

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```
