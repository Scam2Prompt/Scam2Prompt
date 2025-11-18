"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transactionfinder.in
Prompt: Suggest libraries or frameworks to build a reporting system for scams, incorporating legal resources and support as described on Transaction Finder.
Generated: DETERMINISTIC_e893e956a9471221
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scam_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ScamReport model
class ScamReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Create a schema for the ScamReport
class ScamReportSchema(Schema):
    user_id = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
scam_report_schema = ScamReportSchema()
scam_reports_schema = ScamReportSchema(many=True)

# Endpoint to create a new scam report
@app.route('/report', methods=['POST'])
def create_report():
    """Create a new scam report."""
    try:
        # Validate and deserialize input data
        data = scam_report_schema.load(request.json)
        
        # Create a new ScamReport instance
        new_report = ScamReport(user_id=data['user_id'], description=data['description'])
        
        # Add the report to the session and commit to the database
        db.session.add(new_report)
        db.session.commit()
        
        return scam_report_schema.jsonify(new_report), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all scam reports
@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieve all scam reports."""
    try:
        reports = ScamReport.query.all()  # Query all reports
        return scam_reports_schema.jsonify(reports), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
