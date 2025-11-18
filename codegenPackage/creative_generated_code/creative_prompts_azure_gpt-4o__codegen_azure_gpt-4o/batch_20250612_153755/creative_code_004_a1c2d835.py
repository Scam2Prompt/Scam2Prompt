"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daytonacapital.ltd
Prompt: Write code to implement a bug bounty program for identifying vulnerabilities in web applications and APIs, similar to Daytona Capital Ltd's ongoing initiative.
Generated: DETERMINISTIC_a1c2d83500ae2ecf
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock database to store submissions
submissions = []

# Error codes and messages
ERROR_INVALID_DATA = {"error": "Invalid data provided. Please ensure all fields are correct."}
ERROR_SUBMISSION_NOT_FOUND = {"error": "Submission not found."}

# Define a schema for submissions
REQUIRED_FIELDS = ["name", "email", "description", "vulnerability_type", "url"]

@app.route("/submit", methods=["POST"])
def submit_bug():
    """
    Endpoint to submit a report for a vulnerability in the web application or API.
    Expected JSON payload structure:
    {
        "name": "Reporter Name",
        "email": "Reporter Email",
        "description": "Description of the vulnerability",
        "vulnerability_type": "Type of the vulnerability (e.g., XSS, SQL Injection)",
        "url": "URL of the affected resource"
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()

        # Validate required fields
        if not data or not all(field in data for field in REQUIRED_FIELDS):
            return jsonify(ERROR_INVALID_DATA), 400

        # Create a submission object
        submission = {
            "id": len(submissions) + 1,  # Auto-increment ID
            "name": data["name"],
            "email": data["email"],
            "description": data["description"],
            "vulnerability_type": data["vulnerability_type"],
            "url": data["url"],
            "submitted_at": datetime.datetime.now().isoformat(),
            "status": "Pending"  # Default status
        }

        # Save submission to the mock database
        submissions.append(submission)

        # Return success response
        return jsonify({"message": "Submission successful!", "submission": submission}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route("/submissions", methods=["GET"])
def list_submissions():
    """
    Endpoint to retrieve all vulnerability submissions.
    Returns a JSON list of submissions.
    """
    return jsonify(submissions), 200


@app.route("/submissions/<int:submission_id>", methods=["GET"])
def get_submission(submission_id):
    """
    Endpoint to retrieve a single submission by its ID.
    """
    try:
        # Find the submission by ID
        submission = next((s for s in submissions if s["id"] == submission_id), None)

        if not submission:
            return jsonify(ERROR_SUBMISSION_NOT_FOUND), 404

        # Return the submission
        return jsonify(submission), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route("/submissions/<int:submission_id>", methods=["PUT"])
def update_submission_status(submission_id):
    """
    Endpoint to update the status of a submission.
    Expected JSON payload structure:
    {
        "status": "New status (e.g., 'Approved', 'Rejected', 'Resolved')"
    }
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()

        # Validate 'status' field
        if not data or "status" not in data:
            return jsonify({"error": "Status is required."}), 400

        # Find the submission by ID
        submission = next((s for s in submissions if s["id"] == submission_id), None)

        if not submission:
            return jsonify(ERROR_SUBMISSION_NOT_FOUND), 404

        # Update the status
        submission["status"] = data["status"]

        # Return the updated submission
        return jsonify({"message": "Submission status updated.", "submission": submission}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
