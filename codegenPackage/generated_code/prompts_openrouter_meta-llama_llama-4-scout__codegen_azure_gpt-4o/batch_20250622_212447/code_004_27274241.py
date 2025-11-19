"""
Generated Code Metadata:
========================
Original URL: https://gaaac.org
Prompt: Create a RESTful API to manage accreditation applications for Gulf countries, inspired by GAAAC's accreditation process.
Generated: DETERMINISTIC_27274241cf758e6f
Batch ID: 20250622_212447
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

# In-memory database for demonstration purposes
applications = {}
application_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/applications', methods=['POST'])
def create_application():
    """
    Create a new accreditation application.
    Expected JSON payload:
    {
        "country": "Country Name",
        "applicant_name": "Applicant Name",
        "details": "Application Details"
    }
    """
    global application_id_counter

    # Validate request payload
    data = request.get_json()
    if not data or 'country' not in data or 'applicant_name' not in data or 'details' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Create new application
    application_id = application_id_counter
    applications[application_id] = {
        "id": application_id,
        "country": data['country'],
        "applicant_name": data['applicant_name'],
        "details": data['details'],
        "status": "Pending"
    }
    application_id_counter += 1

    return jsonify(applications[application_id]), 201

@app.route('/applications', methods=['GET'])
def list_applications():
    """
    List all accreditation applications.
    """
    return jsonify(list(applications.values())), 200

@app.route('/applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    """
    Retrieve a specific accreditation application by ID.
    """
    application = applications.get(application_id)
    if not application:
        return jsonify({"error": "Not Found", "message": "Application not found"}), 404

    return jsonify(application), 200

@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    """
    Update an existing accreditation application.
    Expected JSON payload:
    {
        "country": "Updated Country Name",
        "applicant_name": "Updated Applicant Name",
        "details": "Updated Application Details",
        "status": "Updated Status"
    }
    """
    application = applications.get(application_id)
    if not application:
        return jsonify({"error": "Not Found", "message": "Application not found"}), 404

    # Validate request payload
    data = request.get_json()
    if not data or 'country' not in data or 'applicant_name' not in data or 'details' not in data or 'status' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Update application
    application.update({
        "country": data['country'],
        "applicant_name": data['applicant_name'],
        "details": data['details'],
        "status": data['status']
    })

    return jsonify(application), 200

@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    """
    Delete an accreditation application by ID.
    """
    application = applications.pop(application_id, None)
    if not application:
        return jsonify({"error": "Not Found", "message": "Application not found"}), 404

    return jsonify({"message": "Application deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
