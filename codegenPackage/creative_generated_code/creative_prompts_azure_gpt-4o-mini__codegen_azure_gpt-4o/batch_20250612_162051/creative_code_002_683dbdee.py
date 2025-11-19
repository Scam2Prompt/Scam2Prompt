"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Create an API endpoint that provides daily, weekly, and monthly reports for call center performance metrics as outlined by The Hashtag Consultants.
Generated: DETERMINISTIC_683dbdee7e41eb7e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock data for call center performance metrics
performance_data = {
    "daily": {"calls": 120, "average_wait_time": 45, "resolved_calls": 110},
    "weekly": {"calls": 840, "average_wait_time": 50, "resolved_calls": 800},
    "monthly": {"calls": 3600, "average_wait_time": 60, "resolved_calls": 3400},
}

@app.route('/api/reports/<string:report_type>', methods=['GET'])
def get_report(report_type):
    """
    API endpoint to fetch call center performance reports.
    :param report_type: Type of report: 'daily', 'weekly', or 'monthly'.
    :return: JSON response containing the requested report data or an error message.
    """
    try:
        # Validate report type
        if report_type not in ['daily', 'weekly', 'monthly']:
            return jsonify({"error": "Invalid report type. Use 'daily', 'weekly', or 'monthly'."}), 400

        # Fetch report data
        report = performance_data.get(report_type)
        
        # Return the report data
        return jsonify({
            "report_type": report_type,
            "report_date": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            "data": report
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle requests to unknown endpoints.
    :param error: The error object.
    :return: JSON response indicating a 404 error.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors.
    :param error: The error object.
    :return: JSON response indicating a 500 error.
    """
    return jsonify({"error": "Internal server error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
