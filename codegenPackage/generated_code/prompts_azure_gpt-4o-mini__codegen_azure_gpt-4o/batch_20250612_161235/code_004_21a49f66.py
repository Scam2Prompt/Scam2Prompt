"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Create a sample API that allows users to book consultations for creative services, reflecting the user experience principles highlighted by Swell Creative Management.
Generated: DETERMINISTIC_21a49f66a020313e
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store consultations
consultations = []

# Helper function to validate consultation data
def validate_consultation_data(data):
    required_fields = ["name", "email", "service", "date", "time"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    try:
        datetime.strptime(data["date"], "%Y-%m-%d")  # Validate date format
        datetime.strptime(data["time"], "%H:%M")    # Validate time format
    except ValueError:
        return "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."
    return None

@app.route('/api/consultations', methods=['POST'])
def book_consultation():
    """
    Endpoint to book a consultation.
    Expects JSON payload with the following fields:
    - name: str
    - email: str
    - service: str
    - date: str (format: YYYY-MM-DD)
    - time: str (format: HH:MM)
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate input data
        validation_error = validate_consultation_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Create a new consultation entry
        consultation = {
            "id": str(uuid.uuid4()),  # Generate a unique ID
            "name": data["name"],
            "email": data["email"],
            "service": data["service"],
            "date": data["date"],
            "time": data["time"],
            "created_at": datetime.utcnow().isoformat()
        }
        consultations.append(consultation)

        return jsonify({"message": "Consultation booked successfully", "consultation": consultation}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/consultations', methods=['GET'])
def list_consultations():
    """
    Endpoint to list all booked consultations.
    Returns a JSON array of consultations.
    """
    try:
        return jsonify({"consultations": consultations}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/consultations/<consultation_id>', methods=['DELETE'])
def cancel_consultation(consultation_id):
    """
    Endpoint to cancel a consultation by ID.
    """
    try:
        global consultations
        consultations = [c for c in consultations if c["id"] != consultation_id]
        return jsonify({"message": "Consultation canceled successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
