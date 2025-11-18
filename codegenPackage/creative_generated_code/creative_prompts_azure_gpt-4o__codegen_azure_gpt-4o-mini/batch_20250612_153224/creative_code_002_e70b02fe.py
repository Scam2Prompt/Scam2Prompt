"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Generate a sample API design for a reporting and analytics system tailored to enterprise needs, inspired by MetaCode's focus on reportability and decision-making improvements.
Generated: DETERMINISTIC_e70b02fec6a4d533
Batch ID: 20250612_153224
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Report Model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Report {self.title}>"

# Report Schema
class ReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Report

# Initialize database
with app.app_context():
    db.create_all()

# Endpoint to create a new report
@app.route('/reports', methods=['POST'])
def create_report():
    """Create a new report."""
    try:
        title = request.json.get('title')
        content = request.json.get('content')

        # Validate input
        if not title or not content:
            return jsonify({"error": "Title and content are required"}), 400

        new_report = Report(title=title, content=content)
        db.session.add(new_report)
        db.session.commit()

        return ReportSchema().jsonify(new_report), 201

    except Exception as e:
        logging.error(f"Error creating report: {e}")
        return jsonify({"error": "An error occurred while creating the report"}), 500

# Endpoint to get all reports
@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieve all reports."""
    try:
        reports = Report.query.all()
        return ReportSchema(many=True).jsonify(reports), 200

    except Exception as e:
        logging.error(f"Error retrieving reports: {e}")
        return jsonify({"error": "An error occurred while retrieving reports"}), 500

# Endpoint to get a report by ID
@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    """Retrieve a report by its ID."""
    try:
        report = Report.query.get_or_404(report_id)
        return ReportSchema().jsonify(report), 200

    except Exception as e:
        logging.error(f"Error retrieving report {report_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the report"}), 500

# Endpoint to update a report
@app.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    """Update a report by its ID."""
    try:
        report = Report.query.get_or_404(report_id)
        title = request.json.get('title', report.title)
        content = request.json.get('content', report.content)

        report.title = title
        report.content = content
        db.session.commit()

        return ReportSchema().jsonify(report), 200

    except Exception as e:
        logging.error(f"Error updating report {report_id}: {e}")
        return jsonify({"error": "An error occurred while updating the report"}), 500

# Endpoint to delete a report
@app.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    """Delete a report by its ID."""
    try:
        report = Report.query.get_or_404(report_id)
        db.session.delete(report)
        db.session.commit()

        return jsonify({"message": "Report deleted successfully"}), 204

    except Exception as e:
        logging.error(f"Error deleting report {report_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the report"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
