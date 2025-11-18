"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Develop an API-based solution for managing visa application workflows, tailored to the administrative services offered by visapwr.
Generated: DETERMINISTIC_c6f53749d9183e20
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# visa_application_api.py

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)

# In-memory database for demonstration purposes
visa_applications = {}
application_id_counter = 1


# Helper function for generating unique application IDs
def generate_application_id():
    global application_id_counter
    application_id_counter += 1
    return application_id_counter


@app.route('/visa-applications', methods=['POST'])
def create_application():
    """
    Endpoint to create a new visa application.
    Expects JSON payload with applicant details.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'passport_number' not in data or 'visa_type' not in data:
            raise BadRequest("Missing or invalid input data.")

        application_id = generate_application_id()
        visa_applications[application_id] = {
            "id": application_id,
            "name": data['name'],
            "passport_number": data['passport_number'],
            "visa_type": data['visa_type'],
            "status": "Pending"
        }

        return jsonify({"message": "Application created successfully", "application_id": application_id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the application"}), 500


@app.route('/visa-applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    """
    Endpoint to fetch details of a specific visa application by ID.
    """
    try:
        application = visa_applications.get(application_id)
        if not application:
            return jsonify({"error": "Application not found"}), 404

        return jsonify(application), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the application"}), 500


@app.route('/visa-applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    """
    Endpoint to update the status of a visa application.
    Expects JSON payload with 'status'.
    """
    try:
        data = request.get_json()
        if not data or 'status' not in data:
            raise BadRequest("Missing or invalid input data.")

        application = visa_applications.get(application_id)
        if not application:
            return jsonify({"error": "Application not found"}), 404

        application['status'] = data['status']
        return jsonify({"message": "Application status updated successfully"}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the application"}), 500


@app.route('/visa-applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    """
    Endpoint to delete a visa application by ID.
    """
    try:
        application = visa_applications.pop(application_id, None)
        if not application:
            return jsonify({"error": "Application not found"}), 404

        return jsonify({"message": "Application deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the application"}), 500


@app.route('/visa-applications', methods=['GET'])
def list_applications():
    """
    Endpoint to fetch all visa applications.
    """
    try:
        return jsonify(list(visa_applications.values())), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while fetching applications"}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
