"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payidarsaglik.com
Prompt: Create a RESTful API specification for a home healthcare service that includes endpoints for booking medical consultations and ambulance requests.
Generated: DETERMINISTIC_c09326e67a77d41c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory databases for demonstration purposes
medical_consultations = []  # To store booked consultations
ambulance_requests = []     # To store ambulance requests

# Helper function to generate unique IDs
def generate_id(data_list):
    return len(data_list) + 1

# Endpoint to book a medical consultation
@app.route('/api/consultations', methods=['POST'])
def book_consultation():
    """
    Endpoint to book a medical consultation.
    Request Body:
    {
        "patient_name": "John Doe",
        "age": 45,
        "symptoms": ["fever", "cough"],
        "date": "2023-10-01",
        "time": "15:30"
    }
    """
    try:
        data = request.json
        
        # Validate incoming data
        if not all(key in data for key in ['patient_name', 'age', 'symptoms', 'date', 'time']):
            return jsonify({"error": "Missing required fields"}), 400
        
        consultation = {
            "id": generate_id(medical_consultations),
            "patient_name": data['patient_name'],
            "age": data['age'],
            "symptoms": data['symptoms'],
            "date": data['date'],
            "time": data['time']
        }
        medical_consultations.append(consultation)
        return jsonify({"message": "Consultation booked successfully", "consultation": consultation}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to request an ambulance
@app.route('/api/ambulance', methods=['POST'])
def request_ambulance():
    """
    Endpoint to request an ambulance.
    Request Body:
    {
        "patient_name": "John Doe",
        "location": "123 Main Street",
        "emergency_type": "heart attack"
    }
    """
    try:
        data = request.json
        
        # Validate incoming data
        if not all(key in data for key in ['patient_name', 'location', 'emergency_type']):
            return jsonify({"error": "Missing required fields"}), 400
        
        ambulance_request = {
            "id": generate_id(ambulance_requests),
            "patient_name": data['patient_name'],
            "location": data['location'],
            "emergency_type": data['emergency_type']
        }
        ambulance_requests.append(ambulance_request)
        return jsonify({"message": "Ambulance request created successfully", "ambulance_request": ambulance_request}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all medical consultations
@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    """
    Endpoint to retrieve all booked medical consultations.
    """
    return jsonify(medical_consultations), 200

# Endpoint to retrieve all ambulance requests
@app.route('/api/ambulance', methods=['GET'])
def get_ambulance_requests():
    """
    Endpoint to retrieve all ambulance requests.
    """
    return jsonify(ambulance_requests), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 Not Found errors.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 Internal Server Errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
