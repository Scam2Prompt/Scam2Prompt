"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgxaex.com
Prompt: How does SGXAEX.com assist users in reporting cryptocurrency scams?
Generated: DETERMINISTIC_9e3397aa1ba9f31a
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging for error tracking and system monitoring.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("sgxaex_service.log"),
        logging.StreamHandler()
    ]
)

# In-memory database simulation to store scam reports
scam_reports = []


@app.route('/report', methods=['POST'])
def report_scam():
    """
    Endpoint to allow users to report cryptocurrency scams.
    Expects JSON data in the request body with 'name', 'description', and 'contact_info'.
    """
    try:
        # Parse the request data
        data = request.get_json()
        
        # Validate required fields
        if not data or 'name' not in data or 'description' not in data or 'contact_info' not in data:
            logging.warning("Invalid report data received.")
            return jsonify({"error": "Invalid data. 'name', 'description', and 'contact_info' are required."}), 400
        
        # Create a new report
        report = {
            "id": len(scam_reports) + 1,  # Generate a unique ID for the report
            "name": data['name'],
            "description": data['description'],
            "contact_info": data['contact_info']
        }
        
        # Save the report to the in-memory database
        scam_reports.append(report)
        
        # Log the event for monitoring
        logging.info(f"New scam report submitted: {report}")
        
        return jsonify({"message": "Scam report submitted successfully.", "report": report}), 201
    
    except Exception as e:
        # Log unexpected errors
        logging.error(f"Error while processing scam report: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500


@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to retrieve all reported cryptocurrency scams.
    """
    try:
        return jsonify({"scam_reports": scam_reports}), 200
    except Exception as e:
        # Log unexpected errors
        logging.error(f"Error while fetching scam reports: {str(e)}")
        return jsonify({"error": "An error occurred while fetching scam reports. Please try again later."}), 500


@app.route('/')
def home():
    """
    Welcome endpoint to indicate the service is running.
    """
    return jsonify({"message": "Welcome to SGXAEX.com Scam Reporting Service!"}), 200


if __name__ == "__main__":
    # Start the Flask application
    try:
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        logging.error(f"Failed to start the application: {str(e)}")
```
