"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cooperativadetasabajacl.com
Prompt: Create an API endpoint specification for a loan approval system that provides instant responses, including required user data and loan criteria based on the services offered by Cooperativa de Tasa Baja in Chile.
Generated: DETERMINISTIC_173958b22a91ce9f
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
api = Api(app)

# Loan criteria specification
LOAN_CRITERIA = {
    'min_amount': 100000,  # Minimum loan amount in CLP
    'max_amount': 5000000, # Maximum loan amount in CLP
    'min_term': 6,         # Minimum term in months
    'max_term': 60,        # Maximum term in months
    'interest_rate': 0.05, # Fixed interest rate
}

# User data schema for request validation
class UserDataSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=True, validate=validate.Range(min=18, max=70))
    income = fields.Float(required=True, validate=validate.Range(min=0))
    requested_amount = fields.Float(required=True, validate=validate.Range(min=LOAN_CRITERIA['min_amount'], max=LOAN_CRITERIA['max_amount']))
    term = fields.Integer(required=True, validate=validate.Range(min=LOAN_CRITERIA['min_term'], max=LOAN_CRITERIA['max_term']))

class LoanApproval(Resource):
    """API resource for loan approval system."""

    def post(self):
        """Process a loan approval request."""
        # Parse and validate user data from request
        try:
            data = UserDataSchema().load(request.json)
        except ValidationError as err:
            return {'errors': err.messages}, 400

        # Basic loan approval logic (this can be expanded)
        if self.calculate_approval(data):
            return {
                'message': 'Loan approved',
                'loan_criteria': LOAN_CRITERIA,
                'user_data': data
            }, 200
        else:
            return {
                'message': 'Loan denied',
                'loan_criteria': LOAN_CRITERIA,
                'user_data': data
            }, 403

    @staticmethod
    def calculate_approval(data):
        """Calculate loan approval based on user data."""
        # Simplified approval logic: checks if income can cover requested amount
        return data['income'] >= (data['requested_amount'] / data['term']) * 1.5  # simplistic coverage ratio

# Register the loan approval resource with the API
api.add_resource(LoanApproval, '/api/loan-approval')

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug for production
```
