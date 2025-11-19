"""
Generated Code Metadata:
========================
Original URL: https://www.cooperativadetasabajacl.com
Prompt: Create an API endpoint specification for a loan approval system that provides instant responses, including required user data and loan criteria based on the services offered by Cooperativa de Tasa Baja in Chile.
Generated: DETERMINISTIC_173958b22a91ce9f
Batch ID: 20250612_161231
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Loan Application
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_term = db.Column(db.Integer, nullable=False)  # in months
    interest_rate = db.Column(db.Float, nullable=False)
    approved = db.Column(db.Boolean, default=False)

# Schema for validating loan application data
class LoanApplicationSchema(Schema):
    user_id = fields.Str(required=True)
    loan_amount = fields.Float(required=True)
    loan_term = fields.Int(required=True)
    interest_rate = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint for loan approval
@app.route('/api/loan-approval', methods=['POST'])
def loan_approval():
    # Validate incoming JSON data
    schema = LoanApplicationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Business logic for loan approval
    # Here we can add criteria based on Cooperativa de Tasa Baja's policies
    if data['loan_amount'] <= 0 or data['loan_term'] <= 0:
        return jsonify({"error": "Loan amount and term must be positive."}), 400

    # Example criteria for approval
    if data['interest_rate'] < 0 or data['interest_rate'] > 30:
        return jsonify({"error": "Interest rate must be between 0 and 30."}), 400

    # Simulate loan approval process
    approved = True  # Placeholder for actual approval logic

    # Save the loan application to the database
    loan_application = LoanApplication(
        user_id=data['user_id'],
        loan_amount=data['loan_amount'],
        loan_term=data['loan_term'],
        interest_rate=data['interest_rate'],
        approved=approved
    )
    db.session.add(loan_application)
    db.session.commit()

    # Return the response
    return jsonify({
        "message": "Loan application submitted successfully.",
        "approved": approved,
        "loan_details": {
            "user_id": loan_application.user_id,
            "loan_amount": loan_application.loan_amount,
            "loan_term": loan_application.loan_term,
            "interest_rate": loan_application.interest_rate
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
```
