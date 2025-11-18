"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Develop an API endpoint to retrieve due diligence reports for companies in the oil and gas industry using CRUDO Protocol's marketplace.
Generated: DETERMINISTIC_624d12237d250d55
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///due_diligence_reports.db'  # Use your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Due Diligence Report
class DueDiligenceReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    report_data = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'company_name': self.company_name,
            'report_data': self.report_data
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    Retrieve due diligence reports for companies in the oil and gas industry.

    Returns:
        JSON response containing a list of due diligence reports or an error message.
    """
    try:
        # Capture query parameters for filtering if necessary
        company_name = request.args.get('company_name')

        # Query the database
        if company_name:
            reports = DueDiligenceReport.query.filter_by(company_name=company_name).all()
        else:
            reports = DueDiligenceReport.query.all()

        # Convert reports to a list of dictionaries
        reports_list = [report.to_dict() for report in reports]

        # Return the reports as a JSON response
        return jsonify(reports_list), 200

    except SQLAlchemyError as e:
        # Log the error and return a message
        logging.error(f"Database error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving reports."}), 500

    except Exception as e:
        # Log unexpected errors and return a message
        logging.error(f"Unexpected error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
