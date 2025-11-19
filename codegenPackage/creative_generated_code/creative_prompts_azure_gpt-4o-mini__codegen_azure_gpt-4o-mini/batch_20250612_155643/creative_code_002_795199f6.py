"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compoundclaims.net
Prompt: Write a code snippet that demonstrates how to integrate Compound Claims into a web application.
Generated: DETERMINISTIC_795199f60eb4b163
Batch ID: 20250612_155643
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///claims.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a database model for Claims
class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Schema for validating input data
class ClaimSchema(Schema):
    description = fields.String(required=True)
    amount = fields.Float(required=True)

# Create a schema instance
claim_schema = ClaimSchema()

# Create database tables
with app.app_context():
    db.create_all()

# Route to create a new claim
@app.route('/claims', methods=['POST'])
def create_claim():
    """
    Create a new claim.
    Expects a JSON body with 'description' and 'amount'.
    Returns the created claim data or an error message.
    """
    try:
        # Validate and deserialize input data
        claim_data = claim_schema.load(request.json)
        
        # Create a new Claim instance
        new_claim = Claim(**claim_data)
        
        # Add the claim to the session and commit
        db.session.add(new_claim)
        db.session.commit()
        
        # Return the created claim as JSON
        return jsonify(claim_schema.dump(new_claim)), 201

    except ValidationError as e:
        # Handle validation errors
        return jsonify({"error": e.messages}), 400
    
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": str(e)}), 500

# Route to retrieve all claims
@app.route('/claims', methods=['GET'])
def get_claims():
    """
    Retrieve all claims.
    Returns a list of claims in JSON format.
    """
    try:
        claims = Claim.query.all()
        return jsonify(claim_schema.dump(claims, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a claim's status
@app.route('/claims/<int:claim_id>', methods=['PUT'])
def update_claim_status(claim_id):
    """
    Update the status of a claim identified by claim_id.
    Expects a JSON body with 'status'.
    Returns the updated claim data or an error message.
    """
    try:
        # Find claim by ID
        claim = Claim.query.get_or_404(claim_id)
        
        # Update claim status from request data
        claim.status = request.json.get('status', claim.status)
        
        # Commit the changes to the database
        db.session.commit()
        
        return jsonify(claim_schema.dump(claim)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
