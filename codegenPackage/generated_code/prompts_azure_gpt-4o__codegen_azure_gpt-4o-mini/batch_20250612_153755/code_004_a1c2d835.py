"""
Generated Code Metadata:
========================
Original URL: https://daytonacapital.ltd
Prompt: Write code to implement a bug bounty program for identifying vulnerabilities in web applications and APIs, similar to Daytona Capital Ltd's ongoing initiative.
Generated: DETERMINISTIC_a1c2d83500ae2ecf
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for reported vulnerabilities
vulnerabilities = []

@app.route('/report', methods=['POST'])
def report_vulnerability():
    """
    Endpoint to report a vulnerability.
    Expects a JSON payload with 'title', 'description', and 'severity'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate the incoming data
        if not data or not all(key in data for key in ('title', 'description', 'severity')):
            return jsonify({"error": "Invalid input"}), 400

        # Create a vulnerability report
        vulnerability = {
            "id": len(vulnerabilities) + 1,
            "title": data['title'],
            "description": data['description'],
            "severity": data['severity'],
            "status": "reported"
        }

        # Store the vulnerability report
        vulnerabilities.append(vulnerability)

        # Log the successful report
        logging.info(f"Vulnerability reported: {vulnerability}")

        return jsonify(vulnerability), 201

    except Exception as e:
        logging.error(f"Error reporting vulnerability: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/vulnerabilities', methods=['GET'])
def list_vulnerabilities():
    """
    Endpoint to list all reported vulnerabilities.
    """
    try:
        return jsonify(vulnerabilities), 200
    except Exception as e:
        logging.error(f"Error retrieving vulnerabilities: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/vulnerability/<int:vuln_id>', methods=['PUT'])
def update_vulnerability(vuln_id):
    """
    Endpoint to update the status of a reported vulnerability.
    Expects a JSON payload with 'status'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate the incoming data
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Find the vulnerability by ID
        vulnerability = next((v for v in vulnerabilities if v['id'] == vuln_id), None)

        if not vulnerability:
            return jsonify({"error": "Vulnerability not found"}), 404

        # Update the vulnerability status
        vulnerability['status'] = data['status']
        logging.info(f"Vulnerability updated: {vulnerability}")

        return jsonify(vulnerability), 200

    except Exception as e:
        logging.error(f"Error updating vulnerability: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Requirements
- Install Flask: `pip install Flask`
- Run the application: `python app.py`
- Use tools like Postman or curl to interact with the API.
