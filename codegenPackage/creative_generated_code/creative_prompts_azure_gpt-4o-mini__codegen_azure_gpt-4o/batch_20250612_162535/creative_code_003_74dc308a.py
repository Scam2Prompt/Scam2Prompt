"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaaac.org
Prompt: Create a RESTful API endpoint that allows educational institutions to submit their accreditation applications to GAAAC.
Generated: DETERMINISTIC_74dc308aced05d8b
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for received applications (for demo purposes)
applications = []

# Function to validate the accreditation application data
def validate_application(data):
    required_fields = ["institution_name", "address", "contact_email", "contact_phone", "accreditation_type"]
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")
    if "@" not in data["contact_email"]:  # Simple email validation
        raise BadRequest("Invalid email format.")
    return True

@app.route('/submit-accreditation', methods=['POST'])
def submit_accreditation():
    """
    RESTful API endpoint for submitting accreditation applications.

    Request Payload:
    {
        "institution_name": "XYZ University",
        "address": "1234 Elm Street, Springfield",
        "contact_email": "info@xyz.edu",
        "contact_phone": "+1-234-567-8900",
        "accreditation_type": "Regional"
    }

    Response:
    Success: HTTP 200 with confirmation message.
    Error: HTTP 400 with error details.
    """
    try:
        # Parse JSON payload from the request
        application_data = request.get_json()

        if not application_data:
            raise BadRequest("Request payload must be in JSON format.")

        # Validate the incoming application data
        validate_application(application_data)

        # Generate a unique application ID (for simplicity, using length of applications list)
        application_id = len(applications) + 1
        application_data["application_id"] = application_id

        # Store application (in-memory storage for demo purposes)
        applications.append(application_data)

        # Return success response
        response = {
            "message": "Accreditation application submitted successfully.",
            "application_id": application_id
        }
        return jsonify(response), 200

    except BadRequest as e:
        # Handle validation errors
        response = {
            "error": "Bad Request",
            "message": str(e)
        }
        return jsonify(response), 400

    except Exception as e:
        # Handle unexpected errors
        response = {
            "error": "Internal Server Error",
            "message": "An unexpected error occurred. Please try again later."
        }
        return jsonify(response), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
