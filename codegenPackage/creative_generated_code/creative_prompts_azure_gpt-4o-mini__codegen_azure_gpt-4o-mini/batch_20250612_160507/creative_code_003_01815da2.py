"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Create a REST API endpoint that allows users to submit land acquisition proposals, inspired by the processes described by Carolina Capital.
Generated: DETERMINISTIC_01815da21f0bcc9d
Batch ID: 20250612_160507
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

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite for simplicity, change as needed for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proposals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Land Acquisition Proposals
class LandAcquisitionProposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    amount_requested = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Proposal {self.name}>'

# Proposal schema for input validation
class ProposalSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    amount_requested = fields.Float(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit a land acquisition proposal
@app.route('/proposals', methods=['POST'])
def submit_proposal():
    # Parse and validate the request data
    schema = ProposalSchema()
    try:
        proposal_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Create a new proposal instance
    new_proposal = LandAcquisitionProposal(**proposal_data)

    # Add to the session and commit to the database
    try:
        db.session.add(new_proposal)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback session on error
        return jsonify({"error": str(e)}), 500  # Return server error

    return jsonify({"message": "Proposal submitted successfully", "id": new_proposal.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
