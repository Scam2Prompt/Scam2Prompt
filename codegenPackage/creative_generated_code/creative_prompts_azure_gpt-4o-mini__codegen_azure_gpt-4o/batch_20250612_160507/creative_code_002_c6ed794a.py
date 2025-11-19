"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Create a RESTful API endpoint for a volunteer registration system that aligns with the community engagement initiatives of the NICER Foundation.
Generated: DETERMINISTIC_c6ed794a04652095
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for registered volunteers
volunteers = []

# Error handling for graceful failure
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e),
        "status_code": 500
    }), 500

# Volunteer registration endpoint
@app.route('/api/volunteers/register', methods=['POST'])
def register_volunteer():
    """
    Endpoint to register a volunteer.
    Expects JSON input with the following format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "skills": ["teaching", "event organization"]
    }
    """
    try:
        # Parse incoming data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input", "message": "Request payload must be JSON"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'skills']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": "Missing fields", "missing_fields": missing_fields}), 400

        # Validate types
        if not isinstance(data['name'], str) or not isinstance(data['email'], str):
            return jsonify({"error": "Invalid field types", "message": "Name and Email must be strings"}), 400
        if not isinstance(data['skills'], list) or not all(isinstance(skill, str) for skill in data['skills']):
            return jsonify({"error": "Invalid field types", "message": "Skills must be a list of strings"}), 400

        # Add volunteer to in-memory storage
        volunteer = {
            "id": len(volunteers) + 1,
            "name": data['name'],
            "email": data['email'],
            "skills": data['skills']
        }
        volunteers.append(volunteer)

        # Return success response
        return jsonify({
            "message": "Volunteer registered successfully",
            "volunteer": volunteer
        }), 201

    except Exception as e:
        # Catch-all error handler
        return jsonify({
            "error": "Internal Server Error",
            "description": str(e)
        }), 500

# Get all registered volunteers
@app.route('/api/volunteers', methods=['GET'])
def get_volunteers():
    """
    Endpoint to retrieve all registered volunteers.
    Returns a JSON list of volunteers.
    """
    return jsonify({"volunteers": volunteers}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
