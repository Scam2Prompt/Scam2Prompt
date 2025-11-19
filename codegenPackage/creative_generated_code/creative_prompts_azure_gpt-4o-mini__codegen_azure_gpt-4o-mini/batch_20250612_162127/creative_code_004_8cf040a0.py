"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paybackclaimltd.com
Prompt: Generate a sample code for a web application that helps users report financial fraud and request chargeback services, inspired by Payback Claim Ltd.'s offerings.
Generated: DETERMINISTIC_8cf040a0a8292c22
Batch ID: 20250612_162127
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fraud_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the FraudReport model
class FraudReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    transaction_id = db.Column(db.String(100), nullable=False)
    report_details = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<FraudReport {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_fraud():
    """
    Endpoint to report financial fraud.
    Expects JSON data with user_id, transaction_id, and report_details.
    Returns a success message or error details.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'user_id' not in data or 'transaction_id' not in data or 'report_details' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new fraud report
    new_report = FraudReport(
        user_id=data['user_id'],
        transaction_id=data['transaction_id'],
        report_details=data['report_details']
    )

    try:
        db.session.add(new_report)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to save report, please try again later.'}), 500

    logging.info(f'New fraud report created: {new_report.id}')
    return jsonify({'message': 'Fraud report submitted successfully!', 'report_id': new_report.id}), 201

@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    """
    Endpoint to retrieve a specific fraud report by its ID.
    Returns the report details or an error if not found.
    """
    report = FraudReport.query.get(report_id)

    if not report:
        return jsonify({'error': 'Report not found'}), 404

    return jsonify({
        'report_id': report.id,
        'user_id': report.user_id,
        'transaction_id': report.transaction_id,
        'report_details': report.report_details,
        'status': report.status
    }), 200

@app.route('/reports', methods=['GET'])
def get_all_reports():
    """
    Endpoint to retrieve all fraud reports.
    Returns a list of all reports.
    """
    reports = FraudReport.query.all()
    report_list = [{
        'report_id': report.id,
        'user_id': report.user_id,
        'transaction_id': report.transaction_id,
        'report_details': report.report_details,
        'status': report.status
    } for report in reports]

    return jsonify(report_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```
