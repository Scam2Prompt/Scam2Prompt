"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sassmgmt.com
Prompt: Develop an API endpoint for submitting applications for commercial extras in a talent management system.
Generated: DETERMINISTIC_e52efef486d30e24
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for applications (for demonstration purposes)
applications = []

# Custom error handler for the API
@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the API."""
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.description}).get_data()
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal Server Error"}), 500

# API endpoint to submit applications
@app.route('/api/applications', methods=['POST'])
def submit_application():
    """
    Endpoint to submit an application for commercial extras in the talent management system.

    Request Body (JSON):
    {
        "name": "string",            # Full name of the applicant (Required)
        "email": "string",           # Email of the applicant (Required)
        "phone": "string",           # Phone number of the applicant (Required)
        "experience_level": "string" # Experience level, e.g., "Beginner", "Intermediate", "Advanced" (Optional)
    }

    Response (JSON):
    201 Created:
    {
        "id": "string",              # Unique identifier for the application
        "message": "Application submitted successfully."
    }

    400 Bad Request:
    {
        "error": "Detailed error message describing the issue."
    }
    """
    try:
        # Parse and validate the request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400
        
        # Required fields
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        
        if not all([name, email, phone]):
            return jsonify({"error": "Fields 'name', 'email', and 'phone' are required"}), 400
        
        # Optional field
        experience_level = data.get("experience_level", "Unknown")
        
        # Create a new application object
        application_id = str(uuid.uuid4())  # Generate a unique ID for the application
        application = {
            "id": application_id,
            "name": name,
            "email": email,
            "phone": phone,
            "experience_level": experience_level
        }
        
        # Store the application in the in-memory list
        applications.append(application)
        
        # Return success response
        return jsonify({
            "id": application_id,
            "message": "Application submitted successfully."
        }), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while processing the request: " + str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
