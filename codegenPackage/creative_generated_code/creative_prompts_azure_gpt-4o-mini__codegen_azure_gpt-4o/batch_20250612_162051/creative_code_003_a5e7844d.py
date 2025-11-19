"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shravrav1.co.il
Prompt: Develop an API endpoint for a plumbing service that allows users to report issues such as pipe blockages or water leaks, referencing the services provided by the plumbing company in Tel Aviv.
Generated: DETERMINISTIC_a5e7844d1b62b8ad
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
import logging

app = Flask(__name__)

# Set up logging for debugging and production error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# List of services offered by the company
AVAILABLE_SERVICES = ["pipe blockage", "water leak", "installation", "maintenance"]

# Endpoint to report plumbing issues
@app.route('/report_issue', methods=['POST'])
def report_issue():
    """
    API endpoint to report plumbing issues.
    Request method: POST
    Expected JSON payload: {
        "name": <str>,
        "contact": <str>,
        "location": <str>,
        "issue": <str>
    }
    Returns:
        HTTP 200 with success message if valid, else HTTP 400 with error message.
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({"error": "Request body must be JSON."}), 400

        name = data.get("name")
        contact = data.get("contact")
        location = data.get("location")
        issue = data.get("issue")

        # Check for missing fields
        if not all([name, contact, location, issue]):
            return jsonify({"error": "Missing required fields: name, contact, location, or issue."}), 400

        # Validate issue against available services
        if issue.lower() not in AVAILABLE_SERVICES:
            return jsonify({"error": f"Issue '{issue}' is not recognized. Available services: {', '.join(AVAILABLE_SERVICES)}"}), 400

        # Log the reported issue (could be saved to a database in production)
        logging.info(f"New issue reported by {name}. Contact: {contact}, Location: {location}, Issue: {issue}")

        # Return success response
        return jsonify({"message": "Issue reported successfully.", "data": data}), 200

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
