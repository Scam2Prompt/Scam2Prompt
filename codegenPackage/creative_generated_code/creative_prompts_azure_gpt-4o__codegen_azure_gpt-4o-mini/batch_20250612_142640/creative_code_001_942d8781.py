"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Create a REST API for an asset finance brokerage service that allows users to submit proposals for financing assets such as HGVs, marine craft, or agricultural equipment, referencing the offerings on Rhino Asset Finance.
Generated: DETERMINISTIC_942d878179d046b8
Batch ID: 20250612_142640
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asset_finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Proposal model
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)

    def __init__(self, asset_type, amount, duration_months):
        self.asset_type = asset_type
        self.amount = amount
        self.duration_months = duration_months

# Proposal schema
class ProposalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proposal

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to submit a proposal
@app.route('/api/proposals', methods=['POST'])
def submit_proposal():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input data
        if not data or 'asset_type' not in data or 'amount' not in data or 'duration_months' not in data:
            return jsonify({"error": "Invalid input data"}), 400

        # Create a new proposal
        new_proposal = Proposal(
            asset_type=data['asset_type'],
            amount=data['amount'],
            duration_months=data['duration_months']
        )

        # Add to the database
        db.session.add(new_proposal)
        db.session.commit()

        # Serialize the proposal
        proposal_schema = ProposalSchema()
        return jsonify(proposal_schema.dump(new_proposal)), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for HTTP errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
