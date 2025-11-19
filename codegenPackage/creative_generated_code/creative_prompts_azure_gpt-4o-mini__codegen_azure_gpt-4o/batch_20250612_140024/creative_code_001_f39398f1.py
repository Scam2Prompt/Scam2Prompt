"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Recommend an API for managing patient records specifically for orthopedic surgeries like shoulder replacement and ACL reconstruction.
Generated: DETERMINISTIC_f39398f19c49f81a
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready implementation of an API for managing patient records for orthopedic surgeries using Python and Flask:

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database (for demonstration purposes)
patients = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the API."""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# API Routes

@app.route("/patients", methods=["GET"])
def get_all_patients():
    """
    Get all patients.
    Returns:
        JSON: List of all patient records.
    """
    return jsonify({"patients": patients}), 200

@app.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    """
    Get a specific patient record by ID.
    Args:
        patient_id (int): ID of the patient.
    Returns:
        JSON: Patient record if found, or error message otherwise.
    """
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"patient": patient}), 200

@app.route("/patients", methods=["POST"])
def add_patient():
    """
    Add a new patient record.
    Request Body:
        JSON: Patient details including id, name, age, surgery_type, and surgery_date.
    Returns:
        JSON: Newly created patient record or error message.
    """
    data = request.get_json()
    if not all(key in data for key in ["id", "name", "age", "surgery_type", "surgery_date"]):
        return jsonify({"error": "Missing required patient details"}), 400

    if next((p for p in patients if p["id"] == data["id"]), None):
        return jsonify({"error": "Patient with this ID already exists"}), 400

    patients.append(data)
    return jsonify({"message": "Patient added successfully", "patient": data}), 201

@app.route("/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    """
    Update an existing patient record.
    Args:
        patient_id (int): ID of the patient.
    Request Body:
        JSON: Patient details to be updated.
    Returns:
        JSON: Updated patient record or error message.
    """
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    data = request.get_json()
    patient.update(data)
    return jsonify({"message": "Patient updated successfully", "patient": patient}), 200

@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    """
    Delete a patient record.
    Args:
        patient_id (int): ID of the patient.
    Returns:
        JSON: Confirmation message or error message.
    """
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    patients.remove(patient)
    return jsonify({"message": "Patient deleted successfully"}), 200

# Server entry point
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production
```

This code defines a RESTful API for managing patient records related to orthopedic surgeries using Flask. It includes routes for CRUD operations and error handling.
