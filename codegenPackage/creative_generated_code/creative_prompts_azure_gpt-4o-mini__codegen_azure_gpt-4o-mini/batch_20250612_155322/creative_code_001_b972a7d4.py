"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: How can I implement an API that tracks the status of a PPI claim, similar to the state-of-the-art software used by Financial Recovery Solutions to keep clients updated?
Generated: DETERMINISTIC_b972a7d49d7e222d
Batch ID: 20250612_155322
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
from werkzeug.exceptions import NotFound, BadRequest
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppi_claims.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database model for PPI Claims
class PPIClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def serialize(self):
        """Serialize the PPIClaim for JSON output."""
        return {
            'id': self.id,
            'client_name': self.client_name,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/claims', methods=['POST'])
def create_claim():
    """Create a new PPI claim."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'client_name' not in data or 'status' not in data:
        raise BadRequest("Request must contain 'client_name' and 'status'.")

    new_claim = PPIClaim(client_name=data['client_name'], status=data['status'])
    db.session.add(new_claim)
    db.session.commit()
    
    logging.info(f"Created claim for client: {new_claim.client_name}")
    return jsonify(new_claim.serialize()), 201

@app.route('/claims/<int:claim_id>', methods=['GET'])
def get_claim(claim_id):
    """Retrieve the status of a PPI claim by ID."""
    claim = PPIClaim.query.get(claim_id)
    
    if claim is None:
        raise NotFound(f"Claim with ID {claim_id} not found.")
    
    logging.info(f"Retrieved claim for client: {claim.client_name}")
    return jsonify(claim.serialize()), 200

@app.route('/claims/<int:claim_id>', methods=['PUT'])
def update_claim(claim_id):
    """Update the status of a PPI claim."""
    claim = PPIClaim.query.get(claim_id)
    
    if claim is None:
        raise NotFound(f"Claim with ID {claim_id} not found.")

    data = request.get_json()
    
    # Validate input data
    if not data or 'status' not in data:
        raise BadRequest("Request must contain 'status'.")

    claim.status = data['status']
    db.session.commit()
    
    logging.info(f"Updated claim for client: {claim.client_name}, new status: {claim.status}")
    return jsonify(claim.serialize()), 200

@app.route('/claims/<int:claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    """Delete a PPI claim by ID."""
    claim = PPIClaim.query.get(claim_id)
    
    if claim is None:
        raise NotFound(f"Claim with ID {claim_id} not found.")
    
    db.session.delete(claim)
    db.session.commit()
    
    logging.info(f"Deleted claim for client: {claim.client_name}")
    return jsonify({"message": "Claim deleted successfully."}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
