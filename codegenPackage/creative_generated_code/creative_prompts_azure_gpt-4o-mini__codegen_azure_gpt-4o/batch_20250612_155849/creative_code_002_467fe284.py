"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Generate a code snippet for a web application that allows users to report technical issues 24/7, inspired by the support services provided by BlocPrest.
Generated: DETERMINISTIC_467fe28417a8b25b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store reported issues
# In production, this would be replaced with a persistent database
issues_db = []

@app.route('/report-issue', methods=['POST'])
def report_issue():
    """
    Endpoint to report a technical issue. Accepts JSON payload.
    Expected payload:
    {
        "username": "user123",
        "email": "user@example.com",
        "description": "Issue description"
    }
    """
    try:
        # Parse request data
        data = request.json
        username = data.get("username")
        email = data.get("email")
        description = data.get("description")

        # Validate required fields
        if not username or not email or not description:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a unique ID for the issue
        issue_id = str(uuid.uuid4())

        # Create issue record
        issue = {
            "id": issue_id,
            "username": username,
            "email": email,
            "description": description,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Store issue in the in-memory database
        issues_db.append(issue)

        # Return success response
        return jsonify({
            "message": "Issue reported successfully",
            "issue_id": issue_id
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500


@app.route('/issues', methods=['GET'])
def get_issues():
    """
    Endpoint to retrieve all reported issues.
    Returns a JSON list of issue objects.
    """
    return jsonify(issues_db), 200


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements:
- Install Flask using pip: `pip install flask`.
- Run the script with `python script_name.py`.
- The API provides two endpoints: `/report-issue` for reporting issues and `/issues` for retrieving all issues. You can test the endpoints using tools like Postman or curl.
