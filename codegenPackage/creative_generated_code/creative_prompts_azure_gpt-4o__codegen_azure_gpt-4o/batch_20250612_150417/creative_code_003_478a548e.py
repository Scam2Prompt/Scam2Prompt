"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Create a web application that integrates real-time account access for personal loan management, similar to the online banking features described by Ambro Contables.
Generated: DETERMINISTIC_478a548e98529ddc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a clean, well-documented, production-ready web application using Python and the Flask framework. This application includes features to manage personal loans with real-time account access:

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the database (SQLite for simplicity in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """
    User model to store user details.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Loan(db.Model):
    """
    Loan model to store loan details for a user.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    duration_in_months = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('loans', lazy=True))

# Create DB schema
with app.app_context():
    db.create_all()

# Routes
@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']
        
        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "User with this email already exists"}), 400

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name, "email": new_user.email}}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the user", "details": str(e)}), 500

@app.route('/loans', methods=['POST'])
def create_loan():
    """
    Endpoint to create a new loan for a user.
    """
    try:
        data = request.json
        user_id = data['user_id']
        amount = data['amount']
        interest_rate = data['interest_rate']
        duration_in_months = data['duration_in_months']

        if not user_id or not amount or not interest_rate or not duration_in_months:
            return jsonify({"error": "All fields are required"}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_loan = Loan(user_id=user_id, amount=amount, interest_rate=interest_rate, duration_in_months=duration_in_months)
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({"message": "Loan created successfully", "loan": {"id": new_loan.id, "amount": new_loan.amount, "interest_rate": new_loan.interest_rate, "duration_in_months": new_loan.duration_in_months, "user_id": new_loan.user_id}}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the loan", "details": str(e)}), 500

@app.route('/users/<int:user_id>/loans', methods=['GET'])
def get_user_loans(user_id):
    """
    Endpoint to fetch all loans for a specific user.
    """
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        loans = Loan.query.filter_by(user_id=user_id).all()
        loans_list = [{"id": loan.id, "amount": loan.amount, "interest_rate": loan.interest_rate, "duration_in_months": loan.duration_in_months} for loan in loans]
        return jsonify({"user": {"id": user.id, "name": user.name, "email": user.email}, "loans": loans_list}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the loans", "details": str(e)}), 500

@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan_details(loan_id):
    """
    Endpoint to fetch details for a specific loan.
    """
    try:
        loan = Loan.query.get(loan_id)
        if not loan:
            return jsonify({"error": "Loan not found"}), 404

        return jsonify({"loan": {"id": loan.id, "amount": loan.amount, "interest_rate": loan.interest_rate, "duration_in_months": loan.duration_in_months, "user_id": loan.user_id}}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the loan details", "details": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True only in development
```

### Features:
- **Create User**: Add a new user with a name and email.
- **Create Loan**: Add a loan for a user with specific attributes (amount, interest rate, duration).
- **Get User Loans**: Retrieve all loans associated with a user.
- **Get Loan Details**: Retrieve detailed information about a specific loan.

### Instructions:
1. Install dependencies: `pip install flask flask-sqlalchemy`.
2. Run the application using `python app.py`.
3. Use tools like Postman or Curl to test the REST endpoints.
