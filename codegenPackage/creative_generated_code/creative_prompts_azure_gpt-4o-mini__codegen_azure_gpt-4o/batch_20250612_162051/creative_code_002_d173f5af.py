"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Create a REST API that allows users to report human rights abuses, incorporating features discussed in Jusoor International's programs and goals.
Generated: DETERMINISTIC_d173f5aff61605c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store reports
reports_db = []

# Error messages dictionary for consistent response structure
ERROR_MESSAGES = {
    "MISSING_FIELDS": "Required fields are missing in the request.",
    "INVALID_DATA": "Invalid data provided.",
    "SERVER_ERROR": "An unexpected error occurred. Please try again later."
}

# Success messages dictionary for consistent response structure
SUCCESS_MESSAGES = {
    "REPORT_CREATED": "Report successfully created.",
    "REPORTS_RETRIEVED": "Reports successfully retrieved."
}

@app.route('/api/reports', methods=['POST'])
def create_report():
    """
    Endpoint to report human rights abuses.
    Expects JSON payload with the following fields:
    - name (str): Name of the reporter
    - contact_info (str): Contact information of the reporter
    - description (str): Details of the abuse
    - location (str): Location of the abuse
    - date (str): Date of the abuse (YYYY-MM-DD)
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'contact_info', 'description', 'location', 'date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": ERROR_MESSAGES["MISSING_FIELDS"]}), 400

        # Validate date format
        try:
            abuse_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": ERROR_MESSAGES["INVALID_DATA"], "details": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Generate report ID
        report_id = str(uuid.uuid4())

        # Create report object
        report = {
            "id": report_id,
            "name": data['name'],
            "contact_info": data['contact_info'],
            "description": data['description'],
            "location": data['location'],
            "date": str(abuse_date),
            "created_at": datetime.utcnow().isoformat()
        }

        # Save report to in-memory database
        reports_db.append(report)

        return jsonify({"message": SUCCESS_MESSAGES["REPORT_CREATED"], "report": report}), 201

    except Exception as e:
        # Log the error (placeholder for real logging)
        print(f"Error creating report: {e}")
        return jsonify({"error": ERROR_MESSAGES["SERVER_ERROR"]}), 500


@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all human rights abuse reports.
    Returns a list of all reports in the database.
    """
    try:
        return jsonify({"message": SUCCESS_MESSAGES["REPORTS_RETRIEVED"], "reports": reports_db}), 200
    except Exception as e:
        # Log the error (placeholder for real logging)
        print(f"Error retrieving reports: {e}")
        return jsonify({"error": ERROR_MESSAGES["SERVER_ERROR"]}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
