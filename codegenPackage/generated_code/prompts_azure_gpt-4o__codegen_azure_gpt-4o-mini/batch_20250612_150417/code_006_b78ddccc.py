"""
Generated Code Metadata:
========================
Original URL: https://claim-idegen.com
Prompt: Write code to implement a simple online loan application system with 24/7 support functionality, as described on Ambro Contables' website.
Generated: DETERMINISTIC_b78ddcccdd56576b
Batch ID: 20250612_150417
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Loan Application model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<LoanApplication {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit a loan application
@app.route('/apply', methods=['POST'])
def apply_loan():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        amount = data.get('amount')

        # Validate input data
        if not name or not email or not amount:
            return jsonify({'error': 'Name, email, and amount are required.'}), 400

        # Create a new loan application
        new_application = LoanApplication(name=name, email=email, amount=amount)
        db.session.add(new_application)
        db.session.commit()

        return jsonify({'message': 'Loan application submitted successfully!', 'application_id': new_application.id}), 201

    except Exception as e:
        logging.error(f'Error submitting loan application: {e}')
        return jsonify({'error': 'An error occurred while submitting your application.'}), 500

# Route to check the status of a loan application
@app.route('/status/<int:application_id>', methods=['GET'])
def check_status(application_id):
    try:
        application = LoanApplication.query.get(application_id)
        if not application:
            return jsonify({'error': 'Application not found.'}), 404

        return jsonify({
            'application_id': application.id,
            'name': application.name,
            'email': application.email,
            'amount': application.amount,
            'status': application.status,
            'created_at': application.created_at
        }), 200

    except Exception as e:
        logging.error(f'Error checking application status: {e}')
        return jsonify({'error': 'An error occurred while checking the application status.'}), 500

# Route for 24/7 support
@app.route('/support', methods=['POST'])
def support():
    try:
        data = request.get_json()
        message = data.get('message')
        email = data.get('email')

        # Validate input data
        if not message or not email:
            return jsonify({'error': 'Message and email are required.'}), 400

        # Here you would typically send the support message to a support system
        logging.info(f'Support request from {email}: {message}')

        return jsonify({'message': 'Support request submitted successfully!'}), 201

    except Exception as e:
        logging.error(f'Error submitting support request: {e}')
        return jsonify({'error': 'An error occurred while submitting your support request.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
