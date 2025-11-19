"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financial-justice.com
Prompt: How can I implement an API to report cryptocurrency fraud incidents, specifically targeting scams like Ponzi schemes and rug pulls?
Generated: DETERMINISTIC_736ac0367a36001d
Batch ID: 20250612_160328
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fraud_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the FraudReport model
class FraudReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FraudReport {self.id}, Type: {self.report_type}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_fraud():
    """
    Endpoint to report cryptocurrency fraud incidents.
    Expects a JSON body containing 'report_type' and 'description'.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate incoming data
        if 'report_type' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid input, must include report_type and description'}), 400

        # Create a new fraud report
        new_report = FraudReport(
            report_type=data['report_type'],
            description=data['description']
        )
        
        # Add the report to the session and commit
        db.session.add(new_report)
        db.session.commit()

        return jsonify({'message': 'Fraud report submitted successfully', 'report_id': new_report.id}), 201
    
    except Exception as e:
        logging.error(f"Error processing report: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all fraud reports.
    Returns a JSON array of fraud reports.
    """
    try:
        reports = FraudReport.query.all()
        reports_list = [{
            'id': report.id,
            'report_type': report.report_type,
            'description': report.description,
            'reported_at': report.reported_at.isoformat()
        } for report in reports]

        return jsonify(reports_list), 200

    except Exception as e:
        logging.error(f"Error retrieving reports: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
