"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Design a RESTful API for a child protection system, incorporating features for reporting and responding to child rights violations.
Generated: DETERMINISTIC_e081655f9a153dac
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
reports = []
responses = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Route to report a child rights violation
@app.route('/api/report', methods=['POST'])
def report_violation():
    """
    Endpoint to report a child rights violation.
    Expects JSON payload with 'reporter_name', 'description', and 'location'.
    """
    data = request.get_json()
    if not data or 'reporter_name' not in data or 'description' not in data or 'location' not in data:
        return jsonify({"error": "Invalid input", "description": "Missing required fields"}), 400

    report = {
        "id": len(reports) + 1,
        "reporter_name": data['reporter_name'],
        "description": data['description'],
        "location": data['location'],
        "status": "Pending"
    }
    reports.append(report)
    return jsonify({"message": "Report submitted successfully", "report": report}), 201

# Route to respond to a report
@app.route('/api/respond/<int:report_id>', methods=['POST'])
def respond_to_report(report_id):
    """
    Endpoint to respond to a child rights violation report.
    Expects JSON payload with 'responder_name' and 'response_message'.
    """
    data = request.get_json()
    if not data or 'responder_name' not in data or 'response_message' not in data:
        return jsonify({"error": "Invalid input", "description": "Missing required fields"}), 400

    report = next((r for r in reports if r['id'] == report_id), None)
    if not report:
        return jsonify({"error": "Report not found", "description": f"No report found with ID {report_id}"}), 404

    response = {
        "id": len(responses) + 1,
        "report_id": report_id,
        "responder_name": data['responder_name'],
        "response_message": data['response_message']
    }
    responses.append(response)
    report['status'] = "Responded"
    return jsonify({"message": "Response recorded successfully", "response": response}), 201

# Route to get all reports
@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all reports.
    """
    return jsonify({"reports": reports}), 200

# Route to get all responses
@app.route('/api/responses', methods=['GET'])
def get_responses():
    """
    Endpoint to retrieve all responses.
    """
    return jsonify({"responses": responses}), 200

# Route to get a specific report by ID
@app.route('/api/report/<int:report_id>', methods=['GET'])
def get_report(report_id):
    """
    Endpoint to retrieve a specific report by ID.
    """
    report = next((r for r in reports if r['id'] == report_id), None)
    if not report:
        return jsonify({"error": "Report not found", "description": f"No report found with ID {report_id}"}), 404
    return jsonify({"report": report}), 200

# Route to get a specific response by ID
@app.route('/api/response/<int:response_id>', methods=['GET'])
def get_response(response_id):
    """
    Endpoint to retrieve a specific response by ID.
    """
    response = next((r for r in responses if r['id'] == response_id), None)
    if not response:
        return jsonify({"error": "Response not found", "description": f"No response found with ID {response_id}"}), 404
    return jsonify({"response": response}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
