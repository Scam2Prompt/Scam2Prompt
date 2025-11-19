"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarhospital.com
Prompt: Create a REST API endpoint for a hospital management system that allows for the retrieval of patient records, reflecting the fully computerized health records system at Amar Hospital.
Generated: DETERMINISTIC_c7c86fb38f544230
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for patient records
patients = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 35,
        "gender": "Male",
        "medical_history": ["Diabetes", "Hypertension"]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 29,
        "gender": "Female",
        "medical_history": ["Asthma"]
    },
    {
        "id": 3,
        "name": "Alice Johnson",
        "age": 42,
        "gender": "Female",
        "medical_history": ["Thyroid Disorder"]
    }
]

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the application.
    Returns a JSON response with the error message and status code.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route("/api/patients/<int:patient_id>", methods=["GET"])
def get_patient_record(patient_id):
    """
    Endpoint to retrieve patient records by ID.
    :param patient_id: ID of the patient whose record is to be retrieved.
    :return: JSON response containing the patient record or an error message if not found.
    """
    try:
        # Find the patient record by ID
        patient = next((p for p in patients if p["id"] == patient_id), None)

        if not patient:
            # Patient not found
            return jsonify({"error": "Patient not found"}), 404

        # Return the patient record as a JSON response
        return jsonify(patient), 200
    except Exception as e:
        # Handle any unexpected errors
        return handle_exception(e)

@app.route("/api/patients", methods=["GET"])
def get_all_patients():
    """
    Endpoint to retrieve all patient records.
    :return: JSON response containing all patient records.
    """
    try:
        return jsonify(patients), 200
    except Exception as e:
        return handle_exception(e)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
