"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Write code to implement a searchable directory of PSHP members, allowing users to filter by organization or role, as mentioned in the "PSHP Members Profile" section.
Generated: DETERMINISTIC_b23326644c0d361b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Flask application to implement a searchable directory of PSHP members

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing the PSHP members profile
# In a production setting, this should be replaced with a database
PSHP_MEMBERS = [
    {"name": "Alice Johnson", "organization": "Org A", "role": "Manager"},
    {"name": "Bob Smith", "organization": "Org B", "role": "Developer"},
    {"name": "Charlie Brown", "organization": "Org A", "role": "Designer"},
    {"name": "Dana White", "organization": "Org C", "role": "Developer"},
    {"name": "Eve Davis", "organization": "Org B", "role": "Manager"},
]

@app.route("/search", methods=["GET"])
def search_members():
    """
    Search and filter PSHP members by organization or role.
    Parameters are passed via query strings:
      - organization: Filter members by organization name.
      - role: Filter members by role.
    Example:
      GET /search?organization=Org+A&role=Manager
    """
    try:
        # Extract query parameters
        organization = request.args.get("organization", "").strip()
        role = request.args.get("role", "").strip()

        # Filter members based on query parameters
        filtered_members = PSHP_MEMBERS
        if organization:
            filtered_members = [member for member in filtered_members if member["organization"] == organization]
        if role:
            filtered_members = [member for member in filtered_members if member["role"] == role]

        # Return the filtered members as JSON
        return jsonify(filtered_members), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.errorhandler(404)
def handle_404(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Custom handler for 400 errors (Bad Request).
    """
    return jsonify({"error": "Bad request.", "details": str(error)}), 400

if __name__ == "__main__":
    # Run the Flask application
    # In production, use a production-ready server like Gunicorn or uWSGI
    app.run(debug=False, host="0.0.0.0", port=5000)
```
