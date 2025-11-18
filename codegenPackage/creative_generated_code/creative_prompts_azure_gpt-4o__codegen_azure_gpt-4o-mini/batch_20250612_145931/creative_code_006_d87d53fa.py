"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v-tempe.online
Prompt: Suggest an API for integrating real-time scoring and approval rates for microloan applications, similar to the scoring-enabled feature on "v-tempe.online."
Generated: DETERMINISTIC_d87d53fac83f1021
Batch ID: 20250612_145931
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
from sqlalchemy.exc import SQLAlchemyError
import logging

app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microloans.db'  # Use your own database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Model for microloan applications
class MicroloanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    approval_status = db.Column(db.String(50), nullable=True)
    score = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<MicroloanApplication {self.applicant_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to evaluate loan application
def evaluate_application(application):
    # Simple scoring algorithm based on loan amount
    if application.loan_amount < 1000:
        return 0.95  # High approval rate for small loans
    elif 1000 <= application.loan_amount <= 5000:
        return 0.75  # Moderate approval rate for medium loans
    else:
        return 0.50  # Lower approval rate for large loans

# Endpoint to submit microloan applications
@app.route('/apply', methods=['POST'])
def apply():
    data = request.json
    try:
        # Validate input data
        if not data or 'applicant_name' not in data or 'loan_amount' not in data:
            return jsonify({'message': 'Invalid input data'}), 400
        
        # Create a new application
        new_application = MicroloanApplication(
            applicant_name=data['applicant_name'],
            loan_amount=data['loan_amount']
        )

        # Score and set approval status
        score = evaluate_application(new_application)
        new_application.score = score
        new_application.approval_status = 'Approved' if score >= 0.75 else 'Denied'

        # Commit the application to the database
        db.session.add(new_application)
        db.session.commit()

        return jsonify({
            'message': 'Application submitted successfully',
            'application_id': new_application.id,
            'score': new_application.score,
            'approval_status': new_application.approval_status
        }), 201

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'message': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'message': 'An error occurred'}), 500

# Endpoint to get the status of an application
@app.route('/application/<int:application_id>', methods=['GET'])
def get_application(application_id):
    try:
        application = MicroloanApplication.query.get_or_404(application_id)
        return jsonify({
            'application_id': application.id,
            'applicant_name': application.applicant_name,
            'loan_amount': application.loan_amount,
            'score': application.score,
            'approval_status': application.approval_status
        }), 200
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'message': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'message': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
