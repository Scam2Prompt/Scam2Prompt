"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Create a REST API that allows users to report human rights abuses, incorporating features discussed in Jusoor International's programs and goals.
Generated: DETERMINISTIC_d173f5aff61605c1
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/reports`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/reports/1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Human Rights Abuse Reporting API**
=====================================

**dependencies:**
* `flask` for the API framework
* `flask_sqlalchemy` for database interactions
* `marshmallow` for serialization and deserialization

**Code:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///hr_abuse.db")
db = SQLAlchemy(app)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    abuse_description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)

class ReportSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    abuse_description = fields.Str(required=True, validate=validate.Length(min=1))
    location = fields.Str(required=True, validate=validate.Length(min=1, max=100))

@app.route("/reports", methods=["POST"])
def create_report():
    try:
        schema = ReportSchema()
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    report = Report(**data)
    db.session.add(report)
    db.session.commit()
    return jsonify({"message": "Report created successfully"}), 201

@app.route("/reports", methods=["GET"])
def get_reports():
    reports = Report.query.all()
    schema = ReportSchema(many=True)
    return jsonify(schema.dump(reports))

@app.route("/reports/<int:report_id>", methods=["GET"])
def get_report(report_id):
    report = Report.query.get(report_id)
    if report is None:
        return jsonify({"error": "Report not found"}), 404
    schema = ReportSchema()
    return jsonify(schema.dump(report))

@app.route("/reports/<int:report_id>", methods=["PUT"])
def update_report(report_id):
    report = Report.query.get(report_id)
    if report is None:
        return jsonify({"error": "Report not found"}), 404

    try:
        schema = ReportSchema()
        data = schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    for key, value in data.items():
        setattr(report, key, value)
    db.session.commit()
    return jsonify({"message": "Report updated successfully"})

@app.route("/reports/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):
    report = Report.query.get(report_id)
    if report is None:
        return jsonify({"error": "Report not found"}), 404
    db.session.delete(report)
    db.session.commit()
    return jsonify({"message": "Report deleted successfully"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Example Usage:**

* Create a new report: `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "abuse_description": "Abuse description", "location": "Location"}' http://localhost:5000/reports`
* Get all reports: `curl http://localhost:5000/reports`
* Get a report by ID: `curl http://localhost:5000/reports/1`
* Update a report: `curl -X PUT -H "Content-Type: application/json" -d '{"abuse_description": "Updated abuse description"}' http://localhost:5000/reports/1`
* Delete a report: `curl -X DELETE http://localhost:5000/reports/1`
