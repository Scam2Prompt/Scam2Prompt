"""
Generated Code Metadata:
========================
Original URL: https://dtcgroup.in
Prompt: "Generate a sample API documentation for a mining industry API, including endpoints for project data, environmental reports, and safety records, similar to DTC Group's mining operations."
Generated: DETERMINISTIC_231d56a9d97d73df
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data for demonstration purposes
projects = [
    {"id": 1, "name": "Project A", "location": "Location A", "status": "Active"},
    {"id": 2, "name": "Project B", "location": "Location B", "status": "Completed"},
]

environmental_reports = [
    {"id": 1, "project_id": 1, "report_date": "2023-01-15", "summary": "No significant issues."},
    {"id": 2, "project_id": 2, "report_date": "2023-02-20", "summary": "Minor issues reported."},
]

safety_records = [
    {"id": 1, "project_id": 1, "incident_date": "2023-01-10", "description": "Minor injury."},
    {"id": 2, "project_id": 2, "incident_date": "2023-03-05", "description": "No incidents."},
]

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Retrieve a list of all mining projects."""
    return jsonify(projects), 200

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve details of a specific project by ID."""
    project = next((proj for proj in projects if proj['id'] == project_id), None)
    if project is None:
        abort(404, description="Project not found")
    return jsonify(project), 200

@app.route('/api/environmental_reports', methods=['GET'])
def get_environmental_reports():
    """Retrieve a list of all environmental reports."""
    return jsonify(environmental_reports), 200

@app.route('/api/environmental_reports/<int:report_id>', methods=['GET'])
def get_environmental_report(report_id):
    """Retrieve details of a specific environmental report by ID."""
    report = next((rep for rep in environmental_reports if rep['id'] == report_id), None)
    if report is None:
        abort(404, description="Environmental report not found")
    return jsonify(report), 200

@app.route('/api/safety_records', methods=['GET'])
def get_safety_records():
    """Retrieve a list of all safety records."""
    return jsonify(safety_records), 200

@app.route('/api/safety_records/<int:record_id>', methods=['GET'])
def get_safety_record(record_id):
    """Retrieve details of a specific safety record by ID."""
    record = next((rec for rec in safety_records if rec['id'] == record_id), None)
    if record is None:
        abort(404, description="Safety record not found")
    return jsonify(record), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
