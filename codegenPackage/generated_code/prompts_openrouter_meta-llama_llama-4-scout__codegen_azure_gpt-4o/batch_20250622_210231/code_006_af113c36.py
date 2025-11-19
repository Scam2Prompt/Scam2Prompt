"""
Generated Code Metadata:
========================
Original URL: https://claim-stu.pages.dev
Prompt: How would you implement a bug bounty program similar to Sturdy's, which is hosted on Immunefi, using a custom backend?
Generated: DETERMINISTIC_af113c368540e717
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database to store bug reports (for demonstration purposes)
# In production, use a proper database like PostgreSQL, MySQL, or MongoDB
bug_reports = []

# Define a custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Define a custom error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unexpected error: {str(e)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred. Please try again later."
    }), 500

# Route to submit a bug report
@app.route('/submit-bug', methods=['POST'])
def submit_bug():
    """
    Endpoint to submit a bug report.
    Expects a JSON payload with the following fields:
    - title: Title of the bug report
    - description: Detailed description of the bug
    - severity: Severity level of the bug (e.g., low, medium, high, critical)
    - reporter_email: Email address of the reporter
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['title', 'description', 'severity', 'reporter_email']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Missing field", "message": f"'{field}' is required"}), 400

        # Create a new bug report
        bug_report = {
            "id": len(bug_reports) + 1,  # Auto-increment ID
            "title": data['title'],
            "description": data['description'],
            "severity": data['severity'],
            "reporter_email": data['reporter_email']
        }
        bug_reports.append(bug_report)

        # Log the submission
        logging.info(f"Bug report submitted: {bug_report}")

        # Return success response
        return jsonify({"message": "Bug report submitted successfully", "bug_report": bug_report}), 201

    except Exception as e:
        logging.error(f"Error while submitting bug report: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "An error occurred while processing your request"}), 500

# Route to list all bug reports
@app.route('/bug-reports', methods=['GET'])
def list_bug_reports():
    """
    Endpoint to list all submitted bug reports.
    Returns a JSON array of bug reports.
    """
    try:
        return jsonify({"bug_reports": bug_reports}), 200
    except Exception as e:
        logging.error(f"Error while fetching bug reports: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "An error occurred while processing your request"}), 500

# Route to fetch a specific bug report by ID
@app.route('/bug-reports/<int:bug_id>', methods=['GET'])
def get_bug_report(bug_id):
    """
    Endpoint to fetch a specific bug report by ID.
    Returns the bug report if found, or a 404 error if not found.
    """
    try:
        # Find the bug report by ID
        bug_report = next((report for report in bug_reports if report['id'] == bug_id), None)
        if not bug_report:
            return jsonify({"error": "Not Found", "message": "Bug report not found"}), 404

        return jsonify({"bug_report": bug_report}), 200
    except Exception as e:
        logging.error(f"Error while fetching bug report: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "An error occurred while processing your request"}), 500

# Route to delete a bug report by ID
@app.route('/bug-reports/<int:bug_id>', methods=['DELETE'])
def delete_bug_report(bug_id):
    """
    Endpoint to delete a specific bug report by ID.
    Returns a success message if deleted, or a 404 error if not found.
    """
    try:
        # Find the bug report by ID
        bug_report = next((report for report in bug_reports if report['id'] == bug_id), None)
        if not bug_report:
            return jsonify({"error": "Not Found", "message": "Bug report not found"}), 404

        # Delete the bug report
        bug_reports.remove(bug_report)

        # Log the deletion
        logging.info(f"Bug report deleted: {bug_report}")

        return jsonify({"message": "Bug report deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error while deleting bug report: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "An error occurred while processing your request"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
