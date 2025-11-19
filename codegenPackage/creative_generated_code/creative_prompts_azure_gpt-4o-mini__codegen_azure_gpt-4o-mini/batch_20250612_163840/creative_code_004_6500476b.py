"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Outline a RESTful API design for a loan application service that supports 100% purchase and rehab financing, referencing the unique features of Appak Capital's loan products.
Generated: DETERMINISTIC_6500476b266b8ec4
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///loans.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Loan model
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower_name = db.Column(db.String(100), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    purchase_financing = db.Column(db.Boolean, default=False)
    rehab_financing = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(50), default='Pending')  # Status can be Pending, Approved, or Rejected

    def __init__(self, borrower_name, loan_amount, purchase_financing, rehab_financing):
        self.borrower_name = borrower_name
        self.loan_amount = loan_amount
        self.purchase_financing = purchase_financing
        self.rehab_financing = rehab_financing

# Loan schema for serialization
class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loan
        load_instance = True

# Initialize the loan schema
loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

# Create a new loan application
@app.route('/loans', methods=['POST'])
def create_loan():
    try:
        # Validate and deserialize input data
        data = request.json
        if not all(key in data for key in ('borrower_name', 'loan_amount', 'purchase_financing', 'rehab_financing')):
            return jsonify({"error": "Missing required fields"}), 400
        
        loan = Loan(
            borrower_name=data['borrower_name'],
            loan_amount=data['loan_amount'],
            purchase_financing=data['purchase_financing'],
            rehab_financing=data['rehab_financing']
        )
        db.session.add(loan)
        db.session.commit()
        return loan_schema.jsonify(loan), 201

    except ValidationError as ve:
        return jsonify(ve.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all loan applications
@app.route('/loans', methods=['GET'])
def get_loans():
    try:
        loans = Loan.query.all()
        return loans_schema.jsonify(loans), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a single loan application by ID
@app.route('/loans/<int:id>', methods=['GET'])
def get_loan(id):
    try:
        loan = Loan.query.get_or_404(id)
        return loan_schema.jsonify(loan), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a loan application by ID
@app.route('/loans/<int:id>', methods=['PUT'])
def update_loan(id):
    try:
        loan = Loan.query.get_or_404(id)
        data = request.json

        # Update loan fields
        loan.borrower_name = data.get('borrower_name', loan.borrower_name)
        loan.loan_amount = data.get('loan_amount', loan.loan_amount)
        loan.purchase_financing = data.get('purchase_financing', loan.purchase_financing)
        loan.rehab_financing = data.get('rehab_financing', loan.rehab_financing)

        db.session.commit()
        return loan_schema.jsonify(loan), 200
    except ValidationError as ve:
        return jsonify(ve.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a loan application by ID
@app.route('/loans/<int:id>', methods=['DELETE'])
def delete_loan(id):
    try:
        loan = Loan.query.get_or_404(id)
        db.session.delete(loan)
        db.session.commit()
        return jsonify({"message": "Loan deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', True))
```
