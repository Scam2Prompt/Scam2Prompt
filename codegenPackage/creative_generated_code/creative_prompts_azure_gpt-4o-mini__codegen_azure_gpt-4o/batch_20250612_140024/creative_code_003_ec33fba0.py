"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io.drremplas.com
Prompt: Develop a RESTful API endpoint that allows healthcare professionals to register and manage their profiles for job placements in various medical fields.
Generated: DETERMINISTIC_ec33fba09beb29a6
Batch ID: 20250612_140024
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
import uuid
import re

app = Flask(__name__)

# In-memory storage for healthcare professionals
# In production, this would be replaced by a database
healthcare_professionals = {}

# Utility function for validating email addresses
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Error handler for custom errors
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Utility function for generating unique IDs
def generate_unique_id():
    return str(uuid.uuid4())

# Endpoint to register a new healthcare professional
@app.route('/api/healthcare-professionals', methods=['POST'])
def register_healthcare_professional():
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'field_of_specialization']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400

        # Validate email format
        if not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        # Generate unique ID for the professional
        professional_id = generate_unique_id()

        # Create profile
        healthcare_professionals[professional_id] = {
            'id': professional_id,
            'name': data['name'],
            'email': data['email'],
            'field_of_specialization': data['field_of_specialization'],
            'experience_years': data.get('experience_years', 0),  # Optional field defaults to 0
        }

        # Respond with the created profile
        return jsonify(healthcare_professionals[professional_id]), 201

    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

# Endpoint to retrieve all healthcare professionals
@app.route('/api/healthcare-professionals', methods=['GET'])
def get_all_healthcare_professionals():
    return jsonify(list(healthcare_professionals.values())), 200

# Endpoint to retrieve a specific healthcare professional by ID
@app.route('/api/healthcare-professionals/<string:professional_id>', methods=['GET'])
def get_healthcare_professional(professional_id):
    profile = healthcare_professionals.get(professional_id)
    if not profile:
        return jsonify({"error": "Healthcare professional not found"}), 404
    return jsonify(profile), 200

# Endpoint to update a healthcare professional's profile by ID
@app.route('/api/healthcare-professionals/<string:professional_id>', methods=['PUT'])
def update_healthcare_professional(professional_id):
    try:
        # Check if the professional exists
        if professional_id not in healthcare_professionals:
            return jsonify({"error": "Healthcare professional not found"}), 404

        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Update the profile with provided fields
        professional_profile = healthcare_professionals[professional_id]
        for key in ['name', 'email', 'field_of_specialization', 'experience_years']:
            if key in data:
                professional_profile[key] = data[key]

        # Validate email format if updated
        if 'email' in data and not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email format"}), 400

        return jsonify(professional_profile), 200

    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

# Endpoint to delete a healthcare professional's profile by ID
@app.route('/api/healthcare-professionals/<string:professional_id>', methods=['DELETE'])
def delete_healthcare_professional(professional_id):
    if professional_id not in healthcare_professionals:
        return jsonify({"error": "Healthcare professional not found"}), 404

    del healthcare_professionals[professional_id]
    return jsonify({"message": "Healthcare professional deleted successfully"}), 200

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
