"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Generate a code snippet for a web application that allows users to apply for a personal loan, incorporating features like flexible repayment terms and quick approval as described on SGFC Finance.
Generated: DETERMINISTIC_e088b20cb8acec74
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Loan Application model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    repayment_terms = db.Column(db.String(100), nullable=False)  # e.g., "6 months", "1 year"
    contact_info = db.Column(db.String(100), nullable=False)

# Create a schema for validating input data
class LoanApplicationSchema(Schema):
    name = fields.Str(required=True)
    amount = fields.Float(required=True)
    repayment_terms = fields.Str(required=True)
    contact_info = fields.Str(required=True)

# Initialize the schema
loan_schema = LoanApplicationSchema()

# Route for applying for a personal loan
@app.route('/apply', methods=['POST'])
def apply_for_loan():
    try:
        # Validate and deserialize input data
        data = loan_schema.load(request.json)
        
        # Create a new loan application instance
        new_application = LoanApplication(
            name=data['name'],
            amount=data['amount'],
            repayment_terms=data['repayment_terms'],
            contact_info=data['contact_info']
        )

        # Add the new application to the session and commit to the database
        db.session.add(new_application)
        db.session.commit()

        return jsonify({"message": "Loan application submitted successfully!", "id": new_application.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle general exceptions
        return jsonify({"error": str(e)}), 500

# Route to create the database
@app.route('/init-db', methods=['GET'])
def init_db():
    db.create_all()
    return jsonify({"message": "Database initialized!"}), 200

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
