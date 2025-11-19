"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Create a REST API endpoint that allows users to submit land acquisition proposals, inspired by the processes described by Carolina Capital.
Generated: DETERMINISTIC_01815da21f0bcc9d
Batch ID: 20250612_160507
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///proposals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Proposal model
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create a schema for validating input data
class ProposalSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    amount = fields.Float(required=True)

# Initialize the schema
proposal_schema = ProposalSchema()

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/proposals', methods=['POST'])
def submit_proposal():
    """
    Endpoint to submit a land acquisition proposal.
    Expects a JSON payload with 'name', 'description', and 'amount'.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = proposal_schema.load(data)

        # Create a new proposal instance
        new_proposal = Proposal(
            name=validated_data['name'],
            description=validated_data['description'],
            amount=validated_data['amount']
        )

        # Add the proposal to the session and commit to the database
        db.session.add(new_proposal)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Proposal submitted successfully", "id": new_proposal.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
