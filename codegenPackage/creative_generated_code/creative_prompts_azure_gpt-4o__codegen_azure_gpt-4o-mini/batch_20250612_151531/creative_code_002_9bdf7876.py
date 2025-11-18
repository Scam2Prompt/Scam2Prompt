"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Generate code for a web service that connects users to lenders based on predefined criteria, such as loan amount and credit score, using a ping-tree model for lender selection.
Generated: DETERMINISTIC_9bdf7876aa15dd9a
Batch ID: 20250612_151531
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lenders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Lender model
class Lender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    min_loan_amount = db.Column(db.Float, nullable=False)
    max_loan_amount = db.Column(db.Float, nullable=False)
    min_credit_score = db.Column(db.Integer, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Define schema for request validation
class LoanRequestSchema(Schema):
    loan_amount = fields.Float(required=True)
    credit_score = fields.Integer(required=True)

# Endpoint to connect users to lenders
@app.route('/find_lender', methods=['POST'])
def find_lender():
    # Validate incoming request
    schema = LoanRequestSchema()
    try:
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    loan_amount = request_data['loan_amount']
    credit_score = request_data['credit_score']

    # Ping-tree model logic to filter lenders
    try:
        lenders = Lender.query.filter(
            Lender.min_loan_amount <= loan_amount,
            Lender.max_loan_amount >= loan_amount,
            Lender.min_credit_score <= credit_score
        ).all()

        # Return a list of matching lenders
        if lenders:
            return jsonify([{'id': lender.id, 'name': lender.name} for lender in lenders]), 200
        else:
            return jsonify({"message": "No lenders found matching the criteria."}), 404

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
