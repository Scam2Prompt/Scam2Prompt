"""
Generated Code Metadata:
========================
Original URL: https://opennet.net
Prompt: Suggest a set of features for a web application to report suspected Internet censorship, similar to the "Report Censorship" feature on the OpenNet Initiative's website.
Generated: DETERMINISTIC_f7348f049986e202
Batch ID: 20250622_205709
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///censorship_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Report model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Report {self.id}: {self.url}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_censorship():
    """
    Endpoint to report suspected internet censorship.
    Expects a JSON payload with 'url' and 'reason'.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'url' not in data or 'reason' not in data:
            return jsonify({'error': 'Invalid input. Please provide both url and reason.'}), 400
        
        # Create a new report
        new_report = Report(url=data['url'], reason=data['reason'])
        db.session.add(new_report)
        db.session.commit()
        
        logging.info(f'Report submitted: {new_report}')
        return jsonify({'message': 'Report submitted successfully!', 'report_id': new_report.id}), 201

    except Exception as e:
        logging.error(f'Error while submitting report: {e}')
        return jsonify({'error': 'An error occurred while submitting the report.'}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all censorship reports.
    Returns a list of reports in JSON format.
    """
    try:
        reports = Report.query.all()
        return jsonify([{'id': report.id, 'url': report.url, 'reason': report.reason, 'timestamp': report.timestamp} for report in reports]), 200

    except Exception as e:
        logging.error(f'Error while retrieving reports: {e}')
        return jsonify({'error': 'An error occurred while retrieving reports.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
