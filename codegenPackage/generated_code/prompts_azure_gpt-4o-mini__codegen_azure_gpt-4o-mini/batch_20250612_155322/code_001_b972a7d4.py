"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: How can I implement an API that tracks the status of a PPI claim, similar to the state-of-the-art software used by Financial Recovery Solutions to keep clients updated?
Generated: DETERMINISTIC_b972a7d49d7e222d
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppi_claims.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for PPI claims
class PPIClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Schema for validating input data
class PPIClaimSchema(Schema):
    client_name = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a new PPI claim
@app.route('/api/claims', methods=['POST'])
def create_claim():
    try:
        # Validate and deserialize input data
        claim_data = PPIClaimSchema().load(request.json)
        new_claim = PPIClaim(client_name=claim_data['client_name'], status=claim_data['status'])
        db.session.add(new_claim)
        db.session.commit()
        return jsonify({"message": "Claim created successfully", "id": new_claim.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating claim: {e}")
        return jsonify({"error": "An error occurred while creating the claim"}), 500

# API endpoint to get the status of a PPI claim
@app.route('/api/claims/<int:claim_id>', methods=['GET'])
def get_claim_status(claim_id):
    try:
        claim = PPIClaim.query.get_or_404(claim_id)
        return jsonify({"client_name": claim.client_name, "status": claim.status}), 200
    except Exception as e:
        logging.error(f"Error retrieving claim status: {e}")
        return jsonify({"error": "An error occurred while retrieving the claim status"}), 500

# API endpoint to update the status of a PPI claim
@app.route('/api/claims/<int:claim_id>', methods=['PUT'])
def update_claim_status(claim_id):
    try:
        claim = PPIClaim.query.get_or_404(claim_id)
        claim_data = PPIClaimSchema().load(request.json)
        claim.status = claim_data['status']
        db.session.commit()
        return jsonify({"message": "Claim status updated successfully"}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating claim status: {e}")
        return jsonify({"error": "An error occurred while updating the claim status"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
