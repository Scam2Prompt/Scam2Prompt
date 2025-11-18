"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for a financial disclosure system that allows non-profits to publish annual financial reports, inspired by the "التقارير المالية الإفصاح 2023" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_c3a549bfe5ed6e07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (Change to your preferred database in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FinancialReport model
class FinancialReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_income = db.Column(db.Float, nullable=False)
    total_expenses = db.Column(db.Float, nullable=False)
    net_assets = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<FinancialReport {self.organization_name} - {self.year}>'

# Define schema for validating the financial report input
class FinancialReportSchema(Schema):
    organization_name = fields.Str(required=True)
    year = fields.Int(required=True)
    total_income = fields.Float(required=True)
    total_expenses = fields.Float(required=True)
    net_assets = fields.Float(required=True)

# Initialize the schema
report_schema = FinancialReportSchema()

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/reports', methods=['POST'])
def create_report():
    """Create a new financial report."""
    try:
        # Validate and deserialize input
        report_data = request.json
        validated_data = report_schema.load(report_data)

        # Create a new financial report
        new_report = FinancialReport(**validated_data)
        db.session.add(new_report)
        db.session.commit()

        return jsonify({'message': 'Financial report created successfully!', 'report_id': new_report.id}), 201
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """Retrieve all financial reports."""
    reports = FinancialReport.query.all()
    return jsonify({'reports': [report_schema.dump(report) for report in reports]}), 200

@app.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    """Retrieve a specific financial report by ID."""
    report = FinancialReport.query.get(report_id)
    if report is None:
        return jsonify({'error': 'Report not found'}), 404
    return jsonify(report_schema.dump(report)), 200

@app.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    """Update a specific financial report."""
    report = FinancialReport.query.get(report_id)
    if report is None:
        return jsonify({'error': 'Report not found'}), 404

    try:
        # Validate and deserialize input
        report_data = request.json
        validated_data = report_schema.load(report_data)

        # Update the financial report
        for key, value in validated_data.items():
            setattr(report, key, value)
        
        db.session.commit()
        return jsonify({'message': 'Financial report updated successfully!'}), 200
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    """Delete a specific financial report."""
    report = FinancialReport.query.get(report_id)
    if report is None:
        return jsonify({'error': 'Report not found'}), 404

    try:
        db.session.delete(report)
        db.session.commit()
        return jsonify({'message': 'Financial report deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
