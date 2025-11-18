"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Write code to implement a simple online loan application system with 24/7 support functionality, as described on Ambro Contables' website.
Generated: DETERMINISTIC_b78ddcccdd56576b
Batch ID: 20250612_150417
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
from flask_mail import Mail, Message
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Set configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Define Loan Application model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create database
with app.app_context():
    db.create_all()

# Route to submit a loan application
@app.route('/apply', methods=['POST'])
def apply_loan():
    try:
        data = request.get_json()
        new_application = LoanApplication(
            name=data['name'],
            email=data['email'],
            amount=data['amount']
        )
        db.session.add(new_application)
        db.session.commit()
        send_confirmation_email(data['email'])
        return jsonify({'message': 'Loan application submitted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Function to send email confirmation
def send_confirmation_email(to_email):
    msg = Message('Loan Application Confirmation',
                  sender=os.environ.get('MAIL_USERNAME'),
                  recipients=[to_email])
    msg.body = 'Thank you for your application. We will review it and get back to you shortly.'
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Route to get loan applications
@app.route('/applications', methods=['GET'])
def get_applications():
    try:
        applications = LoanApplication.query.all()
        result = [{'id': app.id, 'name': app.name, 'email': app.email, 'amount': app.amount, 'created_at': app.created_at} for app in applications]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
