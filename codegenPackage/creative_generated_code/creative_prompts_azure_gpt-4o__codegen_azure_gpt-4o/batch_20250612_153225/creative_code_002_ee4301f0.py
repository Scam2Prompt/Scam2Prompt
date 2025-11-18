"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Develop a prototype for an online portal that allows patients to access their health data and medical staff to monitor patient conditions in real-time, inspired by the features of Hooshmand Teb's smart medical system.
Generated: DETERMINISTIC_ee4301f0c7c1e915
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a prototype written in Python Flask, which provides a basic structure for the requested online portal. The portal has two roles: `Patient` and `Medical Staff`, and includes endpoints for accessing patient health data and monitoring conditions in real-time.

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data storage
patients = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 45,
        "health_data": [
            {"timestamp": "2023-10-01T12:00:00", "heart_rate": 72, "blood_pressure": "120/80"},
            {"timestamp": "2023-10-01T14:00:00", "heart_rate": 75, "blood_pressure": "118/78"}
        ]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 32,
        "health_data": [
            {"timestamp": "2023-10-01T12:00:00", "heart_rate": 80, "blood_pressure": "110/70"},
            {"timestamp": "2023-10-01T14:00:00", "heart_rate": 85, "blood_pressure": "115/75"}
        ]
    }
]

valid_roles = ["patient", "medical_staff"]


@app.route('/health-data/<int:patient_id>', methods=['GET'])
def get_patient_health_data(patient_id):
    """
    Endpoint for patients and medical staff to access a patient's health data.
    This function handles role-based access control.
    """
    role = request.args.get('role')  # Fetch the role from query string

    # Validate role
    if role not in valid_roles:
        return jsonify({"error": "Invalid role. Must be 'patient' or 'medical_staff'"}), 400

    # Find the patient
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    if role == "patient":
        # Restrict data for patients to their own health metrics
        return jsonify({"health_data": patient["health_data"]}), 200

    if role == "medical_staff":
        # Provide full patient details for medical staff
        return jsonify({"patient_details": patient}), 200


@app.route('/monitor/<int:patient_id>', methods=['POST'])
def monitor_patient_condition(patient_id):
    """
    Endpoint for medical staff to update or monitor patient conditions in real-time.
    """
    role = request.args.get('role')  # Fetch the role from query string

    if role != "medical_staff":
        return jsonify({"error": "Unauthorized access. Only medical staff can monitor patient conditions."}), 403

    data = request.json

    if not data:
        return jsonify({"error": "Request payload is empty. Please provide valid health metrics."}), 400

    # Validate payload
    required_fields = ["heart_rate", "blood_pressure"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    # Find the patient
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Update health data
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "heart_rate": data["heart_rate"],
        "blood_pressure": data["blood_pressure"]
    }
    patient["health_data"].append(new_entry)

    return jsonify({"message": "Patient condition updated successfully.", "new_entry": new_entry}), 200


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors gracefully."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle server errors gracefully."""
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500


# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic prototype for the requested portal. It includes endpoints for accessing health data (`GET /health-data/<int:patient_id>`) and updating/monitoring patient conditions (`POST /monitor/<int:patient_id>`). It implements role-based access control, error handling, and adheres to best practices for Flask applications.
