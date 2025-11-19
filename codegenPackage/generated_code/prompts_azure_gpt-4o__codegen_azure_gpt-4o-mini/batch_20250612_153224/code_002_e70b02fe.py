"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Generate a sample API design for a reporting and analytics system tailored to enterprise needs, inspired by MetaCode's focus on reportability and decision-making improvements.
Generated: DETERMINISTIC_e70b02fec6a4d533
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for reports
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Schema for report validation
class ReportSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new report
@app.route('/api/reports', methods=['POST'])
def create_report():
    try:
        # Validate and deserialize input data
        report_schema = ReportSchema()
        report_data = report_schema.load(request.json)

        # Create a new report instance
        new_report = Report(title=report_data['title'], content=report_data['content'])
        db.session.add(new_report)
        db.session.commit()

        return jsonify({"message": "Report created successfully", "id": new_report.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating report: {e}")
        return jsonify({"error": "An error occurred while creating the report."}), 500

# API endpoint to retrieve all reports
@app.route('/api/reports', methods=['GET'])
def get_reports():
    try:
        reports = Report.query.all()
        report_schema = ReportSchema(many=True)
        return jsonify(report_schema.dump(reports)), 200
    except Exception as e:
        logging.error(f"Error retrieving reports: {e}")
        return jsonify({"error": "An error occurred while retrieving reports."}), 500

# API endpoint to retrieve a specific report by ID
@app.route('/api/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    try:
        report = Report.query.get_or_404(report_id)
        report_schema = ReportSchema()
        return jsonify(report_schema.dump(report)), 200
    except Exception as e:
        logging.error(f"Error retrieving report {report_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the report."}), 500

# API endpoint to update a report
@app.route('/api/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    try:
        report = Report.query.get_or_404(report_id)
        report_schema = ReportSchema()
        report_data = report_schema.load(request.json)

        # Update report fields
        report.title = report_data['title']
        report.content = report_data['content']
        db.session.commit()

        return jsonify({"message": "Report updated successfully"}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating report {report_id}: {e}")
        return jsonify({"error": "An error occurred while updating the report."}), 500

# API endpoint to delete a report
@app.route('/api/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    try:
        report = Report.query.get_or_404(report_id)
        db.session.delete(report)
        db.session.commit()
        return jsonify({"message": "Report deleted successfully"}), 204
    except Exception as e:
        logging.error(f"Error deleting report {report_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the report."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
