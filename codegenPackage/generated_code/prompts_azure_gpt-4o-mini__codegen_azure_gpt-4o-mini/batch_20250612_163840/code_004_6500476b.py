"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Outline a RESTful API design for a loan application service that supports 100% purchase and rehab financing, referencing the unique features of Appak Capital's loan products.
Generated: DETERMINISTIC_6500476b266b8ec4
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Loan model
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String(100), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_type = db.Column(db.String(50), nullable=False)  # e.g., 'purchase', 'rehab'
    status = db.Column(db.String(50), default='pending')  # e.g., 'pending', 'approved', 'rejected'

# Loan schema for validation
class LoanSchema(Schema):
    borrower_name = fields.Str(required=True)
    loan_amount = fields.Float(required=True)
    loan_type = fields.Str(required=True, validate=lambda x: x in ['purchase', 'rehab'])
    status = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new loan application
@app.route('/loans', methods=['POST'])
def create_loan():
    try:
        # Validate and deserialize input
        loan_data = LoanSchema().load(request.json)
        new_loan = Loan(**loan_data)
        db.session.add(new_loan)
        db.session.commit()
        return jsonify(LoanSchema().dump(new_loan)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve all loan applications
@app.route('/loans', methods=['GET'])
def get_loans():
    loans = Loan.query.all()
    return jsonify(LoanSchema(many=True).dump(loans)), 200

# Retrieve a specific loan application by ID
@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    return jsonify(LoanSchema().dump(loan)), 200

# Update a loan application
@app.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    try:
        # Validate and deserialize input
        loan_data = LoanSchema().load(request.json)
        for key, value in loan_data.items():
            setattr(loan, key, value)
        db.session.commit()
        return jsonify(LoanSchema().dump(loan)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a loan application
@app.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    db.session.delete(loan)
    db.session.commit()
    return jsonify({"message": "Loan application deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
