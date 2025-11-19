"""
Generated Code Metadata:
========================
Original URL: https://globalfxoption.com
Prompt: Illustrate how to implement a loan application process in a web application, referencing the simplified process described by Global FX Option.
Generated: DETERMINISTIC_d80e9d2235fed19c
Batch ID: 20250612_155651
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
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    loan_purpose = db.Column(db.String(200), nullable=False)
    employment_status = db.Column(db.String(50), nullable=False)
    annual_income = db.Column(db.Float, nullable=False)
    credit_score = db.Column(db.Integer)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'applicant_name': self.applicant_name,
            'email': self.email,
            'phone': self.phone,
            'loan_amount': self.loan_amount,
            'loan_purpose': self.loan_purpose,
            'employment_status': self.employment_status,
            'annual_income': self.annual_income,
            'credit_score': self.credit_score,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Helper Functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

# Routes
@app.route('/api/loan-application', methods=['POST'])
def create_loan_application():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['applicant_name', 'email', 'phone', 'loan_amount', 
                          'loan_purpose', 'employment_status', 'annual_income']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Validate phone format
        if not validate_phone(data['phone']):
            return jsonify({'error': 'Invalid phone number format'}), 400
        
        # Validate loan amount is positive
        if float(data['loan_amount']) <= 0:
            return jsonify({'error': 'Loan amount must be positive'}), 400
        
        # Validate annual income is positive
        if float(data['annual_income']) <= 0:
            return jsonify({'error': 'Annual income must be positive'}), 400
        
        # Create new application
        application = LoanApplication(
            applicant_name=data['applicant_name'],
            email=data['email'],
            phone=data['phone'],
            loan_amount=float(data['loan_amount']),
            loan_purpose=data['loan_purpose'],
            employment_status=data['employment_status'],
            annual_income=float(data['annual_income']),
            credit_score=data.get('credit_score')
        )
        
        db.session.add(application)
        db.session.commit()
        
        return jsonify(application.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/loan-application/<int:application_id>', methods=['GET'])
def get_loan_application(application_id):
    try:
        application = LoanApplication.query.get_or_404(application_id)
        return jsonify(application.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/loan-application/<int:application_id>/status', methods=['PATCH'])
def update_application_status(application_id):
    try:
        data = request.get_json()
        if 'status' not in data:
            return jsonify({'error': 'status is required'}), 400
        
        valid_statuses = ['pending', 'approved', 'rejected', 'under_review']
        if data['status'] not in valid_statuses:
            return jsonify({'error': 'Invalid status value'}), 400
        
        application = LoanApplication.query.get_or_404(application_id)
        application.status = data['status']
        db.session.commit()
        
        return jsonify(application.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Initialization
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
