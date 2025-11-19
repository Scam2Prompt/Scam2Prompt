"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Create a REST API that allows users to report human rights abuses, incorporating features discussed in Jusoor International's programs and goals.
Generated: DETERMINISTIC_d173f5aff61605c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store reports (for demonstration purposes)
reports_db = []

# Error messages
ERROR_MESSAGES = {
    "missing_fields": "Required fields are missing.",
    "invalid_data": "Invalid data provided.",
}

# Helper function to validate report data
def validate_report_data(data):
    required_fields = ["name", "email", "location", "description"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True

@app.route('/api/reports', methods=['POST'])
def report_abuse():
    """
    Endpoint to report human rights abuses.
    Accepts JSON payload with the following fields:
    - name: Name of the reporter
    - email: Email of the reporter
    - location: Location of the abuse
    - description: Description of the abuse
    - optional: additional_info (any other relevant information)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": ERROR_MESSAGES["invalid_data"]}), 400

        # Validate required fields
        if not validate_report_data(data):
            return jsonify({"error": ERROR_MESSAGES["missing_fields"]}), 400

        # Create a new report entry
        report = {
            "id": str(uuid.uuid4()),  # Generate unique ID for the report
            "name": data["name"],
            "email": data["email"],
            "location": data["location"],
            "description": data["description"],
            "additional_info": data.get("additional_info", ""),  # Optional field
            "timestamp": datetime.utcnow().isoformat()  # Record the time of submission
        }

        # Save the report to the in-memory database
        reports_db.append(report)

        # Return success response
        return jsonify({"message": "Report submitted successfully.", "report_id": report["id"]}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all abuse reports.
    Returns a list of all reports in the database.
    """
    try:
        return jsonify({"reports": reports_db}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/reports/<report_id>', methods=['GET'])
def get_report_by_id(report_id):
    """
    Endpoint to retrieve a specific abuse report by its ID.
    """
    try:
        # Find the report by ID
        report = next((r for r in reports_db if r["id"] == report_id), None)
        if not report:
            return jsonify({"error": "Report not found."}), 404

        return jsonify({"report": report}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
