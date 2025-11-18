"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Write code to implement Paya's digital boarding process for SaaS platforms to acquire new customers efficiently.
Generated: DETERMINISTIC_cee44504ea928311
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Paya Digital Boarding Process for SaaS Platforms
This script implements an efficient digital onboarding process to acquire new customers for a SaaS platform.
The process collects customer information, validates the input, and stores it securely.

Language: Python
Requirements:
- Flask for web framework
- SQLAlchemy for database ORM
- EmailValidator for email validation
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from email_validator import validate_email, EmailNotValidError
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Flask application
app = Flask(__name__)

# Configure database (using SQLite for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Customer {self.name}, {self.email}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Helper function to validate email
def validate_customer_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        logging.error(f"Invalid email: {email}. Details: {str(e)}")
        return False

# Endpoint to onboard a new customer
@app.route('/onboard', methods=['POST'])
def onboard_customer():
    """
    Onboards a new customer by collecting their information.
    Required data: name, email, company_name (sent as JSON payload in POST request)
    """
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        email = data.get('email')
        company_name = data.get('company_name')

        # Validate request data
        if not name or not email or not company_name:
            return jsonify({"error": "Missing required fields (name, email, company_name)"}), 400

        if not validate_customer_email(email):
            return jsonify({"error": "Invalid email address"}), 400

        # Check if email is already registered
        if Customer.query.filter_by(email=email).first():
            return jsonify({"error": "Email is already registered"}), 409

        # Create new customer record
        new_customer = Customer(name=name, email=email, company_name=company_name)
        db.session.add(new_customer)
        db.session.commit()

        logging.info(f"New customer onboarded: {new_customer}")
        return jsonify({"message": "Customer onboarded successfully!", "customer_id": new_customer.id}), 201

    except Exception as e:
        logging.error(f"Error occurred during onboarding: {str(e)}")
        return jsonify({"error": "An internal error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
