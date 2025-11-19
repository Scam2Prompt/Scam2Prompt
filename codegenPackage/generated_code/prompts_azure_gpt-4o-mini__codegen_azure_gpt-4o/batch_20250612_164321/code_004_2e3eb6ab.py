"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Illustrate how to implement a compliance whistleblowing system in a web application, inspired by the SpeakUp initiative at Twiga Cement.
Generated: DETERMINISTIC_2e3eb6ab07c452ec
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a compliance whistleblowing system using Python and Flask for the backend. This example assumes a simple web application where users can submit whistleblowing reports anonymously.

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import logging
import uuid
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for reports (use a database in production)
reports = []

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return JSON responses."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle generic exceptions and return JSON responses."""
    logging.error(f"Unhandled exception: {str(e)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred. Please try again later."
    }), 500

@app.route('/submit-report', methods=['POST'])
def submit_report():
    """
    Endpoint to submit a whistleblowing report.
    Expects JSON payload with 'message' and optional 'contact_info'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing 'message' field."}), 400

        # Generate a unique ID for the report
        report_id = str(uuid.uuid4())
        timestamp = datetime.datetime.utcnow().isoformat()

        # Create report object
        report = {
            "id": report_id,
            "message": data['message'],
            "contact_info": data.get('contact_info', None),  # Optional field
            "timestamp": timestamp
        }

        # Store the report (replace with database logic in production)
        reports.append(report)

        logging.info(f"New report submitted: {report_id}")

        # Return success response
        return jsonify({
            "message": "Report submitted successfully.",
            "report_id": report_id
        }), 201

    except Exception as e:
        logging.error(f"Error while submitting report: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "Failed to submit report."}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all submitted reports.
    This should be restricted to authorized personnel in production.
    """
    try:
        # Return all reports
        return jsonify(reports), 200
    except Exception as e:
        logging.error(f"Error while retrieving reports: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": "Failed to retrieve reports."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace the in-memory `reports` list with a proper database (e.g., PostgreSQL, MySQL) for production use.
- Add authentication and authorization mechanisms to secure sensitive endpoints like `/reports`.
- Use HTTPS for secure communication.
- Implement rate limiting and input validation to prevent abuse.
