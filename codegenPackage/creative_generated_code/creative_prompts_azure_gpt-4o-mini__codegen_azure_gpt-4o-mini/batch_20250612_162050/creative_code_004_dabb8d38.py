"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Create a sample application that utilizes the Smart Emergency Medical System (SEMS) to enhance patient care, referencing the solutions provided by Hooshmand Teb.
Generated: DETERMINISTIC_dabb8d38b04341fd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Schema for validating incoming patient data
class PatientSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    medical_history = fields.Str(required=True)
    location = fields.Str(required=True)

# In-memory storage for patients
patients = []

@app.route('/patients', methods=['POST'])
def add_patient():
    """
    Add a new patient to the system.
    Expects JSON data in the request body.
    """
    patient_schema = PatientSchema()

    # Validate incoming data
    try:
        data = patient_schema.load(request.json)
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400

    # Add patient to the system
    patients.append(data)
    logging.info(f"Patient added: {data}")
    
    return jsonify(data), 201

@app.route('/patients', methods=['GET'])
def get_patients():
    """
    Retrieve the list of all patients.
    """
    return jsonify(patients), 200

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Retrieve a specific patient by ID.
    """
    if patient_id < 0 or patient_id >= len(patients):
        logging.warning(f"Patient ID {patient_id} not found.")
        return jsonify({"error": "Patient not found"}), 404

    return jsonify(patients[patient_id]), 200

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle any unexpected exceptions.
    """
    logging.error(f"An error occurred: {str(e)}")
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app in production mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Requirements:
Make sure to install the necessary packages by running:
```bash
pip install Flask marshmallow
```

### Running the Application:
You can start the application with:
```bash
python app.py
```

### API Endpoints:
1. **POST /patients**: Add a new patient.
   - Request body: `{"name": "John Doe", "age": 30, "medical_history": "None", "location": "123 Main St"}`
2. **GET /patients**: Retrieve all patients.
3. **GET /patients/<int:patient_id>**: Retrieve a specific patient by ID.
