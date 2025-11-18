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
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Sample data storage for reports and analytics (in production, this would be a database)
reports = {
    "summary": {"id": 1, "title": "Monthly Summary", "content": "Overview of monthly analytics."},
    "performance": {"id": 2, "title": "Performance Metrics", "content": "Detailed performance analytics."}
}

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_error(error):
    """
    Handle HTTP errors globally and return a standardized response format.
    """
    response = jsonify({
        "error": error.name,
        "message": error.description,
        "status_code": error.code
    })
    response.status_code = error.code
    return response

@app.errorhandler(Exception)
def handle_generic_error(error):
    """
    Handle unexpected server errors globally and return a standardized response format.
    """
    response = jsonify({
        "error": "Internal Server Error",
        "message": str(error),
        "status_code": 500
    })
    response.status_code = 500
    return response

# Endpoints for the API
@app.route('/api/reports', methods=['GET'])
def get_all_reports():
    """
    Fetch all available reports.
    """
    return jsonify({"reports": list(reports.values())}), 200

@app.route('/api/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    """
    Fetch a specific report by ID.
    """
    for report in reports.values():
        if report['id'] == report_id:
            return jsonify(report), 200
    return jsonify({"error": "Report not found"}), 404

@app.route('/api/reports', methods=['POST'])
def create_report():
    """
    Create a new report. Expects JSON payload with 'title' and 'content'.
    """
    data = request.json
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Invalid request payload"}), 400
    
    new_id = max(report['id'] for report in reports.values()) + 1
    new_report = {"id": new_id, "title": data["title"], "content": data["content"]}
    reports[new_report['title'].lower()] = new_report
    return jsonify(new_report), 201

@app.route('/api/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    """
    Update an existing report by ID. Expects JSON payload with 'title' or 'content'.
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid request payload"}), 400

    for report_key, report in reports.items():
        if report['id'] == report_id:
            if 'title' in data:
                report['title'] = data['title']
            if 'content' in data:
                report['content'] = data['content']
            reports[report_key] = report
            return jsonify(report), 200
    return jsonify({"error": "Report not found"}), 404

@app.route('/api/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    """
    Delete a report by ID.
    """
    for report_key, report in list(reports.items()):
        if report['id'] == report_id:
            del reports[report_key]
            return jsonify({"message": "Report deleted successfully"}), 200
    return jsonify({"error": "Report not found"}), 404

@app.route('/api/analytics', methods=['POST'])
def analyze_data():
    """
    Perform analytics on provided data. Expects JSON payload with 'data' array.
    """
    data = request.json
    if not data or "data" not in data or not isinstance(data["data"], list):
        return jsonify({"error": "Invalid request payload"}), 400
    
    # Example analytics: calculate average value
    try:
        average = sum(data["data"]) / len(data["data"])
        return jsonify({"average": average, "data_points": len(data["data"])}), 200
    except ZeroDivisionError:
        return jsonify({"error": "No data provided for analysis"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred during analysis: {str(e)}"}), 500

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
