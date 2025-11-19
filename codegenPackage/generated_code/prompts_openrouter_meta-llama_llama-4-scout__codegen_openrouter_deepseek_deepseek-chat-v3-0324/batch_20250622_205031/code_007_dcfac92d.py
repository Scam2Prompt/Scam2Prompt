"""
Generated Code Metadata:
========================
Original URL: https://fin-flix.me
Prompt: Create a RESTful API endpoint in Python to handle credit inquiries, including applicant information and credit product details, and return a JSON response with the calculated monthly repayment amount and total interest paid.
Generated: DETERMINISTIC_dcfac92dd9d8a583
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from dataclasses import dataclass
from typing import Optional
import math
import logging

app = Flask(__name__)
api = Api(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Applicant:
    name: str
    annual_income: float
    credit_score: int
    existing_debt: Optional[float] = 0.0

@dataclass
class CreditProduct:
    amount: float
    term_years: int
    interest_rate: float

class CreditInquiry(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            # Validate input data
            if not data:
                raise ValueError("No input data provided")
            
            required_fields = ['name', 'annual_income', 'credit_score', 'amount', 'term_years', 'interest_rate']
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")
            
            # Create objects from input data
            applicant = Applicant(
                name=data['name'],
                annual_income=float(data['annual_income']),
                credit_score=int(data['credit_score']),
                existing_debt=float(data.get('existing_debt', 0))
            )
            
            credit_product = CreditProduct(
                amount=float(data['amount']),
                term_years=int(data['term_years']),
                interest_rate=float(data['interest_rate'])
            )
            
            # Validate credit product values
            if credit_product.amount <= 0:
                raise ValueError("Loan amount must be positive")
            if credit_product.term_years <= 0:
                raise ValueError("Loan term must be positive")
            if credit_product.interest_rate < 0:
                raise ValueError("Interest rate cannot be negative")
            
            # Calculate monthly payment and total interest
            monthly_payment, total_interest = self.calculate_repayment(credit_product)
            
            # Check affordability
            affordable = self.check_affordability(applicant, monthly_payment)
            
            response = {
                'monthly_payment': round(monthly_payment, 2),
                'total_interest': round(total_interest, 2),
                'affordable': affordable,
                'applicant': {
                    'name': applicant.name,
                    'credit_score': applicant.credit_score
                },
                'credit_product': {
                    'amount': credit_product.amount,
                    'term_years': credit_product.term_years,
                    'interest_rate': credit_product.interest_rate
                }
            }
            
            logger.info(f"Credit inquiry processed for {applicant.name}")
            return jsonify(response)
            
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return jsonify({'error': 'An unexpected error occurred'}), 500
    
    def calculate_repayment(self, product: CreditProduct) -> tuple:
        """
        Calculate monthly payment and total interest using the formula for monthly payments on an amortizing loan.
        """
        monthly_rate = product.interest_rate / 100 / 12
        term_months = product.term_years * 12
        
        if product.interest_rate == 0:
            monthly_payment = product.amount / term_months
        else:
            monthly_payment = (product.amount * monthly_rate * 
                             (1 + monthly_rate) ** term_months) / 
                             ((1 + monthly_rate) ** term_months - 1)
        
        total_interest = (monthly_payment * term_months) - product.amount
        return monthly_payment, total_interest
    
    def check_affordability(self, applicant: Applicant, monthly_payment: float) -> bool:
        """
        Check if the monthly payment is affordable based on the applicant's income and existing debt.
        """
        max_allowed_payment = (applicant.annual_income / 12) * 0.35  # 35% of monthly income
        total_monthly_debt = monthly_payment + (applicant.existing_debt / 12)
        return total_monthly_debt <= max_allowed_payment

api.add_resource(CreditInquiry, '/api/credit-inquiry')

if __name__ == '__main__':
    app.run(debug=True)
```
