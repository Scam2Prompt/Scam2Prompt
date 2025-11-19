"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Generate an API specification for a health service application that integrates with the Sistema Único de Saúde, focusing on patient data management and service accessibility.
Generated: DETERMINISTIC_3abc4e5fe7fe16e1
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API Specification for Health Service Application integrating with the Sistema Único de Saúde (SUS).
This application focuses on patient data management and service accessibility.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (placeholder for production database)
patients_data = {}

# Error Messages
ERROR_PATIENT_NOT_FOUND = {"error": "Patient not found"}
ERROR_INVALID_INPUT = {"error": "Invalid input data"}

# Health Check Endpoint
@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health status of the API.
    """
    return jsonify({"status": "API is running"}), 200

# Create New Patient
@app.route('/api/v1/patients', methods=['POST'])
def create_patient():
    """
    Endpoint to register a new patient.
    Required JSON fields: name, date_of_birth, sus_number, contact_number
    """
    try:
        data = request.json
        # Validate required fields
        if not all(field in data for field in ["name", "date_of_birth", "sus_number", "contact_number"]):
            return jsonify(ERROR_INVALID_INPUT), 400

        # Create a unique patient ID (in production use a database-generated ID)
        patient_id = len(patients_data) + 1
        patients_data[patient_id] = {
            "name": data["name"],
            "date_of_birth": data["date_of_birth"],
            "sus_number": data["sus_number"],
            "contact_number": data["contact_number"]
        }
        return jsonify({"patient_id": patient_id, "message": "Patient created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Patient Details
@app.route('/api/v1/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Endpoint to retrieve a patient's details by their ID.
    """
    patient = patients_data.get(patient_id)
    if not patient:
        return jsonify(ERROR_PATIENT_NOT_FOUND), 404
    return jsonify(patient), 200

# Update Patient Information
@app.route('/api/v1/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """
    Endpoint to update patient information.
    Required JSON fields: name, date_of_birth, sus_number, contact_number
    """
    try:
        patient = patients_data.get(patient_id)
        if not patient:
            return jsonify(ERROR_PATIENT_NOT_FOUND), 404

        data = request.json
        # Validate required fields
        if not all(field in data for field in ["name", "date_of_birth", "sus_number", "contact_number"]):
            return jsonify(ERROR_INVALID_INPUT), 400

        # Update patient information
        patients_data[patient_id] = {
            "name": data["name"],
            "date_of_birth": data["date_of_birth"],
            "sus_number": data["sus_number"],
            "contact_number": data["contact_number"]
        }
        return jsonify({"message": "Patient updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete Patient Record
@app.route('/api/v1/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """
    Endpoint to delete a patient's record.
    """
    patient = patients_data.pop(patient_id, None)
    if not patient:
        return jsonify(ERROR_PATIENT_NOT_FOUND), 404
    return jsonify({"message": "Patient deleted successfully"}), 200

# Get All Patients
@app.route('/api/v1/patients', methods=['GET'])
def get_all_patients():
    """
    Endpoint to retrieve all patients' data.
    """
    return jsonify(patients_data), 200

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
```
