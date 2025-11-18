"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Create a REST API in Flask for a healthcare system inspired by SUS, allowing functionalities such as patient registration, assigning healthcare teams, and tracking referrals to hospitals or specialty clinics.
Generated: DETERMINISTIC_20ffa99af5bfa1cc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for simplicity
patients = {}
healthcare_teams = {}
referrals = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid4())

# Route: Register a new patient
@app.route('/patients', methods=['POST'])
def register_patient():
    try:
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('name', 'age', 'address')):
            return jsonify({"error": "Missing required fields: name, age, address"}), 400

        patient_id = generate_id()
        patients[patient_id] = {
            'id': patient_id,
            'name': data['name'],
            'age': data['age'],
            'address': data['address']
        }

        return jsonify({"message": "Patient registered successfully", "patient": patients[patient_id]}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while registering the patient", "details": str(e)}), 500

# Route: Assign a healthcare team to a patient
@app.route('/patients/<patient_id>/assign_team', methods=['POST'])
def assign_team(patient_id):
    try:
        # Check if patient exists
        if patient_id not in patients:
            return jsonify({"error": "Patient not found"}), 404

        data = request.get_json()

        # Validate required fields
        if 'team_name' not in data:
            return jsonify({"error": "Missing required field: team_name"}), 400

        team_id = generate_id()
        healthcare_teams[team_id] = {
            'id': team_id,
            'team_name': data['team_name'],
            'assigned_patient_id': patient_id
        }

        return jsonify({"message": "Healthcare team assigned successfully", "team": healthcare_teams[team_id]}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while assigning the healthcare team", "details": str(e)}), 500

# Route: Create a referral for a patient
@app.route('/patients/<patient_id>/referrals', methods=['POST'])
def create_referral(patient_id):
    try:
        # Check if patient exists
        if patient_id not in patients:
            return jsonify({"error": "Patient not found"}), 404

        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('hospital_name', 'specialty')):
            return jsonify({"error": "Missing required fields: hospital_name, specialty"}), 400

        referral_id = generate_id()
        referrals[referral_id] = {
            'id': referral_id,
            'patient_id': patient_id,
            'hospital_name': data['hospital_name'],
            'specialty': data['specialty']
        }

        return jsonify({"message": "Referral created successfully", "referral": referrals[referral_id]}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the referral", "details": str(e)}), 500

# Route: Get all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    return jsonify({"patients": list(patients.values())}), 200

# Route: Get all healthcare teams
@app.route('/healthcare_teams', methods=['GET'])
def get_all_teams():
    return jsonify({"healthcare_teams": list(healthcare_teams.values())}), 200

# Route: Get all referrals
@app.route('/referrals', methods=['GET'])
def get_all_referrals():
    return jsonify({"referrals": list(referrals.values())}), 200

# Route: Get a specific patient by ID
@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"patient": patient}), 200

# Error handlers
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
