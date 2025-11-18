"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: Write a script to integrate HatsFinance's bug bounty program into a Web3 application, ensuring that vulnerabilities can be reported securely.
Generated: DETERMINISTIC_d6c29e48aeca96a5
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bounty_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for vulnerability reports
class VulnerabilityReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reporter_email = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<VulnerabilityReport {self.id} - {self.severity}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_vulnerability():
    """
    Endpoint to submit a vulnerability report.

    Request body should contain:
    - reporter_email: str
    - description: str
    - severity: str (low, medium, high)

    Returns:
        JSON response indicating success or error.
    """

    try:
        # Parse JSON request body
        data = request.get_json()
        
        # Validate incoming data
        if not data or not all(key in data for key in ('reporter_email', 'description', 'severity')):
            return jsonify({'error': 'Invalid input. Please provide reporter_email, description, and severity.'}), 400

        # Create a new vulnerability report
        report = VulnerabilityReport(
            reporter_email=data['reporter_email'],
            description=data['description'],
            severity=data['severity']
        )
        
        # Add and commit the report to the database
        db.session.add(report)
        db.session.commit()
        
        return jsonify({'message': 'Vulnerability report submitted successfully!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error. Please try again later.'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all vulnerability reports.

    Returns:
        JSON response containing a list of all reports.
    """
    try:
        reports = VulnerabilityReport.query.all()
        report_list = [
            {
                'id': report.id,
                'reporter_email': report.reporter_email,
                'description': report.description,
                'severity': report.severity
            } for report in reports
        ]
        
        return jsonify(report_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=False)
```
