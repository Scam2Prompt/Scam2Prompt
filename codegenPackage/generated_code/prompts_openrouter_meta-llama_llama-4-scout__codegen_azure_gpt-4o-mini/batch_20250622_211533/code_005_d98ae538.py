"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Create a mobile app for reporting pollution and waste management issues in urban areas, integrating with local government services for efficient response.
Generated: DETERMINISTIC_d98ae538160234da
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pollution_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the PollutionReport model
class PollutionReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    issue_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PollutionReport {self.id} - {self.issue_type} at {self.location}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to report a pollution issue
@app.route('/report', methods=['POST'])
def report_issue():
    try:
        data = request.get_json()
        if not data or 'location' not in data or 'issue_type' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        new_report = PollutionReport(
            location=data['location'],
            issue_type=data['issue_type'],
            description=data.get('description')
        )
        db.session.add(new_report)
        db.session.commit()

        logging.info(f'Report created: {new_report}')
        return jsonify({'message': 'Report submitted successfully', 'report_id': new_report.id}), 201

    except Exception as e:
        logging.error(f'Error reporting issue: {e}')
        return jsonify({'error': 'An error occurred while submitting the report'}), 500

# Route to get all reports
@app.route('/reports', methods=['GET'])
def get_reports():
    try:
        reports = PollutionReport.query.all()
        return jsonify([{
            'id': report.id,
            'location': report.location,
            'issue_type': report.issue_type,
            'description': report.description,
            'reported_at': report.reported_at.isoformat()
        } for report in reports]), 200

    except Exception as e:
        logging.error(f'Error fetching reports: {e}')
        return jsonify({'error': 'An error occurred while fetching reports'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

### Notes:
- This code is a simple Flask application that allows users to report pollution issues and retrieve existing reports.
- It uses SQLite for the database, which is suitable for development and small-scale applications.
- Proper error handling is implemented for both reporting and fetching reports.
- Logging is included to track application behavior and errors.
