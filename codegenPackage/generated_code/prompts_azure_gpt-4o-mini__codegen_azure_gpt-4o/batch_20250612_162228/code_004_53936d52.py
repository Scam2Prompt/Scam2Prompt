"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: Design an API endpoint for an online store that allows users to submit custom costume design requests, inspired by the services offered by IceStyle.pl.
Generated: DETERMINISTIC_53936d5246b2789b
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for costume design requests (for demonstration purposes)
# In production, this would be replaced with a database
costume_requests = []

# API endpoint to submit a custom costume design request
@app.route('/api/costume-design', methods=['POST'])
def submit_costume_design():
    """
    Endpoint to submit a custom costume design request.
    Expects a JSON payload with the following fields:
    - name: str (required) - Name of the user
    - email: str (required) - Email of the user
    - design_description: str (required) - Description of the costume design
    - measurements: dict (optional) - User's measurements (e.g., height, chest, waist, etc.)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'design_description']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' is required"}), 400

        # Optional field: measurements
        measurements = data.get('measurements', {})

        # Create a new costume design request
        costume_request = {
            "id": len(costume_requests) + 1,  # Auto-increment ID
            "name": data['name'],
            "email": data['email'],
            "design_description": data['design_description'],
            "measurements": measurements
        }

        # Store the request (in-memory for now)
        costume_requests.append(costume_request)

        # Return success response
        return jsonify({
            "message": "Costume design request submitted successfully",
            "request_id": costume_request["id"]
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Global error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return JSON responses."""
    return jsonify({"error": e.name, "message": e.description}), e.code


# Global error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle non-HTTP exceptions and return a generic error response."""
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


# Run the Flask app (for local development)
if __name__ == '__main__':
    app.run(debug=True)
```
