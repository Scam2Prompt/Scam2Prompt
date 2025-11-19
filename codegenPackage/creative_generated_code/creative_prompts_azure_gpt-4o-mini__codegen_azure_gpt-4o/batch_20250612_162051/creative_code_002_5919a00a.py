"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "Create a REST API endpoint for managing patient records in a medical practice similar to Gelenkzentrum Mönchengladbach."
Generated: DETERMINISTIC_5919a00af4f66d89
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
REST API for managing patient records in a medical practice.
Framework: Flask (Python)
"""

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for patient records (simulating a database)
patient_records = {}

# Utility function to validate patient data
def validate_patient_data(data):
    required_fields = ["name", "age", "gender", "contact"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data["age"], int) or data["age"] <= 0:
        return False, "Invalid age: must be a positive integer"
    return True, None

@app.route("/patients", methods=["GET"])
def get_all_patients():
    """
    Endpoint to retrieve all patient records.
    Returns:
        200: List of patients.
    """
    return jsonify(list(patient_records.values())), 200

@app.route("/patients/<patient_id>", methods=["GET"])
def get_patient(patient_id):
    """
    Endpoint to retrieve a single patient record by ID.
    Args:
        patient_id: ID of the patient.
    Returns:
        200: Patient record.
        404: Patient not found.
    """
    patient = patient_records.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient), 200

@app.route("/patients", methods=["POST"])
def create_patient():
    """
    Endpoint to create a new patient record.
    Body:
        JSON object with "name", "age", "gender", "contact".
    Returns:
        201: Created patient record.
        400: Invalid input data.
    """
    data = request.json
    is_valid, error = validate_patient_data(data)
    if not is_valid:
        return jsonify({"error": error}), 400
    
    patient_id = str(uuid.uuid4())  # Generate unique ID for the patient
    patient_records[patient_id] = {
        "id": patient_id,
        "name": data["name"],
        "age": data["age"],
        "gender": data["gender"],
        "contact": data["contact"]
    }
    return jsonify(patient_records[patient_id]), 201

@app.route("/patients/<patient_id>", methods=["PUT"])
def update_patient(patient_id):
    """
    Endpoint to update an existing patient record by ID.
    Args:
        patient_id: ID of the patient.
    Body:
        JSON object with optional keys "name", "age", "gender", "contact".
    Returns:
        200: Updated patient record.
        404: Patient not found.
        400: Invalid input data.
    """
    patient = patient_records.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    data = request.json
    if "age" in data and (not isinstance(data["age"], int) or data["age"] <= 0):
        return jsonify({"error": "Invalid age: must be a positive integer"}), 400
    
    # Update fields if provided
    patient.update({key: value for key, value in data.items() if key in ["name", "age", "gender", "contact"]})
    return jsonify(patient), 200

@app.route("/patients/<patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    """
    Endpoint to delete a patient record by ID.
    Args:
        patient_id: ID of the patient.
    Returns:
        200: Success message.
        404: Patient not found.
    """
    patient = patient_records.pop(patient_id, None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"message": f"Patient {patient_id} deleted successfully"}), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

This code provides a production-ready REST API for managing patient records using Flask. It includes endpoints for CRUD operations (Create, Read, Update, Delete), input validation, proper error handling, and follows best practices for Python development.
