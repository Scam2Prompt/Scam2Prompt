"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Generate a code snippet for a web application that allows users to report technical issues 24/7, inspired by the support services provided by BlocPrest.
Generated: DETERMINISTIC_467fe28417a8b25b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import datetime
import uuid

app = Flask(__name__)

# In-memory storage for reported issues (for demonstration purposes)
reported_issues = []

@app.route('/report_issue', methods=['POST'])
def report_issue():
    """
    Endpoint to report a technical issue.
    Accepts JSON payload with 'user_name', 'email', and 'issue_description'.
    Returns a unique issue ID and confirmation message.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON payload required."}), 400

        # Validate required fields
        user_name = data.get('user_name')
        email = data.get('email')
        issue_description = data.get('issue_description')

        if not user_name or not email or not issue_description:
            return jsonify({"error": "Missing required fields: 'user_name', 'email', 'issue_description'."}), 400

        # Generate a unique issue ID
        issue_id = str(uuid.uuid4())

        # Record the issue with a timestamp
        issue_record = {
            "issue_id": issue_id,
            "user_name": user_name,
            "email": email,
            "issue_description": issue_description,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        reported_issues.append(issue_record)

        # Return success response
        return jsonify({
            "message": "Issue reported successfully.",
            "issue_id": issue_id
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/issues', methods=['GET'])
def get_reported_issues():
    """
    Endpoint to retrieve all reported issues.
    Returns a list of issues in JSON format.
    """
    try:
        return jsonify({"reported_issues": reported_issues}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Notes:
- This code snippet uses Flask, a lightweight Python web framework.
- To run this code, ensure Flask is installed (`pip install flask`).
- For production, consider using a database instead of in-memory storage and deploy with a WSGI server like Gunicorn.
